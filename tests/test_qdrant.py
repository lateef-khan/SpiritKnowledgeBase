from pathlib import Path

from kb.card import parse_card
from kb.config import FacetSpec, KbConfig
from kb.qdrant import VECTOR_NAME, apply_plan, ensure_collection
from kb.state import state_for
from kb.syncplan import plan_sync

CONFIG = KbConfig(
    root=Path("."),
    collection="kb",
    embedding_model="text-embedding-3-small",
    embedding_dimensions=1024,
    kinds=("fact",),
    facets={
        "model": FacetSpec(index="keyword", array=False, values=()),
        "applies_to": FacetSpec(index="keyword", array=True, values=()),
    },
    payload_indexes={
        "text": {"index": "text", "tokenizer": "word", "lowercase": True, "min_token_len": 1},
        "card_id": {"index": "keyword"},
        "authority": {"index": "integer"},
    },
    pdf_command=None,
)

TEMPLATE = """---
id: {id}
title: T
kind: fact
question: Q?
asked_as: [one, two]
keywords: [a, b, c, d]
facets:
  model: {model}
  applies_to: [f63]
authority: 3
not_to_be_confused_with: []
see_also: []
source:
  ref: s
  locator: p.1
  extracted_at: 2026-08-21
---

{body}
"""


def card(id="card-a", model="f63", body="Body."):
    return parse_card(TEMPLATE.format(id=id, model=model, body=body), f"cards/{id}.md")


class FakeClient:
    def __init__(self, exists=False):
        self._exists = exists
        self.created = []
        self.indexes = []
        self.upserted = []
        self.payload_sets = []
        self.deleted = []

    def collection_exists(self, name):
        return self._exists

    def create_collection(self, collection_name, vectors_config, **kwargs):
        self._exists = True
        self.created.append({"name": collection_name, "vectors": vectors_config})

    def create_payload_index(self, collection_name, field_name, field_schema, wait=True):
        self.indexes.append(field_name)

    def upsert(self, collection_name, points, wait=True):
        self.upserted.extend(points)

    def set_payload(self, collection_name, payload, points, wait=True):
        self.payload_sets.append({"payload": payload, "points": list(points)})

    def delete(self, collection_name, points_selector, wait=True):
        self.deleted.append(points_selector)


class FakeEmbedder:
    def __init__(self):
        self.seen = []

    def embed(self, texts):
        self.seen.extend(texts)
        return [[0.5] * 1024 for _ in texts]


def test_ensure_collection_creates_a_single_named_dense_vector():
    client = FakeClient()
    ensure_collection(client, CONFIG, "kb")
    assert client.created[0]["name"] == "kb"
    assert set(client.created[0]["vectors"]) == {VECTOR_NAME}


def test_ensure_collection_creates_every_declared_index():
    client = FakeClient()
    ensure_collection(client, CONFIG, "kb")
    assert set(client.indexes) == {
        "text",
        "card_id",
        "authority",
        "facets.model",
        "facets.applies_to",
    }


def test_ensure_collection_is_idempotent():
    client = FakeClient(exists=True)
    ensure_collection(client, CONFIG, "kb")
    assert client.created == []


def test_upsert_embeds_and_writes_a_point():
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    cards = [card()]
    counts = apply_plan(client, CONFIG, "kb", plan_sync(cards, {}), cards, embedder)
    assert counts["upsert"] == 1
    assert len(client.upserted) == 1
    assert client.upserted[0].payload["card_id"] == "card-a"
    assert len(embedder.seen) == 1


def test_set_payload_writes_payload_and_never_embeds():
    original = card()
    moved = parse_card(
        TEMPLATE.format(id="card-a", model="e95", body="Body."), "cards/other/card-a.md"
    )
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    plan = plan_sync([moved], {"card-a": state_for(original)})
    counts = apply_plan(client, CONFIG, "kb", plan, [moved], embedder)
    assert counts["set_payload"] == 1
    assert embedder.seen == []
    assert client.upserted == []
    assert client.payload_sets[0]["payload"]["facets"]["model"] == "e95"


def test_skip_touches_nothing():
    original = card()
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    plan = plan_sync([original], {"card-a": state_for(original)})
    apply_plan(client, CONFIG, "kb", plan, [original], embedder)
    assert client.upserted == []
    assert client.payload_sets == []
    assert embedder.seen == []


def test_delete_removes_the_point():
    original = card()
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    plan = plan_sync([], {"card-a": state_for(original)}, delete_ratio_limit=1.0)
    counts = apply_plan(client, CONFIG, "kb", plan, [], embedder)
    assert counts["delete"] == 1
    assert len(client.deleted) == 1


def test_embedding_is_batched_into_one_call_for_many_upserts():
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    cards = [card(f"card-{i}") for i in range(5)]
    apply_plan(client, CONFIG, "kb", plan_sync(cards, {}), cards, embedder)
    assert len(embedder.seen) == 5
    assert len(client.upserted) == 5

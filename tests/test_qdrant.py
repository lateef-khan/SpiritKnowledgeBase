from pathlib import Path

from qdrant_client import models

from kb.card import parse_card
from kb.config import FacetSpec, KbConfig
from kb.qdrant import VECTOR_NAME, apply_plan, ensure_collection, rebuild
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
    def __init__(self, exists=False, name="kb"):
        self._collections = {name} if exists else set()
        self.created = []
        self.indexes = []
        self.upserted = []
        self.upsert_targets = []
        self.payload_sets = []
        self.deleted = []
        self.deleted_collections = []
        self.alias_ops = []
        self.calls = []
        self._aliases = []

    def collection_exists(self, name):
        return name in self._collections

    def create_collection(self, collection_name, vectors_config, **kwargs):
        self._collections.add(collection_name)
        self.created.append({"name": collection_name, "vectors": vectors_config})
        self.calls.append(f"create_collection:{collection_name}")

    def create_payload_index(self, collection_name, field_name, field_schema, wait=True):
        self.indexes.append(field_name)

    def upsert(self, collection_name, points, wait=True):
        self.upserted.extend(points)
        self.upsert_targets.append(collection_name)

    def set_payload(self, collection_name, payload, points, wait=True):
        self.payload_sets.append({"payload": payload, "points": list(points)})

    def delete(self, collection_name, points_selector, wait=True):
        self.deleted.append(points_selector)

    def delete_collection(self, collection_name):
        self._collections.discard(collection_name)
        self.deleted_collections.append(collection_name)
        self.calls.append(f"delete_collection:{collection_name}")

    def get_aliases(self):
        return models.CollectionsAliasesResponse(aliases=list(self._aliases))

    def update_collection_aliases(self, change_aliases_operations):
        self.alias_ops.append(list(change_aliases_operations))
        self.calls.append("update_collection_aliases")
        for op in change_aliases_operations:
            create = op.create_alias
            self._aliases = [a for a in self._aliases if a.alias_name != create.alias_name]
            self._aliases.append(
                models.AliasDescription(
                    alias_name=create.alias_name, collection_name=create.collection_name
                )
            )


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


def test_rebuild_creates_the_stamped_collection_and_returns_its_name():
    client, embedder = FakeClient(), FakeEmbedder()
    name = rebuild(client, CONFIG, [card()], embedder, "20260821")
    assert name == "kb_20260821"
    assert client.collection_exists("kb_20260821")


def test_rebuild_embeds_every_card_and_upserts_one_point_each_into_the_new_collection():
    client, embedder = FakeClient(), FakeEmbedder()
    cards = [card("card-a"), card("card-b"), card("card-c")]
    target = rebuild(client, CONFIG, cards, embedder, "stamp")
    assert len(embedder.seen) == 3
    assert len(client.upserted) == 3
    assert {p.payload["card_id"] for p in client.upserted} == {"card-a", "card-b", "card-c"}
    assert client.upsert_targets == [target]


def test_rebuild_points_the_alias_at_the_new_collection():
    client, embedder = FakeClient(), FakeEmbedder()
    target = rebuild(client, CONFIG, [card()], embedder, "stamp")
    aliases = {a.alias_name: a.collection_name for a in client.get_aliases().aliases}
    assert aliases[CONFIG.collection] == target


def test_rebuild_drops_the_previous_alias_target_but_not_the_new_one():
    client, embedder = FakeClient(), FakeEmbedder()
    first = rebuild(client, CONFIG, [card()], embedder, "one")
    second = rebuild(client, CONFIG, [card()], embedder, "two")
    assert client.deleted_collections == [first]
    assert client.collection_exists(second)
    assert not client.collection_exists(first)


def test_rebuild_repoints_the_alias_before_deleting_the_old_collection():
    client, embedder = FakeClient(), FakeEmbedder()
    first = rebuild(client, CONFIG, [card()], embedder, "one")
    client.calls.clear()
    rebuild(client, CONFIG, [card()], embedder, "two")
    alias_step = client.calls.index("update_collection_aliases")
    delete_step = client.calls.index(f"delete_collection:{first}")
    assert alias_step < delete_step


def test_rebuild_on_a_fresh_install_deletes_nothing():
    client, embedder = FakeClient(), FakeEmbedder()
    rebuild(client, CONFIG, [card()], embedder, "stamp")
    assert client.deleted_collections == []


def test_rebuild_recreates_a_colliding_stamped_collection():
    client, embedder = FakeClient(), FakeEmbedder()
    ensure_collection(client, CONFIG, "kb_stamp")
    client.created.clear()
    name = rebuild(client, CONFIG, [card()], embedder, "stamp")
    assert name == "kb_stamp"
    assert client.deleted_collections == ["kb_stamp"]
    assert client.created[0]["name"] == "kb_stamp"
    assert client.collection_exists("kb_stamp")

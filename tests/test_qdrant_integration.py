from pathlib import Path

import pytest
from qdrant_client import QdrantClient, models

from kb.card import parse_card
from kb.config import FacetSpec, KbConfig
from kb.ids import point_id
from kb.qdrant import VECTOR_NAME, apply_plan, ensure_collection
from kb.state import state_for
from kb.syncplan import plan_sync

pytestmark = pytest.mark.integration

CONFIG = KbConfig(
    root=Path("."),
    collection="kb_it",
    embedding_model="text-embedding-3-small",
    embedding_dimensions=1024,
    kinds=("troubleshooting",),
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
title: {title}
kind: troubleshooting
question: What does it mean?
asked_as: [one phrasing, two phrasing]
keywords: [alpha, beta, gamma, delta]
facets:
  model: {model}
  applies_to: [{model}]
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


def card(id, title, model="f63", body="Body text.", path=None):
    return parse_card(
        TEMPLATE.format(id=id, title=title, model=model, body=body), path or f"cards/{id}.md"
    )


class ConstantEmbedder:
    def embed(self, texts):
        return [[float(len(t) % 7) / 7.0] * 1024 for t in texts]


@pytest.fixture
def client():
    c = QdrantClient(url="http://localhost:6333", prefer_grpc=False, timeout=120)
    if c.collection_exists(CONFIG.collection):
        c.delete_collection(CONFIG.collection)
    yield c
    if c.collection_exists(CONFIG.collection):
        c.delete_collection(CONFIG.collection)


def count(client) -> int:
    return client.count(CONFIG.collection, exact=True).count


def test_full_lifecycle_against_real_qdrant(client):
    embedder = ConstantEmbedder()
    ensure_collection(client, CONFIG, CONFIG.collection)

    first = card("e03", "Error E03 - hardware current too large")
    apply_plan(client, CONFIG, CONFIG.collection, plan_sync([first], {}), [first], embedder)
    assert count(client) == 1

    state = {"e03": state_for(first)}
    moved = card("e03", "Error E03 - hardware current too large", path="cards/moved/e03.md")
    plan = plan_sync([moved], state)
    assert plan.counts()["set_payload"] == 1
    apply_plan(client, CONFIG, CONFIG.collection, plan, [moved], embedder)
    assert count(client) == 1
    stored = client.retrieve(CONFIG.collection, ids=[point_id("e03")], with_payload=True)[0]
    assert stored.payload["path"] == "cards/moved/e03.md"

    state = {"e03": state_for(moved)}
    edited = card("e03", "Error E03 - hardware current too large", body="EDITED body.", path="cards/moved/e03.md")
    apply_plan(
        client, CONFIG, CONFIG.collection, plan_sync([edited], state), [edited], embedder
    )
    assert count(client) == 1
    stored = client.retrieve(CONFIG.collection, ids=[point_id("e03")], with_payload=True)[0]
    assert stored.payload["body"] == "EDITED body."

    state = {"e03": state_for(edited)}
    apply_plan(client, CONFIG, CONFIG.collection, plan_sync([], state, delete_ratio_limit=1.0), [], embedder)
    assert count(client) == 0


def test_full_text_index_separates_lookalike_codes(client):
    embedder = ConstantEmbedder()
    ensure_collection(client, CONFIG, CONFIG.collection)
    cards = [
        card("e03", "Error E03 - hardware current too large", body="The hardware current is too large."),
        card("e3", "Error E3 - incline adjustment error", body="The incline motor stalled."),
        card("e31", "Error E31 - over temperature", body="The controller is too hot."),
    ]
    apply_plan(client, CONFIG, CONFIG.collection, plan_sync(cards, {}), cards, embedder)

    hits, _ = client.scroll(
        CONFIG.collection,
        scroll_filter=models.Filter(
            must=[models.FieldCondition(key="text", match=models.MatchText(text="e31"))]
        ),
        limit=10,
        with_payload=True,
    )
    assert {h.payload["card_id"] for h in hits} == {"e31"}


def test_facet_index_filters_by_model(client):
    embedder = ConstantEmbedder()
    ensure_collection(client, CONFIG, CONFIG.collection)
    cards = [
        card("f63-e03", "Error E03 on treadmill", model="f63"),
        card("e95-e03", "Error E03 on elliptical", model="e95"),
    ]
    apply_plan(client, CONFIG, CONFIG.collection, plan_sync(cards, {}), cards, embedder)

    hits, _ = client.scroll(
        CONFIG.collection,
        scroll_filter=models.Filter(
            must=[models.FieldCondition(key="facets.applies_to", match=models.MatchValue(value="f63"))]
        ),
        limit=10,
        with_payload=True,
    )
    assert {h.payload["card_id"] for h in hits} == {"f63-e03"}

from pathlib import Path

import pytest
from qdrant_client import models

from kb.card import parse_card
from kb.cli import default_stamp
from kb.config import FacetSpec, KbConfig
from kb.ids import point_id
from kb.qdrant import (
    VECTOR_NAME,
    AliasConflictError,
    apply_plan,
    ensure_alias,
    ensure_collection,
    rebuild,
)
from kb.state import read_state, state_for
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
        # Qdrant answers true for an alias name too.
        return name in self._collections or name in {a.alias_name for a in self._aliases}

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


class FakeRecord:
    def __init__(self, id, payload):
        self.id = id
        self.payload = payload


class ScrollClient:
    """Replays what the FakeClient was told to write, the way read_state sees it."""

    def __init__(self, records, name="kb"):
        self._records = records
        self._name = name

    def collection_exists(self, name):
        return name == self._name

    def scroll(self, collection_name, limit, offset, with_payload, with_vectors):
        return list(self._records), None


def collection_records(client):
    by_id = {str(point.id): dict(point.payload) for point in client.upserted}
    for write in client.payload_sets:
        for pid in write["points"]:
            by_id.setdefault(str(pid), {}).update(write["payload"])
    return [FakeRecord(pid, payload) for pid, payload in by_id.items()]


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


def aliases_of(client) -> dict:
    return {a.alias_name: a.collection_name for a in client.get_aliases().aliases}


def test_first_sync_creates_a_stamped_collection_behind_the_alias():
    client = FakeClient()
    name = ensure_alias(client, CONFIG, "20260821")
    assert name == CONFIG.collection
    assert client.created[0]["name"] == "kb_20260821"
    assert aliases_of(client) == {"kb": "kb_20260821"}


def test_a_later_sync_reuses_the_existing_alias():
    client = FakeClient()
    ensure_alias(client, CONFIG, "20260821")
    client.created.clear()
    name = ensure_alias(client, CONFIG, "20260822")
    assert name == CONFIG.collection
    assert client.created == []
    assert aliases_of(client) == {"kb": "kb_20260821"}


def test_sync_refuses_a_concrete_collection_holding_the_alias_name():
    client = FakeClient(exists=True)
    with pytest.raises(AliasConflictError, match="--rebuild"):
        ensure_alias(client, CONFIG, "20260821")


def test_rebuild_aborts_before_embedding_when_a_concrete_collection_holds_the_alias_name():
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    with pytest.raises(AliasConflictError, match="--rebuild"):
        rebuild(client, CONFIG, [card()], embedder, "20260821")
    assert embedder.seen == []
    assert client.created == []
    assert client.alias_ops == []


def test_apply_plan_addresses_the_alias_not_the_backing_collection():
    client, embedder = FakeClient(), FakeEmbedder()
    name = ensure_alias(client, CONFIG, "20260821")
    cards = [card()]
    apply_plan(client, CONFIG, name, plan_sync(cards, {}), cards, embedder)
    assert client.upsert_targets == ["kb"]


def test_a_first_sync_then_a_rebuild_leaves_the_alias_on_the_newest_collection():
    client, embedder = FakeClient(), FakeEmbedder()
    cards = [card()]
    name = ensure_alias(client, CONFIG, "20260821")
    apply_plan(client, CONFIG, name, plan_sync(cards, {}), cards, embedder)

    target = rebuild(client, CONFIG, cards, embedder, "20260822")
    assert target == "kb_20260822"
    assert aliases_of(client) == {"kb": "kb_20260822"}
    assert client.deleted_collections == ["kb_20260821"]


def test_ensure_alias_indexes_the_collection_it_creates():
    client = FakeClient()
    ensure_alias(client, CONFIG, "20260821")
    assert set(client.indexes) == {
        "text",
        "card_id",
        "authority",
        "facets.model",
        "facets.applies_to",
    }


def test_a_same_day_sync_then_rebuild_is_refused_before_it_touches_anything():
    """The CLI derives one stamp for both modes, so on the day the alias is first
    created the rebuild target is the collection the alias already resolves to."""
    client, embedder = FakeClient(), FakeEmbedder()
    stamp = default_stamp()
    cards = [card()]

    name = ensure_alias(client, CONFIG, stamp)
    apply_plan(client, CONFIG, name, plan_sync(cards, {}), cards, embedder)
    live = aliases_of(client)[CONFIG.collection]
    embedder.seen.clear()
    client.calls.clear()

    with pytest.raises(AliasConflictError, match="--stamp"):
        rebuild(client, CONFIG, cards, embedder, stamp)

    assert embedder.seen == []
    assert client.deleted_collections == []
    assert client.calls == []
    assert aliases_of(client)[CONFIG.collection] == live
    assert client.collection_exists(live)


def test_upsert_payload_carries_both_sync_hashes():
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    cards = [card()]
    apply_plan(client, CONFIG, "kb", plan_sync(cards, {}), cards, embedder)
    written = client.upserted[0].payload
    expected = state_for(cards[0])
    assert written["embed_hash"] == expected.embed_hash
    assert written["payload_hash"] == expected.payload_hash


def test_set_payload_carries_both_sync_hashes():
    original = card()
    moved = parse_card(
        TEMPLATE.format(id="card-a", model="e95", body="Body."), "cards/other/card-a.md"
    )
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    plan = plan_sync([moved], {"card-a": state_for(original)})
    apply_plan(client, CONFIG, "kb", plan, [moved], embedder)

    written = client.payload_sets[0]["payload"]
    expected = state_for(moved)
    assert written["embed_hash"] == expected.embed_hash
    assert written["payload_hash"] == expected.payload_hash
    assert written["payload_hash"] != state_for(original).payload_hash


def test_rebuild_payloads_carry_both_sync_hashes():
    client, embedder = FakeClient(), FakeEmbedder()
    cards = [card("card-a"), card("card-b", model="e95")]
    rebuild(client, CONFIG, cards, embedder, "stamp")

    written = {point.payload["card_id"]: point.payload for point in client.upserted}
    for one in cards:
        expected = state_for(one)
        assert written[one.id]["embed_hash"] == expected.embed_hash
        assert written[one.id]["payload_hash"] == expected.payload_hash


def test_an_upsert_read_back_plans_skip_for_every_card():
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    cards = [card("card-a"), card("card-b", model="e95"), card("card-c", body="Other.")]
    apply_plan(client, CONFIG, "kb", plan_sync(cards, {}), cards, embedder)

    state = read_state(ScrollClient(collection_records(client)), "kb")
    assert set(state) == {"card-a", "card-b", "card-c"}
    assert state["card-a"].point_id == point_id("card-a")
    assert plan_sync(cards, state).counts() == {
        "upsert": 0,
        "set_payload": 0,
        "delete": 0,
        "skip": 3,
    }


def test_a_set_payload_read_back_plans_skip_and_does_not_repeat_for_ever():
    original = card()
    moved = parse_card(
        TEMPLATE.format(id="card-a", model="e95", body="Body."), "cards/other/card-a.md"
    )
    client, embedder = FakeClient(exists=True), FakeEmbedder()
    apply_plan(client, CONFIG, "kb", plan_sync([original], {}), [original], embedder)

    state = read_state(ScrollClient(collection_records(client)), "kb")
    plan = plan_sync([moved], state)
    assert plan.counts()["set_payload"] == 1
    apply_plan(client, CONFIG, "kb", plan, [moved], embedder)

    state = read_state(ScrollClient(collection_records(client)), "kb")
    assert plan_sync([moved], state).counts() == {
        "upsert": 0,
        "set_payload": 0,
        "delete": 0,
        "skip": 1,
    }

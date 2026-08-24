from qdrant_client import models

from kb.card import parse_card
from kb.ids import embed_hash, point_id
from kb.payload import payload_hash
from kb.state import CardState, read_state, state_for
from kb.syncplan import plan_sync

SAMPLE = """---
id: card-a
title: T
kind: fact
question: Q?
asked_as: [one, two]
keywords: [a, b, c, d]
facets:
  model: f63
authority: 3
not_to_be_confused_with: []
see_also: []
source:
  ref: s
  locator: p.1
  extracted_at: 2026-08-21
---

Body.
"""


class FakeClient:
    def __init__(self, pages=(), exists=True, name="kb"):
        self._collections = {name} if exists else set()
        self._pages = list(pages)
        self.scrolls = []

    def collection_exists(self, name):
        return name in self._collections

    def scroll(self, collection_name, **kwargs):
        self.scrolls.append({"collection_name": collection_name, **kwargs})
        if not self._pages:
            return [], None
        return self._pages.pop(0)


def record(card_id="card-a", record_id=None, **payload):
    body = {"card_id": card_id} if card_id is not None else {}
    body.update(payload)
    return models.Record(id=record_id or point_id(card_id or "card-a"), payload=body)


def test_state_for_uses_the_three_derived_values():
    card = parse_card(SAMPLE, "cards/a.md")
    assert state_for(card) == CardState(
        embed_hash=embed_hash(card),
        payload_hash=payload_hash(card),
        point_id=point_id(card.id),
    )


def test_a_missing_collection_is_empty_state_and_never_scrolls():
    client = FakeClient(exists=False)
    assert read_state(client, "kb") == {}
    assert client.scrolls == []


def test_one_page_yields_a_card_state_per_record():
    client = FakeClient(
        pages=[
            (
                [
                    record("card-a", embed_hash="e-a", payload_hash="p-a"),
                    record("card-b", embed_hash="e-b", payload_hash="p-b"),
                ],
                None,
            )
        ]
    )
    state = read_state(client, "kb")
    assert set(state) == {"card-a", "card-b"}
    assert state["card-a"].embed_hash == "e-a"
    assert state["card-a"].payload_hash == "p-a"
    assert state["card-b"].embed_hash == "e-b"


def test_point_id_comes_from_the_record_not_from_the_card_id():
    client = FakeClient(
        pages=[([record("card-a", record_id=4242, embed_hash="e", payload_hash="p")], None)]
    )
    state = read_state(client, "kb")
    assert state["card-a"].point_id == "4242"
    assert state["card-a"].point_id != point_id("card-a")


def test_scrolling_follows_the_offset_until_it_is_none():
    client = FakeClient(
        pages=[
            ([record("card-a", embed_hash="e-a", payload_hash="p-a")], "page-2"),
            ([record("card-b", embed_hash="e-b", payload_hash="p-b")], None),
        ]
    )
    state = read_state(client, "kb")
    assert set(state) == {"card-a", "card-b"}
    assert len(client.scrolls) == 2
    assert client.scrolls[0]["offset"] is None
    assert client.scrolls[1]["offset"] == "page-2"


def test_a_record_without_a_card_id_is_skipped():
    client = FakeClient(
        pages=[
            (
                [
                    record(None, record_id=1, embed_hash="e", payload_hash="p"),
                    record("card-a", embed_hash="e-a", payload_hash="p-a"),
                ],
                None,
            )
        ]
    )
    assert set(read_state(client, "kb")) == {"card-a"}


def test_a_record_with_no_payload_at_all_is_skipped():
    client = FakeClient(
        pages=[([models.Record(id=1, payload=None), record("card-a")], None)]
    )
    assert set(read_state(client, "kb")) == {"card-a"}


def test_a_missing_hash_reads_as_empty_and_plans_an_upsert():
    card = parse_card(SAMPLE, "cards/a.md")
    client = FakeClient(pages=[([record("card-a", payload_hash=payload_hash(card))], None)])
    state = read_state(client, "kb")
    assert state["card-a"].embed_hash == ""
    plan = plan_sync([card], state)
    assert [action.op for action in plan.actions] == ["upsert"]


def test_scroll_asks_for_the_three_state_fields_and_no_vectors():
    client = FakeClient()
    read_state(client, "kb")
    call = client.scrolls[0]
    assert call["collection_name"] == "kb"
    assert call["with_vectors"] is False
    assert list(call["with_payload"]) == ["card_id", "embed_hash", "payload_hash"]

import pytest

from kb.card import parse_card
from kb.state import CardState, state_for
from kb.syncplan import DangerousSyncError, plan_sync

TEMPLATE = """---
id: {id}
title: T
kind: fact
question: Q?
asked_as: [one, two]
keywords: [a, b, c, d]
facets:
  model: {model}
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


def card(id="card-a", model="f63", body="Body.", path=None):
    return parse_card(
        TEMPLATE.format(id=id, model=model, body=body), path or f"cards/{id}.md"
    )


def ops(plan):
    return {a.card_id: a.op for a in plan.actions}


def test_new_card_is_upserted():
    plan = plan_sync([card()], {})
    assert ops(plan) == {"card-a": "upsert"}


def test_unchanged_card_is_skipped():
    original = card()
    plan = plan_sync([original], {"card-a": state_for(original)})
    assert ops(plan) == {"card-a": "skip"}


def test_body_change_forces_a_re_embed():
    original = card()
    edited = card(body="Different body.")
    plan = plan_sync([edited], {"card-a": state_for(original)})
    assert ops(plan) == {"card-a": "upsert"}


def test_facet_only_change_sets_payload_without_embedding():
    original = card()
    edited = card(model="e95")
    plan = plan_sync([edited], {"card-a": state_for(original)})
    assert ops(plan) == {"card-a": "set_payload"}


def test_path_only_change_sets_payload_without_embedding():
    original = card()
    moved = card(path="cards/treadmill/f63/faults/card-a.md")
    plan = plan_sync([moved], {"card-a": state_for(original)})
    assert ops(plan) == {"card-a": "set_payload"}


def test_deleted_card_is_deleted():
    original = card()
    plan = plan_sync([], {"card-a": state_for(original)}, delete_ratio_limit=1.0)
    assert ops(plan) == {"card-a": "delete"}


def test_counts_reports_each_operation():
    kept = card("kept")
    gone = card("gone")
    state = {"kept": state_for(kept), "gone": state_for(gone)}
    plan = plan_sync([kept, card("fresh")], state, delete_ratio_limit=1.0)
    assert plan.counts() == {"upsert": 1, "set_payload": 0, "delete": 1, "skip": 1}


def test_deleting_more_than_the_limit_raises():
    state = {f"c{i}": CardState("e", "p", "id") for i in range(10)}
    cards = [card(f"c{i}") for i in range(8)]
    with pytest.raises(DangerousSyncError, match="2 of 10"):
        plan_sync(cards, state)


def test_deleting_exactly_at_the_limit_is_allowed():
    state = {f"c{i}": CardState("e", "p", "id") for i in range(10)}
    cards = [card(f"c{i}") for i in range(9)]
    plan = plan_sync(cards, state)
    assert plan.counts()["delete"] == 1


def test_limit_can_be_disabled():
    state = {f"c{i}": CardState("e", "p", "id") for i in range(10)}
    plan = plan_sync([], state, delete_ratio_limit=1.0)
    assert plan.counts()["delete"] == 10


def test_empty_state_never_trips_the_limit():
    plan = plan_sync([card()], {})
    assert plan.counts()["upsert"] == 1

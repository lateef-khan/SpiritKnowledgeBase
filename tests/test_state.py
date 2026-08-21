from kb.card import parse_card
from kb.ids import embed_hash, point_id
from kb.payload import payload_hash
from kb.state import CardState, load_state, save_state, state_for

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


def test_state_for_uses_the_three_derived_values():
    card = parse_card(SAMPLE, "cards/a.md")
    assert state_for(card) == CardState(
        embed_hash=embed_hash(card),
        payload_hash=payload_hash(card),
        point_id=point_id(card.id),
    )


def test_round_trips(tmp_path):
    card = parse_card(SAMPLE, "cards/a.md")
    save_state(tmp_path, {"card-a": state_for(card)})
    assert load_state(tmp_path) == {"card-a": state_for(card)}


def test_missing_state_is_empty(tmp_path):
    assert load_state(tmp_path) == {}


def test_saved_state_is_sorted_and_stable(tmp_path):
    card = parse_card(SAMPLE, "cards/a.md")
    other = parse_card(SAMPLE.replace("id: card-a", "id: card-b"), "cards/b.md")
    save_state(tmp_path, {"card-b": state_for(other), "card-a": state_for(card)})
    first = (tmp_path / ".kb-state.json").read_text()
    save_state(tmp_path, load_state(tmp_path))
    assert (tmp_path / ".kb-state.json").read_text() == first
    assert first.index('"card-a"') < first.index('"card-b"')

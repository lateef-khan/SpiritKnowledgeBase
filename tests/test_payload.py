from kb.card import parse_card
from kb.ids import point_id, retrieval_text
from kb.payload import build_payload

SAMPLE = """---
id: f63-e03-overcurrent
title: Error E03
kind: troubleshooting
question: What does E03 mean?
asked_as:
  - the screen says E03
keywords: [e03, overcurrent]
facets:
  model: f63
  applies_to: [f63, f63-2026]
  section: errors
authority: 3
not_to_be_confused_with: [f63-e3-incline]
see_also: [f63-electrical]
source:
  ref: 2026-f63-om
  locator: p.27
  extracted_at: 2026-08-21
---

Body text here.
"""


def test_payload_carries_identity_and_citation():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    payload = build_payload(card)
    assert payload["card_id"] == "f63-e03-overcurrent"
    assert payload["path"] == "cards/f63/errors/e03.md"
    assert payload["source"] == {
        "ref": "2026-f63-om",
        "locator": "p.27",
        "extracted_at": "2026-08-21",
    }


def test_text_is_retrieval_text_and_body_is_clean():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    payload = build_payload(card)
    assert payload["text"] == retrieval_text(card)
    assert payload["body"] == "Body text here."
    assert "the screen says E03" not in payload["body"]


def test_facets_are_nested_under_one_key():
    payload = build_payload(parse_card(SAMPLE, "cards/f63/errors/e03.md"))
    assert payload["facets"]["model"] == "f63"
    assert payload["facets"]["applies_to"] == ["f63", "f63-2026"]


def test_payload_has_no_none_values():
    payload = build_payload(parse_card(SAMPLE, "cards/f63/errors/e03.md"))
    assert None not in payload.values()

from kb.card import parse_card
from kb.ids import retrieval_text
from kb.payload import EXCLUDED_FROM_HASH, build_payload, payload_hash

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


def card(text: str = SAMPLE, path: str = "cards/f63/errors/e03.md"):
    return parse_card(text, path)


def test_payload_carries_identity_and_citation():
    payload = build_payload(card())
    assert payload["card_id"] == "f63-e03-overcurrent"
    assert payload["path"] == "cards/f63/errors/e03.md"
    assert payload["source"] == {
        "ref": "2026-f63-om",
        "locator": "p.27",
        "extracted_at": "2026-08-21",
    }


def test_text_is_retrieval_text_and_body_is_clean():
    payload = build_payload(card())
    assert payload["text"] == retrieval_text(card())
    assert payload["body"] == "Body text here."
    assert "the screen says E03" not in payload["body"]


def test_facets_are_nested_under_one_key():
    payload = build_payload(card())
    assert payload["facets"]["model"] == "f63"
    assert payload["facets"]["applies_to"] == ["f63", "f63-2026"]


def test_payload_has_no_none_values():
    payload = build_payload(card())
    assert None not in payload.values()


def test_payload_hash_changes_when_path_changes():
    moved = card(path="cards/treadmill/f63/faults/e03.md")
    assert payload_hash(moved) != payload_hash(card())


def test_payload_hash_changes_when_facets_change():
    edited = card(SAMPLE.replace("model: f63", "model: e95"))
    assert payload_hash(edited) != payload_hash(card())


def test_payload_hash_ignores_body():
    edited = card(SAMPLE.replace("Body text here.", "Different body."))
    assert payload_hash(edited) == payload_hash(card())


def test_payload_hash_is_key_order_independent():
    reordered = SAMPLE.replace(
        "facets:\n  model: f63\n  applies_to: [f63, f63-2026]\n  section: errors\nauthority: 3",
        "authority: 3\nfacets:\n  model: f63\n  applies_to: [f63, f63-2026]\n  section: errors",
    )
    assert payload_hash(card(reordered)) == payload_hash(card())


def test_payload_hash_handles_date_valued_facets():
    dated = card(SAMPLE.replace("  section: errors", "  section: errors\n  reviewed: 2026-08-21"))
    payload_hash(dated)
    assert build_payload(dated)["facets"]["reviewed"] == "2026-08-21"


def test_hashed_keys_are_payload_keys_minus_excluded():
    assert EXCLUDED_FROM_HASH == {"card_id", "title", "question", "text", "body"}
    payload = build_payload(card())
    assert set(payload) - EXCLUDED_FROM_HASH == {
        "kind",
        "path",
        "authority",
        "facets",
        "see_also",
        "not_to_be_confused_with",
        "source",
    }

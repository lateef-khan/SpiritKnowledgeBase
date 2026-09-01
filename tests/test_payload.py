from kb.card import parse_card
from kb.ids import embed_hash, retrieval_text
from kb.payload import (
    EXCLUDED_FROM_HASH,
    STATE_FIELDS,
    build_payload,
    build_point_payload,
    payload_hash,
)

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
        "title": "2026-f63-om",
        "locator": "p.27",
        "extracted_at": "2026-08-21",
    }


def test_source_title_is_used_for_the_citation_when_the_manifest_holds_one():
    from dataclasses import replace

    titled = replace(card(), source_title="Spirit F63 owner's manual (curated notes)")
    assert build_payload(titled)["source"]["title"] == (
        "Spirit F63 owner's manual (curated notes)"
    )
    # The ref stays beside it: the title is what the model reads, the ref is what identifies it.
    assert build_payload(titled)["source"]["ref"] == "2026-f63-om"


def test_source_title_change_moves_the_payload_hash_and_not_the_embed_hash():
    from dataclasses import replace

    # A retitled source must be re-upserted, and must NOT be re-embedded: the vector is hashed off
    # the retrieval text, which a title change does not touch.
    titled = replace(card(), source_title="Spirit F63 owner's manual (curated notes)")
    assert payload_hash(titled) != payload_hash(card())
    assert embed_hash(titled) == embed_hash(card())


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
    assert EXCLUDED_FROM_HASH == {
        "card_id",
        "title",
        "question",
        "text",
        "body",
        "embed_hash",
        "payload_hash",
    }
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


HEX_DIGITS = set("0123456789abcdef")


def is_sha256_hex(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and set(value) <= HEX_DIGITS


def test_build_payload_carries_no_state():
    payload = build_payload(card())
    for field in STATE_FIELDS:
        assert field not in payload


def test_point_payload_carries_both_hashes():
    point = build_point_payload(card())
    assert is_sha256_hex(point["embed_hash"])
    assert is_sha256_hex(point["payload_hash"])


def test_point_payload_hashes_match_the_standalone_functions():
    point = build_point_payload(card())
    assert point["payload_hash"] == payload_hash(card())
    assert point["embed_hash"] == embed_hash(card())


def test_point_payload_is_the_base_payload_plus_state():
    payload = build_payload(card())
    point = build_point_payload(card())
    for key, value in payload.items():
        assert point[key] == value
    assert set(point) - set(payload) == set(STATE_FIELDS)


def test_body_edit_moves_only_the_embed_hash():
    edited = card(SAMPLE.replace("Body text here.", "Different body."))
    before = build_point_payload(card())
    after = build_point_payload(edited)
    assert before["payload_hash"] == after["payload_hash"]
    assert before["embed_hash"] != after["embed_hash"]


def test_point_payload_handles_date_valued_facets():
    dated = card(SAMPLE.replace("  section: errors", "  section: errors\n  reviewed: 2026-08-21"))
    point = build_point_payload(dated)
    assert point["facets"]["reviewed"] == "2026-08-21"
    assert is_sha256_hex(point["payload_hash"])

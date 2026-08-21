import uuid

from kb.card import parse_card
from kb.ids import embed_hash, payload_hash, point_id, retrieval_text

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
authority: 3
not_to_be_confused_with: []
see_also: []
source:
  ref: 2026-f63-om
  locator: p.27
  extracted_at: 2026-08-21
---

Body text here.
"""


def card(text: str = SAMPLE, path: str = "cards/f63/errors/e03.md"):
    return parse_card(text, path)


def test_point_id_matches_uuid5_of_prefixed_id():
    assert point_id("f63-e03-overcurrent") == str(
        uuid.uuid5(uuid.NAMESPACE_URL, "kb:f63-e03-overcurrent")
    )


def test_point_id_is_stable_and_distinct():
    assert point_id("a") == point_id("a")
    assert point_id("a") != point_id("b")


def test_retrieval_text_contains_every_retrieval_signal():
    text = retrieval_text(card())
    assert "Error E03" in text
    assert "What does E03 mean?" in text
    assert "the screen says E03" in text
    assert "e03, overcurrent" in text
    assert "Body text here." in text


def test_embed_hash_ignores_facets_and_path():
    moved = card(path="cards/treadmill/f63/faults/e03.md")
    changed_facet = card(SAMPLE.replace("model: f63", "model: f63x"))
    assert embed_hash(moved) == embed_hash(card())
    assert embed_hash(changed_facet) == embed_hash(card())


def test_embed_hash_changes_when_body_changes():
    edited = card(SAMPLE.replace("Body text here.", "Different body."))
    assert embed_hash(edited) != embed_hash(card())


def test_embed_hash_changes_when_asked_as_changes():
    edited = card(SAMPLE.replace("the screen says E03", "screen shows E03"))
    assert embed_hash(edited) != embed_hash(card())


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
        "facets:\n  model: f63\nauthority: 3",
        "authority: 3\nfacets:\n  model: f63",
    )
    assert payload_hash(card(reordered)) == payload_hash(card())

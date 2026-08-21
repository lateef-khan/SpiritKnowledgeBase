import pytest

from kb.card import (
    Card,
    CardParseError,
    load_cards,
    load_cards_leniently,
    parse_card,
    render_card,
)

SAMPLE = """---
id: f63-e03-overcurrent
title: Error E03 - hardware current too large
kind: troubleshooting
question: What does E03 mean on an F63 treadmill?
asked_as:
  - the screen says E03
  - error 3 hardware
keywords: [e03, overcurrent, breaker, controller]
facets:
  model: f63
  applies_to: [f63, f63-2026]
  section: errors
authority: 3
not_to_be_confused_with: [f63-e3-incline]
see_also: [f63-electrical-requirements]
source:
  ref: 2026-f63-om
  locator: p.27
  extracted_at: 2026-08-21
---

# Error E03 - hardware current too large

The hardware current is too large.
"""


def test_parses_scalar_fields():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    assert card.id == "f63-e03-overcurrent"
    assert card.kind == "troubleshooting"
    assert card.authority == 3
    assert card.path == "cards/f63/errors/e03.md"


def test_parses_sequences_as_tuples():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    assert card.asked_as == ("the screen says E03", "error 3 hardware")
    assert card.keywords == ("e03", "overcurrent", "breaker", "controller")
    assert card.see_also == ("f63-electrical-requirements",)
    assert card.not_to_be_confused_with == ("f63-e3-incline",)


def test_parses_facets_including_arrays():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    assert card.facets["model"] == "f63"
    assert card.facets["applies_to"] == ["f63", "f63-2026"]


def test_body_excludes_frontmatter_and_is_stripped():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    assert card.body.startswith("# Error E03")
    assert "---" not in card.body
    assert card.body.endswith("too large.")


def test_missing_frontmatter_raises():
    with pytest.raises(CardParseError, match="frontmatter"):
        parse_card("# Just a heading\n", "cards/x.md")


def test_unterminated_frontmatter_raises():
    with pytest.raises(CardParseError, match="frontmatter"):
        parse_card("---\nid: x\n\n# body\n", "cards/x.md")


def test_missing_required_key_raises():
    bad = SAMPLE.replace("kind: troubleshooting\n", "")
    with pytest.raises(CardParseError, match="kind"):
        parse_card(bad, "cards/x.md")


def test_missing_source_subkey_raises():
    bad = SAMPLE.replace("  locator: p.27\n", "")
    with pytest.raises(CardParseError, match="source.locator"):
        parse_card(bad, "cards/x.md")


def test_render_round_trips():
    card = parse_card(SAMPLE, "cards/f63/errors/e03.md")
    again = parse_card(render_card(card), "cards/f63/errors/e03.md")
    assert again == card


def test_load_cards_walks_tree_sorted(tmp_path):
    (tmp_path / "cards" / "b").mkdir(parents=True)
    (tmp_path / "cards" / "a").mkdir(parents=True)
    (tmp_path / "cards" / "b" / "two.md").write_text(SAMPLE)
    (tmp_path / "cards" / "a" / "one.md").write_text(
        SAMPLE.replace("id: f63-e03-overcurrent", "id: other-card")
    )
    cards = load_cards(tmp_path)
    assert [c.path for c in cards] == ["cards/a/one.md", "cards/b/two.md"]
    assert isinstance(cards[0], Card)


def test_load_cards_leniently_separates_the_broken_from_the_good(tmp_path):
    (tmp_path / "cards").mkdir()
    (tmp_path / "cards" / "good.md").write_text(SAMPLE)
    (tmp_path / "cards" / "broken.md").write_text("---\nid: broken\n")
    cards, failures = load_cards_leniently(tmp_path)
    assert [c.path for c in cards] == ["cards/good.md"]
    assert [f.path for f in failures] == ["cards/broken.md"]
    assert "unterminated frontmatter" in failures[0].message
    assert not failures[0].message.startswith("cards/broken.md")


def test_load_cards_still_raises_on_a_broken_card(tmp_path):
    (tmp_path / "cards").mkdir()
    (tmp_path / "cards" / "broken.md").write_text("---\nid: broken\n")
    with pytest.raises(CardParseError, match="unterminated"):
        load_cards(tmp_path)

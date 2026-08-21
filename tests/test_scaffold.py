from pathlib import Path

import pytest

from kb.card import parse_card
from kb.config import FacetSpec, KbConfig
from kb.lint import lint_cards
from kb.scaffold import ScaffoldError, card_path, new_card_text

CONFIG = KbConfig(
    root=Path("."),
    collection="kb",
    embedding_model="text-embedding-3-small",
    embedding_dimensions=1024,
    kinds=("fact", "troubleshooting"),
    facets={
        "model": FacetSpec(index="keyword", array=False, values=("f63", "*")),
        "applies_to": FacetSpec(index="keyword", array=True, values=()),
    },
    payload_indexes={},
    pdf_command=None,
)


def test_scaffold_parses_as_a_card():
    card = parse_card(new_card_text("new-card", CONFIG, "2026-08-21"), "cards/new-card.md")
    assert card.id == "new-card"
    assert card.source_extracted_at == "2026-08-21"


def test_scaffold_declares_every_facet_with_a_sentinel():
    card = parse_card(new_card_text("new-card", CONFIG, "2026-08-21"), "cards/new-card.md")
    assert card.facets["model"] == "*"
    assert card.facets["applies_to"] == ["*"]


def test_scaffold_uses_the_first_declared_kind():
    card = parse_card(new_card_text("new-card", CONFIG, "2026-08-21"), "cards/new-card.md")
    assert card.kind == "fact"


def test_scaffold_fails_lint_only_on_the_placeholder_source():
    card = parse_card(new_card_text("new-card", CONFIG, "2026-08-21"), "cards/new-card.md")
    checks = {e.check for e in lint_cards([card], CONFIG, set())}
    assert checks == {"unknown-source"}


def test_scaffold_fails_lint_only_on_the_placeholder_source_for_a_hyphenated_id():
    card_id = "f63-e03-overcurrent"
    card = parse_card(new_card_text(card_id, CONFIG, "2026-08-21"), f"cards/{card_id}.md")
    checks = {e.check for e in lint_cards([card], CONFIG, set())}
    assert checks == {"unknown-source"}


def test_card_path_places_a_slug_id_under_cards(tmp_path):
    assert card_path(tmp_path, "f63-e03-overcurrent") == tmp_path / "cards" / "f63-e03-overcurrent.md"


@pytest.mark.parametrize(
    "card_id",
    ["../../escaped", "../evil", "f63/errors/e03", "F63-E03", "e03 overcurrent", "-leading", "trailing-", "e03--double", ""],
)
def test_card_path_refuses_an_id_that_is_not_a_slug(tmp_path, card_id):
    with pytest.raises(ScaffoldError):
        card_path(tmp_path, card_id)


def test_card_path_refuses_an_absolute_id(tmp_path):
    with pytest.raises(ScaffoldError):
        card_path(tmp_path, "/etc/passwd")

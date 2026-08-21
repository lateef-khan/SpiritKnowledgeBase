from __future__ import annotations

import re
from pathlib import Path

from kb.card import Card, render_card
from kb.config import KbConfig

SENTINEL = "*"
TITLE_PLACEHOLDER = "REPLACE WITH THE QUESTION THIS CARD ANSWERS"
CARD_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ScaffoldError(Exception):
    pass


def card_path(root: Path, card_id: str) -> Path:
    """Resolve where `kb new <card_id>` writes, refusing anything but a slug.

    Spec 4.1 makes the card id permanent -- it derives the Qdrant point id --
    so it is worth more scrutiny than a filename, not less.
    """
    if not CARD_ID_PATTERN.match(card_id):
        raise ScaffoldError(
            f"card id {card_id!r} is invalid; ids are lowercase words joined by "
            "single hyphens, for example 'f63-e03-overcurrent'"
        )

    cards_root = Path(root) / "cards"
    target = cards_root / f"{card_id}.md"
    if not target.resolve().is_relative_to(cards_root.resolve()):
        raise ScaffoldError(f"card id {card_id!r} escapes the cards directory")
    return target


def new_card_text(card_id: str, config: KbConfig, today: str) -> str:
    facets: dict[str, object] = {}
    for name, spec in config.facets.items():
        facets[name] = [SENTINEL] if spec.array else SENTINEL

    card = Card(
        id=card_id,
        title=TITLE_PLACEHOLDER,
        kind=config.kinds[0],
        question=f"What is {card_id}?",
        asked_as=("first customer phrasing", "second customer phrasing"),
        keywords=("keyword-one", "keyword-two", "keyword-three", "keyword-four"),
        facets=facets,
        authority=3,
        not_to_be_confused_with=(),
        see_also=(),
        source_ref="REPLACE-WITH-SOURCE-ID",
        source_locator="REPLACE-WITH-PAGE-OR-LINE",
        source_extracted_at=today,
        body="Replace this body with the answer.",
        path=f"cards/{card_id}.md",
    )
    return render_card(card)

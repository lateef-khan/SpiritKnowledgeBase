from __future__ import annotations

from kb.card import Card, render_card
from kb.config import KbConfig

SENTINEL = "*"
TITLE_PLACEHOLDER = "REPLACE WITH THE QUESTION THIS CARD ANSWERS"


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

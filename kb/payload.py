from __future__ import annotations

from kb.card import Card
from kb.ids import retrieval_text


def build_payload(card: Card) -> dict:
    return {
        "card_id": card.id,
        "title": card.title,
        "kind": card.kind,
        "question": card.question,
        "text": retrieval_text(card),
        "body": card.body,
        "path": card.path,
        "authority": card.authority,
        "facets": dict(card.facets),
        "see_also": list(card.see_also),
        "not_to_be_confused_with": list(card.not_to_be_confused_with),
        "source": {
            "ref": card.source_ref,
            "locator": card.source_locator,
            "extracted_at": card.source_extracted_at,
        },
    }

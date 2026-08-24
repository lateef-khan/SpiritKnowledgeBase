from __future__ import annotations

from dataclasses import dataclass

from kb.card import Card
from kb.ids import embed_hash, point_id
from kb.payload import STATE_FIELDS, payload_hash

SCROLL_FIELDS = ("card_id", *STATE_FIELDS)
SCROLL_PAGE_SIZE = 256


@dataclass(frozen=True)
class CardState:
    embed_hash: str
    payload_hash: str
    point_id: str


def state_for(card: Card) -> CardState:
    return CardState(
        embed_hash=embed_hash(card),
        payload_hash=payload_hash(card),
        point_id=point_id(card.id),
    )


def read_state(client, name: str) -> dict[str, CardState]:
    """Rebuild the sync state from the collection itself. Never creates anything."""
    if not client.collection_exists(name):
        return {}

    state: dict[str, CardState] = {}
    offset = None
    while True:
        records, offset = client.scroll(
            collection_name=name,
            limit=SCROLL_PAGE_SIZE,
            offset=offset,
            with_payload=list(SCROLL_FIELDS),
            with_vectors=False,
        )
        for record in records:
            payload = record.payload or {}
            card_id = payload.get("card_id")
            if not card_id:
                continue
            # An absent hash becomes "", which can never equal a sha256, so plan_sync
            # schedules a write and the point repairs itself.
            state[card_id] = CardState(
                embed_hash=payload.get("embed_hash") or "",
                payload_hash=payload.get("payload_hash") or "",
                point_id=str(record.id),
            )
        if offset is None:
            return state

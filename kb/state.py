from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from kb.card import Card
from kb.ids import embed_hash, point_id
from kb.payload import payload_hash

STATE_FILENAME = ".kb-state.json"


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


def load_state(root: Path) -> dict[str, CardState]:
    path = Path(root) / STATE_FILENAME
    if not path.is_file():
        return {}
    raw = json.loads(path.read_text())
    return {card_id: CardState(**value) for card_id, value in raw.items()}


def save_state(root: Path, state: dict[str, CardState]) -> None:
    path = Path(root) / STATE_FILENAME
    payload = {card_id: asdict(state[card_id]) for card_id in sorted(state)}
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")

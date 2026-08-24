from __future__ import annotations

from dataclasses import dataclass

from kb.card import Card
from kb.state import CardState, state_for

OPS = ("upsert", "set_payload", "delete", "skip")
DEFAULT_DELETE_RATIO_LIMIT = 0.10


class DangerousSyncError(Exception):
    pass


@dataclass(frozen=True)
class Action:
    op: str
    card_id: str
    point_id: str


@dataclass(frozen=True)
class SyncPlan:
    actions: tuple[Action, ...]

    def counts(self) -> dict[str, int]:
        tally = {op: 0 for op in OPS}
        for action in self.actions:
            tally[action.op] += 1
        return tally


def plan_sync(
    cards: list[Card],
    state: dict[str, CardState],
    delete_ratio_limit: float = DEFAULT_DELETE_RATIO_LIMIT,
) -> SyncPlan:
    fresh = {card.id: state_for(card) for card in cards}
    removed = [card_id for card_id in state if card_id not in fresh]

    if state and len(removed) / len(state) > delete_ratio_limit:
        raise DangerousSyncError(
            f"sync would delete {len(removed)} of {len(state)} points, "
            f"over the {delete_ratio_limit:.0%} limit; pass --force if this is intended"
        )

    actions: list[Action] = []
    for card in cards:
        now = fresh[card.id]
        before = state.get(card.id)
        if before is None or before.embed_hash != now.embed_hash:
            op = "upsert"
        elif before.payload_hash != now.payload_hash:
            op = "set_payload"
        else:
            op = "skip"
        actions.append(Action(op=op, card_id=card.id, point_id=now.point_id))

    for card_id in removed:
        actions.append(Action(op="delete", card_id=card_id, point_id=state[card_id].point_id))

    return SyncPlan(actions=tuple(actions))

from __future__ import annotations

import yaml

from kb.card import Card
from kb.config import KbConfig


def build_vocab(cards: list[Card], config: KbConfig) -> dict:
    facets: dict[str, list[str]] = {}
    for name, spec in config.facets.items():
        observed: set[str] = set(spec.values)
        for card in cards:
            value = card.facets.get(name)
            if isinstance(value, list):
                observed.update(str(item) for item in value)
            elif value is not None:
                observed.add(str(value))
        facets[name] = sorted(observed)

    return {
        "kinds": list(config.kinds),
        "facets": facets,
        "card_ids": sorted(card.id for card in cards),
    }


def render_vocab(vocab: dict) -> str:
    return yaml.safe_dump(vocab, sort_keys=False, allow_unicode=True, default_flow_style=False)

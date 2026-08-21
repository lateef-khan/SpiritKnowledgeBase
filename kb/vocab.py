from __future__ import annotations

import yaml

from kb.card import FACET_SENTINEL, Card
from kb.config import KbConfig


def _values_on_card(card: Card, name: str) -> set[str]:
    value = card.facets.get(name)
    if isinstance(value, list):
        return {str(item) for item in value}
    if value is None:
        return set()
    return {str(value)}


def build_vocab(cards: list[Card], config: KbConfig) -> dict:
    facets: dict[str, list[str]] = {}
    undeclared: dict[str, list[str]] = {}
    for name, spec in config.facets.items():
        declared = set(spec.values)
        observed: set[str] = set()
        for card in cards:
            observed |= _values_on_card(card, name)
        facets[name] = sorted(declared | observed)
        # A facet that declares no values is open by design, so nothing about it is
        # new; the sentinel is the card format's own marker, never invented vocabulary.
        new_values = observed - declared - {FACET_SENTINEL}
        if declared and new_values:
            undeclared[name] = sorted(new_values)

    return {
        "kinds": list(config.kinds),
        "facets": facets,
        "undeclared_facet_values": undeclared,
        "card_ids": sorted(card.id for card in cards),
    }


def render_vocab(vocab: dict) -> str:
    return yaml.safe_dump(vocab, sort_keys=False, allow_unicode=True, default_flow_style=False)

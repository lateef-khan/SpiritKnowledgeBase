from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from kb.card import Card
from kb.config import KbConfig

ASKED_AS_RANGE = (2, 4)
KEYWORDS_RANGE = (4, 10)
CODE_PATTERN = re.compile(r"\b[a-z]{1,2}\d{1,3}\b", re.IGNORECASE)


@dataclass(frozen=True)
class LintError:
    path: str
    check: str
    message: str


def _is_empty(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple)):
        return all(isinstance(item, str) and not item.strip() for item in value)
    if isinstance(value, dict):
        return len(value) == 0
    return False


def lint_cards(cards: list[Card], config: KbConfig, source_refs: set[str]) -> list[LintError]:
    errors: list[LintError] = []
    known_ids = {card.id for card in cards}

    counts = Counter(card.id for card in cards)
    for card in cards:
        if counts[card.id] > 1:
            errors.append(
                LintError(card.path, "unique-id", f"id {card.id!r} is used by {counts[card.id]} cards")
            )

    for card in cards:
        for key, links in (("see_also", card.see_also), ("not_to_be_confused_with", card.not_to_be_confused_with)):
            for link in links:
                if link not in known_ids:
                    errors.append(
                        LintError(card.path, "dangling-link", f"{key} points at unknown id {link!r}")
                    )

        if card.source_ref not in source_refs:
            errors.append(
                LintError(card.path, "unknown-source", f"source.ref {card.source_ref!r} is not in the manifest")
            )

        for key in card.facets:
            if key not in config.facets:
                errors.append(
                    LintError(card.path, "undeclared-facet", f"facet {key!r} is not declared in kb.yaml")
                )
        for key in config.facets:
            if key not in card.facets or _is_empty(card.facets[key]):
                errors.append(
                    LintError(
                        card.path,
                        "empty-facet",
                        f"facet {key!r} is missing or empty; write \"*\" rather than omitting it",
                    )
                )

        if card.kind not in config.kinds:
            errors.append(
                LintError(card.path, "unknown-kind", f"kind {card.kind!r} is not in {list(config.kinds)}")
            )

        for field_name, values, (low, high) in (
            ("asked_as", card.asked_as, ASKED_AS_RANGE),
            ("keywords", card.keywords, KEYWORDS_RANGE),
        ):
            if not low <= len(values) <= high:
                errors.append(
                    LintError(
                        card.path,
                        "list-length",
                        f"{field_name} needs {low}-{high} entries, has {len(values)}",
                    )
                )

        if not card.body.strip():
            errors.append(LintError(card.path, "empty-body", "card body is empty"))

        codes = {match.lower() for match in CODE_PATTERN.findall(card.title)}
        if len(codes) > 1:
            errors.append(
                LintError(
                    card.path,
                    "shared-lookalike",
                    f"title names more than one identifier {sorted(codes)}; split into one card each",
                )
            )

    return errors

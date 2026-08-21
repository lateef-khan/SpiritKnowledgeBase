from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

FENCE = "---"
SCALAR_KEYS = ("id", "title", "kind", "question")
SEQUENCE_KEYS = ("asked_as", "keywords", "not_to_be_confused_with", "see_also")
SOURCE_KEYS = ("ref", "locator", "extracted_at")
# Spec 4.1: write this rather than omitting a facet. group_by drops a point whose
# grouping field is missing.
FACET_SENTINEL = "*"


class CardParseError(Exception):
    pass


@dataclass(frozen=True)
class CardLoadFailure:
    path: str
    message: str


def _without_path(message: str, path: str) -> str:
    prefix = f"{path}: "
    return message[len(prefix) :] if message.startswith(prefix) else message


@dataclass(frozen=True)
class Card:
    id: str
    title: str
    kind: str
    question: str
    asked_as: tuple[str, ...]
    keywords: tuple[str, ...]
    facets: dict[str, object]
    authority: int
    not_to_be_confused_with: tuple[str, ...]
    see_also: tuple[str, ...]
    source_ref: str
    source_locator: str
    source_extracted_at: str
    body: str
    path: str


def _split(text: str, path: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FENCE:
        raise CardParseError(f"{path}: missing frontmatter; a card must open with '---'")
    for index in range(1, len(lines)):
        if lines[index].strip() == FENCE:
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1 :])
    raise CardParseError(f"{path}: unterminated frontmatter; no closing '---'")


def parse_card(text: str, path: str) -> Card:
    front_text, body = _split(text, path)
    try:
        front = yaml.safe_load(front_text) or {}
    except yaml.YAMLError as exc:
        raise CardParseError(f"{path}: frontmatter is not valid YAML: {exc}") from exc
    if not isinstance(front, dict):
        raise CardParseError(f"{path}: frontmatter must be a mapping")

    for key in SCALAR_KEYS:
        value = front.get(key)
        if not isinstance(value, str) or not value.strip():
            raise CardParseError(f"{path}: missing or empty required key {key!r}")

    authority = front.get("authority")
    if not isinstance(authority, int) or isinstance(authority, bool):
        raise CardParseError(f"{path}: 'authority' must be an integer")

    facets = front.get("facets")
    if not isinstance(facets, dict):
        raise CardParseError(f"{path}: 'facets' must be a mapping")

    source = front.get("source")
    if not isinstance(source, dict):
        raise CardParseError(f"{path}: 'source' must be a mapping")
    for key in SOURCE_KEYS:
        value = source.get(key)
        # An unquoted extracted_at like 2026-08-21 is auto-parsed by YAML as a date.
        if not isinstance(value, (str, int, date)) or not str(value).strip():
            raise CardParseError(f"{path}: missing or empty required key 'source.{key}'")

    sequences: dict[str, tuple[str, ...]] = {}
    for key in SEQUENCE_KEYS:
        value = front.get(key) or []
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise CardParseError(f"{path}: {key!r} must be a list of strings")
        sequences[key] = tuple(value)

    return Card(
        id=front["id"].strip(),
        title=front["title"].strip(),
        kind=front["kind"].strip(),
        question=front["question"].strip(),
        asked_as=sequences["asked_as"],
        keywords=sequences["keywords"],
        facets=dict(facets),
        authority=authority,
        not_to_be_confused_with=sequences["not_to_be_confused_with"],
        see_also=sequences["see_also"],
        source_ref=str(source["ref"]).strip(),
        source_locator=str(source["locator"]).strip(),
        source_extracted_at=str(source["extracted_at"]).strip(),
        body=body.strip(),
        path=path,
    )


def render_card(card: Card) -> str:
    front = {
        "id": card.id,
        "title": card.title,
        "kind": card.kind,
        "question": card.question,
        "asked_as": list(card.asked_as),
        "keywords": list(card.keywords),
        "facets": card.facets,
        "authority": card.authority,
        "not_to_be_confused_with": list(card.not_to_be_confused_with),
        "see_also": list(card.see_also),
        "source": {
            "ref": card.source_ref,
            "locator": card.source_locator,
            "extracted_at": card.source_extracted_at,
        },
    }
    dumped = yaml.safe_dump(front, sort_keys=False, allow_unicode=True).rstrip("\n")
    return f"{FENCE}\n{dumped}\n{FENCE}\n\n{card.body}\n"


def load_cards_leniently(root: Path) -> tuple[list[Card], list[CardLoadFailure]]:
    """Parse every card, collecting failures instead of raising on the first one.

    Lint must report a broken card as a check, not a traceback, and must still
    check the cards around it.
    """
    root = Path(root)
    cards_dir = root / "cards"
    if not cards_dir.is_dir():
        return [], []
    cards: list[Card] = []
    failures: list[CardLoadFailure] = []
    for file in sorted(cards_dir.rglob("*.md")):
        rel = file.relative_to(root).as_posix()
        try:
            cards.append(parse_card(file.read_text(), rel))
        except CardParseError as exc:
            failures.append(CardLoadFailure(path=rel, message=_without_path(str(exc), rel)))
    return cards, failures


def load_cards(root: Path) -> list[Card]:
    cards, failures = load_cards_leniently(root)
    if failures:
        raise CardParseError(f"{failures[0].path}: {failures[0].message}")
    return cards

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass

from kb.card import FACET_SENTINEL, SENTINEL_EXEMPT_FACETS, Card, CardLoadFailure
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


def _brand_list(card: Card) -> list[str]:
    """Read `brand` as a list. A bare string is reported, not silently accepted."""
    value = card.facets.get("brand")
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str):
        return [value]
    return []


def _brand_errors(card: Card, config: KbConfig) -> list[LintError]:
    if "brand" not in config.facets:
        return []

    raw = card.facets.get("brand")
    if raw is not None and not isinstance(raw, list) and not _is_empty(raw):
        # Same trap as applies_to: a dropped "- " makes the sort and duplicate rules
        # vacuous and breaks the array shape the reader's filter relies on.
        return [
            LintError(
                card.path,
                "brand-model-agree",
                "brand must be a list of brand keys, not a bare value; write '- ' before each key",
            )
        ]

    brands = _brand_list(card)
    errors: list[LintError] = []

    if brands != sorted(brands):
        errors.append(
            LintError(card.path, "brand-model-agree", f"brand is not sorted; write {sorted(brands)}")
        )
    if len(set(brands)) != len(brands):
        errors.append(LintError(card.path, "brand-model-agree", "brand holds a duplicate"))

    legal = ", ".join(sorted(config.models)) or "(kb.yaml's models map declares no brands)"
    for brand in brands:
        if brand not in config.models:
            errors.append(
                LintError(
                    card.path,
                    "brand-model-agree",
                    f"brand {brand!r} is not a brand in kb.yaml's models map; "
                    f"brand must be one or more of: {legal}",
                )
            )

    model = card.facets.get("model")
    if isinstance(model, str) and model != FACET_SENTINEL:
        for brand in brands:
            if brand in config.models and model not in config.models[brand]:
                errors.append(
                    LintError(
                        card.path,
                        "brand-model-agree",
                        f"model {model!r} is not a model of brand {brand!r}",
                    )
                )

    return errors


def _applies_to_errors(card: Card, config: KbConfig) -> list[LintError]:
    if "brand" not in config.facets:
        return []

    applies = card.facets.get("applies_to")
    if _is_empty(applies):
        # empty-facet already reports this, and reporting it twice helps nobody.
        return []
    if not isinstance(applies, list):
        # A dropped "- " turns the list into a bare string. _is_empty says a non-blank
        # string is fine, so nothing else in lint catches it, and the card would reach
        # exactly one machine while taking the sentinel branch of every other rule.
        return [
            LintError(
                card.path,
                "applies-to-valid",
                "applies_to must be a list of model ids, not a bare value; write '- ' before each id",
            )
        ]

    applies = [str(item) for item in applies]
    brands = _brand_list(card)
    errors: list[LintError] = []

    if applies != sorted(applies):
        errors.append(
            LintError(card.path, "applies-to-valid", f"applies_to is not sorted; write {sorted(applies)}")
        )
    if len(set(applies)) != len(applies):
        errors.append(LintError(card.path, "applies-to-valid", "applies_to holds a duplicate"))

    model = card.facets.get("model")
    if isinstance(model, str) and model != FACET_SENTINEL:
        if applies != [model]:
            errors.append(
                LintError(
                    card.path,
                    "applies-to-valid",
                    f"model is {model!r}, so applies_to must be exactly ['{model}']",
                )
            )
        return errors

    if len(applies) < 2:
        errors.append(
            LintError(
                card.path,
                "applies-to-valid",
                "model is '*', so applies_to needs two or more machines; "
                "a card about one machine names it in 'model'",
            )
        )

    owner = {model_id: brand for brand, ids in config.models.items() for model_id in ids}
    for value in applies:
        brand = owner.get(value)
        if brand is None:
            errors.append(
                LintError(card.path, "applies-to-valid", f"{value!r} is not a model in kb.yaml's models map")
            )
        elif brand not in brands:
            errors.append(
                LintError(
                    card.path,
                    "applies-to-valid",
                    f"{value!r} is a {brand} model but this card does not list brand {brand!r}",
                )
            )

    for brand in brands:
        if brand in config.models and not any(owner.get(value) == brand for value in applies):
            errors.append(
                LintError(
                    card.path,
                    "applies-to-valid",
                    f"brand names {brand!r} but no entry in applies_to is a {brand} model",
                )
            )

    return errors


def _names_token(text: str, token: str) -> bool:
    """Whether `token` appears in `text` as a whole identifier.

    A bare substring test is useless here: 'ct900' sits inside 'CT900ENT', which
    is exactly the mislabel this catches, and 'sole' sits inside 'console'. The
    hyphen keeps a future variant id such as 'f63-2026' from reading as 'f63'.
    """
    pattern = rf"(?<![a-z0-9_-]){re.escape(token)}(?![a-z0-9_-])"
    return re.search(pattern, text, re.IGNORECASE) is not None


def _question_naming_errors(card: Card, config: KbConfig) -> list[LintError]:
    if "brand" not in config.facets:
        return []

    model = card.facets.get("model")
    if isinstance(model, str) and model != FACET_SENTINEL:
        # Question only. The title cannot carry the model: shared-lookalike fails a
        # title holding two identifier-shaped words, and CODE_PATTERN matches ids
        # like ct900 and f63, so a title with a model and an error code is impossible.
        if _names_token(card.question, model):
            return []
        return [
            LintError(
                card.path,
                "question-names-model",
                f"question does not name model {model!r}; write it so a reader knows "
                f"which machine this answers for",
            )
        ]

    # A card about several machines has no one model to name, so it names its brands.
    # The title is fair game here: a brand name never trips shared-lookalike.
    haystack = f"{card.question}\n{card.title}"
    return [
        LintError(
            card.path,
            "question-names-model",
            f"model is '*', so question or title must name brand {brand!r}",
        )
        for brand in _brand_list(card)
        if not _names_token(haystack, brand)
    ]


def _empty_facet_message(key: str, config: KbConfig) -> str:
    """Name the repair the author must make, never a value the facet forbids."""
    if key == "brand":
        legal = ", ".join(sorted(config.models)) or "(kb.yaml's models map declares no brands)"
        return f"facet 'brand' is missing or empty; list one or more of: {legal}"
    if key in SENTINEL_EXEMPT_FACETS:
        return (
            f"facet {key!r} is missing or empty; list one or more model ids. "
            f"The facet sentinel is not allowed here."
        )
    return f"facet {key!r} is missing or empty; write \"*\" rather than omitting it"


def lint_cards(
    cards: list[Card],
    config: KbConfig,
    source_refs: set[str],
    failures: Sequence[CardLoadFailure] = (),
) -> list[LintError]:
    errors = [LintError(f.path, "unparseable", f.message) for f in failures]
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
                    LintError(card.path, "empty-facet", _empty_facet_message(key, config))
                )

        errors.extend(_brand_errors(card, config))
        errors.extend(_applies_to_errors(card, config))
        errors.extend(_question_naming_errors(card, config))

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

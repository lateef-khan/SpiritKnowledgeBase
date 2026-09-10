from __future__ import annotations

import re
import unicodedata
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass

from kb.card import FACET_SENTINEL, SENTINEL_EXEMPT_FACETS, Card, CardLoadFailure
from kb.config import KbConfig

ASKED_AS_RANGE = (2, 4)
KEYWORDS_RANGE = (4, 10)
CODE_PATTERN = re.compile(r"\b[a-z]{1,2}\d{1,3}\b", re.IGNORECASE)
FOLD_KEEP_CATEGORIES = frozenset({"Lu", "Ll", "Lt", "Lm", "Lo", "Nd", "Nl", "No", "Mn", "Mc"})


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

    raw_model = card.facets.get("model")
    if isinstance(raw_model, list) and FACET_SENTINEL in raw_model:
        errors.append(
            LintError(
                card.path,
                "brand-model-agree",
                "model list holds '*'; write '*' as a bare value, or list the machine ids",
            )
        )
    for model in _model_list(card):
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


def _model_list(card: Card) -> list[str]:
    """Every model id the card's `model` facet names, with the sentinel left out.

    A product card lists a whole family here so Qdrant's keyword filter on any one
    machine still reaches it. A sentinel inside a list is reported by brand-model-agree.
    """
    value = card.facets.get("model")
    items = value if isinstance(value, list) else [value]
    return [str(item) for item in items if isinstance(item, str) and item != FACET_SENTINEL]


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

    if isinstance(model, list):
        # A list-valued model names a family. Every machine the card applies to must be
        # in that list, or a filter on the machine would miss the card that is for it.
        models = [str(item) for item in model]
        for value in applies:
            if value not in models:
                errors.append(
                    LintError(
                        card.path,
                        "applies-to-valid",
                        f"applies_to names {value!r} but the model list does not; "
                        f"a list-valued model holds every machine in applies_to",
                    )
                )
        errors.extend(_owner_errors(card, config, applies, brands))
        return errors

    if FACET_SENTINEL in applies:
        # AgentCore's wildcard scope puts IN [value, "*"] on every query, so ["*"] alone reaches
        # every machine. A mix would also match turn 1's bare IN ["*"] and serve one machine's
        # card before anyone has named a machine.
        if applies != [FACET_SENTINEL]:
            errors.append(
                LintError(
                    card.path,
                    "applies-to-valid",
                    "applies_to must not mix '*' with a model id; write ['*'] for every machine, "
                    "or list the machines",
                )
            )
        return errors

    if len(applies) < 2:
        errors.append(
            LintError(
                card.path,
                "applies-to-valid",
                "model is '*', so applies_to is ['*'] or two or more machines; "
                "a card about one machine names it in 'model'",
            )
        )

    errors.extend(_owner_errors(card, config, applies, brands))
    return errors


def _owner_errors(card: Card, config: KbConfig, applies: list[str], brands: list[str]) -> list[LintError]:
    """Every applies_to entry is a known machine of a listed brand, and every brand contributes one."""
    errors: list[LintError] = []
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
    shape = "a list" if isinstance(model, list) else "'*'"
    return [
        LintError(
            card.path,
            "question-names-model",
            f"model is {shape}, so question or title must name brand {brand!r}",
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
        return f"facet {key!r} is missing or empty; list one or more model ids."
    return f"facet {key!r} is missing or empty; write \"*\" rather than omitting it"


def _facet_type_errors(card: Card, config: KbConfig) -> list[LintError]:
    """
    A keyword facet must hold strings.

    YAML reads an unquoted 585818 as an integer. Nothing downstream complains:
    _is_empty accepts it, _facet_values drops it from every value check, and the
    payload reaches Qdrant as an integer against a keyword index, where no string
    filter will ever match it.
    """
    errors: list[LintError] = []
    for key, value in card.facets.items():
        spec = config.facets.get(key)
        if spec is None or spec.index not in ("keyword", "text"):
            continue
        for item in (value if isinstance(value, list) else [value]):
            if item is None or isinstance(item, str):
                continue
            errors.append(
                LintError(
                    card.path,
                    "non-string-facet",
                    f"facet {key!r} holds {item!r}, which YAML read as "
                    f"{type(item).__name__}; quote it so it stays text",
                )
            )
    return errors


def _fold(value: str) -> str:
    """The comparable form of one facet value. Empty when nothing survives."""
    return "".join(
        character
        for character in unicodedata.normalize("NFC", value).lower()
        if unicodedata.category(character) in FOLD_KEEP_CATEGORIES
    )


def _facet_values(card: Card, key: str) -> list[str]:
    """
    Every string one card writes into one facet.

    The sentinel is a wildcard, not a value. A blank belongs to empty-facet, which says
    the same thing in the words the author needs.
    """
    raw = card.facets.get(key)
    items = raw if isinstance(raw, list) else [raw]
    return [
        item
        for item in items
        if isinstance(item, str) and item.strip() and item != FACET_SENTINEL
    ]


def _fold_errors(cards: list[Card], config: KbConfig) -> list[LintError]:
    """
    Report the values a vocabulary could never tell apart.

    Two spellings that fold alike, or one that folds away to nothing, stop AgentCore at
    boot. Boot names only the pair; this names the cards that have to change.
    """
    errors: list[LintError] = []

    for key in config.facets:
        holders: dict[str, list[Card]] = {}
        for card in cards:
            for value in _facet_values(card, key):
                holders.setdefault(value, []).append(card)

        groups: dict[str, list[str]] = {}
        for value in holders:
            groups.setdefault(_fold(value), []).append(value)

        for folded, values in sorted(groups.items()):
            if not folded:
                errors.extend(
                    LintError(
                        card.path,
                        "facet-folds-to-empty",
                        f"facet {key!r} value {value!r} keeps no letter or digit, so nothing "
                        f"a caller says could ever match it",
                    )
                    for value in sorted(values)
                    for card in holders[value]
                )
                continue

            if len(values) < 2:
                continue

            # The spelling most cards already use wins, so the report names the few cards
            # to change rather than the many.
            winner = max(sorted(values), key=lambda value: len(holders[value]))
            errors.extend(
                LintError(
                    card.path,
                    "facet-fold-collision",
                    f"facet {key!r} value {value!r} folds to {folded!r}, the same as {winner!r} "
                    f"which {len(holders[winner])} cards use; write {winner!r}",
                )
                for value in sorted(values)
                if value != winner
                for card in holders[value]
            )

    return errors


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

    errors.extend(_fold_errors(cards, config))

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
        errors.extend(_facet_type_errors(card, config))
        for key, spec in config.facets.items():
            if spec.optional and key not in card.facets:
                continue
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

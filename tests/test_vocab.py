from dataclasses import replace
from pathlib import Path

import yaml

from kb.card import parse_card
from kb.config import FacetSpec, KbConfig
from kb.vocab import build_vocab, render_vocab

CONFIG = KbConfig(
    root=Path("."),
    collection="kb",
    embedding_model="text-embedding-3-small",
    embedding_dimensions=1024,
    kinds=("fact", "troubleshooting"),
    facets={
        "model": FacetSpec(index="keyword", array=False, values=("f63", "*")),
        "applies_to": FacetSpec(index="keyword", array=True, values=()),
    },
    payload_indexes={},
    pdf_command=None,
)

TEMPLATE = """---
id: {id}
title: T
kind: fact
question: Q?
asked_as: [one, two]
keywords: [a, b, c, d]
facets:
  model: {model}
  applies_to: [{applies}]
authority: 3
not_to_be_confused_with: []
see_also: []
source:
  ref: s
  locator: p.1
  extracted_at: 2026-08-21
---

Body.
"""


def card(id, model, applies):
    return parse_card(TEMPLATE.format(id=id, model=model, applies=applies), f"cards/{id}.md")


def test_vocab_merges_declared_and_observed_values():
    vocab = build_vocab([card("a", "e95", "e95")], CONFIG)
    assert vocab["facets"]["model"] == ["*", "e95", "f63"]


def test_vocab_flattens_array_facet_values():
    vocab = build_vocab([card("a", "f63", "f63, f63-2026")], CONFIG)
    assert vocab["facets"]["applies_to"] == ["f63", "f63-2026"]


def test_vocab_lists_every_card_id_sorted():
    vocab = build_vocab([card("zeta", "f63", "f63"), card("alpha", "f63", "f63")], CONFIG)
    assert vocab["card_ids"] == ["alpha", "zeta"]


def test_vocab_lists_kinds():
    assert build_vocab([], CONFIG)["kinds"] == ["fact", "troubleshooting"]


def test_render_is_valid_deterministic_yaml():
    vocab = build_vocab([card("a", "f63", "f63")], CONFIG)
    text = render_vocab(vocab)
    assert render_vocab(vocab) == text
    assert yaml.safe_load(text) == vocab


def test_a_value_no_card_uses_is_not_reported_as_new():
    vocab = build_vocab([card("a", "f63", "f63")], CONFIG)
    assert vocab["undeclared_facet_values"] == {}


def test_a_value_cards_use_but_kb_yaml_does_not_declare_is_reported():
    vocab = build_vocab([card("a", "e95", "e95")], CONFIG)
    assert vocab["undeclared_facet_values"] == {"model": ["e95"]}


def test_an_open_facet_with_no_declared_values_reports_nothing():
    vocab = build_vocab([card("a", "f63", "f63, f63-2026")], CONFIG)
    assert "applies_to" not in vocab["undeclared_facet_values"]


def test_undeclared_values_are_sorted_and_deduplicated():
    cards = [card("a", "e95", "e95"), card("b", "c65", "c65"), card("c", "e95", "e95")]
    assert build_vocab(cards, CONFIG)["undeclared_facet_values"] == {"model": ["c65", "e95"]}


def test_the_declared_facet_block_still_lists_every_known_value():
    vocab = build_vocab([card("a", "e95", "e95")], CONFIG)
    assert vocab["facets"]["model"] == ["*", "e95", "f63"]


def test_render_puts_undeclared_values_in_their_own_block():
    text = render_vocab(build_vocab([card("a", "e95", "e95")], CONFIG))
    assert "undeclared_facet_values:" in text
    assert yaml.safe_load(text)["undeclared_facet_values"] == {"model": ["e95"]}


def test_the_wildcard_sentinel_is_never_reported_as_a_new_value():
    """Spec 4.1 makes "*" the "not applicable" marker, not invented vocabulary."""
    closed = replace(
        CONFIG,
        facets={
            "model": FacetSpec(index="keyword", array=False, values=("f63",)),
            "applies_to": FacetSpec(index="keyword", array=True, values=()),
        },
    )
    vocab = build_vocab([card("a", '"*"', '"*"')], closed)
    assert vocab["undeclared_facet_values"] == {}
    assert build_vocab([card("a", "e95", "e95")], closed)["undeclared_facet_values"] == {
        "model": ["e95"]
    }


def test_vocab_takes_model_values_from_the_models_map():
    config = replace(CONFIG, models={"spirit": ("ct900",), "sole": ("f63",)})
    vocab = build_vocab([card("a", "ct900", "ct900")], config)
    assert vocab["facets"]["model"] == ["*", "ct900", "f63"]
    assert "model" not in vocab["undeclared_facet_values"]


def test_vocab_keeps_declared_values_when_the_map_is_empty():
    vocab = build_vocab([card("a", "e95", "e95")], CONFIG)
    assert vocab["facets"]["model"] == ["*", "e95", "f63"]
    assert vocab["undeclared_facet_values"]["model"] == ["e95"]

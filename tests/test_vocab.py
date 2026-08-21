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

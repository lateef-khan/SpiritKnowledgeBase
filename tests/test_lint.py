from dataclasses import replace

from kb.card import CardLoadFailure, parse_card
from kb.config import FacetSpec, KbConfig
from kb.lint import lint_cards
from pathlib import Path

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
title: {title}
kind: {kind}
question: What does it mean?
asked_as:
  - one phrasing
  - two phrasing
keywords: [alpha, beta, gamma, delta]
facets:
{facets}
authority: 3
not_to_be_confused_with: {ncw}
see_also: {see_also}
source:
  ref: {ref}
  locator: p.1
  extracted_at: 2026-08-21
---

{body}
"""

GOOD_FACETS = "  model: f63\n  applies_to: [f63]"


def make(
    id="card-a",
    title="Card A",
    kind="troubleshooting",
    facets=GOOD_FACETS,
    ncw="[]",
    see_also="[]",
    ref="src-1",
    body="Some body.",
    path=None,
):
    text = TEMPLATE.format(
        id=id, title=title, kind=kind, facets=facets, ncw=ncw, see_also=see_also, ref=ref, body=body
    )
    return parse_card(text, path or f"cards/{id}.md")


def slugs(errors):
    return sorted(e.check for e in errors)


def test_clean_repo_has_no_errors():
    errors = lint_cards([make()], CONFIG, {"src-1"})
    assert errors == []


def test_duplicate_id_is_reported():
    errors = lint_cards([make(path="cards/a.md"), make(path="cards/b.md")], CONFIG, {"src-1"})
    assert "unique-id" in slugs(errors)


def test_dangling_see_also_is_reported():
    errors = lint_cards([make(see_also="[nope]")], CONFIG, {"src-1"})
    assert "dangling-link" in slugs(errors)


def test_dangling_not_to_be_confused_with_is_reported():
    errors = lint_cards([make(ncw="[nope]")], CONFIG, {"src-1"})
    assert "dangling-link" in slugs(errors)


def test_unknown_source_ref_is_reported():
    errors = lint_cards([make(ref="ghost")], CONFIG, {"src-1"})
    assert "unknown-source" in slugs(errors)


def test_undeclared_facet_key_is_reported():
    errors = lint_cards([make(facets=GOOD_FACETS + "\n  colour: red")], CONFIG, {"src-1"})
    assert "undeclared-facet" in slugs(errors)


def test_missing_declared_facet_is_reported():
    errors = lint_cards([make(facets="  model: f63")], CONFIG, {"src-1"})
    assert "empty-facet" in slugs(errors)


def test_empty_string_facet_is_reported():
    errors = lint_cards([make(facets='  model: ""\n  applies_to: [f63]')], CONFIG, {"src-1"})
    assert "empty-facet" in slugs(errors)


def test_empty_list_facet_is_reported():
    errors = lint_cards([make(facets="  model: f63\n  applies_to: []")], CONFIG, {"src-1"})
    assert "empty-facet" in slugs(errors)


def test_blank_entries_in_list_facet_is_reported():
    errors = lint_cards([make(facets='  model: f63\n  applies_to: ["", " "]')], CONFIG, {"src-1"})
    assert "empty-facet" in slugs(errors)


def test_unknown_kind_is_reported():
    errors = lint_cards([make(kind="rumour")], CONFIG, {"src-1"})
    assert "unknown-kind" in slugs(errors)


def test_too_few_asked_as_is_reported():
    card = make()
    thin = parse_card(
        TEMPLATE.format(
            id="card-a", title="Card A", kind="fact", facets=GOOD_FACETS,
            ncw="[]", see_also="[]", ref="src-1", body="Body.",
        ).replace("  - one phrasing\n  - two phrasing", "  - only one"),
        "cards/a.md",
    )
    assert "list-length" in slugs(lint_cards([thin], CONFIG, {"src-1"}))
    assert lint_cards([card], CONFIG, {"src-1"}) == []


def test_too_few_keywords_is_reported():
    errors = lint_cards(
        [parse_card(
            TEMPLATE.format(
                id="card-a", title="Card A", kind="fact", facets=GOOD_FACETS,
                ncw="[]", see_also="[]", ref="src-1", body="Body.",
            ).replace("[alpha, beta, gamma, delta]", "[alpha]"),
            "cards/a.md",
        )],
        CONFIG,
        {"src-1"},
    )
    assert "list-length" in slugs(errors)


def test_empty_body_is_reported():
    errors = lint_cards([make(body="")], CONFIG, {"src-1"})
    assert "empty-body" in slugs(errors)


def test_two_lookalike_codes_in_one_card_is_reported():
    errors = lint_cards(
        [make(title="Errors E03 and E31 - two codes in one card")], CONFIG, {"src-1"}
    )
    assert "shared-lookalike" in slugs(errors)


def test_single_code_in_title_is_fine():
    errors = lint_cards([make(title="Error E03 - hardware current too large")], CONFIG, {"src-1"})
    assert errors == []


def test_an_unparseable_card_is_reported_as_a_lint_error():
    failures = [CardLoadFailure(path="cards/broken.md", message="unterminated frontmatter")]
    errors = lint_cards([make()], CONFIG, {"src-1"}, failures)
    assert [(e.path, e.check, e.message) for e in errors] == [
        ("cards/broken.md", "unparseable", "unterminated frontmatter")
    ]


def test_the_good_cards_are_still_checked_alongside_an_unparseable_one():
    failures = [CardLoadFailure(path="cards/broken.md", message="unterminated frontmatter")]
    errors = lint_cards([make(ref="ghost")], CONFIG, {"src-1"}, failures)
    assert {e.check for e in errors} == {"unparseable", "unknown-source"}


def test_the_ten_spec_checks_all_have_a_slug():
    """Spec section 5 lists ten checks. Check 9 went missing once already."""
    duplicated = make(id="card-a", ref="ghost")
    broken_text = TEMPLATE.format(
        id="card-a",
        title="Error E03 and error E31",
        kind="anecdote",
        facets="  model: ''\n  invented: nonsense",
        ncw="[nobody]",
        see_also="[nobody-either]",
        ref="ghost",
        body="   ",
    ).replace("keywords: [alpha, beta, gamma, delta]", "keywords: [alpha]")
    broken = parse_card(broken_text, "cards/card-b.md")
    failures = [CardLoadFailure(path="cards/broken.md", message="unterminated frontmatter")]
    assert set(slugs(lint_cards([duplicated, broken], CONFIG, {"src-1"}, failures))) == {
        "unique-id",
        "dangling-link",
        "unknown-source",
        "undeclared-facet",
        "empty-facet",
        "unknown-kind",
        "list-length",
        "empty-body",
        "unparseable",
        "shared-lookalike",
    }


def test_empty_exempt_facet_message_does_not_tell_you_to_write_the_sentinel():
    card = make(facets="  model: f63\n  applies_to: []")
    errors = [e for e in lint_cards([card], CONFIG, {"src-1"}) if e.check == "empty-facet"]
    assert len(errors) == 1
    assert '"*"' not in errors[0].message
    assert "model ids" in errors[0].message


def test_empty_ordinary_facet_still_says_to_write_the_sentinel():
    card = make(facets="  applies_to: [f63]")
    errors = [e for e in lint_cards([card], CONFIG, {"src-1"}) if e.check == "empty-facet"]
    assert len(errors) == 1
    assert errors[0].check == "empty-facet"
    assert '"*"' in errors[0].message


BRAND_CONFIG = replace(
    CONFIG,
    facets={
        "brand": FacetSpec(index="keyword", array=True, values=("sole", "spirit")),
        "model": FacetSpec(index="keyword", array=False, values=("f63", "*")),
        "applies_to": FacetSpec(index="keyword", array=True, values=()),
    },
    models={"sole": ("f63", "f80"), "spirit": ("ct900",)},
)

BRAND_TEMPLATE = "  brand: {brand}\n  model: {model}\n  applies_to: {applies}"


def branded(brand="[sole]", model="f63", applies="[f63]", **kw):
    return make(facets=BRAND_TEMPLATE.format(brand=brand, model=model, applies=applies), **kw)


def checks_for(card, config=BRAND_CONFIG):
    return [e for e in lint_cards([card], config, {"src-1"})]


def test_brand_model_agree_accepts_a_good_card():
    assert [e for e in checks_for(branded()) if e.check == "brand-model-agree"] == []


def test_brand_model_agree_rejects_an_unknown_brand():
    errors = [e for e in checks_for(branded(brand="[sprit]")) if e.check == "brand-model-agree"]
    assert len(errors) == 1
    assert "sprit" in errors[0].message
    assert "sole, spirit" in errors[0].message


def test_brand_model_agree_rejects_a_model_from_another_brand():
    errors = [e for e in checks_for(branded(brand="[spirit]", model="f63", applies="[f63]"))
              if e.check == "brand-model-agree"]
    assert len(errors) == 1
    assert "not a model of brand 'spirit'" in errors[0].message


def test_brand_model_agree_ignores_the_model_when_it_is_the_sentinel():
    card = branded(brand="[sole]", model="'*'", applies="[f63, f80]")
    assert [e for e in checks_for(card) if e.check == "brand-model-agree"] == []


def test_brand_model_agree_rejects_an_unsorted_brand_list():
    errors = [e for e in checks_for(branded(brand="[spirit, sole]", model="'*'", applies="[ct900, f63]"))
              if e.check == "brand-model-agree"]
    assert any("sorted" in e.message for e in errors)


def test_brand_model_agree_rejects_a_duplicate_brand():
    errors = [e for e in checks_for(branded(brand="[sole, sole]")) if e.check == "brand-model-agree"]
    assert any("duplicate" in e.message for e in errors)


def test_brand_model_agree_rejects_a_bare_string_brand():
    """A dropped '- ' makes brand a string, which would make rule 3 vacuous."""
    errors = [e for e in checks_for(branded(brand="sole")) if e.check == "brand-model-agree"]
    assert len(errors) == 1
    assert "not a bare value" in errors[0].message


def test_brand_model_agree_is_silent_when_brand_is_not_declared():
    """Must use a card that WOULD fail if the guard were removed, or it asserts nothing.
    Under CONFIG there is no brand facet, so an unknown-brand card must stay silent."""
    card = make(facets="  model: f63\n  applies_to: [f63]")
    assert [e for e in checks_for(card, config=CONFIG) if e.check == "brand-model-agree"] == []


def test_empty_brand_names_the_legal_values():
    """Spec section 5: the generic empty-facet message would loop the extractor."""
    errors = [e for e in checks_for(branded(brand="[]")) if e.check == "empty-facet"]
    assert len(errors) == 1
    assert "list one or more of: sole, spirit" in errors[0].message


def test_empty_brand_falls_back_when_the_models_map_is_empty():
    config = replace(BRAND_CONFIG, models={})
    errors = [e for e in checks_for(branded(brand="[]"), config=config) if e.check == "empty-facet"]
    assert len(errors) == 1
    assert "declares no brands" in errors[0].message


def applies_errors(card):
    return [e for e in checks_for(card) if e.check == "applies-to-valid"]


def test_applies_to_accepts_a_concrete_model_card():
    assert applies_errors(branded(brand="[sole]", model="f63", applies="[f63]")) == []


def test_applies_to_rejects_a_concrete_model_that_does_not_match():
    errors = applies_errors(branded(brand="[sole]", model="f63", applies="[f80]"))
    assert len(errors) == 1
    assert "exactly ['f63']" in errors[0].message


def test_applies_to_accepts_a_sentinel_card_spanning_two_machines():
    assert applies_errors(branded(brand="[sole]", model="'*'", applies="[f63, f80]")) == []


def test_applies_to_rejects_a_sentinel_card_reaching_one_machine():
    errors = applies_errors(branded(brand="[sole]", model="'*'", applies="[f63]"))
    assert any("two or more" in e.message for e in errors)


def test_applies_to_rejects_an_unknown_machine():
    errors = applies_errors(branded(brand="[sole]", model="'*'", applies="[f63, f99]"))
    assert any("'f99' is not a model" in e.message for e in errors)


def test_applies_to_rejects_a_machine_whose_brand_is_not_listed():
    errors = applies_errors(branded(brand="[sole]", model="'*'", applies="[ct900, f63]"))
    assert any("does not list brand 'spirit'" in e.message for e in errors)


def test_applies_to_rejects_a_brand_that_contributes_nothing():
    errors = applies_errors(branded(brand="[sole, spirit]", model="'*'", applies="[f63, f80]"))
    assert any("no entry in applies_to is a spirit model" in e.message for e in errors)


def test_applies_to_rejects_an_unsorted_list():
    errors = applies_errors(branded(brand="[sole]", model="'*'", applies="[f80, f63]"))
    assert any("not sorted" in e.message for e in errors)


def test_applies_to_rejects_a_duplicate():
    errors = applies_errors(branded(brand="[sole]", model="'*'", applies="[f63, f63]"))
    assert any("duplicate" in e.message for e in errors)


def test_applies_to_rejects_a_bare_string():
    """A dropped '- ' makes applies_to a string. _is_empty calls that non-empty, so
    nothing else in lint catches it, and the card answers for the wrong machine."""
    errors = applies_errors(branded(brand="[sole]", model="'*'", applies="f63"))
    assert len(errors) == 1
    assert "not a bare value" in errors[0].message


def test_applies_to_rejects_a_bare_string_on_a_concrete_model_card():
    errors = applies_errors(branded(brand="[spirit]", model="ct900", applies="ct900ent"))
    assert len(errors) == 1
    assert "not a bare value" in errors[0].message


def test_applies_to_checks_sortedness_on_a_concrete_model_card_too():
    errors = applies_errors(branded(brand="[sole]", model="f63", applies="[f80, f63]"))
    assert any("not sorted" in e.message for e in errors)


def test_applies_to_is_silent_when_brand_is_not_declared():
    """Must use a card that WOULD fail if the guard were removed, or it asserts nothing."""
    card = make(facets="  model: f63\n  applies_to: [f80]")
    assert [e for e in checks_for(card, config=CONFIG) if e.check == "applies-to-valid"] == []

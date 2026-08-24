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

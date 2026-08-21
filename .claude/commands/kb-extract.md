---
description: Turn one ingested source into knowledge cards and open a PR
---

# Extract cards from a source

You turn one source document into knowledge cards. A card is one Markdown file
that answers exactly one question.

The source id is: $ARGUMENTS

## 1. Read before you write

1. Confirm the source is on disk and will reach the PR:
   `git status --porcelain sources/$ARGUMENTS sources/manifest.yaml`. `kb ingest`
   wrote both before this branch existed, so they are usually untracked. They
   must be committed alongside the cards or CI's `kb lint` reports
   `unknown-source` for every card you write.
2. Read `sources/$ARGUMENTS/text.md` in full. All of it, before writing anything.
3. Run `kb vocab`. It prints the declared facet keys, every value already in use,
   the allowed `kind` values, and every existing card id.
4. Reuse existing facet values. Do not invent `section: fault-codes` when
   `section: errors` already exists. If you must add a new value, note it and
   report it at the end.

## 2. Create a branch

```bash
git switch -c extract/$ARGUMENTS
```

## 3. One card answers one question

Split so each card answers exactly one thing a person would ask.

- One card per error code.
- One card per assembly step.
- One card per program, console feature, or policy rule.
- A numbered procedure whose steps are only meaningful together stays in **one**
  card.

Keep bodies short. A card should be readable at a glance.

For an email thread the job is: **find the answer, discard the conversation.**
One thread usually yields 0 to 2 cards. Zero is a correct result. Say so.

## 4. Write each card

```bash
kb new <card-id>
```

Then fill in the file it wrote at `cards/<card-id>.md`. Move it into a folder
that helps a human browse — `cards/<model>/<section>/<card-id>.md`. The folder is
for humans only; retrieval uses `facets`, never the path.

Frontmatter rules:

- `id` — lowercase, hyphenated, unique, and **never changed later**. It is the
  Qdrant point id.
- `title` — what this card answers, as a phrase.
- `kind` — one of the values `kb vocab` printed.
- `question` — the one question this card answers, in plain words.
- `asked_as` — 2 to 4 phrasings a real customer would type. Sloppy, lowercase,
  no jargon.
- `keywords` — 4 to 10 lowercase terms, **including synonyms the source never
  uses**.
- `facets` — every declared key, always filled. Write `"*"` rather than leaving
  one out. A missing facet makes the card invisible to grouped search.
- `authority` — 3 for a manual or spec, 2 for a technician note, 1 for an email
  or anecdote.
- `source.ref` — `$ARGUMENTS`. `source.locator` — page, line range, or message
  id, enough for a human to check you.

## 5. Look-alike identifiers

Codes that differ by a character are the classic wrong-answer trap. `E3`, `E03`
and `E31` are three different faults.

- Give each its own card. Never one card for two codes.
- List the neighbours in `not_to_be_confused_with`.
- Say it in the first line of the body:

```markdown
**This is E03, not E3 (incline) and not E31 (overtemperature).**
```

## 6. Facts that live in two places

A retriever stops at the first plausible answer. If the source states a rule in
one place and qualifies it in another, a card holding only the first half gives
an incomplete answer and does not know it.

For each such fact:

1. Put it where a reader would look first.
2. Put the other half where the source put it.
3. Link both ways with `see_also`.
4. State in the body of each that the other half exists, in one sentence.

Never silently merge the two.

## 7. Repair the extraction, do not repeat it

Converted text carries damage. Fix it.

- Re-join words split across lines.
- Rebuild tables as Markdown tables when the columns are recoverable.
- Drop running headers, footers, and page numbers.
- Keep **exact** every number, part number, tool size, unit, and step order.

When a table's structure is genuinely unrecoverable, do not invent a mapping.
Preserve the values in their printed order in a fenced block and add one line
saying what is ambiguous and why.

## 8. Never do these

- Invent a fact the source does not state.
- Answer a question the source does not answer. Absence is information.
- Change a number, a unit, a part number, or a step order.
- Write a card that covers two identifiers.
- Reuse an existing `id` for different content.

## 9. Check yourself

```bash
kb lint
```

Fix every problem it reports, then run it again. Do not open a PR while it
fails.

## 10. Open the PR

```bash
git add cards/ sources/
git commit -m "feat(kb): extract cards from $ARGUMENTS"
gh pr create --fill
```

`sources/` belongs in the same commit. Without it the manifest row every card's
`source.ref` names is absent from the branch and CI fails on `unknown-source`.

If `gh` reports that it cannot determine the repository, the SSH host alias in
`origin` is the cause. Retry with:

```bash
GH_REPO=lateef-khan/SpiritKnowledgeBase gh pr create --fill
```

## 11. Report in the PR body

- Cards added, and cards changed.
- **Every new facet value you introduced**, and why the existing ones did not
  fit.
- **Anything you could not place**, and why.
- **Every two-place fact you found**, and where each half went.
- **Anything ambiguous, contradictory, or damaged in the source**, and what you
  did. A contradiction in the source is a finding, not something to smooth over.

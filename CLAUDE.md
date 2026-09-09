# Spirit Knowledge Base

Markdown knowledge cards in `cards/`, synced into Qdrant.

## The organising rule

A card is keyed to the **fact**, not to the document it came from. Two manuals
that state the same fact produce **one** card whose `applies_to` names both
machines — never one card per manual.

Before you write a card, search `cards/` for the fact and **extend** the card
that already holds it. This governs every task that touches `cards/`, not only
extraction.

## Where the procedure lives

`.claude/commands/kb-extract.md` holds the full extraction procedure: card
shapes, facet rules, look-alike codes, and the PR report. Read it before you
write or edit any card. `/kb-extract <source-id>` runs it.

`README.md` holds the command table and the Qdrant setup.

## What `kb lint` cannot catch

CI runs `kb lint`. Three things stay green that should not:

- **A card restating a fact another card already holds.** Nothing detects this.
  Search first.
- **An invented facet value.** Lint checks `brand` and `applies_to` against
  `kb.yaml`'s `models` map, and checks every facet *key* is declared. It never
  checks the *values* of `section`, `product_line`, `code`, or `kind`. Read
  `kb vocab`'s `undeclared_facet_values` block before opening a PR.
- **A filename that overwrites another card.** Card basenames repeat across
  model folders, so moving a card into `cards/shared/<section>/` can land on an
  existing file. Check the target path is free before you move.

## Conventions the code does not enforce

- **A title names the fact and carries no model id.** The card can then grow to
  cover more machines without its title becoming wrong.
- **An `id` never changes.** It is the Qdrant point id, even when the card grows
  from one machine to ten.

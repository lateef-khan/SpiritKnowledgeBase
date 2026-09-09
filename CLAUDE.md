# Spirit Knowledge Base

Markdown knowledge cards in `cards/`, synced into Qdrant.

## The organising rule

A card is keyed to the **fact**, not to the document it came from. Two manuals
that state the same fact produce **one** card whose `applies_to` names both
machines — never one card per manual.

Before you write a card, search `cards/` for the fact and **extend** the card
that already holds it. This governs every task that touches `cards/`, not only
extraction.

## One brand per card

The organising rule stops at the brand boundary. **A card carries exactly one
brand.** Never extend a Sole card to cover a Spirit machine, or the reverse, even
when both manuals state the fact word for word. Write a separate card for the
other brand.

Two reasons. The same fact is usually held by *several* per-model cards of the
other brand — one console fact sits in about eleven separate Sole cards — so
merging one of them leaves the rest behind and half-merges the repository. And
nothing filters a brand back out at retrieval time.

Link across brands with `see_also` and `not_to_be_confused_with` instead. Those
are pointers, not merges: the card keeps its single brand, and
`not_to_be_confused_with` is what stops a Sole `E01` being served for a Spirit
`E1`. Extending a card of the **same** brand stays correct and expected.

## Where the procedure lives

`.claude/commands/kb-extract.md` holds the full extraction procedure: card
shapes, facet rules, look-alike codes, and the PR report. Read it before you
write or edit any card. `/kb-extract <source-id>` runs it.

`README.md` holds the command table and the Qdrant setup.

## What `kb lint` cannot catch

CI runs `kb lint`. Six things stay green that should not:

- **A card restating a fact another card already holds.** Nothing detects this.
  Search first.
- **An invented facet value.** Lint checks `brand` and `applies_to` against
  `kb.yaml`'s `models` map, and checks every facet *key* is declared. It never
  checks the *values* of `section`, `product_line`, `code`, or `kind`. Read
  `kb vocab`'s `undeclared_facet_values` block before opening a PR.
- **A filename that overwrites another card.** Card basenames repeat across
  model folders, so moving a card into `cards/shared/<section>/` can land on an
  existing file. Check the target path is free before you move.
- **A card whose two brands should have been two cards.** Lint checks that each
  brand key exists and contributes a machine. It never objects to a card listing
  both. See "One brand per card" above.
- **An `id` that disagrees with its own `section` facet.** An id reading
  `...-maintenance-calibration-basic` on a card whose facet says
  `section: console` passes silently and misleads every later reader. Fix the id
  while the card is still unmerged; after it syncs, the id is frozen.
- **A move that breaks a relative link.** Other cards may point at a card by
  relative path. Moving it into `cards/shared/` leaves those links dangling in a
  way lint does not report. Grep for links to a card before moving it.

## Conventions the code does not enforce

- **A title names the fact and carries no model id.** The card can then grow to
  cover more machines without its title becoming wrong.
- **An `id` never changes.** It is the Qdrant point id, even when the card grows
  from one machine to ten.

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
- **Two cards sharing one title.** Lint checks that an `id` is unique. It never
  looks at `title`. As of 2026-09-09 the repository holds **625 duplicate-title
  groups covering 2065 cards** — one title is used by 29 of them. Some are
  legitimate (the same question about different machines), some are the duplicate
  facts the organising rule forbids. Before adding a card, check its title is not
  already in use:

  ```bash
  grep -rh '^title:' cards/ --include='*.md' | sed 's/^title: //' | sort | uniq -d
  ```

## A filename year is not evidence

Twice now a manual's folder or filename has named a year the document does not.
Before you create a model id from a filename, prove the year from the document.

- `CT850 2012 OM 850812.pdf` is effective **November 1, 2013**.
- `CT800_2010_OM_800810.pdf` is a **photocopy of the 2012 manual**. Both print the
  stamp `CT800_20130729` and "Effective March 1, 2012", both are 30 pages, and they
  match **95.1%** at word level once OCR letter confusions are normalised — against
  73.7% for the genuinely different CT800-2016. It was carded as `ct800-2010` and had
  to be stripped from 84 cards.

Check three things before ingesting, in this order:

```bash
pdfinfo FILE.pdf | grep -E 'Pages|Producer|CreationDate|Title'
grep -oE '<MODEL>_[0-9]{8}' text.md | sort -u     # the internal revision stamp
grep -i 'effective' text.md                        # the warranty effective date
```

A `Producer` naming a scanner (Lexmark, Xerox, Canon) with `Title: Scanned Document`
means someone photocopied a book — the file's date tells you when it was scanned, not
when it was printed. A document cannot predate its own warranty effective date.

Then compare against the manual you think it duplicates. Normalise the OCR confusions
(`l`/`1`/`I`, `O`/`0`, `S`/`5`, `|`) and run `difflib.SequenceMatcher` at word level.
**Above roughly 90% it is the same document**; a real sibling generation sits far
lower. A phantom model id is worse than a missing one: every card it touches gains a
machine that does not exist, and claims a second manual corroborates a fact when only
one manual ever said it.

## A manual can hide whole pages from `pdftotext`

A PDF that extracts cleanly overall can still print individual pages as flat
pictures with no text behind them. `pdftotext` returns the heading and nothing
under it, so the page looks empty rather than broken, and an extraction agent
reports the machine as simply not covering that topic.

On 2026-09-09 the CE900-2025 and CES880-2025 owner's manuals extracted to ~9,000
words each and looked complete. Their troubleshooting and error-code pages were
images. One agent rendered them and recovered a six-row Condition/Reason/Solve
matrix and an eight-row error table that eleven cards now rest on. Checking the
other seven manuals in the same family found **2,323 further words** across 71
pages — program pages, exploded views and part-name callout diagrams.

**Before briefing anyone on a PDF-backed source, count the words on every page:**

```bash
n=$(pdfinfo FILE.pdf | awk '/^Pages/{print $2}')
for p in $(seq 1 $n); do
  w=$(pdftotext -f $p -l $p -layout FILE.pdf - | wc -w)
  [ "$w" -lt 25 ] && echo "page $p: $w words"
done
```

Render anything under about 25 words at 300 dpi and read it with
`tesseract --psm 4`, then append it to `text.md` under a marked
`=== OCR SUPPLEMENT, PDF PAGE n ===` header so a later reader knows which text is
OCR and which is native. A genuinely blank page costs one OCR pass; a missed
error table costs a wave.

## Prove an absence twice before you card it

"The manual prints no X" is a real answer here and many cards give it. That makes a
**false** absence a real defect: it tells a reader to stop looking for something that
is on the page.

Two ways it has happened:

- **A page-number offset that is not there.** An agent looked for printed page 32 on
  PDF pages 33 and 34, found a different chapter, and concluded the section was
  missing. In those manuals printed page 32 *is* PDF page 32. Check the offset against
  a page you can identify before trusting it.
- **A heading the extractor letter-spaces.** "Using the Spirit FIT App" comes out of
  `pdftotext` as `Using the Spirit F IT App`, so a grep for the product name returns
  nothing while the section sits there in full.

Before writing that a manual lacks something:

```bash
grep -ric 'app'        sources/<id>/text.md     # the loose word, not the exact phrase
grep -in  'F *I *T'    sources/<id>/text.md     # allow spaces between letters
pdftotext -f N -l N -layout FILE.pdf -          # read the page itself, no offset guess
```

Then confirm the page is not a flattened image — see "A manual can hide whole pages
from `pdftotext`" above. Only after a loose-word search, a spacing-tolerant search and
a look at the page is an absence safe to card.

## Never compare manuals with `diff`

`diff` is **not reliable** in this environment. On 2026-09-09 the same two
274 KB files, unchanged on disk, produced `[ok] Files are identical` with exit 0
on one run and a correct one-line diff on the next. In the failing run `cmp`, in
the same command, correctly reported the files differ. An extraction agent hit
the same false negative on two real manuals and caught it only because it
re-checked in Python.

A false "identical" silently merges two machines' facts into one card. Use
instead:

- `cmp -s a b` — a trustworthy same/differ answer.
- `comm -12 <(sort -u a) <(sort -u b)` — set overlap, with `LC_ALL=C` so the
  sort order matches what `comm` expects.
- `python3 -c "import difflib; ..."` — when you need the actual changed lines.

For measuring how much two manuals share, none of those is enough on its own:
compare **8-word phrase shingles**, not lines. See "Never diff by raw line" in
`docs/superpowers/specs/2026-09-09-spirit-owners-manuals-digest-design.md`.

## Conventions the code does not enforce

- **A title names the fact and carries no model id.** The card can then grow to
  cover more machines without its title becoming wrong.
- **When two cards hold the same kind of fact with different values, the title
  carries the distinguishing value.** "The highest speed the console will accept"
  on three cards with three different speeds gives a reader three identical-looking
  results. Write the figure into the title — "The console accepts up to 9.9 mph and
  incline level 9.5" — which distinguishes without naming a model, so the card can
  still grow. The same applies to a variant: "...on the console with MP3 speakers".
- **An `id` never changes.** It is the Qdrant point id, even when the card grows
  from one machine to ten.

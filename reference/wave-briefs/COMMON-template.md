# Common brief — Spirit medical range and owner's-manual gaps wave (2026-09-11)

You are one of eight agents. Each agent owns **one section** across **all 28
sources** in this wave. Sections are disjoint, so you never collide with another
agent. You write cards; you never commit. The orchestrator reconciles and commits.

Repository: `/mnt/HDD/Projects/SpiritKnowledgeBase` (branch
`feat/kb-spirit-medical-and-om-gaps`, already checked out — do not switch
branches). Scratchpad: `/tmp/claude-1000/-mnt-HDD-Projects-SpiritKnowledgeBase/0a783e4d-cf1c-441c-980f-25b3f9be5062/scratchpad`
(call it `$S`). **Namespace every scratch file you create under `$S/med/<your-section>/`** (earlier waves used `$S/<section>/`, `$S/bikes/`, `$S/ell/`, `$S/rc/`; leave those alone)
— the scratchpad is shared by all eight agents.

Read, in this order, before writing anything:

1. `/mnt/HDD/Projects/SpiritKnowledgeBase/CLAUDE.md` — the organising rule, one
   brand per card, ghost text, absences.
2. `/mnt/HDD/Projects/SpiritKnowledgeBase/.claude/commands/kb-extract.md` — card
   shape, facets, §4b section rulings, look-alike codes. **Overrides below win
   where they disagree with it.**
3. Your section brief (the file you were given).
4. Every source in this wave that has content for your section (§ "Sources").

## Sources in this wave

All under `sources/<id>/text.md`. The 28 ids, with the **`product_line` each card
from that source must carry**. OM = owner's manual, SM = service manual.

```
spirit-bike-40r-2025-owners-manual                 OM  40r-2025   bike      (Spirit Medical 4.0R, Rev 10.03.25)
spirit-bike-40r-2025-service-manual                SM  40r-2025   bike      (FR800-SB022-03)
spirit-bike-40r-pt-owners-manual                   OM  40r-pt     bike      (Dyaco "PT" 4.0 R user manual, UNDATED, 2016 PDF; brand spirit - the Spirit Medical 4.0R sold under the Dyaco cover)
spirit-bike-40u-2025-owners-manual                 OM  40u-2025   bike      (Rev 10.03.25)
spirit-bike-40u-2025-service-manual                SM  40u-2025   bike      (FU800-SB022-03)
spirit-bike-40u-pt-owners-manual                   OM  40u-pt     bike      (Dyaco "PT" 4.0 U, UNDATED)
spirit-bike-70r-2025-owners-manual                 OM  70r-2025   bike      (Rev 12.23.25)
spirit-bike-70r-2025-service-manual                SM  70r-2025   bike      (MR490-SB018-03)
spirit-bike-70r-2021-owners-manual                 OM  70r-2021   bike      (Dyaco "MED" 7.0R rehabilitation bike, Rev. 1.2.1 2021/10/14, CE MDD, 90 pages)
spirit-bike-70u-2025-owners-manual                 OM  70u-2025   bike      (Rev 12.09.2025)
spirit-bike-70u-2025-service-manual                SM  70u-2025   bike      (MU470-SB018)
spirit-bike-80u-2025-owners-manual                 OM  80u-2025   bike      (Rev 12.03.25)
spirit-bike-80u-2025-service-manual                SM  80u-2025   bike      (MU2000-SB036-01)
spirit-bike-85r-2025-owners-manual                 OM  85r-2025   bike      (Rev 12.15.25; filed under Treadmills)
spirit-bike-85r-2025-service-manual                SM  85r-2025   bike      (MR2000-SB036-01)
spirit-bike-85ue-2025-service-manual               SM  85ue-2025  bike      (MZ2000-SB036-01; the 8.5UE owner's manual is carded: cards/85ue-2025/)
spirit-stepper-70s-2025-service-manual             SM  70s-2025   climber   (RS9500-SS021-02; owner's manual carded: cards/70s-2025/)
spirit-stepper-75s-2025-service-manual             SM  75s-2025   climber   (RS9600-SS021-03; 97% the RS9600-SS021-01 book carded on 2026-09-11 as 7-5s-med - extend those cards where the page is unchanged)
spirit-treadmill-40t-2025-owners-manual            OM  40t-2025   treadmill (Rev 02.04.25, (c)2024, warranty eff. Oct 31 2024; 90% the 2026 book carded as 40t-2026)
spirit-treadmill-40t-2025-owners-manual-may-2025-printing   OM  40t-2025  treadmill (Rev 05.19.25; 99.9% the February printing - one document, cite both)
spirit-treadmill-40t-2026-service-manual-st8700a   SM  40t-2026   treadmill (ST8700A-ST026-01; 88% the ST8700-ST017 book carded as 40t-2026 - extend where unchanged, new cards where the A revision differs)
spirit-treadmill-70t-2025-owners-manual            OM  70t-2025   treadmill (Rev 01.10.25, (c)2024, warranty eff. Oct 23 2024; 91% the 2026 book carded as 70t-2026)
spirit-treadmill-70t-2026-service-manual           SM  70t-2026   treadmill (the DYACO MT8000 book re-exported with 770885 on the cover; its 23 cards already list 70t-2026 - add only what this export prints differently)
spirit-treadmill-80t-2026-service-manual           SM  80t-2026   treadmill (MT2000-ST022/027-01; owner's manual carded: cards/80t-2026/)
spirit-treadmill-ct850-2013-owners-manual          OM  ct850-2013 treadmill (a scanned 2013 book, ALL OCR, stamp CT850_20131015, warranty eff. Nov 1 2013; NEW machine; the CT850-2016/2018 owner's-manual cards exist)
spirit-treadmill-xt485-2013-owners-manual          OM  xt485-2013 treadmill (485812, SPT0033, 2014 PDF; NEW machine; the XT485-2015 cards exist)
spirit-strength-css-delt-owners-manual-2026        OM  css-delt   strength  (2026 revision, 87% the carded 2025 book; its text layer is a SHIFTED FONT - read the OCR supplements only)
spirit-strength-csd-cpsp-owners-manual-2025-update OM  csd-cpsp   strength  (May 2025 update, 53% the carded 2024 book)
```

A source is evidence **only** for the model id(s) on its line. The 2025 medical
books (4.0R/4.0U/7.0R/7.0U/8.0U/8.5R) are the machines' **first cards ever** —
expect most of your work here to be new cards; their service manuals share the
Dyaco template with the bikes carded on 2026-09-11 (`cards/cu1000ent-2023/`,
`cards/shared/*/spirit-cu800-*`, `spirit-cr900-*`), so search on the fact, and
write a bike card that links to the twin rather than extending across lines
where the product line differs. The 40t-2025 / 70t-2025 books are the
**previous model year** of the 2026 machines: where the 2026 owner's-manual
card states the same fact, extend it with the 2025 id; where the 2025 book
differs (warranty date, a figure), that is its own card.

The Dyaco PT / MED books (40r-pt, 40u-pt, 70r-2021) are patient-therapy
editions: CE MDD class, Type B applied parts, contraindications, therapist
instructions. Card them under `safety` (medical warnings), `console`, `programs`
(therapy programs), `specs` and `warranty` as the sections rule; keep the
Dyaco wording, say the book is the Dyaco edition, and never merge a PT figure
into a 2025 Spirit card without the page saying the same.

Ids: `<model-id>-<section>-<slug>` for one machine; for several,
`spirit-<family>-<section>-<slug>` (e.g. `spirit-med-bike-safety-…`). Files:
`cards/<model-id>/<section>/…` or `cards/shared/<section>/<full id>.md`.

The book's page numbers and the PDF page numbers usually agree; cite as
`p. 43 (printed 42)` when they differ. Every locator must give the PDF page
**and** the `text.md` line range.

## How to read a source (the rtk hook will bite you otherwise)

A hook rewrites `cat`, `head`, `sed`, `grep` and `diff` and **silently truncates
or reformats their output**. Do not read sources with them. Use:

- The `Read` tool on `sources/<id>/text.md` — it is not rewritten.
- `rtk proxy python3 $S/pages.py <source-id> <from> <to>` — prints PDF pages with
  their text.md line ranges, and each page's OCR supplement under it.
- `rtk proxy python3 $S/pages.py <source-id> grep '<regex>'` — which pages match.
- `rtk proxy python3 $S/pages.py <source-id> supplements` — which pages carry OCR.
- Prefix **any** shell command whose exact output matters with `rtk proxy`.
- Never bare `diff`. Use `git diff --no-index` or python `difflib`.

Read every source that has content for your section **in full** before you write.
That is the rule and there is no shortcut.

`text.md` holds three kinds of text: the native layer, `=== OCR SUPPLEMENT, PDF PAGE n ===`
blocks (what a 300 dpi render shows that the text layer does not — tables, callouts,
diagram labels), and possibly **ghost text** the OEM left in the file that is not
printed on the page (metric figures in a US book, a stale schedule, a foreign-language
block). Where a figure matters and looks off, look at the page:
`pdftoppm -r 150 -png -f N -l N "<pdf>" $S/<section>/pg` then `Read` the PNG. The PDF
path is in the header comment of each `text.md` and in `sources/manifest.yaml`.

## Before you write: search, then sort every fact into one of four outcomes

The knowledge base is keyed to the **fact**, not the document. 6,421 cards exist;
every one of these machines already has owner's-manual cards, and the 2025 medical bikes have none yet. Search **on the thing itself**
(`E3`, `speed sensor`, `torque boost`, `lower controller`), never on the model id.

```bash
rtk proxy grep -rn '^title:' cards/ --include='*.md' | grep -i '<distinctive word>'
rtk proxy grep -rli '<the code or component>' cards/
rtk proxy grep -rl '<model-id>' cards/ | xargs grep -l '^  section: <your-section>$'
```

Then each fact is one of:

1. **No card holds it** → write a new card.
2. **A Spirit card holds the same fact** (same figure, same steps) → **extend it**:
   add the machine(s) to `applies_to` (sorted), set `model: '*'`, add this source
   to `source.locator` (keep `source.ref` as it is; enumerate the extra sources in
   the locator), and add a body sentence if the wording of this book adds
   anything. Never change its `id`. You may only edit an existing card whose
   `section` facet is **your** section.
3. **A Sole card holds the same fact** (much of this is Dyaco boilerplate already
   filed for Sole F/TT machines) → write a **Spirit** card, link with `see_also`
   (same figures) or `not_to_be_confused_with` (figures differ), and list the Sole
   card in your report as a cross-brand twin. **Never add a brand to a card.**
4. **A card holds a fact that only looks the same** (different figure, order, part
   number, rating) → its own card, linked with `see_also`; put the difference in
   the first line of both bodies.

**Existing cards can be wrong, not just incomplete.** Owner's-manual cards were
written without these books. Verify every machine already listed on a card you
extend; if the service manual for a listed machine prints a different figure,
that is a finding: write it in the report and put it in the card body in words.
Owner's-manual **absence** cards ("no parts list", "no specification table", "no
LED-debugging card exists for any Spirit machine") are scoped to the owner's
manual — if the service manual supplies the thing, write the card, and edit the
absence card **only if it is your section**, otherwise report it.

**A differing revision date is a locator line; a differing value is a new card.**
Do not make four near-identical cards out of one table printed under four dates.

## Card rules (overrides to kb-extract.md)

- **Ignore kb-extract.md §1, §2, §9b's "before opening the PR", §10 and §11.** No
  branch, no `git add`, no commit, no PR. Report instead.
- **Run no writing git command.** `git status`, `git diff`, `git ls-files`,
  `git show` are fine. `git add`, `commit`, `checkout`, `switch`, `stash`,
  `restore`, `clean`, `rm` are forbidden.
- **Never edit `kb.yaml`, `sources/`, `reference/`, or a card outside your section.**
- **Filenames.** A one-machine card lives at
  `cards/<model-id>/<section>/<id-with-the-model-prefix-stripped>.md`. A
  multi-machine card lives at `cards/shared/<section>/<FULL id>.md` — **keep the
  prefix**; `cards/shared/<section>/` is one flat namespace and stripping the
  prefix has overwritten Sole cards before. Before writing any path, check it is
  not in `git ls-files cards/` unless you are deliberately extending that card.
  After every generation run: `rtk proxy git status --porcelain cards/ | grep -v '^??'`
  — every ` M` line must be a card you meant to extend; anything else is a bug in
  your run. Recover with `git show HEAD:<path> > <path>`.
- **Never delete a directory you do not exclusively own.** Regenerate by deleting
  only `cards/<model-id>/<your-section>/<your-file>.md` and your own named files
  in `cards/shared/<your-section>/`. Never `rm -rf cards/<model-id>` and never a
  shared section folder wholesale.
- **`id`**: `<model-id>-<section>-<slug>` for one machine; for several,
  `spirit-<family>-<section>-<slug>` (e.g. `spirit-med-bike-errors-eeprom-err`,
  `spirit-40t-console-engineering-mode`). Lowercase, hyphens. The id must agree
  with the `section` facet. It never changes after merge.
- **`title`** names the fact, never a model id. `shared-lookalike` lint rejects a
  title matching `\b[a-z]{1,2}\d{1,3}\b`, which catches `ct850`, `xt485`, `e3`
  written as a word — write "error E3" as `E3` in caps, it passes; never put
  `XT485` in a title. When two cards hold the same kind of fact with different
  values, put the value in the title ("…trips its onboard 20 amp circuit").
- **`question`** must name the machine: the model id for a one-machine card
  ("…on a Spirit xt485-2023 treadmill?" — the id spelled literally), or the brand
  and family for a several-machine card ("…on a Spirit XT 2023 treadmill?").
- **`facets`**: every key filled. `brand: [spirit]` only. `product_line`: **the value on the source's line** (bike, treadmill, climber, strength).
  `model`: the id, or `'*'` when `applies_to` lists two or more. `applies_to`:
  sorted list of the real ids — never `'*'` in this wave. `section`: yours.
  `code`: the error code for an error-code card, **lowercase** (`e1`, `40h`,
  `eeprom-err`; the `facet-fold-collision` rule requires it), else `'*'`. **Omit `model_number` and `lookup`** — the product cards
  carry them.
- **`kind`**: one of `fact, procedure, troubleshooting, policy, spec, definition`.
- **`authority`**: 3 for every source in this wave.
- **`source.ref`** is one source id; a card built from several books cites one
  representative ref and enumerates the rest in `locator`. `extracted_at: '2026-09-11'`.
- **`see_also` / `not_to_be_confused_with`** may name only ids that exist now
  (`rtk proxy .venv/bin/kb vocab` lists them) or ids you wrote in this run. The
  `dangling-link` check covers both fields. Cross-links to cards another agent is
  writing go in your report under "intended links", not in the card.
- **Look-alike codes**: `E3`, `E03`, `E-03H`, `E30` are four faults. One card per
  code, neighbours in `not_to_be_confused_with`, and the first body line says
  which this is. Spirit families in this wave do not agree with each other: the
  the MT8000 inverter list on the 7.0T/8.0T books, the CT850-2013 owner's codes, the medical
  bikes' own lists - read each book; the 2025 medical bikes have no cards to collide with. **Never carry a code between families.**
- **Rebuild tables** as Markdown tables. Keep every number, unit, part number,
  wire colour, pin number and step order exact. Drop running headers and folios.
- **Absence is a finding**, and it must be proved twice before it is carded: a
  loose-word grep, a spacing-tolerant grep (`F *I *T`), the page itself, and the
  OCR supplement. Half the false absences in this repo were flattened images.
- **A contradiction inside one book or between two books goes into the body of
  both cards in words.** Never smooth it over.

## Generating cards

`kb new` once per card does not scale. Write them from a script with
`kb.card.render_card`. `Card` is a frozen dataclass with **flat** source fields:

```python
import sys; sys.path.insert(0, '/mnt/HDD/Projects/SpiritKnowledgeBase')
from kb.card import Card, render_card
c = Card(
    id='70r-2025-errors-e2-no-tension-motor-signal', title='...', kind='troubleshooting',
    question='...', asked_as=('...','...'), keywords=('...','...','...','...'),
    facets={'brand': ['spirit'], 'product_line': 'bike', 'model': '70r-2025',
            'applies_to': ['70r-2025'], 'section': 'errors', 'code': 'e2'},
    authority=3, not_to_be_confused_with=(), see_also=(),
    source_ref='spirit-bike-70r-2025-service-manual',
    source_locator='8.2 Error Message: E2, PDF p. 31; text.md lines 602-631',
    source_extracted_at='2026-09-11', body='...', path='')
open(path, 'w').write(render_card(c))
```

Run it with `rtk proxy .venv/bin/python $S/<section>/gen.py`. Make the generator
**refuse** any target path that is in `git ls-files cards/` unless that id is in
your explicit "extend" list.

To extend an existing card, edit the file in place (the `Edit` tool is fine):
`applies_to` gains the ids, `model` becomes `'*'`, `source.locator` gains the new
book's page and lines, and the body gains a sentence only if this book adds one.
Do not move the file, even if it now covers several machines — other cards link
to it by relative path.

## Check yourself

`rtk proxy .venv/bin/kb lint` is read-only and safe any time. Fix every problem in
a card you wrote or edited; leave the rest. Then check your relative links resolve:

```bash
rtk proxy git status --porcelain -uall cards/ | awk '{print $2}' | while read f; do
  grep -oE '\]\(([^)]+\.md)\)' "$f" | sed 's/](//;s/)//' | while read l; do
    [ -f "$(dirname "$f")/$l" ] || echo "BROKEN $f -> $l"; done; done
```

And that no title you wrote is already in use:
`rtk proxy grep -rh '^title:' cards/ --include='*.md' | sort | uniq -d`.

## Report

Write `$S/reports-med/<section>.md` (create `$S/reports-med/` if needed), **at most 60
lines**, with these headings: Cards written (count, and the list of ids);
Cards extended (id → ids added, and the source page); Existing cards found wrong
(id, what the book says instead); Cross-brand twins (Spirit id ↔ Sole id);
Intended links to other sections' cards; Boundary calls (facts you left to a
neighbouring section, and which); Absences proved; Contradictions and damaged
text; Brief defects (anything in this brief or your section brief that was
wrong — every wave so far the brief has been wrong somewhere).

Your final message to the orchestrator is **at most 25 lines**: counts, the
report path, and anything that needs a human decision. Do not paste cards.

Do not use `AskUserQuestion`, `Artifact`, or any git writing command. If you are
blocked, write the block into your report and finish what you can.

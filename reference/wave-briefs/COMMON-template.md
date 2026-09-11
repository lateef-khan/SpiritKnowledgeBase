# Common brief — Xterra treadmill wave X1 (2026-09-11)

You are one of eight agents. Each agent owns **one section** across **all 30
sources** in this wave. Sections are disjoint, so you never collide with another
agent. You write cards; you never commit. The orchestrator reconciles and commits.

Repository: `/mnt/HDD/Projects/SpiritKnowledgeBase` (branch
`feat/kb-xterra-treadmills`, already checked out — do not switch branches).
Scratchpad: `/tmp/claude-1000/-mnt-HDD-Projects-SpiritKnowledgeBase/e835e5c4-bdf0-4d59-988b-1d30984c2ffd/scratchpad`
(call it `$S`). **Namespace every scratch file you create under `$S/x1/<your-section>/`**
— the scratchpad is shared by all eight agents. `$S/pages.py` is the page printer.

Read, in this order, before writing anything:

1. `/mnt/HDD/Projects/SpiritKnowledgeBase/CLAUDE.md` — the organising rule, one
   brand per card, ghost text, absences.
2. `/mnt/HDD/Projects/SpiritKnowledgeBase/.claude/commands/kb-extract.md` — card
   shape, facets, §4b section rulings, look-alike codes. **Overrides below win
   where they disagree with it.**
3. Your section brief (the file you were given).
4. Every source in this wave that has content for your section (§ "Sources").

## This is a NEW BRAND

**Xterra** is a brand `kb.yaml` declares as of this branch, with 19 treadmill
ids. **No Xterra card exists yet** except the 19 product cards
(`cards/shared/specs/<family>-model-numbers.md`, which you never edit). Every card
you write is `brand: [xterra]`, `product_line: treadmill`.

Xterra is a separate range, not rebadged Spirit — owner's manual against owner's
manual the best Spirit match is 48%. But the safety, electrical, grounding,
maintenance and warranty pages are **Dyaco boilerplate**, and most of those
sentences already exist as Spirit or Sole cards. That does **not** make them
extendable: **a card carries exactly one brand.** You write the Xterra card and
point at the twin with `see_also` (same figures) or `not_to_be_confused_with`
(figures differ). Never add `xterra` to a Spirit or Sole card, never edit one.

Because nothing exists yet, "extend" in this wave means **extend the card you or
your own run wrote a minute ago**: the organising rule is one card per *fact*, so
a sentence printed in nineteen owner's manuals is **one** card whose `applies_to`
lists every machine that prints it — never nineteen cards. Where a figure differs
(user weight 250 vs 300 vs 350 lb, speed 0.5–10 vs 0.5–12 mph) it is one card per
value, with the value in the title.

## Sources in this wave

All under `sources/<id>/text.md`. OM = owner's manual, SM = service manual.
A source is evidence **only** for the model id(s) on its line.

```
xterra-treadmill-tr150-2021-owners-manual        OM  tr150-2021    24 pp, Rev 04.13.2021, eff. Mar 13 2021, 2021 batch
xterra-treadmill-tr200-2021-owners-manual        OM  tr200-2021    24 pp, Rev 04.13.2021, eff. Mar 13 2021, 2021 batch
xterra-treadmill-tr300-2021-owners-manual        OM  tr300-2021    26 pp, ©2021, eff. Mar 13 2021, 2021 batch
xterra-treadmill-tr66-2021-owners-manual         OM  tr66-2021     32 pp, ©2021, eff. Mar 13 2021, 2021 batch; the book calls the machine "TR6.6"
xterra-treadmill-trx1000-2021-owners-manual      OM  trx1000-2021  20 pp, Rev 3.0, eff. Mar 13 2021, 2021 batch
xterra-treadmill-tr260-2022-owners-manual        OM  tr260-2022    28 pp, Rev 4.0, ©2022, eff. Aug 24 2022
xterra-treadmill-trx1400-2023-owners-manual      OM  trx1400-2023  44 pp, Rev 05.09.23, eff. Mar 8 2023; file named TR1400, the book says TRX1400 / T3-NT053-01
xterra-treadmill-tr65-2023-owners-manual         OM  tr65-2023     48 pp, Rev 09.28.23, cover prints SKU 165873
xterra-treadmill-ws200-2023-owners-manual        OM  ws200-2023    39 pp, Rev 10.09.23, cover prints SKU 120082; a folding walking treadmill
xterra-treadmill-ws300-2023-owners-manual        OM  ws300-2023    39 pp, Rev 10.09.23, cover prints SKU 130082; a folding walking treadmill
xterra-treadmill-tr95h-2024-owners-manual        OM  tr95h-2024    54 pp, Rev 01.19.24, ©2023, eff. Jan 3 2024, cover prints SKU 195813
xterra-treadmill-trx5500-2024-owners-manual      OM  trx5500-2024  44 pp, ©2024, eff. Mar 20 2024, cover prints SKU 155810 and code GT90D-NT041-01
xterra-treadmill-tr64-2024-owners-manual         OM  tr64-2024     28 pp, ©2024, eff. Jun 7 2024, 2024 batch; the book calls the machine "TR6.4"
xterra-treadmill-tr75-2024-owners-manual         OM  tr75-2024     48 pp, Rev 06.07.24, cover prints SKU 175873, 2024 batch
xterra-treadmill-tr85-2024-owners-manual         OM  tr85-2024     48 pp, Rev 06.07.24, cover prints SKU 185873, 2024 batch
xterra-treadmill-trx2500-2024-owners-manual      OM  trx2500-2024  24 pp, ©2024, eff. Jun 7 2024, 2024 batch
xterra-treadmill-trx3500-2024-owners-manual      OM  trx3500-2024  28 pp, ©2024, eff. Jun 7 2024, 2024 batch
xterra-treadmill-trx4500-2024-owners-manual      OM  trx4500-2024  28 pp, ©2024, eff. Jun 7 2024, 2024 batch
xterra-treadmill-tr75h-2025-owners-manual        OM  tr75h-2025    52 pp, Rev 08.19.25, eff. May 29 2025, cover prints SKU 175825; JKEXER 330

xterra-treadmill-tr150-2021-service-manual             SM  tr150-2021               50 pp, Dyaco GT65-NT014 (2019 PDF); same E0/E1/E2 codes as the OM
xterra-treadmill-tr260-2022-service-manual             SM  tr260-2022               64 pp, Dyaco GT75A-NT050 (2022)
xterra-treadmill-trx1400-2023-service-manual           SM  trx1400-2023             89 pp, Dyaco T3-NT053-01 (2023)
xterra-treadmill-trx2500-2024-service-manual           SM  trx2500-2024             86 pp, Dyaco GT90B-NT022 (2018 PDF; the only TRX2500 SKU, 125817, dates from 2017 - one machine)
xterra-treadmill-trx3500-trx4500-2024-service-manual   SM  trx3500-2024 trx4500-2024  94 pp, Dyaco GT90C-NT023 (TRX3500) + GT90D-NT024 (TRX4500) in one book; a page that names only one code is evidence for that machine only
xterra-treadmill-trx5500-2024-service-manual           SM  trx5500-2024             85 pp, Dyaco GT90D-NT041 (2021 PDF)
xterra-treadmill-tr95h-2024-service-manual             SM  tr95h-2024               17 pp, JKEXER 337, Sept 2024 - assembly sequence, precautions, a short parts/wiring set
xterra-treadmill-tr75h-2025-service-manual             SM  tr75h-2025               17 pp, V1.0 Jan 2026 - same shape as the TR95H book

xterra-treadmill-ws200-ws300-upright-wire-video        video  ws200-2023 ws300-2023  86 s, described frame by frame; corroboration only (authority 2)
xterra-treadmill-tr95h-2024-belt-tracking-video        video  tr95h-2024             42 s, described frame by frame; corroboration only (authority 2)
xterra-treadmill-tr150-2021-mcb-wiring-photo           photo  tr150-2021             annotated MCB photo; label text is verbatim (authority 2)
```

Three book families, which matters for "same fact, many machines":

- **2021 batch** (TR150, TR200, TR300, TR6.6, TRX1000) and **2024 batch** (TR6.4,
  TR75, TR85, TRX2500/3500/4500): the older XTERRA layout, "Congratulations On
  Your New Treadmill", Q&A-style troubleshooting, warranty on the last pages.
- **New layout** (TRX1400, TR65, TR75, TR75H, TR85, TR95H, WS200, WS300,
  TRX5500): "Online Support" cover, Product Labels page, Pack List, Console Screen
  Overview, Exploded View Diagram, FCC Warning.
- **Dyaco SMs**: Outlines, Electronic Parts, Electrical Configuration, Product
  Operation, Block Diagrams, Wiring and PCB, Safety, Error Messages (E0/E1/E2/E4/ER…
  per code), Folding, General Maintenance, Disassembly. Most pages are pictures:
  read the **OCR supplements**. **JKEXER SMs** (TR75H, TR95H) are 17 pages of
  assembly sequence, precautions and a few checks.

Ids: `<model-id>-<section>-<slug>` for one machine; for several,
`xterra-<family>-<section>-<slug>` where family is `tr`, `trx`, `ws`, or
`treadmill` when it spans families (e.g. `xterra-treadmill-safety-user-weight-limit-300-lb`,
`xterra-trx-errors-e1-no-rpm-signal`). Files: `cards/<model-id>/<section>/…` or
`cards/shared/<section>/<full id>.md`.

The book's page numbers and the PDF page numbers usually differ by one or two in
the new-layout books (a cover and a blank page); cite as `p. 21 (printed 20)`.
Every locator must give the PDF page **and** the `text.md` line range.

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
That is the rule and there is no shortcut. Nineteen owner's manuals is a lot of
reading; read the 2021-batch books and the new-layout books once each *carefully*,
then check the siblings page by page for the figure that differs.

`text.md` holds three kinds of text: the native layer, `=== OCR SUPPLEMENT, PDF PAGE n ===`
blocks (what a 300 dpi render shows that the text layer does not — tables, callouts,
diagram labels, the whole of most SM pages), and possibly **ghost text** the OEM left in
the file that is not printed on the page (a foreign-language block, metric figures in a
US book, a stale schedule). Where a figure matters and looks off, look at the page:
`pdftoppm -r 150 -png -f N -l N "<pdf>" $S/x1/<section>/pg` then `Read` the PNG. The PDF
path is in the header comment of each `text.md` and in `sources/manifest.yaml`.

## Before you write: search, then sort every fact into one of four outcomes

8,049 cards exist. Search **on the thing itself** (`E1`, `speed sensor`, `GFCI`,
`silicone`, `safety key`), never on the model id.

```bash
rtk proxy grep -rn '^title:' cards/ --include='*.md' | grep -i '<distinctive word>'
rtk proxy grep -rli '<the code or component>' cards/
```

Then each fact is one of:

1. **No card holds it** → write a new Xterra card.
2. **A Spirit or Sole card holds the same fact** (the Dyaco boilerplate) → write the
   **Xterra** card anyway, link with `see_also` (same figures) or
   `not_to_be_confused_with` (figures differ), and list the twin in your report.
   **Never add a brand to a card. Never edit a Spirit or Sole card.**
3. **An Xterra card from your own run holds it** → extend it: add the machine(s)
   to `applies_to` (sorted), `model: '*'`, add the book to `source.locator`.
4. **A card holds a fact that only looks the same** (different figure, order, part
   number, rating) → its own card, linked with `see_also`; put the difference in
   the first line of both bodies.

**A differing revision date is a locator line; a differing value is a new card.**
Do not make nineteen near-identical cards out of one table printed under
nineteen effective dates.

## Card rules (overrides to kb-extract.md)

- **Ignore kb-extract.md §1, §2, §9b's "before opening the PR", §10 and §11.** No
  branch, no `git add`, no commit, no PR. Report instead.
- **Run no writing git command.** `git status`, `git diff`, `git ls-files`,
  `git show` are fine. `git add`, `commit`, `checkout`, `switch`, `stash`,
  `restore`, `clean`, `rm` are forbidden.
- **Never edit `kb.yaml`, `sources/`, `reference/`, a product card, or a card
  outside your section.**
- **Filenames.** A one-machine card lives at
  `cards/<model-id>/<section>/<id-with-the-model-prefix-stripped>.md`. A
  multi-machine card lives at `cards/shared/<section>/<FULL id>.md` — **keep the
  prefix**; `cards/shared/<section>/` is one flat namespace and stripping the
  prefix has overwritten Sole cards before. Before writing any path, check it is
  not in `git ls-files cards/`. After every generation run:
  `rtk proxy git status --porcelain cards/ | grep -v '^??'` — every line is a bug
  in your run (nothing pre-existing may change in this wave). Recover with
  `git show HEAD:<path> > <path>`.
- **Never delete a directory you do not exclusively own.** Regenerate by deleting
  only `cards/<model-id>/<your-section>/<your-file>.md` and your own named files
  in `cards/shared/<your-section>/`. Never `rm -rf cards/<model-id>` and never a
  shared section folder wholesale.
- **`id`**: `<model-id>-<section>-<slug>` for one machine; for several,
  `xterra-<family>-<section>-<slug>`. Lowercase, hyphens. The id must agree
  with the `section` facet. It never changes after merge.
- **`title`** names the fact, never a model id. `shared-lookalike` lint rejects a
  title matching `\b[a-z]{1,2}\d{1,3}\b` **twice** — `tr150`, `ws200`, `e1` all
  match, so never put a model name in a title; write "error E1" as `E1` in caps
  and nothing else identifier-shaped. When two cards hold the same kind of fact
  with different values, put the value in the title ("The user weight limit is 300 lb").
- **`question`** must name the machine: the model id for a one-machine card
  ("…on an Xterra tr150-2021 treadmill?" — the id spelled literally), or the
  brand and family for a several-machine card ("…on an Xterra TRX treadmill?").
- **`facets`**: every key filled. `brand: [xterra]` only. `product_line: treadmill`.
  `model`: the id, or `'*'` when `applies_to` lists two or more. `applies_to`:
  sorted list of the real ids — **never `'*'` in this wave**, even for a policy
  page: list the Xterra ids that print it (a `'*'` would be served to Sole and
  Spirit customers, and nothing filters a brand back out). `section`: yours.
  `code`: the error code for an error-code card, **lowercase** (`e0`, `e1`, `er`),
  else `'*'`. **Omit `model_number` and `lookup`** — the product cards carry them.
- **`kind`**: one of `fact, procedure, troubleshooting, policy, spec, definition`.
- **`authority`**: 3 for a manual; 2 for the two videos and the photo.
- **`source.ref`** is one source id; a card built from several books cites one
  representative ref and enumerates the rest in `locator`. `extracted_at: '2026-09-11'`.
- **`see_also` / `not_to_be_confused_with`** may name only ids that exist now
  (`rtk proxy .venv/bin/kb vocab` lists them) or ids you wrote in this run. The
  `dangling-link` check covers both fields. Cross-links to cards another agent is
  writing go in your report under "intended links", not in the card.
- **Look-alike codes**: `E0`, `E1`, `E2`, `E4`, `ER` are separate faults; the Dyaco
  SMs and the OM Q&A tables may explain the same code differently — one card per
  code per family, neighbours in `not_to_be_confused_with`, first body line says
  which this is. **Spirit and Sole carry the same code letters with different
  meanings** — link with `not_to_be_confused_with`, never merge.
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
    id='xterra-trx-errors-e1-no-rpm-signal', title='...', kind='troubleshooting',
    question='...', asked_as=('...','...'), keywords=('...','...','...','...'),
    facets={'brand': ['xterra'], 'product_line': 'treadmill', 'model': '*',
            'applies_to': ['trx2500-2024','trx3500-2024'], 'section': 'errors', 'code': 'e1'},
    authority=3, not_to_be_confused_with=(), see_also=(),
    source_ref='xterra-treadmill-trx2500-2024-service-manual',
    source_locator='8.2 Error Message: E1, PDF p. 34; text.md lines 602-631; also trx3500-trx4500 SM p. 40',
    source_extracted_at='2026-09-11', body='...', path='')
open(path, 'w').write(render_card(c))
```

Run it with `rtk proxy .venv/bin/python $S/x1/<section>/gen.py`. Make the generator
**refuse** any target path that is in `git ls-files cards/`.

## Check yourself

`rtk proxy .venv/bin/kb lint` is read-only and safe any time. Fix every problem in
a card you wrote; leave the rest. Then check your relative links resolve:

```bash
rtk proxy git status --porcelain -uall cards/ | awk '{print $2}' | while read f; do
  grep -oE '\]\(([^)]+\.md)\)' "$f" | sed 's/](//;s/)//' | while read l; do
    [ -f "$(dirname "$f")/$l" ] || echo "BROKEN $f -> $l"; done; done
```

And that no title you wrote is already in use:
`rtk proxy grep -rh '^title:' cards/ --include='*.md' | sort | uniq -d`.
A title already used by a Spirit or Sole card **is** a collision — reword yours
(say "Xterra" nowhere in the title; change the phrasing instead).

## Report

Write `$S/reports-x1/<section>.md`, **at most 60 lines**, with these headings:
Cards written (count, and the list of ids); Cross-brand twins (Xterra id ↔ Spirit
or Sole id, and whether the figure matches); Intended links to other sections'
cards; Boundary calls (facts you left to a neighbouring section, and which);
Absences proved; Contradictions and damaged text; Brief defects (anything in this
brief or your section brief that was wrong — every wave so far the brief has been
wrong somewhere).

Your final message to the orchestrator is **at most 25 lines**: counts, the
report path, and anything that needs a human decision. Do not paste cards.

Do not use `AskUserQuestion`, `Artifact`, or any git writing command. If you are
blocked, write the block into your report and finish what you can.

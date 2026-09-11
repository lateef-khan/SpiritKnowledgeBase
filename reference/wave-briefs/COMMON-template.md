# Common brief — Xterra wave X2: bikes, ellipticals, climber, app Q&A (2026-09-11)

You are one of eight agents. Each agent owns **one section** across **all 37
sources** in this wave. Sections are disjoint, so you never collide with another
agent. You write cards; you never commit. The orchestrator reconciles and commits.

Repository: `/mnt/HDD/Projects/SpiritKnowledgeBase` (branch
`feat/kb-xterra-x2`, already checked out — do not switch branches).
Scratchpad: `/tmp/claude-1000/-mnt-HDD-Projects-SpiritKnowledgeBase/e835e5c4-bdf0-4d59-988b-1d30984c2ffd/scratchpad`
(call it `$S`). **Namespace every scratch file you create under `$S/x2/<your-section>/`**
— the scratchpad is shared by all eight agents. `$S/pages.py` is the page printer.

Read, in this order, before writing anything:

1. `/mnt/HDD/Projects/SpiritKnowledgeBase/CLAUDE.md` — the organising rule, one
   brand per card, ghost text, absences.
2. `/mnt/HDD/Projects/SpiritKnowledgeBase/.claude/commands/kb-extract.md` — card
   shape, facets, §4b section rulings, look-alike codes. **Overrides below win
   where they disagree with it.**
3. Your section brief (the file you were given).
4. Every source in this wave that has content for your section (§ "Sources").

## The brand, and what already exists

**Xterra** has 19 treadmill ids carded on 2026-09-11 (548 cards, wave X1) and,
as of this branch, 30 bike / elliptical / climber ids with **no cards yet** except
the 30 product cards (`cards/shared/specs/<family>-model-numbers.md`, which you
never edit). Every card you write is `brand: [xterra]`; `product_line` is the
value on the source's line below (`bike`, `elliptical`, `climber`; the app Q&A
is `'*'`).

Xterra is a separate range, not rebadged Spirit — but the safety, electrical,
maintenance and warranty pages are **Dyaco boilerplate**, and most of those
sentences already exist as Spirit or Sole cards. That does **not** make them
extendable: **a card carries exactly one brand.** You write the Xterra card and
point at the twin with `see_also` (same figures) or `not_to_be_confused_with`
(figures differ). Never add `xterra` to a Spirit or Sole card, never edit one.

**Xterra treadmill cards from X1 are a different matter — same brand.** Search
them first (`rtk proxy grep -rl '^  - xterra$' cards/ | xargs grep -l 'section: <yours>'`).
A fact that is the **same page with no line-specific figure** (a warranty term,
the registration and support page, the 48-states clause, a Proposition 65
label, "children under 13", the pulse-sensor disclaimer) is **one card**: extend
the X1 card — add the ids to `applies_to`, set `product_line: '*'`, add the book
to the locator. A fact with a line-specific figure or wording (weight limits,
clearances, anything that says "belt" or "pedal") stays per line: write the bike
or elliptical card and link with `see_also`.

Because nothing exists yet for these 30 machines, "extend" otherwise means
**extend the card your own run wrote a minute ago**: one card per *fact*, with
`applies_to` listing every machine that prints it — never one card per book.
Where a figure differs (user weight 250 vs 300 vs 350 lb, resistance 8 vs 16 vs
24 levels) it is one card per value, with the value in the title.

## Rule on contradictions — do not leave them open

When two books, or one book and itself, disagree, **you rule**: pick the reading
common sense supports — the owner's manual for what the customer sees and does,
the service manual for the board and its test values, the printed table over the
boilerplate paragraph, the drawing and the pack list over a step sentence that
contradicts them, the later printing over the earlier where the later one is
clearly a correction — write **both** readings in the body, and say in one
sentence which one the card follows and why. Never write "needs a human
decision". A figure that no book settles (a missing SKU) is an absence, not a
conflict; say it is unconfirmed.

## Sources in this wave

All under `sources/<id>/text.md`. OM = owner's manual, SM = service manual.
A source is evidence **only** for the model id(s) on its line.

```
xterra-bike-air350-2019-owners-manual          OM  air350-2019    bike   20 pp, stamp 20190613
xterra-bike-air650-2021-owners-manual          OM  air650-2021    bike   24 pp, stamp AIR650_20210125 ((c)2020, warranty Dec 12 2020)
xterra-bike-air650-2021-service-note           SM  air650-2021    bike   2 pp, scanned: "See Spirit AB900 Service Manual" + the two differences (AIR650 has NO Bluetooth; different wind cover / connecting-arm cover)
xterra-bike-fb150-2021-owners-manual           OM  fb150-2021     bike   16 pp, VER9_20210827
xterra-bike-fb350-2021-owners-manual           OM  fb350-2021     bike   18 pp, VER9_20210827; 96% the FB150 book, footers still say "FB150"
xterra-bike-fb160-2019-owners-manual           OM  fb160-2019     bike   20 pp, VER2_20191007
xterra-bike-fb160-2019-service-document        SM  fb160-2019     bike   3 pp, Nov 2019 service document (prints SKU 116419)
xterra-bike-fb360-2019-owners-manual           OM  fb360-2019     bike   24 pp, VER2_20191007; 90% the FB160 book
xterra-bike-fb180-2025-owners-manual           OM  fb180-2025     bike   20 pp, Revision 04.09.2025, new layout, SKU 118425 on the cover
xterra-bike-mb500-2014-owners-manual           OM  mb500-2014     bike   11 pp, SCAN (all OCR), stamp MB500_20140925
xterra-bike-mb550-2018-owners-manual           OM  mb550-2018     bike   20 pp, MB550_20180821
xterra-bike-mbx2500-2018-owners-manual         OM  mbx2500-2018   bike   20 pp, MBX2500_20180821
xterra-bike-sb120-2022-owners-manual           OM  sb120-2022     bike   24 pp, SB120_20220719
xterra-bike-sb120-2022-service-document        SM  sb120-2022     bike   4 pp, Dec 2019 service document
xterra-bike-sb150-2018-owners-manual           OM  sb150-2018     bike   27 pp, VER5_20180821
xterra-bike-sb240-2023-owners-manual           OM  sb240-2023     bike   44 pp, Rev 08/16/23, new layout, SKU 124013 on the cover
xterra-bike-sb250-2024-owners-manual           OM  sb250-2024     bike   28 pp, VER9_20240418 ((c)2019, warranty June 21 2019), SKU 125313 on the cover
xterra-bike-sb25r-2020-owners-manual           OM  sb25r-2020     bike   20 pp, SB25_20200706; the book says SB2.5r
xterra-bike-sb4500-2021-owners-manual          OM  sb4500-2021    bike   32 pp, SB4500_20210810
xterra-bike-sb45r-2013-owners-manual           OM  sb45r-2013     bike   24 pp, SCAN, stamp SB4.5r_20130605; the book says SB4.5r
xterra-bike-sb500-2020-owners-manual           OM  sb500-2020     bike   24 pp, SB500_20200706 ((c)2018, warranty July 6 2020)
xterra-bike-sb500-2020-owners-manual-2014-printing  OM  sb500-2020  bike   24 pp, SCAN, the same book printed 2014 (warranty Aug 1 2014) - 98.5% identical; cite it only where it differs (warranty date)
xterra-bike-sb600-2023-owners-manual           OM  sb600-2023     bike   44 pp, Rev 08/01/23, new layout, SKU 160113
xterra-bike-sb600-2023-service-manual          SM  sb600-2023     bike   30 pp, V1.0 (2025), JKEXER-style: assembly sequence, precautions, parts, checks
xterra-bike-ub120-2023-owners-manual           OM  ub120-2023     bike   24 pp, UB120_20231206 ((c)2019)
xterra-climber-rsx1500-2021-owners-manual      OM  rsx1500-2021   climber 32 pp, RSX1500_20210712 ((c)2021, warranty page still Aug 21 2018)
xterra-climber-rsx1500-2021-owners-manual-2017-printing  OM  rsx1500-2021  climber 26 pp, SCAN, stamp RSX1500_20171222, warranty Dec 20 2017 - 91% the 2021 book; cite where it differs
xterra-elliptical-eu100-2018-owners-manual     OM  eu100-2018     elliptical 20 pp, VER6_20180821
xterra-elliptical-eu150-2024-owners-manual     OM  eu150-2024     elliptical 29 pp, VER6_20240426, SKU 115024
xterra-elliptical-fs150-2016-owners-manual     OM  fs150-2016     elliptical 26 pp, SCAN, VER1_20160524
xterra-elliptical-fs15-2019-owners-manual      OM  fs15-2019      elliptical 20 pp, FS15_20190215; the book says FS1.5
xterra-elliptical-fs25-2020-owners-manual      OM  fs25-2020      elliptical 20 pp, FS25_20200706; the book says FS2.5
xterra-elliptical-fs30-2018-owners-manual      OM  fs30-2018      elliptical 20 pp, FS3.0_20180821; the book says FS3.0
xterra-elliptical-fs35-2020-owners-manual      OM  fs35-2020      elliptical 20 pp, FS35_20200706; the book says FS3.5; 87% the FS2.5 book
xterra-elliptical-fs58e-2013-owners-manual     OM  fs58e-2013     elliptical 24 pp, SCAN, FS58e_20130605
xterra-elliptical-fs59e-2014-owners-manual     OM  fs59e-2014     elliptical 28 pp, SCAN, FS59e_20140214
xterra-app-qa-2018                             QA  (see below)    '*'    2 pp, October 2018 app questions and answers
```

**The AIR650's service manual is the Spirit AB900's.** The manufacturer's note
says so, and lists the only differences: the AIR650 has **no Bluetooth**, and a
different iron-net wind cover and connecting-arm cover. So
`spirit-bike-ab900-2018-service-manual` (carded on `cards/ab900-2018/`, 88 cards)
is evidence for `air650-2021` **service** facts — error codes, wiring, boards,
disassembly, test values — and you write **Xterra** cards from it for
air650-2021 (never extend the ab900 cards; link them with `see_also`), omitting
anything Bluetooth. Say on each such card that the figure comes from the AB900
book by way of the note. The AIR650 owner's manual stays the source for what the
customer sees.

**The app Q&A** (`xterra-app-qa-2018`): two pages of questions about the
XTERRA Fitness app (pairing, accounts, which consoles). Card it under `console`
with `product_line: '*'` and `applies_to` = every Xterra id (X1 and X2) whose
owner's manual mentions the app or Bluetooth — grep `sources/xterra-*/text.md`
for `app|bluetooth` to build the list.

Scans (`SCAN` above) are all OCR: every page is a supplement block; read them as
such, and where a figure matters look at the render.

Seven books have printed **model-name quirks**: FS1.5 / FS2.5 / FS3.0 / FS3.5,
SB2.5r, SB4.5r (the ids drop the dot: fs15, sb25r, sb45r); the FB350 book's
footers say FB150. Cards use the id and may quote the printed name in the body.

Ids: `<model-id>-<section>-<slug>` for one machine; for several,
`xterra-<family>-<section>-<slug>` where family is `fb`, `sb`, `mb`, `air`,
`ub`, `fs`, `eu`, `bike`, `elliptical`, or `xterra-<section>-<slug>` spanning
product lines (e.g. `xterra-sb-safety-user-weight-limit-300-lb`,
`xterra-bike-errors-e1-no-rpm-signal`). Check `kb vocab` — X1 used
`xterra-tr-…`, `xterra-trx-…`, `xterra-ws-…`, `xterra-treadmill-…`. Files: `cards/<model-id>/<section>/…` or
`cards/shared/<section>/<full id>.md`.

The book's page numbers and the PDF page numbers usually differ by one or two
(a cover and a blank page); cite as `p. 21 (printed 20)`.
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
`pdftoppm -r 150 -png -f N -l N "<pdf>" $S/x2/<section>/pg` then `Read` the PNG. The PDF
path is in the header comment of each `text.md` and in `sources/manifest.yaml`.

## Before you write: search, then sort every fact into one of four outcomes

8,608 cards exist, 548 of them Xterra treadmill cards. Search **on the thing itself** (`E1`, `speed sensor`, `GFCI`,
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
3. **An Xterra card holds it** — from X1 (your section only, same page, no
   line-specific figure) or from your own run → extend it: add the machine(s) to
   `applies_to` (sorted), `model: '*'`, `product_line: '*'` if it now spans
   lines, add the book to `source.locator`. You may edit an X1 card only if its
   `section` is yours; report the others as intended extensions.
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
  `rtk proxy git status --porcelain cards/ | grep -v '^??'` — every ` M` line must
  be an X1 Xterra card of **your** section that you meant to extend; anything
  else is a bug in your run. Recover with `git show HEAD:<path> > <path>`.
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
  ("…on an Xterra sb600-2023 recumbent bike?" — the id spelled literally), or the
  brand and family for a several-machine card ("…on an Xterra FS elliptical?").
- **`facets`**: every key filled. `brand: [xterra]` only. `product_line`: the
  value on the source's line, or `'*'` when the card spans lines.
  `model`: the id, or `'*'` when `applies_to` lists two or more. `applies_to`:
  sorted list of the real ids — **never `'*'` in this wave**, even for a policy
  page: list the Xterra ids that print it (a `'*'` would be served to Sole and
  Spirit customers, and nothing filters a brand back out). `section`: yours.
  `code`: the error code for an error-code card, **lowercase** (`e1`, `e2`, `err`),
  else `'*'`. **Omit `model_number` and `lookup`** — the product cards carry them.
- **`kind`**: one of `fact, procedure, troubleshooting, policy, spec, definition`.
- **`authority`**: 3 for a manual or the app Q&A; 2 for the AIR650 service note.
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
    id='xterra-fb-errors-e1-no-rpm-signal', title='...', kind='troubleshooting',
    question='...', asked_as=('...','...'), keywords=('...','...','...','...'),
    facets={'brand': ['xterra'], 'product_line': 'bike', 'model': '*',
            'applies_to': ['fb150-2021','fb350-2021'], 'section': 'errors', 'code': 'e1'},
    authority=3, not_to_be_confused_with=(), see_also=(),
    source_ref='xterra-bike-fb150-2021-owners-manual',
    source_locator='Troubleshooting, PDF p. 14; text.md lines 402-431; also FB350 OM p. 15',
    source_extracted_at='2026-09-11', body='...', path='')
open(path, 'w').write(render_card(c))
```

Run it with `rtk proxy .venv/bin/python $S/x2/<section>/gen.py`. Make the generator
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

Write `$S/reports-x2/<section>.md`, **at most 60 lines**, with these headings:
Cards written (count, and the list of ids); Cards extended (X1 id → ids added); Cross-brand twins (Xterra id ↔ Spirit
or Sole id, and whether the figure matches); Intended links to other sections'
cards; Boundary calls (facts you left to a neighbouring section, and which);
Absences proved; Contradictions and the ruling you made on each; Damaged text; Brief defects (anything in this
brief or your section brief that was wrong — every wave so far the brief has been
wrong somewhere).

Your final message to the orchestrator is **at most 25 lines**: counts, the
report path, and anything that needs a human decision. Do not paste cards.

Do not use `AskUserQuestion`, `Artifact`, or any git writing command. If you are
blocked, write the block into your report and finish what you can.

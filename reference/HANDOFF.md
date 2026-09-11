# Handoff — where the knowledge base stands and how to continue

**Written:** 2026-09-10, at a clean pause. **Updated 2026-09-11** after all four
sub-waves of 3a merged; 3a is done except the twelve Spirit medical books the Xterra
folder holds (see 3a-bis). Nothing is ingested but uncarded.
**Branch to start from:** `main`. Every branch below it is merged and deleted.

Read `CLAUDE.md` before touching `cards/`. Then `.claude/commands/kb-extract.md`.
This file tells you what is done, what is next, and how the work is actually run.

---

## 1. State of `main`

| | |
|---|---|
| cards | **7,628** |
| `kb lint` | 0 problems |
| declared model ids | **312** (196 Spirit, 116 Sole) — every one has at least one card |
| sources ingested | 451 |
| machines carrying `model_number` | **230** of 258 with single-machine cards |

Check it yourself:

```bash
.venv/bin/kb lint
.venv/bin/kb facet-gaps          # machines still without a model number
.venv/bin/kb vocab               # undeclared_facet_values must be {}
```

---

## 2. What is finished

**Every Spirit owner's manual in `/mnt/HDD/Downloads/Spirit Folder/Spirit Owners Manuals`** — treadmills, ellipticals, bikes, indoor cycles, air bikes, climbers, steppers, rowers, the ergometer, the MED rehabilitation steppers, and the 39-machine strength range. Eighteen waves, PRs #22 through #51.

**The `model_number` facet** — a list of six-digit SKUs on every card that names exactly one machine. `reference/model-numbers.md` explains where every number came from and which shortcuts were measured and rejected. `reference/model-numbers.csv` is the mapping; `reference/model-numbers-open.csv` the 25 machines still without one.

---

## 3. What is next, in this order

### 3a. Spirit service manuals — 123 PDFs, 103 distinct documents

Folder: `/mnt/HDD/Downloads/Spirit Folder/Spirit Service Manuals`

Surveyed, clustered and **identified — not ingested**. Byte-identical copies
and 95%+ re-exports are collapsed to 103. `reference/service-manuals-identified.tsv`
names the machine each document belongs to, with the sentence that decided it.
Read its `verdict` and `confidence` columns before anything else.

| verdict | documents |
|---|---|
| `existing` — belongs to a model id already in `kb.yaml` | 69 |
| `already-ingested` — a re-export of a source already in the repository | 11 |
| `new-machine` | 13 |
| `multi-machine` — one manual covering several machines | 3 |
| `not-a-manual` | 7 |

So **85 documents to ingest**, of which **34 rows are marked `unsure`** — mostly
2016-code manuals mapped to the earliest pre-2023 id, and "2020 ver." ENT manuals
mapped to the 2022/2023 ENT ids. Re-check those against the owner's manual
already carded for that id before ingesting.

**New machines, cover-proven:** the **1000 series** — `ct1000-2023`,
`cr1000-2023`, `cu1000-2023`, `ce1000-2023` (certain); `ce900ent-2021`;
`cr800-2011` (the XR898); `crw800-2016`; `cs800-2016`. **Multi-machine:** one
2008 dealer manual for `xbr25-2008` + `xbr55-2008`; one for
`xt175/275/375/475/675-2008`, an older generation than the XT185 family; and the
XE100–XE500 manual adds `xe400-2007` and `xe500-2007` to the three that exist.
Years marked unsure come from PDF creation dates or the SKU table, not a
printed stamp — prove them before declaring the id.

**Three the folder got wrong.** `XS895 (XE895-SE022 2016)` is an *elliptical*
manual, 98% identical to the CE850 one, and belongs to `xe895-2018`. `DYACO 7.0T
(MT8000-ST021-02)` shares its parts list with the **MT200** owner's manuals and
only 3% with the 7.0T — it is `mt200-2022`, not `70t-2026`. `XIC600 (SB700,
SB702)` is a 2009 Dyaco SB700 manual and belongs to Sole `sb700-2011`.

**Five files in this folder are Xterra**, a brand `kb.yaml` does not yet declare:
SB600, ERG160, ERG180, ERG800W, and ERG-750W. Hold them for 3b.

**Two filename SKUs disagree with the repository**: XBU55 service `553123`
against the carded `552123`; XBR55 service `551123` against the owner's-manual
filename `551223`. Resolve from the database before trusting either.

The seven that are **not machine manuals**, each still worth a card or two: an
AB900/AIR650 discrepancy sheet; a scanned CIC850 pairing tip; an E-50H service
bulletin for the CT800 800840; an E27 email for the 7.0T model 770844; a
commercial cardio warranty sheet (Rev 03.07.2019); a power-requirements sheet
(Rev 03.06.2019); and the MT200 error-code list. The three `ENT Support` tips
are already ingested as text sources.

**Run it as sub-waves by product line**, not as one wave of 103: treadmills 27,
bikes 32, ellipticals 17, rowers 10, climbers/steppers 10, odds 7.

**Treadmills: done** (PR #54, 2026-09-11) — 24 sources plus the E-50H bulletin
that was filed under Bikes; 346 new cards, 282 extended. Decisions it settled,
all recorded in the TSV's `evidence` column:

- The 1000 series is **ENT**: `dbo.MODEL` has only `CT1000ENT` 210854,
  `CE1000ENT` 210054, `CR1000ENT` 210154, `CU1000ENT` 210354, and every cover
  reads "ENT". Ids are `ct1000ent-2023`, `ce1000ent-2023`, `cr1000ent-2023`,
  `cu1000ent-2023` — not `ct1000-2023`.
- The XT175/275/375/475/675 dealer manual is **`-2007`**, not 2008: all five
  rows carry `FP_DATE` 8/20/2007, the batch date shared by every Sole "2007" row
  and by XE100–XE500, already carded as `-2007`. Expect the same for the XBR25 /
  XBR55 dealer manual (251117 / 551117, same date) in the bikes wave.
- The "2020 ver." ENT service manuals map to the `-2022` ENT ids (their
  engineering-mode chapters match the 2022 owner's-manual cards). `dbo.MODEL`
  also lists "CT800ENT 2020" 800850 and "CT850ENT 2020" 850851 with no manual.
- The Dyaco 7.0T (MT8000-ST021-02) book is `mt200-2022`; `dbo.MODEL` lists
  770884 "MT8000" and 770881 "7.0T" apart from the MT200 pair — a 3c question.
- The CT900 "Error Codes & Troubleshooting Guide" is a strict subset of the
  full CT900 manual and was not ingested.
- `Mannual Service v1.0 (magnetic) 900660.pdf` in the Bikes folder is a
  **CSC900 climber** manual and 900660 **is** a `dbo.MODEL` row (the TSV said it
  was not); run it with the climbers, not the bikes.

**Bikes: done** (PR #55, 2026-09-11) — 26 sources, 305 new cards, 226 extended.
Seven new ids: `cu1000ent-2023`, `cr800-2009` (the XR898 book, January 2011,
can only be the "CR800 2009" rows 800149/800143), `xbr25-2007` / `xbr55-2007`
(the 2007 batch date), and `xbr25-2016` / `xbr55-2016` / `xbu55-2016`: **the
2016-coded Dyaco books (2017 PDFs) predate the 2019 SKUs' first production**
(Jul/Oct 2018), so they belong to the explicit "2016" rows, not to the 2019
owner's-manual ids. Where the table has no later row (XBR25) the 2019 manual is
probably a reprint for the 2016 SKU; both ids stand and the product card says so.
The table also settled `xbr55-2019` 551118, `xbu55-2019` 551218, `xbr95-2016`
951115 and `xbr55-2023` 551123/551223 (a colour pair). The XBU55 service
filename's 553123 is in no row. The SB700 book in the XIC600 folder is Sole and
was ingested as `sole-bike-sb700-2011-service-manual`. Expect the ellipticals to
follow the same 2016-SKU rule: XE195 195015, XE295 295015, XE395 395015, XE795
795015, XG400 400415 all exist and no 2018/2019 rows do.

**Ellipticals: done** (PR #56, 2026-09-11) — 16 sources (one of them the
"XE895-SE022" book the Climbers Steppers folder held under XS895), 265 new
cards, 140 extended. Eleven new ids: `ce1000ent-2023` (210054), `ce900ent`
(900050, no year — no stamp, no owner's manual, like `cu900ent`), `xe400-2007`
/ `xe500-2007`, and by the 2016-SKU rule `ce800-2016` (800045, the "XE890B"
book), `xe195-2016`, `xe295-2016`, `xe395-2016`, `xe795-2016`, `xg400-2016`,
`xe895-2016`. The three per-line "the only tool is a multi-meter" cards were
one fact and are now one card with `product_line: '*'` — when a fact is the
same Dyaco page across product lines and carries no line-specific figure, make
it one card, not one per line.

**Rowers, climbers/steppers, medical, strength, sheets: done** (PR #57,
2026-09-11) — 18 sources, 274 new cards, 214 extended. Three new ids:
`cr1000ent-2023` (a bike filed under Rowers), `crw800-2016` (800945) and
`cs800-2016` (800645). The XS895 "enter EM and reset ODO" video was described
frame by frame (no ffmpeg on PATH; `.venv` has `imageio_ffmpeg`) and cited as
corroboration only. The two 2019 sheets are `product_line: '*'` cards whose
`applies_to` holds the ids current in March 2019; MS350/MR100/MU100 have no ids.

### 3a-bis. Spirit medical books in the Xterra folder, and owner's manuals the
### handoff wrongly called done

`Xterra Service Manuals/Bikes/MEDICAL/` and `Treadmills/MEDICAL/` hold twelve
February-2026 exports with the SKU on the cover: 4.0R 740145, 4.0U 740245,
7.0R 770145, 7.0S 770545, 7.0U 770245, 7.5S 775545, 8.0U 780245, 8.5R 784145,
8.5UE 785045, 4.0T 740885 (ST8700A-ST026-01, a newer revision), 7.0T 770885
(99.7% the DYACO MT8000 book carded as `mt200-2022` — so those cards must gain
`70t-2026`), 8.0T 780885. **The six medical bikes have no id and no card**, yet
their owner's manuals sit in `Spirit Owners Manuals/Bikes/4.0R`, `4.0U`, `70R`,
`70U`, `8.0U` and `Treadmills/8.5R` — nine PDFs the manifest never saw. A hash
check of the whole owner's folder (2026-09-11) also found: `XT485/2013/485812
XT485.pdf` (dbo.MODEL "XT485-2013"), two Lexmark scans of the 2013 CT850
(850812 / 850813, no text layer), `CU800/2015/CU800_OM_800312.pdf` (secured
scan), `bike backup/XBR95/XBR95_NewStyle_OM_2024_0715.pdf` (©2023), three
strength files (one with a shifted font encoding), `Treadmills/70T/740881 -
70T.pdf` (©2024, 32% of the 2026 book — an earlier 7.0T), and 2025 printings
of the 4.0T / 7.0T / CR900 / CU900 books at ~90%. The plan is in the session
scratchpad as `plan-medical-and-om-gaps.md`; run it as one wave before 3b.

Two things the wave learned about the method: tesseract cannot read a
photographed page (the E-50H bulletin got 8–19 words a page and was typed by
eye from the render instead), and a killed sweep's `xargs` children keep
running and append a second copy of every supplement — kill by PID and
re-check `sort | uniq -d` on the supplement headers before committing.
The bikes wave added a third: two section agents will card the same Q&A row
when the brief gives it to both (belt slip went to errors *and* maintenance);
say in the errors brief that a row whose remedy is a care procedure belongs to
maintenance, and check for pairs at reconciliation.

**Service manuals overlap owner's manuals.** A section agent must grep existing
`applies_to` before writing, or it restates cards that exist. What a service
manual genuinely adds: exploded views with part numbers, wiring, test and
engineering modes, disassembly, error-code tables with remedies.

### 3b. Xterra — 66 owner's + 26 service manuals

Folders: `/mnt/HDD/Downloads/Spirit Folder/Xterra Owners Manuals` and
`.../Xterra Service Manuals`

**Measured, not started.** The user's instruction: *if it says Xterra, that is a
new brand; otherwise it is all Spirit.* So `xterra` must be added to
`kb.yaml`'s `brand.values` and `models:` before the first card.

**Xterra is a separate range, not rebadged Spirit.** Owner's manual against
owner's manual: TR300/XT385 47.9%, TR150/XT185 46.5%, TRX2500/XT485 34.8%,
FS25/XE195 27.0%, SB150/XBR25 18.8%, TR75/XT685 18.8%. A re-export of one
document measures 95-100% here. Nothing Xterra comes close; the overlap is Dyaco
boilerplate. All 92 are real new work. The range is AIR, FB, MB, SB, UB, RSX,
EU, FS, ERG, ADB, TR, TRX, WS — not one Spirit XE/XT/XB among them.

**The folder names lie in both directions.** The Xterra *service* folder holds
service manuals for a dozen **Spirit medical** machines by SKU (4.0T 740885,
7.0T 770885, 8.0T 780885, 7.0S, 7.5S, 8.5UE, 4.0R, 4.0U, 7.0R, 7.0U, 8.0U,
8.5R). The 7.0T is 99.8% and the 7.5S 96.9% identical to their Spirit-folder
twins; the **4.0T is 87.7% — a newer revision (`ST8700A-ST026-01`) the Spirit
folder does not have.** Meanwhile the Spirit service folder holds Xterra
machines: SB600, ERG160, ERG180, ERG800W, ERG-750W, and an AIR650 note. **Take
the brand from the document, never from the folder.**

Also: `Rowers/ERG750/ERG750W_OM_20251112.pdf` in the Spirit owner's folder is an
XTERRA rower, held back from the Spirit waves for this reason.

### 3c. Left over from the model-number work

25 machines have no `model_number`. `reference/model-numbers-open.csv` lists
each with its candidates. Most are one model id facing two SKUs because the
other generation has no cards yet; they will resolve as 3a and 3b card those
generations. Do not guess them.

---

## 4. How a wave is run

This is the method that has held for eighteen waves. It is in the memory notes
too, but it is repeated here so a fresh session does not have to rediscover it.

1. **Survey and cluster before ingesting.** Check `sources/manifest.yaml` for
   what is already in — but its `sha256` is **inconsistent**: 240 entries hash
   the PDF, 116 hash the source's own `text.md`, 9 neither. Hash both, and fall
   back to filename plus 95%+ text overlap. Then cluster the rest on **native
   PDF text** at 95% or higher. Different machines share one template at 92-94%, so use a
   model-name guard: two files whose names differ never merge. Keep the fullest
   file per document.
2. **Prove every model id from the document.** Back cover revision stamp, native
   text first, render second. A filename year is not evidence. A phantom id
   contaminates every card it touches.
3. **Build the text with the render-vs-extraction sweep.** For every page, count
   the words a 300 dpi render knows that the text layer does not; five new words
   means append the OCR under an `=== OCR SUPPLEMENT, PDF PAGE n ===` header.
   Score all four rotations for scans. The build script lives in the session
   scratchpad and is short; the rules are in `CLAUDE.md`.
4. **Ingest by shell**, declare the model ids in `kb.yaml`, run `kb vocab`,
   commit the ingest on its own.
5. **Write one brief per section** — safety, assembly, console, programs,
   errors, maintenance, specs, warranty — to disk. Every brief says: read all
   the manuals in the wave, never split by manual; search before writing;
   extend, do not restate; one brand per card; omit `model_number`; prove an
   absence twice; report in 25 lines.
6. **Launch eight agents at once**, each given only its brief's path. Their
   reports come back capped. They correct each other in flight, and they will
   correct the brief — every wave so far, the brief has been wrong somewhere.
7. **Reconcile** before committing: two-brand cards, Sole cards touched,
   dangling model ids, id/section mismatch, near-duplicate titles (normalise
   `ise`/`ize`, sort words), broken relative links, dangling `see_also`,
   stray `model_number`. Then `kb lint`, then commit, PR, wait for CI,
   squash-merge, delete the branch.

The user merges nothing by hand; the session opens the PR, waits for the
`lint` check, and merges it.

---

## 5. Things that went wrong and how they were caught

Kept short. Each one is now a rule in `CLAUDE.md` or in this file.

- **A clustering pass merged XT285 with XT185 at 99.4%.** Different machines,
  one template. Fixed by refusing to merge files whose names disagree.
- **A pass attributed a 2024 manual's SKU to the 2018 machine** by matching on
  product name instead of the machine's own source. A manual is evidence only
  for its own model id.
- **A filename carried another machine's SKU.** `F89(2023)_585822_…` holds the
  F85's number; `CIC850_800390_…` holds the CIC800's. Cross-check every
  filename number against the database rows for that product.
- **A rule "no year in the name means the same machine" tied the 2023 and 2026
  E25 numbers to the 2019 machine.** Five different LCRs are all named plainly
  "LCR". A shared name proves nothing.
- **The report command broke when the facet became a list** and claimed no
  machine had a number. Fixed the same hour.
- **Four ghost-text finds in one wave**: Chinese OEM part lists under English
  covers, a page printing `(951)(908)` where the text layer says `(951)`,
  "emergency dismount" printed where the layer says "emergency escape".
- **A shifted font encoding that looks like real text** (`&RXQWHU3ODFDUG`) —
  a new failure mode alongside flattened images and ghost layers.
- **Dyaco service manuals carry no Spirit back-cover stamp** and almost never a
  printed date. Their year comes from the cover — "(2020)", "(2023)" — the
  factory-code suffix (an `A` suffix means 2023), the SKU, or the SKU table.
- **The SKU database is `CustService` on the Spirit Server for every brand.**
  An earlier note pointed Sole lookups at Azure; that was wrong and cost a
  round trip.

---

## 6. Where the pieces are

| thing | where |
|---|---|
| SKU table | `dbo.MODEL` in `CustService`, over `ssh spirit`; recipe in the memory note `spirit-sku-lookup-custservice` |
| model-number method and evidence | `reference/model-numbers.md`, `.csv`, `-open.csv` |
| service-manual identification | `reference/service-manuals-identified.tsv` |
| Xterra measurement | section 3b above |
| the eight section briefs from the last wave | not kept; they are rewritten per wave from the pattern in section 4 |
| Sole manuals on disk | `/mnt/HDD/Downloads/Sole Treadmill/` — not the Spirit folder |

`docs/` is gitignored in this repository. Anything meant to be committed goes
in `reference/`.

---

## 7. Known defects left in place

- `cards/ctsbs900/maintenance/sanitizing-equipment.md` restates
  `cards/shared/maintenance/sanitizing-equipment.md`, whose `applies_to` is `*`.
  Pre-existing; the id is frozen.
- Wave-9 manifest entries store a relative `origin_uri`
  (`file://Ellipticals/CE900/…`) rather than an absolute path. Match sources to
  PDFs by `sha256`, never by that field.
- `spirit-rehab-stepper-programs-ten-program-keys-including-an-hr-key-no-manual-describes`
  has a corrected title and body but a stale id, which cannot change.
- `xe150-2005` is carded as Spirit; the database brands it XTERRA. Left as is;
  revisit when the Xterra brand exists.

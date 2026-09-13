# Handoff — where the knowledge base stands and how to continue

**Written:** 2026-09-10, at a clean pause. **Updated 2026-09-12** after the third and
last Xterra wave (X3) merged, after a full hash-and-text check of every PDF on
disk, and after Sole treadmill waves **A1** (PR #64) and **A2** (PR #66) merged.
**3a (Spirit) and 3b (Xterra) are done. Sole is IN PROGRESS: 49 of 95 legacy
owner's manuals ingested** — see section 3d.
Read section 8 first. Nothing is ingested but uncarded.
**Branch to start from:** `main`. Every branch below it is merged and deleted.

Read `CLAUDE.md` before touching `cards/`. Then `.claude/commands/kb-extract.md`.
This file tells you what is done, what is next, and how the work is actually run.

---

## 1. State of `main`

| | |
|---|---|
| cards | **9,827** |
| `kb lint` | 0 problems |
| declared model ids | **445** (209 Spirit, 172 Sole, 64 Xterra) — every one has at least one card |
| sources ingested | 616 |
| machines carrying `model_number` | **322** of 363 with single-machine cards |

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
of the 4.0T / 7.0T / CR900 / CU900 books at ~90%. **Done** (PR #58, 2026-09-11): 28 sources, 395 new cards, 535 extended. Thirteen
new ids: `40r-2025`, `40u-2025`, `70r-2025`, `70u-2025`, `80u-2025`, `85r-2025`
(the 2025 medical bikes, SKUs on their service-manual covers; 784145 for the 8.5R
is in no `dbo.MODEL` row), `40r-pt` / `40u-pt` (the undated Dyaco "PT" consumer
books — not therapy editions), `70r-2021` (the Dyaco "MED" book, Rev 1.2.1
2021-10-14), `40t-2025` (740881 — the two 2025 4.0T printings, one misnamed
"740881 - 70T.pdf") and `70t-2025` (770881), `xt485-2013` (485812), `ct850-2013`
(850813; the scanned 2013 book, all OCR). The 7.0T-770885 export's 23 cards list
`70t-2026`. The 85UE keeps `product_line: ergometer`. Not ingested, with reasons in
the commit: XBR95/CR900/CU900 2024 re-exports, CSD-LPSR 2024, a third CU800-2012 scan.

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

**X1 treadmills: done** (PR #60, 2026-09-11) — 19 owner's manuals, 8 service
manuals, two videos and one annotated photo (each described frame by frame as a
text source, authority 2); the `xterra` brand and 19 ids added to `kb.yaml`; 19
product cards and **529 new cards** (console 105, errors 104, assembly 78,
programs 67, specs 59, maintenance 46, safety 44, warranty 26); nothing
extended — no Xterra card existed, and no Spirit or Sole card was touched.
Decisions it settled:

- **Ids follow the owner's manual's revision stamp**, and a service manual whose
  factory code or error table matches the owner's book joins that id — the
  2018/2019 Dyaco books (GT90B-NT022, GT90C/D-NT023/024, GT65-NT014) sit under
  `trx2500-2024`, `trx3500-2024`, `trx4500-2024`, `tr150-2021`, because
  `dbo.MODEL` holds exactly one SKU per name (125817 from June 2017, and so
  on) and the 2024 owner's books are a batch re-issue dated 7 June 2024. The
  TRX5500 owner's book prints `GT90D-NT041-01`, the service manual is
  `GT90D-NT041`. `TR1400_OM_*.pdf` is the **TRX1400** (the book says so, with
  `T3-NT053-01`).
- **The survey missed a stamp.** `TR260_OM_20231208.pdf` prints *Revision 4.0:
  12.08.2023* on page 3 under a ©2022 / August 2022 warranty; the survey TSV
  recorded only "4.0". The id is `tr260-2023`, renamed mid-wave (grep the
  stamp with the date, not just the word).
- **Seven owner's books print their SKU on the cover** in the file stamp
  (`TR65_OwnersManual_165873_20230928`, TR75 175873, TR75H 175825, TR85
  185873, TR95H 195813, WS200 120082, WS300 130082, TRX5500 155810); the
  first search missed them because `_` is a word character. WS200/WS300 have
  no `dbo.MODEL` row at all. Open: TR200 (two rows), TR260 (no row), TR6.4
  and TR6.6 (only 2013/2014 rows). The table brands most Xterra rows SPIRIT;
  the query in `reference/xterra-survey/` context matched on the MODEL name.
- `xe150-2005` stays Spirit: its manual is the Spirit XE150/XE350/XE550 book
  and 54 cards share it with the two XE siblings. The database's XTERRA brand
  on 150005 is noted here and nowhere else.
- One-machine filenames strip **both** the model id and the section
  (`cards/tr65-2023/programs/user-programs-of-twenty-segments.md`), the repo
  majority (1,227 to 953); the agents had left `programs-` on and 211 files
  were renamed with their links rewritten.

What the wave learned about the method: **the sweep's rotation scorer was
wrong** — common words plus 0.1 × token count let a garbage rotation of a
label-only landscape page win, and most Dyaco service-manual picture pages
came out upside down; three agents read the renders instead. `sweep.py` now
scores by dictionary hits and `fix_rotation.py` re-scores existing
supplements. The Xterra books print three service numbers ((870) 336-4286,
(870) 935-1107, 1-800-258-8511 — the last is Spirit's) and the TRX1400 book
says "Spirit Fitness warranty"; carded as printed. The TR6.6, TRX4500 and
TRX5500 books print a bike-template "external power supply" paragraph.

**Open questions for a human from X1**, all on the cards and in PR #60:
TRX4500 max incline 15 (owner's) vs 12 (the shared service manual); the TRX
owner's E6 "power" vs service E6 "controller" / E7 "power"; every warranty
page's SERVICE paragraph (12 months) contradicting its own table (90 days /
1 year); the SM "never use a GFCI" vs OM "avoid if possible" and SM 230 V /
10 A / 16 AWG vs OM 120 V / 15 A / 14 AWG; TR95H and TR75H levelling feet
turning opposite ways; TR260 step 5 "4 bolts" vs a pack list of 6; the TR260
5-pin cable pin-out printed two ways; the TR75H console-features page being a
copy of the TR95H's and contradicting its own program pages.

**X2 bikes, ellipticals, climber, app Q&A: done** (PR #61, 2026-09-11) — 30
owner's manuals (seven of them scans with no text layer, OCR'd at all four
rotations), the SB600 service manual, the FB160 and SB120 service documents, the
AIR650 service note and the 2018 app Q&A; 30 ids, 30 product cards, **433 new
cards** (assembly 160, console 76, programs 56, specs 40, safety 36, errors 27,
warranty 20, maintenance 18) and **30 X1 treadmill cards extended** to
`product_line: '*'` where the page is the same across lines (warranty terms,
registration, Prop 65, pulse-sensor disclaimer, RPE, target zone, chest-strap
cards, sanitizing). Decisions it settled:

- **The stamp names the document, and three plan years moved:** `air650-2021`
  (AIR650_20210125 under (c)2020), `sb250-2024` (VER9_20240418 under (c)2019),
  `sb45r-2013` (SB4.5r_20130605 under (c)2012). ERG400 likewise stamps
  ERG400_20150205 for X3.
- **Two printings of one machine's book share one id, named by the newer
  printing**: `sb500-2020` (the 2014 scan is 98.5% the 2020 export),
  `rsx1500-2021` (the 2017 scan is 91%); the older printing is a second source
  cited where it differs (warranty dates).
- **The AIR650's service manual is the Spirit AB900's** by the manufacturer's
  two-page note (no Bluetooth, no wind cover, no connecting-arm covers). Cards
  for `air650-2021` were written from `spirit-bike-ab900-2018-service-manual`
  with the `ab900-2018` twin in `see_also`; every locator names the note.
- **SKUs printed on covers but absent from `dbo.MODEL`**: SB240 124013, SB250
  125313 (the table's SB250 row is 125316). FB180 prints 118425 and the table
  also holds 115425. `sb150-2018` is open (115314 / 115316, same name).
- **The FS5.8e scan is truncated** at printed p. 22: no maintenance, warranty or
  chest-strap pages exist in the file; a complete copy is needed before any
  term is stated for it.
- Contradictions were **ruled on the card** (the user's instruction after X1):
  the FB150/FB350 front-page "one year" vs the 90-day table (table wins), the
  FB160/FB360 3-months-from-shipping clock, the SB240 FCC "Class C" misprint,
  the RSX1500 mast's 5 bolts vs a printed 4, the SB500 "a few hours" pedal
  re-tighten vs SB4.5r "a few months" (hours), the FB180 (870) 335-5500 misprint
  of 333-5500. Both readings sit in every such body.
- Moving / transport cards are `maintenance`; four assembly duplicates were
  deleted at reconciliation with `dedupe.py` (now in `reference/wave-briefs/`,
  restricted to the wave's own cards after it cleaned two Spirit and Sole
  see_also lists it had no business touching).

**X3 rowers and strength: done** (PR #62, 2026-09-12) — 11 rower owner's
manuals (one scan), six rower service manuals (four filed in the Spirit
folders: ERG160, ERG180, ERG-750W, ERG800W_R80), the ERG750W owner's manual
from the Spirit owner's folder, and the four dumbbell books; 15 ids, 15 product
cards, **349 new cards** (assembly 152, console 39, specs 37, safety 36,
programs 34, errors 25, maintenance 17, warranty 9) and **53 X1/X2 cards
extended** (24 warranty, 9 safety, 5 console, 5 errors, 5 maintenance, 3 specs,
2 programs). Decisions:

- Stamps moved three plan years: `erg220-2023` (VER3_20230313 under (c)2019),
  `erg400-2015` (ERG400_20150205 on the scan), `erg700-2022` (VER6_20220131
  under (c)2020). The "ER800W" file is the **ERG800W** (the book says so; SKU
  180913 printed) and the ERG800W_R80 service manual joins it. `erg550w-2023`
  and the four dumbbells have no `dbo.MODEL` row.
- Two Dyaco twins across brands, linked not merged: the ERG650W's kit and
  build are the Spirit CRW800 H2O's; the ERG700's console pages are the Spirit
  CRW800 / XRW600 and Sole SR500 pages. Noted on the product cards.
- Only the ERG700 prints error codes (E1 RAM, E2 cable) — the reverse of the
  Xterra bikes' E1/E2, said on the first line of each card.
- Rulings on the cards: ERG600W SM 5 mm gap vs a "25MM" photo callout (5 mm);
  ERG650W race "L1-L5" vs its own 15-level table (15); ERG650W manual-mode
  pulse 30-240 (copied from the ERG600W) vs 90-200 (90-200); ERG180 "lift the
  front" (a bike sentence) vs a drawing lifting the rear (rear); ERG750W
  (870) 335-5500 vs the sticker's 333-5500 (sticker); ERG-750W SM pages
  headed "Model R48" treated as the ERG750W.
- Tank capacity tables are `specs`; one maintenance duplicate deleted.

### 3d. Sole owner's manuals 2006-2025 — 95 PDFs, 25 ingested (A1 merged)

Found 2026-09-12 by hashing every PDF under `/mnt/HDD/Downloads/` against the
manifest and text-comparing the rest against the ingested sources of the same
model. Earlier handoffs said "every Sole manual is done"; only the Sole **bikes**
(B94/R92, LCB/LCR, SB700, SB900, SB1200, all years) and the **2026** books were.
The list is `reference/sole-legacy-owners-manuals-not-ingested.tsv` (path, native
word count) — 93 rows plus 2 the survey caught it missing (`UE25 UE55 E55 2007`
ellipticals, `VF80 VF83 VF85 2008` treadmills). Digest **only** from
`/mnt/HDD/Downloads/Sole Treadmill/Owners Manuals-20260904T175611Z-1-001/Owners Manuals`:
the rest of that download folder (Bikes, 2026, Rowers/Service/SRVO/Treadmills
zip-extracts) is already ingested, confirmed file-by-file against the manifest.

**A1 treadmills native-text era: done** (PR #64, 2026-09-12) — 25 books, 25
sources, 53 new ids, 233 new cards + 16 extensions. Wave file
`reference/sole-treadmills-a1-wave.tsv`; briefs in `/tmp/sole-a1/briefs/`
(not committed — rebuild per wave from `reference/wave-briefs/`). What it
settled: ids from footer revision stamps (`MODEL_YYYYMMDD`) + warranty
effective dates + one full `dbo.MODEL` SOLE dump, never the filename (TT9
"2019" is a 2018 revision; AS77 "2011" stamps 2012-01-23; V-machines are
2007 under 2008 filenames; W-books pair two years under one SKU);
`f60-2013` = 560813, 560812 unassigned; TT8C has no DB row.

**A2 treadmills stencil era: done** (PR #66, 2026-09-12) — 24 books, full
300dpi OCR sweep (27–36 supplemented pages each, 7–11k words a book; run
with system `python3`, `.venv` has no PIL). 3 new ids: `f63-2025`,
`td80-2019`, `tt8-2021` (footer `TT8_2021 Ver.C`); shared-SKU numbers
encoded per the 2026-09-03/08 user decisions (`tt8-2020`, `f85-2020`,
`f85-2021`, `st90-2020`, `st90-2021`). 157 new cards + 141 extensions.
No E01/LS1 in any A2 book. Wave file
`reference/sole-treadmills-a2-wave.tsv`; briefs in `/tmp/sole-a2/briefs/`.

Remaining, in this order: **B** 32 ellipticals (incl. the UE25 extra),
**C** 14 climbers / rowers / SRVO / strength.

They are real new work: the F80 2019 book measures 0.00 against the F80 2026 book
and the 2023 service manual; the E20/E25 2012-2015 book 0.51 against its nearest
neighbour. Several files bundle years and SKUs in one book
(`SOLE E35 E95 2012 2013 2014 2015 Owners Manual (535012, … 595015).pdf`), so one
source will carry several `<model>-<year>` ids — prove each year from the book,
not the filename (see "A filename year is not evidence" in `CLAUDE.md`), and the
Sole ids already declared in `kb.yaml` (169) decide which are new.

Also **not** gaps, checked the same day: the Spirit strength 2025 revisions of
CSD-ACBE, CSD-ITOT, CSD-LELC, CSD-LPCE and CSD-PUDA measure 0.65-0.70 against
their carded 2024 books — genuine revisions, like the CSD-CPSP 2025 update that
was ingested at 0.53, and worth one small wave; every other unmatched Spirit file
is a re-export at 0.95-1.00 (the XBR95 "NewStyle 2024" is the 2023 book at 1.00;
the CSD-BCUR 2025-06-26 file is the CSS-BCUR 2025-06-17 source at 1.00 — the
folder names hold non-breaking spaces, so match them with `glob`, not typed paths).

### 3c. Left over from the model-number work

26 machines have no `model_number` (`tt8c-2011` joined them: SKU 589810 is in
no `dbo.MODEL` row). `reference/model-numbers-open.csv` lists
each with its candidates. Most are one model id facing two SKUs because the
other generation has no cards yet; they will resolve as 3d cards those
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

---

## 8. Where to pick up (written 2026-09-12; A1 and A2 merged the same day)

Spirit (3a) and Xterra (3b) are merged; Sole 3d waves **A1** (25 native-text
treadmills, PR #64) and **A2** (24 stencil treadmills, PR #66) are merged.
**Next is B: the 32 Sole ellipticals** (31 TSV rows plus the UE25 UE55 E55
2007 extra), then **C** (14 climbers / rowers / SRVO / strength), all from
`Sole Treadmill/Owners Manuals-20260904T175611Z-1-001/Owners Manuals` and
listed in `reference/sole-legacy-owners-manuals-not-ingested.tsv` (95 rows).
Reuse the A2 briefs as the template (stencil-image method, render-verified
figures, shared-SKU sibling ids); ellipticals add stride/step-up assembly,
pedal-arm maintenance and the E35/E95 multi-year books. The Sole 2026
error-code family rule holds: never one card across code families. Then the
five Spirit strength 2025 revisions (section 3d, last paragraph). Then 3c,
which needs a person.

Small things a later session could pick up:

- The **FS5.8e** owner's-manual scan is truncated at printed p. 22 (no
  maintenance, warranty or chest-strap pages); a complete copy would add a few
  cards to `fs58e-2013`.
- `sb150-2018` faces two `dbo.MODEL` rows with the same name (115314 / 115316).
- `xe150-2005` stays Spirit though the database brands it XTERRA (section 7).
- The X2 wave's AIR650 rests on the Spirit AB900 service manual by way of a
  two-page note; if a real AIR650 service manual turns up, its cards are the
  ones under `cards/air650-2021/` with `spirit-bike-ab900-2018-service-manual`
  in their locators.

`reference/wave-briefs/` holds the **X2 brief set** (the most general: a brand
with existing cards, extension across product lines, the "rule on
contradictions" section, the filename rule with model *and* section stripped)
and the scripts: `sweep.py` (dictionary rotation scorer), `pages.py`,
`reconcile.py`, `fix_rotation.py`, `model_numbers_pass.py`, `dedupe.py`. Copy
them into the session scratchpad; the briefs name `$S` paths.

**How a wave ran today, in one paragraph.** Branch from `main`. Write a
`wave-*.tsv` (`relative path <TAB> source id <TAB> title <TAB> model ids`),
`kb ingest` each row, prepend the source header comment, run `sweep.py` over
the wave in the background (4 manuals × 4 threads, single-threaded tesseract),
check `grep '^=== OCR SUPPLEMENT' | sort | uniq -d` on every source, declare
the ids in `kb.yaml`, add `reference/model-numbers.csv` rows and the same rows
to `sources/custservice-model-numbers/text.md` (refresh its manifest sha256),
write or rebuild the family product cards (`<family>-model-numbers`, list-valued
`model`, `lookup: model-numbers`), lint, **commit the ingest on its own**. Write
COMMON + eight section briefs, launch eight agents at once with only the brief
paths, wait. Snapshot `cards/` to the scratchpad. Run `reconcile.py`, strip
`model_number` from widened cards and add it to new one-machine cards, look for
the same fact carded by two sections (belt slip, erratic heart rate, tool lists —
merge into the section the repo already uses and re-point references), commit,
update this file, push, `gh pr create --body-file`, wait for the `lint` check,
`gh pr merge --squash --delete-branch`, pull `main`.

**Open questions for a human**, all recorded on the cards and in the PR bodies
#54–#58: which book support should quote where owner's and service manuals
disagree on volts / amps / gauge / GFCI; the CT900 and XS895 warranty terms
(sheet vs manual); the CU800-2012 adapter-vs-generator and JB950 generator-vs-
battery power source; the FTP credentials on `ct900ent-console-ftp-settings-error-log-upload`;
whether the 2019 sheet cards should reach post-2019 ids; the 7.0R "set Unit Type
to upright" and the CSD-CPSP 679 lb / 598 lb placards.
From #64 (A1): the second "F60 2013" SKU 560812 (unassigned — both 560812 and
560813 claim 2013); whether the pre-existing f80/f85/f83-2026 belt-dust and
military-fitness splits should join the A1 sentence now on f80's cards; the
F60-2016 calibration min-speed split (10 = 1.0 vs 5 = 0.5) kept as both readings.


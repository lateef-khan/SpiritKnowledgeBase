# Handoff — where the knowledge base stands and how to continue

**Written:** 2026-09-10, at a clean pause. Nothing is ingested but uncarded.
**Branch to start from:** `main`. Every branch below it is merged and deleted.

Read `CLAUDE.md` before touching `cards/`. Then `.claude/commands/kb-extract.md`.
This file tells you what is done, what is next, and how the work is actually run.

---

## 1. State of `main`

| | |
|---|---|
| cards | **6,294** |
| `kb lint` | 0 problems |
| declared model ids | **285** (169 Spirit, 116 Sole) — every one has at least one card |
| sources ingested | 365 |
| machines carrying `model_number` | **197** of 222 with single-machine cards |

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

Surveyed, clustered, **not ingested**. Byte-identical copies and 95%+ re-exports
are collapsed to 103. `reference/service-manuals-identified.tsv` names the
machine each document belongs to, with the evidence — read its `verdict` column.

It brings machines the repository has never seen: a **1000 series** (CT1000,
CR1000, CU1000, CE1000), **SB600**, **XT175/275/375/475/675** (one manual for
five machines, an older generation than the XT185 family), **CTSB900**,
**CE900ENT**. Each needs a new model id in `kb.yaml`, its year proven from the
document, not the filename.

It also holds documents that are **not machine manuals**: a commercial warranty
sheet, a power-requirements sheet, three `ENT Support` tips (Bluetooth pairing,
internet, screen mirroring — these belong with the ENT console cards), an E27
troubleshooting note for the 7.0T, an AB900/AIR650 discrepancy note, and an
i-Strength maintenance manual.

**Run it as sub-waves by product line**, not as one wave of 103: treadmills 27,
bikes 32, ellipticals 17, rowers 10, climbers/steppers 10, odds 7.

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
machines: ERG160, ERG180, SB600, AIR650. **Take the brand from the document,
never from the folder.**

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

1. **Survey and cluster before ingesting.** Hash every PDF (`sha256`) and check
   `sources/manifest.yaml`; then cluster the rest on **native PDF text** at 95%
   or higher. Different machines share one template at 92-94%, so use a
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

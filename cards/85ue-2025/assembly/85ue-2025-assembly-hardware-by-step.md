---
id: 85ue-2025-assembly-hardware-by-step
title: Five hardware tables an ergometer prints only as pictures, invisible to every
  text extraction of the manual
kind: fact
question: What fasteners does each step of the Spirit 8.5UE (85ue-2025) upper body
  ergometer assembly use, and how many of each?
asked_as:
- what bolts come with the 8.5ue
- how many screws are in the ergometer hardware bag
- what size bolt holds the seat back on the 8.5ue
- i am short a screw for my upper body ergometer
keywords:
- hardware
- fasteners
- bolt size
- screw size
- flat washer
- bolt count
- missing hardware
- hardware table
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: assembly
  code: '*'
  model_number: '785045'
authority: 3
not_to_be_confused_with:
- crw800h2o-assembly-hardware-kit
- crw800-2024-assembly-hardware-kit
see_also:
- 85ue-2025-assembly-procedure
- 85ue-2025-assembly-tools-named-in-steps
- 85ue-2025-assembly-parts-diagram-labels
source:
  ref: spirit-ergometer-85ue-2025-owners-manual
  locator: pp. 14-18, the No./Item/Description/Qty table on each of the five ASSEMBLY
    step pages - read from 300 dpi renders and confirmed at 600 dpi, because
    `pdftotext` returns none of these tables
  extracted_at: '2026-09-10'
---

**Every one of these five tables is a flat image.** `pdftotext` returns the step text
above each table and stops; the table itself comes back as nothing. The step prose names
its own counts, so an unrendered extraction of this manual tells you how many fasteners a
step takes - and **not one fastener size for this machine anywhere**. The rows below were
read at 300 dpi and confirmed at 600 dpi.

## Step one

| No. | Item | Description | Qty |
|---|---|---|---|
| 170 | Screw | 3.5 x 10L | 2 |
| 171 | Screw | M5 x 5L | 6 |
| 172 | Screw | M5 x 10L | 4 |

## Step two

| No. | Item | Description | Qty |
|---|---|---|---|
| 587 | Bolt | 3/8" x 1-3/4" | 2 |
| 588 | Flat washer | 3/8" x Ø25 x 2T | 2 |
| 610 | Nut | 3/8" x 7T | 2 |
| 615 | Bolt | M6 x 12L | 4 |

## Step three

| No. | Item | Description | Qty |
|---|---|---|---|
| 609 | Bolt | M8 x 20L | 4 |

## Step four

| No. | Item | Description | Qty |
|---|---|---|---|
| 605 | Bolt | M8 x P1.25 x 20L | 4 |
| 606 | Bolt | M8 x P1.25 x 60L | 2 |
| 607 | Nut | M8 x 7T | 2 |
| 608 | Flat washer | 8.5 x Ø26 x 2T | 2 |

## Step five

| No. | Item | Description | Qty |
|---|---|---|---|
| 173 | Screw | M5 x 12L | 8 |

## Every table closes against its own step

All five steps call for exactly these counts. **Step four is the one that reads short**:
its text says "Install 2 bolts (605) on the right and left side", which is **two per side
and four in total**, and the table's 4 is the one to count against the bag. **Forty-four
fasteners in all** - twelve, ten, four, ten and eight.

## Step two mixes imperial and metric in one joint

The seat back tube is held by a **3/8" x 1-3/4" bolt** through a **3/8" flat washer** into
a **3/8" nut**, while the support arm pad four rows below takes **M6 x 12L**. The book
never explains the mix and gives no metric equivalent for the 3/8" set. **It is the only
imperial hardware in the build.**

## Two M8 bolts of the same pitch, forty millimetres apart

Item 605 is **M8 x P1.25 x 20L** and item 606 is **M8 x P1.25 x 60L**, both in step four,
and item 609 in step three is **M8 x 20L** with no pitch given. Item 609 and item 605 are
the same length and are listed differently; the manual never says whether they are the
same part.

## No torque figure, and two steps say "firmly" instead

Step four says to tighten both its joints **"firmly"** and no page of the build gives a
torque value.

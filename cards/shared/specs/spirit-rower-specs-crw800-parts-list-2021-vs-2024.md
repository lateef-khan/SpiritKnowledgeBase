---
id: spirit-rower-specs-crw800-parts-list-2021-vs-2024
title: Two rows changed between the 2021 and 2024 printings of the air rower parts
  list - a 0.5T washer became 0.3T and a screw quantity went from 2 to 3
kind: spec
question: Is the parts list in the 2021 Spirit CRW800 rower manual the same as the
  one in the 2024 manual?
asked_as:
- is the crw800 parts list the same in both manuals
- did the crw800 parts change between 2021 and 2024
- which crw800 manual do i order parts from
- what is item 96 on the spirit rower
keywords:
- parts list
- item 96
- item 132
- flat washer
- sheet metal screw
- quantity
- revision
- '2021'
- '2024'
- washer thickness
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2021
  - crw800-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800-specs-parts-list-2021-vs-2023
- crw800h2o-outlines-part-names
see_also:
- crw800-2024-specs-parts-list
- spirit-rower-specs-which-manuals-print-a-parts-list
- crw800-2024-specs-resistance-system
source:
  ref: spirit-rower-crw800-2021-owners-manual
  locator: CRW800-2021 parts list printed pp. 41-42 (PDF pp. 43-44) against CRW800-2024
    parts list printed pp. 36-37 (PDF pp. 38-39). Both lists have a clean native text
    layer and both were extracted with `pdftotext -layout` from the PDFs themselves,
    not from the ingested text
  extracted_at: '2026-09-10'
---

**The two lists are the same list.** Compared row by row, **118 of the part names
are shared - 98.3%** - the item numbers run 1 to 139 with the same gaps in both,
and no quantity differs except one. **Two rows changed and nothing else did.**

| Item | CRW800-2021 | CRW800-2024 |
|---|---|---|
| **96** | `Ø20 × Ø30 × **0.5T**_Flat Washer`, qty 1 | `Ø20 × Ø30 × **0.3T**_Flat Washer`, qty 1 |
| **132**, second printing | `3 × 10L_Sheet Metal Screw`, qty **2** | `3 × 10L_Sheet Metal Screw`, qty **3** |

**Item 96 is a real part change, not a typo of the kind the rest of the list is
full of.** `0.5T` and `0.3T` are two thicknesses of the same 20 mm bore washer.
**Order the one printed in the book for the machine in front of you**, and if the
serial year is not known, ask Spirit Fitness rather than guessing.

## Item 132 is printed twice in both books, with a different quantity each time

Both printings carry item 132 **twice**: once out of numerical order on the first
parts page as `3 × 10m/m_Sheet Metal Screw`, quantity 1, and again in its proper
place on the second page as `3 × 10L_Sheet Metal Screw`. The second row is
quantity **2** in 2021 and quantity **3** in 2024.

**Neither book says which of its own two rows is right.** Items 94 and 95 are the
same `3 × 10L_Sheet Metal Screw` at quantities 4 and 1. **Ask Spirit Fitness
before quoting a quantity for item 132 in either year.** See
`crw800-2024-specs-parts-list`, which reproduces the full 2024 table.

## What is identical

Everything else: the fan, flywheel, drive belt and flywheel pulley, the
`Generator/Brake Controller` and `Gear Motor`, the six-part `Controller Assembly`
with its `RF Module` and battery, the seven-part `Console Assembly`, the
`008L`/`008R` attaching plates with their leading zeros, and every fastener size.
**The machine did not change between the two books; the manual around it did.**
See `crw800-2024-specs-resistance-system`.

## The heading changed and the drawing code stayed

The 2021 list is headed **`CW800B-YR003-01 Part List_SPIRIT`** and closes with a
bare **`200428`** drawing date code under the last row. The 2024 list is headed
plainly **`PARTS LIST`** with no code and no trailing number - but its
exploded-view page still carries the string `CW800B` in its text layer. **`CW800B`
is the factory's drawing code for this machine across both printings.** It is not
a model number and not a part number; do not quote it to a customer as either.

---
id: spirit-climber-specs-no-specification-table
title: No specification table in eleven stepper, stair climber and vertical climber
  owner's manuals, and the figures printed instead
kind: fact
question: Where are the dimensions, machine weight, shipping weight, flywheel weight
  and step height for a Spirit stepper, stair climber or vertical climber?
asked_as:
- how much does the spirit stepper weigh
- how big is the recumbent stepper
- what is the step height on the stair climber
- how heavy is the flywheel on this stepper
keywords:
- specifications
- spec sheet
- assembled dimensions
- footprint
- machine weight
- shipping weight
- carton size
- flywheel weight
- step height
- stride
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - crs800s-2024
  - cs800-2021
  - cs800-2024
  - csc880-2025
  - csc900-2019
  - csc900-2021
  - csc900-2024
  - cvc800
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-crw800-specs-no-specification-table
- spirit-ce-specs-no-specification-table
- spirit-bike-specs-no-specification-table
- spirit-ct800-specs-no-specification-table
- spirit-climber-specs-rehabilitation-stepper-specification-page
see_also:
- spirit-climber-2024-specs-resistance-system
- spirit-climber-specs-which-manuals-print-a-parts-list
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
- crs800s-2024-specs-parts-list
- cs800-2024-specs-parts-list
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: Table of Contents printed p. 1 and whole document; the same absence was
    re-checked in the CRS800S-2024 and CSC900-2024 owner's manuals, and then in eight
    more - XS895-2018, XS895-2021, CSC900-2019, CSC900-2021, CRS800S-2021, CS800-2021,
    CVC800-2021 and CSC880-2025 - each at its own Table of Contents and throughout,
    including every OCR supplement in the ingested text
  extracted_at: '2026-09-10'
---

**Eleven Spirit stepper, stair climber and vertical climber owner's manuals
contain no specification table.** No table of contents in any of them has a
Specifications entry, and none of these figures is printed anywhere in any of
them:

- **assembled dimensions** - no length, width or height, in any unit
- **machine weight**, shipping weight, gross weight or carton size
- **flywheel weight or diameter**, and no gear ratio
- **step height, step travel, stride length or seat travel**
- a **resistance range in watts, newtons or kilograms**. Resistance is given only
  as a count of console levels, and two of the eleven do not even print that
- a **certifications list**

Get these figures from Spirit Fitness or the product spec sheet, and say the
owner's manual does not state them. **Do not carry a figure across from one of
the eleven to another, and never in from a Sole machine.**

| Machine | Pages | Book ends at |
|---|---|---|
| XS895-2018 incline stepper | 40 | Warranty printed p. 36, then two blank pages and a back cover |
| XS895-2021 incline stepper | 40 | the same |
| CSC900-2019 StairClimber | 36 | Warranty printed p. 30 |
| CSC900-2021 StairClimber | 40 | Warranty printed p. 34 |
| CRS800S-2021 recumbent stepper | 48 | Parts List printed pp. 41-43 |
| CS800-2021 stepper | 48 | Parts List printed pp. 41-42 |
| CVC800-2021 Vertical Climber | 36 | Parts List printed pp. 31-32 |
| CSC880-2025 stair climber | 44 | Exploded View printed p. 35, Warranty p. 38 |
| CRS800S-2024, CS800-2024, CSC900-2024 | 44-48 | see the row above and the note below |

## The five rehabilitation steppers are the exception

**The MS300, 7.0S, 7.5S, 8.5S and 8.5S-FIT rehabilitation recumbent steppers do
print a specification page**, with dimensions, a product weight, a workload range
in watts and (on four of the five) a medical certification list. See
`spirit-climber-specs-rehabilitation-stepper-specification-page`. Nothing on that
page may be carried across to any machine on the table above - the rehabilitation
steppers are a different platform built to IEC 60601-1.

## The check was run against the OCR as well as the text layer

A missing specification table is exactly the claim a flat-image page fakes, so
this absence was not taken from the `pdftotext` layer alone. Every page of all
eleven books had already been rendered at 300 dpi and read with
`tesseract --psm 4`, and whatever the render knew that the text layer did not was
appended to each source's `text.md`. The tail pages of the four books that end at
the warranty - both XS895 printings and both CSC900 printings - were rendered
again page by page and compared word for word against the extraction. **On the
XS895-2018 the native and rendered word counts agree to within two words on every
page from printed p. 34 to the back cover, and PDF pages 38 and 39 are genuinely
blank**, not imaged.

The words *specification*, *dimension*, *shipping* and *carton* occur in the
combined native-plus-OCR text only in warranty boilerplate ("Product features or
specifications ... subject to change", "the original factory shipping date"), in
the operating-temperature safety line, in "remove all parts from the carton", in
the hardware-package instruction ("the hardware is labeled with its
specification"), and - in the CSC900 and CSC880 only - in the sentence that calls
the clearance minimums "recommended minimum distances".

**There is no specification table in any of the eleven. Do not re-run this
check.**

## What these books do print, and where each fact lives

| Figure | What is printed | Section |
|---|---|---|
| Resistance levels | **20** on the XS895, CRS800S, CS800 and CSC900 of every year - but the CSC900's twenty mean the opposite of the others, see `spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top`. **The CVC800 and the CSC880 print no level count at all** - see `spirit-climber-specs-no-level-count-printed` | specs |
| Brake and resistance unit | named only where there is a parts list - a gear motor, magnet and flywheel on the CRS800S, CS800 and CVC800 of both generations; the stair climbers name a **generator brake** or **Brake** in their warranty tables and a 24 V power-failure brake in troubleshooting - see `spirit-climber-2024-specs-resistance-system` | specs |
| Exploded view and parts list | printed by six of the eleven and by none of the stair climbers except as an unlabelled drawing - see `spirit-climber-specs-which-manuals-print-a-parts-list` | specs |
| User weight limit | **450 lb** on the CRS800S and CS800 of both generations; **400 lb** on the XS895 and the CVC800; **400 lb (180 kg)** on the CSC900 of every year; **330 lb** on the CSC880-2025 - four different figures, so read the customer's own book | safety |
| Operating temperature / humidity | 40 to 120 degrees F, 95% non-condensing | safety |
| Power supply | a 110-volt, 15-amp grounded outlet with a dedicated 5-amp circuit breaker on most; the CSC900 books state no circuit requirement at all | safety |
| Minimum clearance | **the stair climbers only** - 20 in (0.5 m) each side and 48 in (1.25 m) behind | safety |

**The stair climbers are the odd ones.** Across 2019, 2021, 2024 and the CSC880
of 2025 their weight limit is the lowest in the family, theirs are the only books
with a clearance dimension, the only ones with no stated circuit rating, and the
only ones with no usable parts list. **The CSC880-2025 drops the limit again, to
330 lb** - 120 lb below the CS800's. Read a stair climber from its own book.

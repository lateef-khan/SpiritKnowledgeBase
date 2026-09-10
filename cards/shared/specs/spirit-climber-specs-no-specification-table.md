---
id: spirit-climber-specs-no-specification-table
title: No specification table in the three commercial stepper and stair climber owner's
  manuals, and the figures printed instead
kind: fact
question: Where are the dimensions, machine weight, shipping weight, flywheel weight
  and step height for a Spirit commercial stepper or stair climber?
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
  - crs800s-2024
  - cs800-2024
  - csc900-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-crw800-specs-no-specification-table
- spirit-ce-specs-no-specification-table
- spirit-bike-specs-no-specification-table
- spirit-ct800-specs-no-specification-table
see_also:
- spirit-climber-2024-specs-resistance-system
- spirit-climber-specs-which-manuals-print-a-parts-list
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
- crs800s-2024-specs-parts-list
- cs800-2024-specs-parts-list
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: Table of Contents printed p. 1 and whole document; the same absence was
    checked in the CRS800S-2024 and CSC900-2024 owner's manuals, each at its own Table
    of Contents and throughout, including every OCR supplement in the ingested text
  extracted_at: '2026-09-10'
---

**None of the three Spirit commercial stepper and stair climber owner's manuals
contains a specification table.** All three were checked - the CRS800S recumbent
stepper, the CS800 stepper and the CSC900 stair climber, all three warranted in
September 2024. No table of contents has a Specifications entry, the word
*dimension* appears in only one of them and not as a machine measurement, and
none of these figures is printed anywhere in any of them:

- **assembled dimensions** - no length, width or height, in any unit
- **machine weight**, shipping weight, gross weight or carton size
- **flywheel weight or diameter**, and no gear ratio
- **step height, step travel, stride length or seat travel**
- a **resistance range in watts, newtons or kilograms**. Resistance is given only
  as a count of console levels
- a **certifications list**

Get these figures from Spirit Fitness or the product spec sheet, and say the
owner's manual does not state them. **Do not carry a figure across from one of
the three to another, and never in from a Sole machine.**

## The check was run against the OCR as well as the text layer

A missing specification table is exactly the claim a flat-image page fakes, so
this absence was not taken from the `pdftotext` layer alone. Every page of all
three books had already been rendered at 300 dpi and read with
`tesseract --psm 4`, and whatever the render knew that the text layer did not was
appended to each source's `text.md`. **The words *specification*, *dimension*,
*shipping* and *carton* occur in the combined native-plus-OCR text only** in
warranty boilerplate ("Product features or specifications ... subject to
change"), in the operating-temperature safety line, in "remove all parts from the
carton", and - in the CSC900 only - in the sentence that calls the clearance
minimums "recommended minimum distances".

A search for weight-shaped and dimension-shaped figures returns only the user
weight limit, the `kg-m/min` unit in the fitness-test tables, a 65 kg default
body weight in the console set-up, and fastener sizes from the parts lists.
**There is no specification table. Do not re-run this check.**

## What the three books do print, and where each fact lives

| Figure | What is printed | Section |
|---|---|---|
| Resistance levels | **20** in all three - but the CSC900's twenty mean the opposite of the other two, see `spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top` | specs |
| Brake and resistance unit | named only where there is a parts list - a gear motor, magnet and flywheel on the CRS800S and CS800; the CSC900 names a **generator brake** in its warranty table and a 24 V brake in its troubleshooting page - see `spirit-climber-2024-specs-resistance-system` | specs |
| Exploded view and parts list | **CRS800S and CS800 only; the CSC900 prints neither** - see `spirit-climber-specs-which-manuals-print-a-parts-list` | specs |
| User weight limit | **450 lb** on the CRS800S and CS800; **400 lb (180 kg)** on the CSC900 | safety |
| Operating temperature / humidity | 40 to 120 °F, 95% non-condensing, in all three | safety |
| Power supply | 110-volt, 15-amp grounded outlet with a dedicated 5-amp circuit breaker, on the CRS800S and CS800; the CSC900 book states no voltage or amperage at all | safety |
| Minimum clearance | **CSC900 only** - 20 in (0.5 m) each side and 48 in (1.25 m) behind | safety |

**The CSC900 is the odd one of the three on four of those seven rows.** Its
weight limit is 50 lb lower, its manual is the only one with a clearance
dimension, the only one with no stated circuit rating, and the only one with no
parts list. Read it from its own book.

---
id: spirit-crw800-specs-no-specification-table
title: Not one of the six rower owner's manuals or four rower service manuals prints a
  specification table, and none of them states a dimension in any unit
kind: fact
question: Where are the dimensions, machine weight, shipping weight, flywheel weight
  and rail length for a Spirit rower?
asked_as:
- how much does the spirit rower weigh
- how long is the spirit rowing machine
- how heavy is the flywheel on the rower
- what is the shipping weight of the rower
keywords:
- specifications
- spec sheet
- assembled dimensions
- footprint
- machine weight
- shipping weight
- flywheel weight
- rail length
- damper
- carton size
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  - crw800h2o
  - crw900-2021
  - xrw600-2019
  - xrw600-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-no-specification-table
- spirit-bike-specs-no-specification-table
- 85ue-2025-specs-specification-page
- spirit-climber-specs-rehabilitation-stepper-specification-page
see_also:
- crw800-2024-specs-resistance-system
- crw800-2024-specs-level-range-1-to-16
- crw800-2024-specs-parts-list
- spirit-rower-specs-which-manuals-print-a-parts-list
- crw900-2021-specs-ten-level-tank-adjuster
- crw800h2o-specs-six-water-fill-levels
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: "Table of Contents printed p. 1 and whole document, including every OCR supplement in the
    ingested text; console ranges printed p. 14 (PDF p. 16). The same check was run over the
    whole of the CRW800-2021, CRW900-2021, CRW800H2O-2021, XRW600-2019 and XRW600-2021
    manuals, native text layer and OCR supplement together. Service manuals: the CRW800
    (2020) book 800940, CW800-YR001 (CRW800-2016), DW400-YR002 (XRW600-2019) and the CRW900
    book, whole documents with their OCR supplements; loose-word greps for specif,
    dimension, weight, kg and lb, of which the only hits are belt-tension pounds and a
    warranty sentence"
  extracted_at: '2026-09-10'
---

**Not one of the six Spirit rower owner's manuals contains a specification
table.** No table of contents in the six has a Specifications entry, and **the
word *specification* appears in each book exactly once or twice, always inside the
warranty boilerplate** - *"Product features or specifications as described or
illustrated are subject to change without notice."*

**The word *dimension* appears in none of the six, in any form, in any unit.**

| Manual | Specification page | Any dimension | What it does print |
|---|---|---|---|
| CRW800-2021 air rower | **none** | **none** | console window ranges, printed p. 14 |
| CRW800-2024 air rower | **none** | **none** | console window ranges, printed p. 14 |
| XRW600-2019 rower | **none** | **none** | console window ranges, printed pp. 15-16 |
| XRW600-2021 rower | **none** | **none** | console window ranges, printed pp. 15-16 |
| CRW900-2021 water rower | **none** | **none** | a **20 litre** tank capacity, printed p. 33 |
| CRW800H2O-2021 water rower | **none** | **none** | a six-step water level gauge, printed p. 18 |

**The CRW900's 20 litres is the only capacity figure in any of the six**, and it
is a fill limit printed inside the tank-filling procedure, not a specification -
see `crw900-2021-specs-ten-level-tank-adjuster`. The CRW800H2O prints no tank
capacity at all, and **its tank volume must not be inferred from the CRW900's.**

The rest of this card is written from the CRW800-2024 book, whose absences are the
same as the other five.

## What the CRW800 book in particular does not print

Its table of contents has no Specifications entry, and none of these figures is
printed anywhere in the book:

- **assembled dimensions** - no length, width or height, in any unit, and no
  folded dimension even though the machine has a Folding End Assembly (item 6 in
  the parts list)
- **machine weight**, shipping weight, gross weight or carton size
- **flywheel weight or diameter**, fan diameter, or a gear ratio
- **rail length, seat height or the maximum user height**
- a **damper setting or drag factor** of any kind
- a **resistance range in watts, newtons or kilograms** - the Watts window
  reports the work the rower is doing, not the setting
- a **certifications list**

Get these figures from Spirit Fitness or the product spec sheet, and say the
owner's manual does not state them.

**The six machines are three different families and share no figures.** The
CRW800 and XRW600 are console-braked air rowers, the CRW900 and CRW800H2O are
water rowers with different tanks, and no dimension of one is a dimension of
another. This card says only that **none of the six books prints any of them.**

## One Spirit machine in this corpus does print a specification page

The **8.5UE upper body ergometer** prints a full one, over two pages - dimensions,
product weight, power supply, fuse rating, workload, resistance, manufacturer and
a certifications block. See `85ue-2025-specs-specification-page`. **It is an
ergometer, not a rower**, and none of its figures belongs to any machine on this
card. The five Spirit rehabilitation recumbent steppers print a page of the same
shape - `spirit-climber-specs-rehabilitation-stepper-specification-page`.

## The check was run against the OCR as well as the text layer

Every page of this PDF had already been rendered at 300 dpi and read with
`tesseract --psm 4`, and whatever the render knew that the text layer did not was
appended to the source's `text.md`. In the combined native-plus-OCR text the
words *specification*, *dimension*, *shipping* and *carton* appear only in
warranty boilerplate, in the operating-temperature safety line and in "remove all
parts from the carton". A search for weight-shaped and dimension-shaped figures
returns only the 450 lb user weight limit and fastener sizes from the parts list.
**There is no specification table. Do not re-run this check.**

## What the book prints instead

The nearest thing to a specification page is the **console window-function list
on printed p. 14**, which gives the range of each readout rather than any
property of the machine:

| Window | Range printed |
|---|---|
| Level | **1~16** - the resistance setting, see `crw800-2024-specs-level-range-1-to-16` |
| Calories | 0~999 |
| Watts | 0~2000, shown as 1.00 for 1000 and up |
| Time | 00:00~99:59 minutes and seconds |
| Distance | 0~9999, switching to 1X.XX above 9999 |
| Heart rate | 40~220 bpm |

**Only the Level range is a machine fact.** The other five are what the display
can show, and they belong to the `console` section; do not read them as
capacities of the rower.

## Where the other figures the book does print live

| Figure | What is printed | Section |
|---|---|---|
| User weight limit | 450 lb | safety |
| Operating temperature / humidity | 40 to 120 °F, 95% non-condensing | safety |
| Console power | two C cells, not included | specs - see `crw800-2024-specs-resistance-system` |
| Mains input | `AC100 ~ 240V`, stated only inside a troubleshooting step | specs - see `crw800-2024-specs-resistance-system` |
| Exploded view and parts list | printed pp. 35-37 | specs - see `crw800-2024-specs-parts-list` |

**The mains figure is the one to be careful with.** `AC100 ~ 240V` is printed
only as a thing to measure when the console is dim, not as a supply
specification, and the electrical safety page of this book states no voltage and
no circuit rating at all - unlike the CS800 and CRS800S books, which ask for a
110-volt, 15-amp outlet with a dedicated 5-amp breaker.

## The service manuals do not print one either

The four rower service manuals in the repository - the CRW800 (2020) book, the CW800-YR001 book
for the `crw800-2016`, the DW400-YR002 book for the `xrw600-2019` and the CRW900 book - contain
**no specification table, no dimension in any unit and no machine weight**. The word *weight*
does not occur in any of them; *lb* occurs only as the drive-belt tension ("70~80BLS") in the
two CRW800 books and the XRW600 book. What they add instead is electrical: motor working
voltages, a generator controller, an adapter rating and pin definitions - see
`crw800-2021-specs-electrical-configuration-tension-motor-dc-4-0-to-6-0-v`,
`spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack` and
`crw900-2021-specs-service-manual-prints-no-wiring-diagram-outline-or-block-diagram`.

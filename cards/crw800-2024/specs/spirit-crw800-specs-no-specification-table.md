---
id: spirit-crw800-specs-no-specification-table
title: No specification table in the commercial rower's owner's manual, and the console
  ranges printed instead
kind: fact
question: Where are the dimensions, machine weight, shipping weight, flywheel weight
  and rail length for a Spirit crw800-2024 commercial rower?
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
  model: crw800-2024
  applies_to:
  - crw800-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-no-specification-table
- spirit-bike-specs-no-specification-table
- crw800h2o-outlines-part-names
see_also:
- crw800-2024-specs-resistance-system
- crw800-2024-specs-level-range-1-to-16
- crw800-2024-specs-parts-list
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: Table of Contents printed p. 1 and whole document, including every OCR supplement
    in the ingested text; console ranges printed p. 14 (PDF p. 16)
  extracted_at: '2026-09-10'
---

**The CRW800 owner's manual contains no specification table.** Its table of
contents has no Specifications entry, and none of these figures is printed
anywhere in the book:

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

**This is not the water rower.** The repository also holds `crw800h2o`, a Spirit
**water** rower with a different mechanism, a different parts drawing and no
resistance levels at all. `crw800h2o-outlines-part-names` is not an answer for
this machine, and nothing from that card should be carried across.

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

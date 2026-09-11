---
id: spirit-climber-specs-parts-electronic-parts-named
title: 'The named electronic parts: display and cooling fan above; tension motor and
  speed sensor below, plus an incline motor on the incline stepper'
kind: fact
question: Which electronic parts do the Spirit stepper service manuals (CRS800S, CS800,
  XS895 and the 7.5S medical stepper) name, and where are they?
asked_as:
- what electronic parts are in the cs800 stepper
- where is the speed sensor on the crs800s
- tension motor location on the xs895
- which boards does the 7.5s stepper have
keywords:
- electronic parts
- upper controller
- lower controller
- part names
- service manual
- display
- cooling fan
- tension motor
- speed sensor
- incline motor
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-5s-med
  - crs800s-2021
  - cs800-2016
  - cs800-2021
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-specs-parts-electronic-parts-named
- cu1000ent-2023-specs-parts-electronic-parts-named
see_also:
- spirit-treadmill-specs-parts-service-manual-tool-list-is-one-multimeter
- 7-5s-med-specs-parts-list
- spirit-ce850-specs-parts-electronic-parts-named
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: 'CS800 (2020): 2-1 Upper Controllers PDF p. 8 (printed 7), text.md lines
    138-149; 2-2 Lower Controller and Driver PDF p. 9 (printed 8), lines 149-162.
    XS200-SS003 (spirit-stepper-cs800-2016-service-manual): 2-1 PDF p. 8, lines 133-147;
    2-1 [sic] Lower Controller and Driver PDF p. 9, lines 147-163. CRS800S 2020 ver.
    (spirit-stepper-crs800s-2021-service-manual): Upper Controllers PDF p. 6, lines
    73-83; Lower Controller and Driver PDF p. 7, lines 83-94. XS300B-YS006 (spirit-stepper-xs895-2021-service-manual):
    2-1 PDF p. 6 (printed 5), lines 81-90; 2-2 PDF p. 7 (printed 6), lines 90-108.
    7.5S RS9600-SS021-01 (spirit-stepper-7-5s-med-service-manual): Electronic Parts,
    PDF pp. 5-6, flat images read from a 300 dpi render (OCR supplements at text.md
    lines 909-935)'
  extracted_at: '2026-09-11'
---

**Five stepper service manuals, the same two photographs, and between three and five labels.**
Each book's chapter 2 shows the console with its callouts, then the machine with its shroud
off and the lower parts called out. No part number, rating or wire colour is printed on
either page in any of the five; those are on the specs cards for chapters 3 and 6.

| Book | Upper Controllers names | Lower Controller and Driver names |
|---|---|---|
| CS800 2016 (XS200-SS003) | Cooling FAN, DISPLAY | TENSION MOTOR, SPEED SENSOR |
| CS800 (2020) | Console, Cooling Fan | Tension Motor, Speed Sensor |
| CRS800S 2020 ver. | Display | Tension Motor, Speed Sensor |
| XS895 (XS300B-YS006) | Display | Tension Motor, **Incline motor**, Speed Sensor |
| 7.5S (RS9600-SS021-01) | Cooling FAN, DISPLAY | TENSION MOTOR, **Optical SENSOR** (two boards) |

**The XS895 is the only one that names an incline motor**, because it is the only incline
stepper; its Electrical Configurations page describes it as an AC motor with four wires and a
three-pin position-sensor cable. The other four have no incline drive at all.

**The 7.5S calls its sensor an optical sensor and photographs two boards for it.** The labels on
the boards in the photograph read CS63008-00 (two reflective heads) and CS63008-10 (one head),
and the parts list confirms them as items 221 and 222 (`7-5s-med-specs-parts-list`). The
CS800 and CRS800S books call the equivalent part a speed sensor and print no board number.

**The 2016 CS800 book mis-numbers its second heading** - both pages are headed 2-1, "Upper
Controllers" and then "Lower Controller and Driver". It is the same two-page chapter as the
2020 book's 2-1 and 2-2.

**The CRS800S book labels the console photograph only `Display`** and names no fan, though
the same book's console page shows a fan switch; the CS800 books name the cooling fan on
the console. Quote the book in hand rather than carrying the fan label across.

The CE850 ellipticals name a thumb switch and a motor controller these steppers do not
(`spirit-ce850-specs-parts-electronic-parts-named`); the CU1000ENT and CR1000ENT bikes name an
NFC reader, a driver board and a hybrid generator (`cu1000ent-2023-specs-parts-electronic-parts-named`).


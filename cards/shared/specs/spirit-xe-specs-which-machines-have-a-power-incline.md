---
id: spirit-xe-specs-which-machines-have-a-power-incline
title: Whether the machine has a powered incline ramp at all
kind: spec
question: Which Spirit residential XE and XG home ellipticals have a powered incline
  ramp, and which have none?
asked_as:
- does my spirit elliptical go uphill
- is there an incline on this elliptical
- why has my elliptical got no incline buttons
- can you raise the ramp on this machine
keywords:
- incline
- power incline
- ramp
- elevation
- incline motor
- incline rail
- uphill
- fixed ramp
- no incline
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe100-2007
  - xe150-2005
  - xe195-2016
  - xe195-2019
  - xe195-2021
  - xe200-2007
  - xe295-2016
  - xe295-2019
  - xe295-2021
  - xe300-2007
  - xe350-2005
  - xe395-2010
  - xe395-2016
  - xe395-2018
  - xe395-2023
  - xe395ent-2021
  - xe400-2007
  - xe500-2007
  - xe550-2005
  - xe795-2016
  - xe795-2018
  - xe795-2021
  - xe795-2023
  - xe895-2016
  - xe895-2018
  - xg400-2016
  - xg400-2019
  - xg400-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xe395-2010-specs-incline-forty-levels-in-half-steps
see_also:
- spirit-xe-specs-no-specification-table
- xe895-2018-specs-powered-stride-set-per-segment-with-no-length-printed
- spirit-ce850-specs-stride-length-18-to-24-inches
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
- spirit-xe400-xe500-2007-specs-wiring-schematic
- spirit-xe-2007-specs-electrical-configuration-adapter-or-mains-incline-transformer
- spirit-xe-2016-specs-unit-block-diagram-no-driver-board
- xe395-2016-specs-outline-part-names
source:
  ref: spirit-elliptical-xe395-2010-owners-manual
  locator: 'p. 15, Console, POWER INCLINE; the absence was re-checked across the
    other thirteen manuals, in twelve of which the word incline does not occur at
    all. The thirteenth, the XE895-2018, uses it once in its text, on p. 12 in an
    assembly wiring label, and once more in the console drawing on p. 17, and has
    no incline control anywhere. Service manuals: XE395-2016 section 3 PDF p. 12
    (text.md lines 219-241) and outline PDF p. 6 (106-143); XE395ENT-2021 PDF p. 9
    (70-105); XE100-XE500 2007 dealer manual troubleshooting PDF p. 3 (51-98), PROCEDURE
    6 PDF p. 7 (202-243) and the XE400/XE500 schematic PDF p. 9 (294-300); the XE195,
    XE295, XG400, XE795-2016 and XE795-2023 books name no incline part in their
    section 3, block diagram or circuit diagram, and the XE895-2016 book names a stride
    motor there instead'
  extracted_at: '2026-09-09'
---

**Among the owner's manuals, only the four XE395 machines have a powered incline
ramp; the service manuals add a fifth XE395 printing and the 2007 XE400 and XE500.**
The XE395-2010, the XE395-2018, the XE395ENT-2021 and the XE395-2023 each have an incline rail
assembly and an incline motor in their assembly steps, incline keys on the console,
and an incline reading on the display. The three books that print a parts list also
list an incline controller; the XE395-2018 prints no parts list at all.

The XE395-2010 manual states it outright: "The XE395 has a motorized incline ramp
feature that allows you to simulate walking uphill." The XE395-2018 drops that
sentence but keeps the incline rail assembly and the incline motor wiring in its
assembly steps, an Incline down key in the final assembly step, an incline-banded
Muscle Activation Figure, incline profiles in every preset program, an Incline
on/off and Max Incline step in program setup, and an Incline Calibration routine.

**Twelve of the other thirteen manuals never use the word incline once.** No
incline key, no incline rail in the assembly, no incline motor in any parts list,
and no incline readout described on any console:

| Machine | Powered incline |
|---|---|
| XE395-2010, XE395-2018, XE395ENT-2021, XE395-2023 | yes |
| XE795, the 2018 printing, both 2021 printings and the 2023 | no - the word does not appear |
| XE195-2021, XE295-2021, XE195-2019, XE295-2019 | no - the word does not appear |
| XG400-2021 and XG400-2019 E-Glide Trainer | no - the word does not appear |
| XE100-2007, XE200-2007, XE300-2007 | no - the word does not appear |
| XE150-2005, XE350-2005, XE550-2005 | no - the word does not appear |
| **XE895-2018** | **no - but the word survives in two leftovers, see below** |

## The XE895-2018 keeps two *incline* leftovers, and has no incline

The XE895-2018 book is an edit of the XE395 book and two places were not changed
over:

- **p. 12, assembly.** The handlebar wiring step prints "RESISTANCE/ INCLINE
  (White/Red)"; the same wire is labelled "RESISTANCE/STRIDE" on p. 14. This is
  native text in the PDF, not an OCR artefact.
- **p. 17, the console drawing.** The readout window beside LEVEL is labelled
  **INCLINE**. The picture is the XE395's console artwork reused unchanged - the
  XE395-2018 book prints the same drawing on its own p. 18, down to the same key
  row - and the page was rendered at 300 dpi and read to confirm the label.

**The XE895 has no incline.** It has no incline key, no incline rail, no incline
profile in any program, no Incline on/off step in program setup and no Incline
Calibration; what it has in each of those places is a **stride**. Do not read
either leftover as an incline feature.

**Only the XE395-2010 book gives an incline range.** It is 40 levels in half-level
steps - see `xe395-2010-specs-incline-forty-levels-in-half-steps`. Neither the
XE395ENT-2021 nor the XE395-2023 states how far its ramp travels, in levels,
degrees or percent, and their consoles are not the XE395-2010's. **Do not quote the
2010 figure for either of them.**

The XE395ENT-2021 comes closest and still gives no absolute figure: its program
descriptions say things like "the incline alternates between 25 & 65 % of maximum
elevation", which is a share of a maximum the manual never states.

## What the service manuals add

- **XE395-2016** - its service manual's Electrical Configuration names an **INCLINE
  MOTOR, 120 volt AC**, its outline drawing labels an *Incline Motor*, an *Inclinable
  Rail Cover* and an *Incline Cover*, and its Function page prints the 0-20 half-step
  scale - a powered incline, stated outright
  (`spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor`,
  `xe395-2016-specs-outline-part-names`).
- **XE395ENT-2021** - the service manual names the same motor at 115 volt AC; the
  owner's manual's "% of maximum elevation" is the only range either book gives.
- **XE400-2007 and XE500-2007** - the 2007 dealer manual, which covers five machines,
  says in its troubleshooting table and Procedure 6 that these two have an incline
  motor, an incline controller (ALT-670100A) and an incline transformer, and draws
  them on the only schematic in the book; the XE100, XE200 and XE300 of the same book
  have none (`spirit-xe400-xe500-2007-specs-wiring-schematic`,
  `spirit-xe-2007-specs-electrical-configuration-adapter-or-mains-incline-transformer`).
- **XE195-2016, XE295-2016, XG400-2016** - no incline: their service manuals name a
  console and a tension motor only, draw no driver board and no actuator
  (`spirit-xe-2016-specs-unit-block-diagram-no-driver-board`).
- **XE795-2016 and XE795-2023** - no incline: a generator, a controller and a brake.
- **XE895-2016** - no incline: the book is the CE850-2016 book reissued and names a
  **stride** motor; its outline drawing does label the actuator *Incline Motor*, the
  same leftover the 2018 owner's manual carries.

**A raised ramp is not an adjustable stride, and one machine here has the stride
instead.** The XE895-2018 has a powered stride adjustment and no incline; the four
XE395s have a powered incline and no stride; the other twelve manuals have neither.
See `xe895-2018-specs-powered-stride-set-per-segment-with-no-length-printed`.

**The XE895 manual states no stride length.** The Spirit commercial CE850 is the
only Spirit elliptical whose manual prints one - 18 to 24 inches - and that card is
not an answer for a home machine.

---
id: spirit-xbr95-2016-cu800-2012-specs-unit-block-diagram
title: Bike Configuration block diagram with a driver board between the display and
  the generator, the RPM sensor into the display board, and speakers only on the recumbent
kind: spec
question: What does the unit block diagram of a Spirit XBR95 2016 recumbent or CU800
  2012 upright bike show?
asked_as:
- block diagram of the xbr95 2016
- cu800 2012 block diagram
- where does the rpm sensor go on the xr829
- xu878 configuration diagram
keywords:
- block diagram
- bike configuration
- display board
- driver board
- generator
- generator brake
- rpm sensor
- cooling fan
- amplifier
- speaker l/r
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cu800-2012
  - xbr95-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-unit-block-diagram
- spirit-cr900-cu900-2018-specs-unit-block-diagram
see_also:
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
- spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: 'XBR95-2016: section 5 ''Bike Configuration'', PDF p. 24, text.md lines
    379-384, flattened image read from a 300 dpi render (OCR supplement lines 1350-1354).
    CU800-2012 (XU878-AB04M): PDF p. 22, lines 373-378 (OCR lines 923-938, upside
    down)'
  extracted_at: '2026-09-11'
---

Read from the renders. The two drawings differ only in the audio blocks.

**Both:** HR HANDLEBAR, KEY and WIRELESS HR RECEIVER into the **DISPLAY BOARD**; **COOLING FAN**
out of it; the **RPM SENOR** (spelt so) **into the display board**; display board and **DRIVER
BOARD** both ways; **GENERATOR** into the driver board; **GENERATOR BRAKE** out of it.

**XBR95 only:** the display board feeds an **AMPLIFIER**, which drives **SPEAKER L/R** and takes a
**LINE IN**.

**The RPM sensor goes to the console on these two, not to the lower board** - the display board
has an *RPM IN* socket (J3) and the circuit diagram runs the sensor lead up the console cable. On
the 2018 CR900/CU900 and the 2023 XBR95 the sensor lands on the driver board instead.

No mains or adapter block is drawn on either.


---
id: spirit-med-40-bike-specs-unit-block-diagram
title: Unit block diagram with a wireless heart-rate receiver, a cooling fan and an
  RPM sensor, and no mains block at all
kind: spec
question: What does the unit block diagram of a Spirit Medical 4.0R or 4.0U bike show?
asked_as:
- 4.0r block diagram
- what feeds the display board on the 4.0u
- does the 4.0r have a wireless hr receiver
- spirit medical bike configuration diagram
keywords:
- block diagram
- bike configuration
- display board
- driver board
- hr handlebar
- wireless hr receiver
- cooling fan
- rpm sensor
- generator brake
- key
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40u-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-med-40-bike-specs-circuit-diagram-6-pin-computer-cable-to-a-cs52005-controller
- spirit-med-40-bike-specs-electrical-configuration-generator-brake
- spirit-cr800-cu800-2021-specs-unit-block-diagram
- 40t-2026-specs-unit-block-diagram
source:
  ref: spirit-bike-40r-2025-service-manual
  locator: '4.0R: 6-1. Bike Configuration, PDF p. 21 (printed 21), text.md lines 266-272,
    a flat drawing read from a 110 dpi render (OCR supplement lines 1022-1042). 4.0U:
    6-1, PDF p. 21 (printed 18), lines 275-281 (OCR 935-953); the same drawing'
  extracted_at: '2026-09-11'
---

One drawing, the same in both books, with two boxes and eight inputs and outputs.

**Into the DISPLAY BOARD:** **HR HANDLEBAR**, **KEY** and a **WIRELESS HR RECEIVER** (three boxes across
the top). Out of it: the **COOLING FAN**. A two-headed arrow joins the display board to the driver
board - the 6-pin computer cable.

**Into the DRIVER BOARD:** the **RPM SENOR** (as printed) and the **GENERATOR**. Out of it: the
**GENERATOR BRAKE**.

**Nothing else.** There is no power switch, breaker, adapter or safety key on the sheet, because the
generator is the only power source and a bike has no tether. The chapter is titled *FR800 Unit Block
Diagrams* in the 4.0R book and *FU800 Unit Block Diagrams* in the 4.0U book; the picture is identical.

The sheet is the CR800/CU800 generator-bike drawing
(`spirit-cr800-cu800-2021-specs-unit-block-diagram`) with the receiver box unlabelled as to type -
the 4.0T treadmill's version of the same drawing says *Bluetooth* on that box
(`40t-2026-specs-unit-block-diagram`).


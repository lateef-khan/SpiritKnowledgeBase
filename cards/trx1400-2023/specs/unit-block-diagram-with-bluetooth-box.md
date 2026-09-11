---
id: trx1400-2023-specs-unit-block-diagram-with-bluetooth-box
title: The unit block diagram with a Bluetooth box hanging off the display board,
  an amplifier with line in, and a driver board with motor, incline motor, VR set
  and RPM sensor
kind: spec
question: What does the unit block diagram in the Xterra trx1400-2023 treadmill service
  manual show?
asked_as:
- trx1400 block diagram
- how are the boards connected on the trx1400
- trx1400 bluetooth on the block diagram
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- bluetooth
- amplifier
- line in
- vr set
- rpm sensor
- wireless hr receiver
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-unit-block-diagram-gt90-family
- tr260-2023-specs-unit-block-diagram-with-incline-motor-vr-set-and-amplifier
see_also:
- spirit-dc-treadmill-specs-unit-block-diagram
- trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM (T3-NT053-01) '5. T3 Treadmill Unit Block Diagrams', PDF p.
    24 (printed 22), lines 347-358, OCR supplement lines 1747-1776; drawing read from
    the render
  extracted_at: '2026-09-11'
---

The drawing, headed *Treadmill Configuration*:

**Upper half.** **KEY**, **COOLING FAN** (an output) and **HR HANDLEBAR** sit to the left of the **DISPLAY BOARD**;
**WIRELESS HR RECEIVER** and **SAFETY KEY** feed it from the right; a **BULETOOTH** box (spelled so on the drawing)
hangs off the bottom-left corner of the display board with a two-way arrow. The display board feeds an
**AMPLIFIER**, which also takes a **LINE IN** and drives **SPEAKER L/R**.

**Lower half.** **POWER** goes through the **POWER SWITCH** and a **CURRENT BRAKER** into the **DRIVER BOARD**, which
drives the **MOTOR** and the **INCLINE MOTOR**, takes the **VR SET** back from the incline, and takes the **RPM
SENSOR** from below.

The drawing carries no part numbers or pin counts. It is the TR260 drawing plus the Bluetooth box, and the GT90
family drawing (TRX2500/3500/4500) with the KEY box present. The Spirit 2015 XT185/XT285 books draw the same
Bluetooth box (`spirit-dc-treadmill-specs-unit-block-diagram`).

---
id: trx5500-2024-specs-unit-block-diagram-with-line-out
title: The unit block diagram with a key, cooling fan, HR handlebar, wireless HR receiver
  and safety key on the display board, an amplifier with line in and line out, and
  a driver board with motor, incline motor, VR set and RPM sensor
kind: spec
question: What does the unit block diagram in the Xterra trx5500-2024 treadmill service
  manual show?
asked_as:
- trx5500 block diagram
- how are the boards connected on the trx5500
- trx5500 line out on the block diagram
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- amplifier
- line in
- line out
- vr set
- rpm sensor
- wireless hr receiver
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx5500-2024
  applies_to:
  - trx5500-2024
  section: specs
  code: '*'
  model_number:
  - '155810'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-unit-block-diagram-gt90-family
see_also:
- spirit-dc-treadmill-specs-unit-block-diagram
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
source:
  ref: xterra-treadmill-trx5500-2024-service-manual
  locator: TRX5500 SM (GT90D-NT041) '5. Unit Block Diagrams', PDF p. 22 (printed 21),
    lines 360-361, OCR supplement lines 1395-1421; drawing read from the render
  extracted_at: '2026-09-11'
---

The drawing has no heading on the page beyond the chapter title:

**Upper half.** **KEY**, **COOLING FAN** (an output) and **HR HANDLEBAR** sit to the left of the **DISPLAY BOARD**;
**WIRELESS HR RECEIVER** and **SAFETY KEY** feed it from the right. The display board feeds an **AMPLIFIER**, which
also takes a **LINE IN** and drives both **SPEAKER L/R** and a **LINE OUT**.

**Lower half.** **POWER** goes through the **POWER SWITCH** and a **CURRENT BRAKER** into the **DRIVER BOARD**, which
drives the **MOTOR** and the **INCLINE MOTOR**, takes the **VR SET** back from the incline, and takes the **RPM
SENSOR** from below.

The LINE OUT box is what sets this drawing apart from the TRX2500/3500/4500 one; there is no Bluetooth or USB box,
although the display-board photograph on p. 25 has a "USB wires socket" and a "Bluetooth & Wifi board". No part
numbers or pin counts are drawn. The Spirit CT800-2016 draws the same LINE OUT
(`spirit-dc-treadmill-specs-unit-block-diagram`).

---
id: tr260-2023-specs-unit-block-diagram-with-incline-motor-vr-set-and-amplifier
title: 'The unit block diagram: key, cooling fan and HR handlebar on the left of the
  display board, wireless HR receiver and safety key on the right, an amplifier with
  line in, and a driver board with motor, incline motor, VR set and RPM sensor'
kind: spec
question: What does the unit block diagram in the Xterra tr260-2023 treadmill service
  manual show?
asked_as:
- tr260 block diagram
- how are the boards connected on the tr260
- tr260 treadmill configuration drawing
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- amplifier
- line in
- vr set
- rpm sensor
- wireless hr receiver
- cooling fan
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-unit-block-diagram-no-incline-motor-no-fan-no-bluetooth
- xterra-trx-specs-unit-block-diagram-gt90-family
see_also:
- spirit-dc-treadmill-specs-unit-block-diagram
- tr260-2023-specs-circuit-diagram-with-a-filter-and-a-relay-pwm-vdd-rpm-gnd-pin-define
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM (GT75A-NT050) '5. Unit Block Diagrams', PDF p. 16 (printed 16),
    lines 255-261, OCR supplement lines 1168-1207; drawing read from the render
  extracted_at: '2026-09-11'
---

The drawing, headed *Treadmill Configuration*:

**Upper half.** **KEY** and **HR HANDLEBAR** feed the **DISPLAY BOARD** from the left and the display board drives
a **COOLING FAN**. **WIRELESS HR RECEIVER** and **SAFETY KEY** feed it from the right. The display board feeds an
**AMPLIFIER**, which also takes a **LINE IN** and drives **SPEAKER L/R**. A double arrow joins the display board to
the driver board.

**Lower half.** **POWER** goes through the **POWER SWITCH** and a **CURRENT BRAKER** into the **DRIVER BOARD**. The
driver board drives the **MOTOR** and the **INCLINE MOTOR**, takes the **VR SET** (incline position) back from the
incline side, and takes the **RPM SENSOR** from below.

No Bluetooth box is drawn, although the display-board photograph on p. 18 has a "Bluetooth board wires socket";
no USB or line-out box either. The drawing carries no part numbers or pin counts. It is the same drawing family as the
Spirit DC treadmills (`spirit-dc-treadmill-specs-unit-block-diagram`) and as the TRX books, which add a Bluetooth
box (TRX1400, TRX3500/4500) or a line out (TRX5500).

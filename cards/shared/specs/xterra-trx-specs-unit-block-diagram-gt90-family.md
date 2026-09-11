---
id: xterra-trx-specs-unit-block-diagram-gt90-family
title: 'The unit block diagram of the folding TRX family: cooling fan and HR handlebar
  into the display board, amplifier with line in, and a driver board with motor, incline
  motor, VR set and RPM sensor; a Bluetooth box on two of the three'
kind: spec
question: What does the unit block diagram in the Xterra TRX treadmill service manual
  show, and what is ghost text on that page?
asked_as:
- trx3500 block diagram
- trx2500 treadmill configuration drawing
- does the trx4500 block diagram show bluetooth or usb
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- bluetooth
- usb
- amplifier
- line in
- vr set
- ghost text
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx5500-2024-specs-unit-block-diagram-with-line-out
- trx1400-2023-specs-unit-block-diagram-with-bluetooth-box
see_also:
- spirit-dc-treadmill-specs-unit-block-diagram
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: TRX3500/TRX4500 SM '5. Treadmill Unit Block Diagrams', PDF p. 23 (printed
    22), lines 366-379, OCR supplement lines 1440-1473; TRX2500 SM PDF p. 21 (printed
    20), lines 339-352, OCR supplement lines 1625-1653. Both drawings read from the
    render
  extracted_at: '2026-09-11'
---

One drawing, headed *Treadmill Configuration*, in both books:

**Upper half.** **COOLING FAN** (an output) and **HR HANDLEBAR** sit to the left of the **DISPLAY BOARD**;
**WIRELESS HR RECEIVER** and **SAFETY KEY** feed it from the right. The display board feeds an **AMPLIFIER**, which
also takes a **LINE IN** and drives **SPEAKER L/R**. Where the TR260 and TRX1400 drawings have a KEY box at the top
left there is a blank white patch.

**Lower half.** **POWER** goes through the **POWER SWITCH** and a **CURRENT BRAKER** into the **DRIVER BOARD**, which
drives the **MOTOR** and the **INCLINE MOTOR**, takes the **VR SET** back from the incline, and takes the **RPM
SENSOR** from below.

| Book | Bluetooth box | What the text layer adds that is not printed |
|---|---|---|
| TRX3500 / TRX4500 | yes - a **BLUETOOTH** box with an arrow into the display board's lower left | "USB (Only Charge)" |
| TRX2500 | **no** - the rendered page has no Bluetooth box | "USB (Only Charge)" and "BLUETOOTH" |

**Ghost text.** Both pages' text layers carry "USB (Only Charge)", and the TRX2500's "BLUETOOTH" as well, but the
rendered drawings do not show a USB box on either and no Bluetooth box on the TRX2500. Read from the render, only
the boxes named above are printed. The drawing carries no part numbers or pin counts.

---
id: cvc800-tension-motor-connector-at-the-motor
title: Tension motor connector pin definition, read at the motor
kind: spec
question: What is the tension motor connector pinout at the motor on a Spirit cvc800
  climber?
asked_as:
- tension motor plug pins on the cvc800
- 5 pin connector on the climber resistance motor
- which pin is m plus on the cvc800 motor
- steel rope motor wiring climber
keywords:
- tension motor
- connector
- pinout
- 5 pin
- m+
- m-
- vr1
- vr2
- gnd
- steel rope
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cvc800-console-to-driver-board-connector-pin-map
- e25-2016-tension-motor-connector-pinout
- sole-bike-tension-motor-connector-pinout
see_also:
- cvc800-electrical-part-descriptions
source:
  ref: spirit-climber-cvc800-service-manual
  locator: p. 18 (printed 18), section 5 'Tension Motor Connector definition function'
  extracted_at: '2026-09-08'
---

**This is the map printed at the motor. Section 8-4 on p. 33 prints a different one for the same
five-way connector at the console board.**

Labelled **MAIN CONTROL** on the photograph of the motor:

| Pin | Signal |
|---|---|
| 1 | M- |
| 2 | M+ |
| 3 | VR1 |
| 4 | VR2 |
| 5 | GND |

The connector on the motor is numbered **1 at the bottom rising to 5 at the top**. The steel rope
that changes resistance leaves the motor beside it.

Pins 3 and 4 are the disagreement: this page calls them **VR1 and VR2**, while p. 33 calls them
**+5V and VR**. Meter the wires before you rely on either.

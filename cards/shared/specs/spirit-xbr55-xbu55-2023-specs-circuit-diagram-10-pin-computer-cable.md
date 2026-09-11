---
id: spirit-xbr55-xbu55-2023-specs-circuit-diagram-10-pin-computer-cable
title: 'Circuit diagram: two hand-pulse plugs on the console and one 10-pin computer
  cable that splits into 5 pins for the tension motor, 2 pins for the RPM sensor and
  3 pins for the adapter''s DC power cord'
kind: spec
question: What does the circuit diagram of a Spirit XBR55 or XBU55 2023 bike show?
asked_as:
- xbr55 2023 wiring diagram
- how many pins is the xbu55 computer cable
- xbu55 schematic
- which branch of the console cable goes to the adapter on the xbr55
keywords:
- circuit diagram
- wiring diagram
- schematic
- 10 pins computer cable
- 5 pins
- 2 pins
- 3 pins
- tension motor
- rpm sensor
- dc power cord
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55-2023
  - xbu55-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-circuit-diagram
- xbr95-2023-specs-circuit-diagram-6-pin-computer-cable
see_also:
- spirit-xbr55-xbu55-2023-specs-unit-block-diagram
- spirit-xb-specs-gear-motor-connector-5-pin-definition
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55-2023: 8.3 Circuit Diagram, PDF p. 15 (printed 15 of 30), text.md
    lines 294-298, flattened drawing read from a 300 dpi render (OCR supplement lines
    1027-1048). XBU55-2023: PDF p. 15, lines 293-297 (OCR 894-908). The same drawing'
  extracted_at: '2026-09-11'
---

A block schematic with pin counts and no wire colours.

- **CONSOLE** at the top, with a **HAND PULSE** plug on each side.
- One **10 PINS COMPUTER CABLE** leaves the bottom of the console and forks into three:
  - **5 PINS** to the **Tension Motor** (the five-way plug defined on
    `spirit-xb-specs-gear-motor-connector-5-pin-definition`);
  - **2 PINS** to the **RPM SENSOR**;
  - **3 PINS** to a **DC POWER CORD**, whose in-line plug meets the lead from the **AC ADAPTER**.

5 + 2 + 3 = 10: the whole harness is one cable from the console. **No controller board is
drawn.** The adapter's rating is not printed anywhere in either book.

The XBR95-2023 drawing is the one with a controller and a six-pin cable
(`xbr95-2023-specs-circuit-diagram-6-pin-computer-cable`); the 2016 and ENT books draw the same
three-way split as a harness picture without pin counts (`spirit-xb-2016-specs-circuit-diagram`).


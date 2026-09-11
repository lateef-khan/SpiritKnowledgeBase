---
id: xe795-2023-specs-circuit-diagram-6-pin-computer-cable
title: Circuit diagram with a 6-pin computer cable to the CS52005-23, a generator
  white, black and red wire, a red brake wire and a speed sensor, with the generator
  lead miscaptioned TO Brake
kind: spec
question: What does the circuit diagram of a Spirit xe795-2023 elliptical show?
asked_as:
- xe795 2023 wiring diagram
- xe795 schematic 6 pin
- which generator wire goes to j1 on the xe795
- what does to brake mean on the xe795 circuit diagram
keywords:
- circuit diagram
- wiring diagram
- schematic
- 6 pins computer cable
- cs52005-23
- j1 j3 j4
- generator
- white black red wire
- speed sensor
- hand pulse
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2023
  applies_to:
  - xe795-2023
  section: specs
  code: '*'
  model_number:
  - '795023'
authority: 3
not_to_be_confused_with:
- xe795-2016-specs-circuit-diagram-xe815-se024
- xbr95-2023-specs-circuit-diagram-6-pin-computer-cable
see_also:
- xe795-2023-specs-generator-controller-cs52005-23-connections
- xe795-2023-specs-unit-block-diagram
- xe795-2023-specs-display-board-cs11039-and-interface-board-connections
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
source:
  ref: spirit-elliptical-xe795-2023-service-manual
  locator: '8.2 Circuit Diagram, PDF p. 16 (printed 16), text.md lines 283-299; the
    drawing is a flattened image read from a 300 dpi render (OCR supplement lines
    966-996). It shares the page with 8.1 Error Message: EEPROM ERR'
  extracted_at: '2026-09-11'
---

Five boxes and four cables, no title code:

- **CONSOLE**, with a **HAND PULSE** block on a short lead at each side.
- A **6 PINS COMPUTER CABLE** from the console down to the controller.
- **CS52005-23** in the middle.
- **Generator** at the left: a **WHITE, BLACK, RED wire** lead captioned **TO J1**, and a **RED
  wire** lead captioned **TO J4**.
- **SPEED SENSOR** at the right, captioned **TO J3**.

**The three-wire generator lead also carries the caption "TO Brake"** above its TO J1 label - a
misplacement. The brake coil is the two-wire red lead to J4; J1 is the generator's stator
input, as the driver-board page names it (*GENERATOR POWER*). Read J1 = generator, J4 = brake.

**No adapter, inlet or fuse**: the generator powers the machine. **No pin numbers** are printed
for the six-pin cable anywhere in the book. The 2023 XBR95 bike's sheet is the same drawing with
its CS52005-33 board (`xbr95-2023-specs-circuit-diagram-6-pin-computer-cable`); the 2016 XE795's
sheet routes the speed sensor up the console cable instead
(`xe795-2016-specs-circuit-diagram-xe815-se024`).


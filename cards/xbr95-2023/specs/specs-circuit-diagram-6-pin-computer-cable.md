---
id: xbr95-2023-specs-circuit-diagram-6-pin-computer-cable
title: Circuit diagram with a level quick key and two hand pulses on the console,
  a 6-pin computer cable to the CS52005-33 controller, and colour-labelled generator
  and brake wires
kind: spec
question: What does the circuit diagram of a Spirit xbr95-2023 recumbent bike show?
asked_as:
- xbr95 2023 wiring diagram
- how many pins is the xbr95 computer cable
- xbr95 schematic
- what colour are the generator wires on the xbr95
keywords:
- circuit diagram
- wiring diagram
- schematic
- 6 pins computer cable
- level quick key
- hand pulse
- cs52005-33
- white black red wire
- red wire
- to j1
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2023
  applies_to:
  - xbr95-2023
  section: specs
  code: '*'
  model_number:
  - '951123'
authority: 3
not_to_be_confused_with:
- spirit-xbr55-xbu55-2023-specs-circuit-diagram-10-pin-computer-cable
- spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b
see_also:
- xbr95-2023-specs-generator-controller-cs52005-33-connections
- xbr95-2023-specs-unit-block-diagram
source:
  ref: spirit-bike-xbr95-2023-service-manual
  locator: 8.2 Circuit Diagram, PDF p. 14 (printed 14 of 28), text.md lines 246-251,
    flattened drawing read from a 300 dpi render (OCR supplement lines 1005-1029)
  extracted_at: '2026-09-11'
---

A block schematic with pin counts and wire colours.

- **CONSOLE** with a **HAND PULSE** plug on each side and a **LEVEL QUICK KEY** plug on the left -
  the seat-handle resistance buttons.
- One **6 PINS COMPUTER CABLE** from the console to the **CS52005-33** controller.
- From the **Generator**: a **WHITE, BLACK, RED wire** marked *TO J1*, and a **RED wire** marked
  *TO J4*. The three-colour lead is captioned *TO Brake* on the drawing, which contradicts the
  controller page (J1 is the three-phase generator input); see the controller card.
- The controller's **TO J3** socket to the **SPEED SENSOR**.

**No adapter, DC jack or mains block** - the generator powers the bike. **A six-pin cable, not the
ten-pin one** of the XBR55/XBU55 (`spirit-xbr55-xbu55-2023-specs-circuit-diagram-10-pin-computer-cable`),
because the motor and sensor branches end at the controller here rather than at the console.


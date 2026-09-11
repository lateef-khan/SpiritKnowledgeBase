---
id: ct850ent-2022-specs-console-transfer-and-power-bridge-boards
title: The console transfer board and power bridge board connectors on the AC-inverter
  ENT machine
kind: spec
question: What are the connectors on the console back-cover transfer board and the
  power bridge board of a Spirit ct850ent-2022 treadmill?
asked_as:
- what plugs into the transfer board behind the ct850 ent console
- ct850ent power bridge board connectors
- how many pins is the keyboard cable on the ct850 ent
- rm6t3 control connector pins
keywords:
- transfer board
- power bridge board
- connector
- console back cover
- hdmi cable
- coaxial cable
- keyboard
- c-safe
- rm6t3 control
- dc 13v
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850ent-2022
  applies_to:
  - ct850ent-2022
  section: specs
  code: '*'
  model_number:
  - '850852'
authority: 3
not_to_be_confused_with:
- ct800ent-2022-specs-console-transfer-and-power-bridge-boards
- ct850-2020-console-back-cover-transfer-board
see_also:
- ct850-2020-display-board-connector-pinouts
- spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter
- ct850ent-2022-specs-circuit-diagram
- ct850-2020-console-keypad-board
source:
  ref: spirit-treadmill-ct850ent-2022-service-manual
  locator: PDF p. 19 (printed 19) 'Transfer PCB board of Console Back', text.md lines
    334-366; PDF p. 21 (printed 21) 'The console POWER BRIDGE PCB board', lines 380-401
  extracted_at: '2026-09-11'
---

**Transfer PCB board of console back (p. 19)** - the cables landing on it, with the pin counts the book
prints:

| Left column | Right column |
|---|---|
| RM6T3 Control (6 PINS) | HDMI cable |
| RM6T3 Control (4 PINS) | Coaxial cable |
| Safety Key (3 PINS) | KEYBOARD+RF (10 PINS) |
| GND | Audio (4 PINS) |
| HAND-RIGHT (3 PINS) | C-Safe (5 PINS) |
| HAND-LEFT (4 PINS) | Fan (2 PINS) |

**Console power bridge PCB board (p. 21)** - the terminals:

- **RM6T3 control (8 Pins) (Inverter End)**
- **RM6T3 control (2 Pins)**, twice
- **RM6T3 control (6 Pins)**
- **DC_13V/4A (Converter End)**

The **RM6T3** name is the inverter-control path; on the CT800ENT the same two boards carry **STD control**
connectors, because that machine drives a DC motor. The pin definitions the book prints for the transfer
board are the same tables the CT850-2020 prints for its display board and are on
`ct850-2020-display-board-connector-pinouts`.

---
id: ct800ent-2022-specs-console-transfer-and-power-bridge-boards
title: The console transfer board and power bridge board connectors on the DC-motor
  ENT machine
kind: spec
question: What are the connectors on the console back-cover transfer board and the
  power bridge board of a Spirit ct800ent-2022 treadmill?
asked_as:
- what plugs into the transfer board behind the ct800 ent console
- ct800ent power bridge board connectors
- how many pins is the keyboard cable on the ct800 ent
- std control connector pins
keywords:
- transfer board
- power bridge board
- connector
- console back cover
- hdmi cable
- coaxial cable
- keyboard
- c-safe
- std control
- dc 13v
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800ent-2022
  applies_to:
  - ct800ent-2022
  section: specs
  code: '*'
  model_number:
  - '800852'
authority: 3
not_to_be_confused_with:
- ct850ent-2022-specs-console-transfer-and-power-bridge-boards
- ct850-2020-console-back-cover-transfer-board
see_also:
- ct850-2020-display-board-connector-pinouts
- spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter
- ct800ent-2022-specs-circuit-diagram
- ct850-2020-console-keypad-board
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: PDF p. 19 (printed 19) 'Transfer PCB board of Console Back', text.md lines
    337-368; PDF p. 21 (printed 21) 'The console POWER BRIDGE PCB board', lines 382-412
  extracted_at: '2026-09-11'
---

**Transfer PCB board of console back (p. 19)** - the cables landing on it, with the pin counts the book
prints:

| Left column | Right column |
|---|---|
| Safety Key (3 PINS) | HDMI cable |
| STD control (4 PINS) | Coaxial cable |
| STD control (6 PINS) | KEYBOARD+RF (10 PINS) |
| HAND-RIGHT (3 PINS) | Audio (4 PINS) |
| HAND-LEFT (4 PINS) | C-Safe (5 PINS) |
| | Fan (2 PINS) |

**Console power bridge PCB board (p. 21)** - the terminals, each named for what it connects to:

- **STD control (6+2+2 Pins)** and **STD control (Drive Board End)**
- **AC_L (Converter End)**, **AC_N (Converter End)**
- **AC_N (Driver Board End)**, **AC_L (Driver Board End)**
- **AC_N (Filter End)**, **AC_L (Filter End)**
- **DC_13V/4A (Converter End)**

The **STD** name marks the DC-drive control path; on the CT850ENT the same two boards carry **RM6T3
control** connectors instead, because that machine talks to an inverter. The pin definitions the book
prints for the transfer board are the same tables the CT850-2020 prints for its display board and are on
`ct850-2020-display-board-connector-pinouts`.

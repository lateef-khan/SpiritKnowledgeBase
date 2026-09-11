---
id: ct900-specs-transfer-board-pin-definitions
title: Pin definitions of the 12-pin main connector, keypad, safety and heart-rate
  plugs on the transfer board
kind: spec
question: What are the pin definitions of the console back-cover transfer board connectors
  on a Spirit ct900 treadmill?
asked_as:
- ct900 main connector pinout
- which pin is the safe key on the ct900 12 pin cable
- keypad connector pins on the ct900
- hr board connector pin define
keywords:
- pin definition
- pinout
- main connector
- 12 pin
- keypad
- safety
- hr board
- erp
- inc_up/dn
- position
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: specs
  code: '*'
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct850-2020-display-board-connector-pinouts
- ct800-2016-specs-console-12-pin-cable-pinout
see_also:
- ct900-specs-console-back-cover-transfer-board
- ct900-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct900-service-manual
  locator: PDF p. 24 (printed 24) 'The console back cover transfer PCB board pin define',
    text.md lines 306-311; the OCR supplement at lines 1913-1939 is upside down; read
    from the render. The same four tables are repeated on the circuit diagram, PDF
    p. 39
  extracted_at: '2026-09-11'
---

Each table is headed with both faces' connector numbers.

**J1 · J9 → MAIN CONNECTOR (12 pins)**

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | GND | 7 | ERP PWR |
| 2 | +12V | 8 | SAFE KEY |
| 3 | SG+ | 9 | ERP EN |
| 4 | GND | 10 | INC_EN |
| 5 | +12V | 11 | INC_UP/DN |
| 6 | SG- | 12 | POSITION |

**J5 · J15 → KEYPAD (9 pins)**: 1 DATA0, 2 DATA1, 3 DATA2, 4 DATA3, 5 DATA4, 6 DATA5, 7 DATA6, 8 GND, 9
GND.

**J4 · J14 → SAFETY (3 pins)**: 1 VIN, 2 NC, 3 SAFETY_IN.

**J6 · J16 → HR BOARD (4 pins)**: 1 GND, 2 +5V, 3 HP_MON, 4 HP/WP.

The circuit diagram prints the same four tables beside the console and calls the main connector's cable
the **12 PIN COMPUTER CABLE (MIDDLE)**. The ERP pins go to the ERP board that sits between the console
cable and the inverter's signal wire.

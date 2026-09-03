---
id: b94-2019-console-to-driver-board-pinout
title: "Console to driver board cable pin-out"
kind: spec
question: "What is the console to driver board pin-out on a Sole B94-2019?"
asked_as:
- "console cable pinout on my 2019 b94"
- "which pin is rpm in on the b94 console cable"
keywords:
- "pinout"
- "console cable"
- "driver board"
- "11 pin"
- "rpm in"
- "moto up"
- "inc_up"
- "wiring"
facets:
  brand:
  - sole
  product_line: bike
  model: b94-2019
  applies_to:
  - b94-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-tension-motor-connector-pinout
- b94-2016-console-to-driver-board-pinout
source:
  ref: sole-bike-b94-2019-service-manual
  locator: "Section 8, Test configuration: the console to driver board connector pin define function"
  extracted_at: '2026-09-03'
---

The connector is read 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 on the board.

| Pin | Signal |
|---|---|
| 1 | RPM IN |
| 2 | GND |
| 3 | +5V |
| 4 | MOTO AD |
| 5 | GND |
| 6 | MOTO DN |
| 7 | MOTO UP |
| 8 | VIN |
| 9 | INC_UP |
| 10 | INC_DN |
| 11 | INC_AD |

This list differs from the B94 2016 and R92 2016, which use FLY, MPOS, MTR- and MTR+ and leave pins 9 to 11 unused. Pins 9 to 11 here are incline signals; this bike does not incline.

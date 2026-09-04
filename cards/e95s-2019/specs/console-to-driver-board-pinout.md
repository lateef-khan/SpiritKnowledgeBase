---
id: e95s-2019-console-to-driver-board-pinout
title: Console to driver board connector pin definition
kind: spec
question: What is the console to driver board connector pinout on a Sole e95s-2019
  elliptical?
asked_as:
- what are the pins on the console cable of a sole elliptical
- 6 pin connector on the e95s driver board
- console to controller wiring elliptical
keywords:
- console
- driver board
- connector
- pinout
- 6 pin
- gnd
- rxd
- txd
- vin0
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2019
  applies_to:
  - e95s-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e95s-2019-e3-stride-error
- e95s-2019-tension-motor-connector-pinout
source:
  ref: sole-elliptical-e95s-2019-service-manual
  locator: Test configuration, console to driver board connector, page 46
  extracted_at: '2026-09-04'
---

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | RXD |
| 3 | TXD |
| 4 | VIN0 |
| 5 | S/W |
| 6 | S/W |

This is a **6-pin serial link**, not the 11-pin analogue harness the E25 and E35 manuals print. The E3 troubleshooting tables on this machine name the same cable the 6-pin cable throughout.

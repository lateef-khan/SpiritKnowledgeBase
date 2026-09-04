---
id: f65-2019-console-to-driver-board-pinout
title: Console to driver board connector pinout
kind: spec
question: What is the console to driver board connector pinout on a Sole f65-2019
  treadmill?
asked_as:
- what are the pins on the treadmill console cable
- 6 pin main control wire pinout sole treadmill
- which pin is tx on the treadmill console connector
keywords:
- pinout
- console
- driver board
- 6 pin
- main control wire
- txd
- rxt
- vcc
- gnd
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2019
  applies_to:
  - f65-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2019-driver-board-connectors
- f65-2019-e5-communication-error
source:
  ref: sole-tm-f65-2019-service-manual
  locator: Section 8.3, test configuration - console to driver board connector
  extracted_at: '2026-09-04'
---

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | TXD |
| 3 | RXT |
| 4 | VCC |
| 5 | SW |
| 6 | N/A |

The connector positions are drawn as **1, 2, 3, 4, 5, 6**. The same cable is called the 6-pin main control wire elsewhere in the manual; it carries the speed signal on TX/RX and the +12V safety switch loop on SW.

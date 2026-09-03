---
id: sole-bike-7-pin-console-cable-pinout
title: "Seven-pin console to driver board cable pin-out"
kind: spec
question: "What is the console to driver board pin-out on a Sole LCB-2016 or LCR-2016?"
asked_as:
- "console cable pinout on my light commercial bike"
- "which pin carries speed on the lcb console cable"
- "7 pin cable wiring sole bike"
keywords:
- "pinout"
- "console cable"
- "driver board"
- "7-pin"
- "eup_control"
- "speed"
- "d/a"
- "wiring"
- "bike"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - lcb-2016
  - lcr-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-ems-brake-resistance-not-changing
- sole-bike-ems-brake-spec
source:
  ref: sole-bike-lcb-2016-service-manual
  locator: "Section 8, Test configuration: the console to driver board connector pin define function (same page in the LCB 2016 and LCR 2016 manuals)"
  extracted_at: '2026-09-03'
---

| Pin | Signal |
|---|---|
| 1 | +12V |
| 2 | GND |
| 3 | +5V |
| 4 | NC |
| 5 | D/A |
| 6 | SPEED |
| 7 | EUP_CONTROL |

The EMS brake output side of the driver board is a 2-pin connector:

| Pin | Signal |
|---|---|
| 1 | SPD |
| 2 | GND |

The LCB 2019 uses a **6-pin** console cable instead. Its manual does not print the pin list.

---
id: sc200-2019-console-connector-pinout
title: Console to driver board connector pin definition
kind: spec
question: What is the console to driver board connector pinout on a Sole sc200-2019?
asked_as:
- what are the pins on the console cable of a sole climber
- 10 pin connector on the sc200 board
- console to controller wiring climber
keywords:
- console
- driver board
- connector
- pinout
- 10 pin
- speed
- vr in
- m+
- +12v
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2019
  applies_to:
  - sc200-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2019-e2-tension-motor-failure
- sc200-2019-tension-motor-connector-pinout
source:
  ref: sole-elliptical-sc200-2019-service-manual
  locator: Test configuration, console to driver board connector, page 38
  extracted_at: '2026-09-04'
---

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | GND |
| 3 | +12V |
| 4 | SPEED |
| 5 | GND |
| 6 | GND |
| 7 | VR IN |
| 8 | +5V |
| 9 | M- |
| 10 | M+ |

The same drawing labels the other connectors on the display board: BLE symbol display, AMP power, two FAN connectors, HR HAND, HR RECEIVER, KEYS and USB.

The E2 troubleshooting tables call the cable to the tension motor the **8-pin cable**, while this connector is drawn with 10 pins. They are different connectors on the same board.

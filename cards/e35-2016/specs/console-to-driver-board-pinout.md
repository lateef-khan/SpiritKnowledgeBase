---
id: e35-2016-console-to-driver-board-pinout
title: Console to driver board connector pin definition
kind: spec
question: What is the console to driver board connector pinout on a Sole e35-2016
  elliptical?
asked_as:
- what are the pins on the console cable of my sole elliptical
- console to controller wiring on a sole elliptical
- 11 pin connector on the driver board
keywords:
- console
- driver board
- connector
- pinout
- 11 pin
- vin
- inc+
- inc vr
- 14-pin
facets:
  brand:
  - sole
  product_line: elliptical
  model: e35-2016
  applies_to:
  - e35-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e35-2016-tension-motor-connector-pinout
- e35-2016-e3-ramp-error
source:
  ref: sole-elliptical-e35-2016-service-manual
  locator: Test configuration, console to driver board connector, page 50
  extracted_at: '2026-09-04'
---

| Pin | Signal |
|---|---|
| 1 | SPEED |
| 2 | GND |
| 3 | VCC+5V |
| 4 | VR |
| 5 | GND |
| 6 | M- |
| 7 | M+ |
| 8 | VIN |
| 9 | INC+ |
| 10 | INC - |
| 11 | INC VR |

A second drawing on page 51 gives the 14-pin system harness at the controller as 1.M-, 2.M+, 3.+5Vcc, 4.VR, 5.GND, 6.SPEED, 7.GND, 8.NA, 9.NA, 10.VIN, 11.GND, 12.INC+, 13.INC-, 14.INC VR, the tension motor plug as 1.M-, 2.M+, 3.+5V, 4.VR, 5.GND, and the speed sensor plug as 1.SPEED, 2.GND.

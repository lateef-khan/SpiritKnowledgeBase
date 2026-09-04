---
id: e35-2019-console-to-driver-board-pinout
title: Console to driver board connector pin definition
kind: spec
question: What is the console to driver board connector pinout on a Sole e35-2019
  elliptical?
asked_as:
- what are the pins on the console cable of a sole elliptical
- 11 pin connector on the e35 driver board
- console to controller wiring elliptical
keywords:
- console
- driver board
- connector
- pinout
- 11 pin
- rpm in
- inc_up
- moto ad
- vin
facets:
  brand:
  - sole
  product_line: elliptical
  model: e35-2019
  applies_to:
  - e35-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e35-2019-tension-motor-connector-pinout
- e35-2019-e3-ramp-error
source:
  ref: sole-elliptical-e35-2019-service-manual
  locator: Test configuration, console to driver board connector, page 47
  extracted_at: '2026-09-04'
---

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

A second drawing on page 48 gives the 14-pin system harness at the controller as 1.M-, 2.M+, 3.+5Vcc, 4.VR, 5.GND, 6.SPEED, 7.GND, 8.NA, 9.NA, 10.VIN, 11.GND, 12.INC+, 13.INC-, 14.INC VR, and the speed sensor plug as 1.SPEED, 2.GND.

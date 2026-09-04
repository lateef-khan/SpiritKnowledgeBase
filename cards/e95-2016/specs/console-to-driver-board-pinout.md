---
id: e95-2016-console-to-driver-board-pinout
title: Console to driver board connector pin definition
kind: spec
question: What is the console to driver board connector pinout on a Sole e95-2016
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
- position sensor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95-2016
  applies_to:
  - e95-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e95-2016-tension-motor-connector-pinout
- e95-2016-e3-ramp-error
source:
  ref: sole-elliptical-e95-2016-service-manual
  locator: Test configuration, console to driver board connector, page 48, and the
    parts location drawing, page 49
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

The parts location drawing on the next page labels the same 11-pin plug differently: **1.SPEED, 2.GND, 3.VCC+5V, 4.ZERO, 5.COUNT, 6.MOTOR-, 7.MOTOR+, 8.VIN, 9.INC UP, 10.INC DOWN, 11.INC VR**. Pins 4 to 7 and 9 to 10 carry different names in the two drawings; both are printed in this manual.

The position sensor plug is **1. Red = ground, 2. White = position signal, 3. Black = 5vdc**, with the signal running 0~5v depending on incline position.

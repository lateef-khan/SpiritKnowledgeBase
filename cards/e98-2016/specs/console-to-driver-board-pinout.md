---
id: e98-2016-console-to-driver-board-pinout
title: Console to driver board connector pin definition
kind: spec
question: What is the console to driver board connector pinout on a Sole e98-2016
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
- pwm
- p/c
- inc vr
- position sensor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2016
  applies_to:
  - e98-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e98-2016-ems-brake-spec
- e98-2016-e3-incline-vr-error
source:
  ref: sole-elliptical-e98-2016-service-manual
  locator: Test configuration, console to driver board connector, pages 42-43
  extracted_at: '2026-09-04'
---

| Pin | Signal |
|---|---|
| 1 | +12V |
| 2 | GND |
| 3 | VCC+5V |
| 4 | PWM |
| 5 | AD |
| 6 | SPD |
| 7 | P/C |
| 8 | INC+ |
| 9 | INC - |
| 10 | INC VR |
| 11 | NA |

**This pinout belongs to the EMS machine only.** It carries a **PWM** brake drive on pin 4 and **+12V** on pin 1. The E25, E35, E55, E95 and E95S manuals of the same year print a different 11-pin or 10-pin list starting with SPEED, GND, VCC+5V, VR. Do not read across.

The position sensor plug is **1. Red = ground, 2. White = position signal, 3. Black = 5vdc**, with the signal running 0~5v depending on incline position.

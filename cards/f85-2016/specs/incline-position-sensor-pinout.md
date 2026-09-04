---
id: f85-2016-incline-position-sensor-pinout
title: Incline position sensor and power connector pins
kind: spec
question: How is the incline position sensor wired on a Sole F85-2016 treadmill?
asked_as:
- incline potentiometer wire colours
- which pin is the incline position signal
- how do i test the incline sensor voltage
keywords:
- position sensor
- potentiometer
- incline vr
- pinout
- three pin connector
- 5vdc
- wire colours
- incline board
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2016
  applies_to:
  - f85-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2016-incline-motor
see_also:
- f85-2016-incline-motor
- f85-2016-incline-motor-and-position-sensor-test
- f85-2016-e3-incline-vr-error
source:
  ref: sole-tm-f85-2016-service-manual
  locator: section 8.3 Test Configuration, printed pages 49 to 50
  extracted_at: '2026-09-04'
---

**Two different three wire looms run to the incline motor, and red means a different thing on each.**

**Position sensor loom (the VR or potentiometer cable)**

| Wire | Function |
|---|---|
| Black | Ground |
| White | Position signal, 0 to 5 V depending on incline position |
| Red | 5 vdc supply |

**Incline power loom**

| Wire | Function |
|---|---|
| Black | DOWN |
| White | COM |
| Red | UP |

**Console connector pins.** These connections are the same on the incline board and at the console:

| Pin | Function |
|---|---|
| 1 | Ground |
| 2 | Position signal, 0 to 5 vdc |
| 3 | 5 vdc |

Expect about **5 vdc between the black and red** sensor wires, and about **4.5 to 4.7 vdc between the red and white** when the incline motor is at its lowest position. The manual notes that number is not critical as long as it is in that neighbourhood.

There are no electronic components on the incline board for this signal, only circuit connections from the potentiometer connector to the console connector, so the only faults possible on the board itself are a bad solder joint or a broken track.

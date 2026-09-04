---
id: f65-2016-incline-position-sensor-wiring
title: Incline position sensor and console connector wiring
kind: spec
question: How is the incline position sensor wired on a Sole f65-2016 treadmill?
asked_as:
- what are the three wires on the incline potentiometer
- incline position sensor pinout on a sole treadmill
- which pin is 5v on the incline connector
keywords:
- position sensor
- potentiometer
- incline vr
- 3 pin
- 5vdc
- ground
- position signal
- pinout
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2016
  applies_to:
  - f65-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2016-incline-motor-test-procedure
- f65-2016-e3-incline-error
source:
  ref: sole-tm-f65-2016-service-manual
  locator: Test Configuration, incline motor control function relate parts location
  extracted_at: '2026-09-04'
---

The incline motor carries one **3-pin VR wire** - the position wire. The drawing labels it **GND, SENSOR PIN (AD), +5V VCC**.

The console connector wiring, which the manual says is the same on the incline board and at the console:

| Pin | Signal |
|---|---|
| 1 | 5vdc |
| 2 | position signal 0~5vdc |
| 3 | ground |

Measured at the potentiometer there should be **5vdc between the black and red wire**, and a voltage between the red and white wire of about **4.5~4.7 Vdc with the motor at its lowest position**.

The incline power output socket beside it is labelled **Com-white, UP-Red, DOWN-black**.

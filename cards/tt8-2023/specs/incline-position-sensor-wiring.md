---
id: tt8-2023-incline-position-sensor-wiring
title: Incline position sensor pinout and voltages
kind: spec
question: What voltages should the incline position sensor read on a Sole tt8-2023
  treadmill?
asked_as:
- what should the incline potentiometer read
- incline position sensor pinout
- 5 volts on the incline sensor
keywords:
- position sensor
- potentiometer
- incline vr
- pin 1
- pin 2
- pin 3
- 5vdc
- 0-5v
- wiring
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2023
  applies_to:
  - tt8-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- tt8-2023-incline-vr-test-procedure
- tt8-2023-e3-error-code
source:
  ref: sole-tm-tt8-2023-service-manual
  locator: Section 8.4, Test procedure, pages 46-47 of 69
  extracted_at: '2026-09-04'
---

**TT8 2023 ST738-YT066, DC drive motor.**

The 3-pin connector is wired the same at the controller and at the console:

| Pin | Signal |
|---|---|
| 1 | Ground |
| 2 | Position signal 0~5 Vdc |
| 3 | 5 Vdc |

Expected readings at the potentiometer: **5 Vdc between the black and red wire**, and a voltage between the
red and white wire that sits around **4.5 to 4.7 Vdc when the motor is at the lowest position**. The exact
figure is not critical as long as it is in that neighbourhood.

There are no electronic components on the controller for this signal — only circuit connections from the
potentiometer connector to the console connector — so a fault on the board can only be a bad solder joint or
a broken track.

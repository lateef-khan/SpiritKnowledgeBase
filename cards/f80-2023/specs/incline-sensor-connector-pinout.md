---
id: f80-2023-incline-sensor-connector-pinout
title: Incline position sensor connector pinout
kind: spec
question: What is the incline position sensor connector pinout on a Sole f80-2023
  treadmill?
asked_as:
- incline sensor pinout on my treadmill
- what are the 3 pins on the incline connector
- which pin is 5 volts on the incline cable
keywords:
- pinout
- 3 pin connector
- position sensor
- potentiometer
- 5vdc
- ground
- incline
- console connector
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2023
  applies_to:
  - f80-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2023-incline-position-sensor-test
- f80-2023-e3-incline-vr-voltage
- f80-2023-incline-motor-spec
source:
  ref: sole-tm-f80-2023-service-manual
  locator: Section 8.4 Test procedure, pages 41-42
  extracted_at: '2026-09-04'
---

These three connections are **the same at the controller and at the console**.

| Pin | Function |
|---|---|
| Pin 1 | ground |
| Pin 2 | position signal 0~5vdc |
| Pin 3 | 5vdc |

At the potentiometer itself there should be **5vdc between the black and red wire**, and a voltage between the red
and white wire that reads about **4.5~4.7 Vdc at the lowest incline position**.

**The 2023 treadmill manuals do not agree on this pinout.** The F65 manual prints Pin 1 = 5VDC and Pin 3 = Ground.
The F80, F85 and F89 manuals print the reverse: Pin 1 = ground and Pin 3 = 5vdc. Meter the connector before
trusting either.

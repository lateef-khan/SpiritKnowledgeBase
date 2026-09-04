---
id: s77-2019-incline-sensor-pinout
title: Incline position sensor wire colours and connector pins
kind: spec
question: What are the incline position sensor wires and pins on a Sole S77-2019 treadmill?
asked_as:
- what colour is the incline sensor signal wire
- incline potentiometer pinout on my s77
- 3 pin incline connector on my treadmill
keywords:
- position sensor
- potentiometer
- vr
- pin 1
- pin 3
- 5vdc
- ground
- position signal
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- s77-2019-incline-position-sensor-test
- s77-2019-e3-incline-vr
- s77-2019-incline-motor-spec
source:
  ref: sole-tm-s77-2019-service-manual
  locator: E3 test configuration, pages 48-49
  extracted_at: '2026-09-04'
---

**At the motor, the position sensor wires**

| Colour | Function |
|---|---|
| Black | Ground |
| White | Position signal |
| Red | 5 V DC |

The signal swings 0 to 5 V with the incline position.

**At the 3-pin console connector.** The manual says these connections are the same at the incline board and at the console.

| Pin | Function |
|---|---|
| 1 | **5 V DC** |
| 2 | Position signal, 0 to 5 V DC |
| 3 | **Ground** |

**The earlier ST725 manual for this machine family prints pin 1 and pin 3 the other way round**, as pin 1 = ground and pin 3 = 5 V DC, with pin 2 unchanged. The two manuals cannot both be right. Ring the connector out before you rely on either.

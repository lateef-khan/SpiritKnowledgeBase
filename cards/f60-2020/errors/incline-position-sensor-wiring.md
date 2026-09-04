---
id: f60-2020-incline-position-sensor-wiring
title: Wire colours and terminals for the incline position sensor
kind: spec
question: What are the incline sensor wire colours on a Sole F60-2020?
asked_as:
- which incline wire is the position signal
- incline potentiometer wire colours
- what colour is the incline up wire
keywords:
- position sensor
- incline vr
- wire colours
- com
- up
- down
- potentiometer
- 5vdc
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2020
  applies_to:
  - f60-2020
  section: errors
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- f60-2020-e3-error-code
- f60-2020-console-to-controller-pinout
- f60-2020-incline-motor-spec
source:
  ref: sole-tm-f60-2020-service-manual
  locator: page 45, Test Configuration under 8.4
  extracted_at: '2026-09-04'
---

**The 3-pin position sensor wires**

| Colour | Signal |
|---|---|
| Red | Ground |
| White | Position signal |
| Black | 5vdc |

The position signal reads 0 to 5V depending on the incline position.

**The incline power wires at the controller**

| Terminal | Colour |
|---|---|
| INCLINE POWER COM | White |
| INCLINE POWER UP | Red |
| INCLINE POWER DOWN | Black |

**The console to driver board connector**: 1. SW, 2. +12V, 3. TXD, 4. RXD, 5. GND.

---
id: e95-2016-tension-motor-connector-pinout
title: Tension motor connector pin definition
kind: spec
question: What is the tension motor connector pinout on a Sole e95-2016 elliptical?
asked_as:
- tension motor connector pins on my sole elliptical
- what are the 8 pins on the resistance motor
- wiring for the gear motor plug
keywords:
- tension motor
- connector
- pinout
- 8 pin
- count
- zero
- vin
- speed sensor
- steel rope
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
- e95-2016-tension-motor-spec
- e95-2016-e2-tension-motor-failure
source:
  ref: sole-elliptical-e95-2016-service-manual
  locator: Section 6-10 Tension Motor connector definition function, page 36
  extracted_at: '2026-09-04'
---

Main control side, **8 pins**:

| Pin | Signal |
|---|---|
| 1 | VIN |
| 2 | M+ |
| 3 | M- |
| 4 | COUNT |
| 5 | ZERO |
| 6 | 3V |
| 7 | GND |
| 8 | SPEED |

A separate 2-pin speed sensor plug is drawn beside it:

| Pin | Signal |
|---|---|
| 1 | GND |
| 2 | SPEED |

The drawing shows the steel rope leaving the motor.

**This is not the 5-pin tension motor connector.** The E25, E35 and E55 manuals of the same year print a 5-pin plug carrying M+, M-, +5V, VR and GND. Do not read this pinout onto those machines.

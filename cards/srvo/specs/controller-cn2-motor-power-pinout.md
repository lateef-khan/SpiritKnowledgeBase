---
id: srvo-controller-cn2-motor-power-pinout
title: Pinout of CN2, the SRVO motor power port
kind: spec
question: What is the pinout of the motor power port on a SOLE SRVO controller?
asked_as:
- srvo motor power connector pinout
- srvo uvw wiring
- which pin is u on the srvo motor connector
keywords:
- cn2
- motor power port
- pinout
- uvw
- three phase
- controller module
- servo motor
- wiring
- odd pins
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: cn2
authority: 3
not_to_be_confused_with:
- srvo-power-board-dc-output-pinout
- srvo-controller-cn3-ac-pinout
see_also:
- srvo-controller-connector-map
- srvo-error-0x4000000-uvw-cord-error
- srvo-servo-motor-specification
source:
  ref: sole-srvo-service-manual
  locator: page 36, section 8-2-2
  extracted_at: '2026-09-04'
---

**This is CN2 on a controller module, the three phase feed to one servo motor. It is not CN2 on the full range power board, which is a DC output.**

| Pin | Name | Description |
|---|---|---|
| 1 | U | U |
| 3 | V | V |
| 5 | W | W |

**The pin numbers really are 1, 3 and 5 in the manual.** Pins 2, 4 and any further positions are not listed, so this is either an alternating layout with unused pins between the phases or a gap in the table. The manual does not say which, and prints no default value for any pin.

A loose connection here is what error `0x4000000`, UVW cord error, reports.

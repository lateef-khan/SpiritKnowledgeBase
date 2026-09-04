---
id: e98-2019-driver-board-led-debugging
title: Controller indicator LED debugging
kind: spec
question: What do the LEDs on the driver board of a Sole e98-2019 elliptical mean?
asked_as:
- driver board lights on my sole elliptical
- led1 and led2 on the elliptical controller
- what do the incline board leds mean
keywords:
- led
- led1
- led2
- controller
- driver board
- relay
- transistor
- incline motor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2019
  applies_to:
  - e98-2019
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e98-2019-incline-motor-test-procedure
- e98-2019-fuse-replacement
source:
  ref: sole-elliptical-e98-2019-service-manual
  locator: Controller Indicator LED debugging, page 33
  extracted_at: '2026-09-04'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| LED1 | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| LED2 | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |

This table has only the two incline LEDs. Unlike the E25 and E35 manuals of the same year, it has no controller power LED row, so there is no printed "check the supply voltage is 110~120V" step attached to an LED on this machine.

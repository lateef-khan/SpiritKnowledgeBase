---
id: e95s-2016-driver-board-led-debugging
title: Controller indicator LED debugging
kind: spec
question: What do the LEDs on the driver board of a Sole e95s-2016 elliptical mean?
asked_as:
- what does the power led on the controller mean
- driver board lights on my sole machine
- controller leds on a sole elliptical
keywords:
- led
- led1
- led2
- controller
- driver board
- relay
- transistor
- stride motor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2016
  applies_to:
  - e95s-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e95s-2016-fuse-replacement
source:
  ref: sole-elliptical-e95s-2016-service-manual
  locator: Controller Indicator LED debugging, page 34
  extracted_at: '2026-09-04'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| LED1 | Motion of stride motor | Motion of stride motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| LED2 | Motion of stride motor | Motion of stride motor is down. | Transistor was broken. Relay failed. | Replace controller. |

**There is no controller power LED row in this manual.** The E25, E35 and E55 manuals of the same year print a third row, D5 POWER, telling you to check the supply voltage is 110~120V. This table has only the two motion LEDs, named LED1 and LED2.

The board drawing on the previous page labels the positions **INCLINE MOTOR UP** and **INCLINE MOTOR DOWN**, while this table calls the same part the stride motor. The section carries no number in this manual.

---
id: e55-2016-driver-board-led-debugging
title: Controller indicator LED debugging
kind: spec
question: What do the LEDs on the driver board of a Sole e55-2016 elliptical mean?
asked_as:
- what does the power led on the controller mean
- driver board lights on my sole machine
- controller leds on a sole elliptical
keywords:
- led
- d5
- d2
- d4
- power led
- controller
- driver board
- relay
- transformer
facets:
  brand:
  - sole
  product_line: elliptical
  model: e55-2016
  applies_to:
  - e55-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e55-2016-fuse-replacement
source:
  ref: sole-elliptical-e55-2016-service-manual
  locator: Section 6-8 Controller Indicator LED debugging, page 34
  extracted_at: '2026-09-04'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| D5 POWER | Controller power | If DC voltage is normal it would be always ON. If off, a fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110~120V. Replace fuse. Replace controller. |
| D2 | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| D4 | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |

Section 6-7 shows the board positions as POWER, INCLINE MOTOR DOWN and INCLINE MOTOR UP.

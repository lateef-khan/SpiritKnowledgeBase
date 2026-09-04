---
id: e98-2016-driver-board-led-debugging
title: Controller indicator LED debugging
kind: spec
question: What do the LEDs on the driver board of a Sole e98-2016 elliptical mean?
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
- incline motor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2016
  applies_to:
  - e98-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e98-2016-fuse-replacement
source:
  ref: sole-elliptical-e98-2016-service-manual
  locator: Section 6-8 Controller Indicator LED debugging, page 35
  extracted_at: '2026-09-04'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| LED1 | Motion of incline motor | Motion of incline motor is **down**. | Transistor was broken. Relay failed. | Replace controller. |
| LED2 | Motion of incline motor | Motion of incline motor is **up**. | Transistor was broken. Relay failed. | Replace controller. |

**Note which way round this table runs.** In this manual LED1 is the DOWN motion and LED2 is the UP motion. The E95 and E95S manuals of the same year print the opposite: LED1 up, LED2 down. Check the board in front of you rather than assuming.

**There is no controller power LED row in this manual.** The E25, E35 and E55 manuals of the same year print a third row, D5 POWER, telling you to check the supply voltage is 110~120V.

The board drawing in section 6-7 shows the positions as INCLINE MOTOR UP and INCLINE MOTOR DOWN.

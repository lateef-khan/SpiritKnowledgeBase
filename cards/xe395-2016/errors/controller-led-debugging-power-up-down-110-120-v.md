---
id: xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v
title: 'Reading the three controller LEDs: POWER checked against 110 to 120 V, the
  fuse and the transformer, and UP and DOWN for the incline motor'
kind: troubleshooting
question: What do the POWER, UP and DOWN LEDs on the controller of a Spirit xe395-2016
  elliptical mean?
asked_as:
- what are the leds on the xe395 controller board
- controller power led not lit elliptical
- incline board up down lights meaning
- spirit elliptical driver board leds
keywords:
- controller led
- power led
- up led
- down led
- incline motor
- relay
- transistor
- fuse
- 110-120v
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395-2016
  applies_to:
  - xe395-2016
  section: errors
  code: '*'
  model_number:
  - '395015'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds
see_also:
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- e25-2016-driver-board-led-debugging
- ct800-2016-errors-controller-led-debugging-90-to-110-v
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: XE395 2016 (XE539S-SE019-01) service manual Controller Indicator LED debugging;
    Driver Board LED Indicator Locations, PDF p. 33, PDF p. 34, text.md lines 527-543
  extracted_at: '2026-09-11'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110-120V. Replace Fuse. Replace controller. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |

**The three reasons and three fixes on the POWER row pair off in order**: wrong voltage - check the supply is 110-120V; blown fuse - replace the fuse (a 5A fuse on the motor controller, on the fuse page of the same book); bad transformer - replace the controller.

The UP and DOWN LEDs are step 3 of the nine-step incline test and the relays behind them are step 4: `xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`. The fault they help find is `Err` (`xe395-2016-errors-err-incline-vr-out-of-range-or-not-read`). The POWER LED is also step 6 of the tension-motor voltage test - *inspect the drive board POWER LED whether lit; if no lit the drive board is bad* (`spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc`).

**The CE850 2016 and XE895 2016 print a two-row version with no POWER row**, LED1 and LED2 for the stride motor (`spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds`). Sole's E25, E35 and E55 2016 print this three-row table with the power LED named D5 (`e25-2016-driver-board-led-debugging`); Spirit treadmills print four or six LEDs with their own voltage (`ct800-2016-errors-controller-led-debugging-90-to-110-v`). Different machines; separate cards.

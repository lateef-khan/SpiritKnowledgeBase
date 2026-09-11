---
id: spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds
title: 'Reading the two stride-motor LEDs on the controller: LED1 for up, LED2 for
  down, and a dark one means the controller is replaced'
kind: troubleshooting
question: What do the LED1 and LED2 indicators on the controller of a Spirit CE850-2016
  or XE895-2016 elliptical mean?
asked_as:
- what are the leds on the elliptical controller board
- stride board lights meaning
- led1 led2 on the spirit ce850 controller
- controller led not lit stride
keywords:
- controller led
- led1
- led2
- stride motor
- relay
- transistor
- driver board
- indicator
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe895-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v
see_also:
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- e95s-2016-driver-board-led-debugging
- ct800-2016-errors-controller-led-debugging-90-to-110-v
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual Controller Indicator LED debugging;
    Driver Board LED Indicator Locations, PDF p. 32, PDF p. 33, text.md lines 531-544;
    XE895 2016 (XE895-SE022) service manual Controller Indicator LED debugging; Driver
    Board LED Indicator Locations, PDF p. 33, PDF p. 34, text.md lines 532-545
  extracted_at: '2026-09-11'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| LED1 | Motion of stride motor | Motion of stride motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| LED2 | Motion of stride motor | Motion of stride motor is down. | Transistor was broken. Relay failed. | Replace controller. |

**There is no controller power LED row in these two books.** The XE395 2016 prints a third row, `POWER`, checked against a 110-120V supply, a fuse and the transformer (`xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v`). Here the table has only the two motion LEDs.

**The board drawing on the page before labels the same two positions `INCLINE MOTOR UP` and `INCLINE MOTOR DOWN`**, and a third, `POWER`, that the table does not mention. The drawing is the incline-elliptical template; the table is what applies to the stride machine.

The two LEDs are step 3 of the nine-step stride test - *do the Up/down lights on the stride board light?* - and the relays behind them are step 4: `spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`. The fault the LEDs help find is `E3` (`spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read`).

Sole's E95S 2016 prints this exact two-row table, drawing mismatch included (`e95s-2016-driver-board-led-debugging`); Spirit treadmills print a four- or six-LED version (`ct800-2016-errors-controller-led-debugging-90-to-110-v`). Different machines; separate cards.

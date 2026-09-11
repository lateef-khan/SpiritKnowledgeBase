---
id: spirit-xt-2023-errors-controller-led-debugging-five-leds
title: 'Reading the five controller LEDs: power, limit current, incline up, incline
  down and speed'
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Spirit XT385 2023, XT485
  2023 or XT685 2023 treadmill?
asked_as:
- what do the lights on the treadmill controller mean
- limit current led is on
- power led off on the lower board
keywords:
- controller led
- indicator led
- power led
- limit current
- over current
- up down led
- speed led
- rpm sensor
- fuse
- 3 mm
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt385-2023
  - xt485-2023
  - xt685-2023
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps
- spirit-xt-errors-controller-led-debugging-power-and-limit-only
- spirit-xt-ent-errors-controller-power-led-only
- f65-2023-controller-led-debugging
see_also:
- spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
- spirit-xt-errors-e1-check-rpm-sensor-procedure
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT385 2023 service manual 6.9 Controller Indicator LED debugging, PDF p.
    18, text.md lines 243-281; XT485 2023 service manual 6.9 Controller Indicator
    LED debugging, PDF p. 18, text.md lines 243-281; XT685 2023 service manual LED
    debugging table under 6.8, PDF p. 17, text.md lines 270-312
  extracted_at: '2026-09-11'
---

The table the 2023 XT385, XT485 and XT685 service manuals print under *Controller Indicator LED debugging*. Where the LEDs sit on the board is a specs fact; this card is what each state means.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110 VAC or 230 VAC. Replace fuse. Replace controller. |
| Limit current | Over current protection warning light | When the lower board detects over current, the LED will be lit. | Protection of lower board and motor. | Replace controller. Replace motor. Do not block belt running. Between belt and running board need to smear silicone oil. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| SPEED | RPM sensor indicator | The speed sensor didn't detect signal completely. | Check the gap between speed sensor and magnet. | To keep the gap-distance less than 3 mm. |

**No current threshold is printed for the limit LED**; the 2015 XT385 and XT485 give one (`spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps`). The 2023 XT185 and XT285 boards carry only the first two LEDs (`spirit-xt-errors-controller-led-debugging-power-and-limit-only`), and the two ENT consoles only the first (`spirit-xt-ent-errors-controller-power-led-only`).

The limit LED is the hardware side of the E2 over-current code (`spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller`); the SPEED LED is the hardware side of E1 (`spirit-xt-errors-e1-check-rpm-sensor-procedure`).

**The XT685 2023 prints this table without its `6.9 Controller Indicator LED debugging` heading**; the table sits under the 6.8 LED-locations heading on the same page, and its contents list still names 6.9 on page 18.

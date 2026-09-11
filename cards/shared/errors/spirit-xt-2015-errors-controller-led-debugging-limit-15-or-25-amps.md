---
id: spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps
title: Reading the five controller LEDs, with the limit LED tripping at 15 amps on
  220 V and 25 amps on 120 V
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Spirit XT385 2015 or
  XT485 2015 treadmill, and at what current does LIMIT light?
asked_as:
- what do the lights on the treadmill controller mean
- limit led on my spirit xt
- controller shut down led amps
keywords:
- controller led
- indicator led
- power led
- limit
- 15a
- 25a
- motor lock
- up down led
- speed led
- 3 mm
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt385-2015
  - xt485-2015
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- spirit-xt-errors-controller-led-debugging-power-and-limit-only
- f65-2023-controller-led-debugging
see_also:
- spirit-xt-2015-errors-e2-over-current-silicone-oil-then-board-or-motor
- spirit-xt-errors-e1-check-rpm-sensor-procedure
source:
  ref: spirit-treadmill-xt485-2015-service-manual
  locator: XT385 2015 service manual 6.7 Controller Indicator LED debugging, PDF p.
    31, text.md lines 441-472; XT485 2015 service manual 6.7 Controller Indicator
    LED debugging, PDF p. 31, text.md lines 440-471
  extracted_at: '2026-09-11'
---

The table the 2015 XT385 and XT485 service manuals print under *Controller Indicator LED debugging*. It is the only XT page that gives a current figure for the over-current LED.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 220 Vac (on 120 Vac electronic power system need 110 Vac). Replace fuse. Replace controller. |
| LIMIT | Limit the current of DC motor. Controller shut down. | When current of motor exceeds **15 A**, the LCD will turn on (on 220 Vac electronic power system). When current of motor exceeds **25 A**, the LCD will turn on (on 120 Vac electronic system). If LIMIT light is bright for 3 to 5 seconds, the LIMIT LED will turn on. | Loading is too high on belt. Operation is not correct, motor lock. Motor lock, LIMIT light will be bright for 3 to 5 seconds previously. | Belt/deck lubrication. Check mechanical drive system is not locked or jammed. Replace controller. Replace motor. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| SPEED | RPM sensor indicator | The speed sensor didn't detect signal completely. | Check the gap between speed sensor and magnet. | To keep the gap-distance less than 3 mm. |

The LIMIT row says *the LCD will turn on* where it means the LED; the row is reproduced as printed. The two thresholds sit the way the supply does: a 220 V machine draws about half the current of a 120 V one for the same load, so its limit is set lower.

The 2023 XT385 and XT485 print the same five LEDs with no threshold and a shorter remedy (`spirit-xt-2023-errors-controller-led-debugging-five-leds`). The 2015 XT185 and XT285 boards carry only the first two LEDs (`spirit-xt-errors-controller-led-debugging-power-and-limit-only`).

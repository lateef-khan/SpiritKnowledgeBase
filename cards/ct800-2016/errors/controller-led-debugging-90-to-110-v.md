---
id: ct800-2016-errors-controller-led-debugging-90-to-110-v
title: Reading the four controller LEDs, with the power LED checked against a 90 to
  110 V supply
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Spirit ct800-2016 treadmill?
asked_as:
- what do the lights on the treadmill controller mean
- power led off on the lower board
- incline up led on the controller
keywords:
- controller led
- indicator led
- power led
- up down led
- speed led
- rpm sensor
- fuse
- transformer
- 3 mm
- shut_down
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: errors
  code: no-code
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- ct900ent-errors-controller-led-debugging-six-leds-110-120-v
see_also:
- ct850-2016-low-speed-solution-flow-chart
- ct800-2016-errors-incline-err-during-incline-action
- ct800-2016-errors-low-speed-after-ten-seconds
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: CT800 2016 service manual 6.4 DRIVER BOARD LED Indicator Locations and
    6.5 Controller Indicator LED debugging, PDF p. 26-27 (printed 25-26), text.md
    lines 445-493
  extracted_at: '2026-09-11'
---

The table the CT800 2016 service manual prints under *6.5 Controller Indicator LED debugging*. Where the LEDs sit on the board is a specs fact; the LED-locations page names eight - `MOT_DRV`, `SHUT_DOWN`, `LIMI`, `RPM SENSOR`, `PWM`, `POWER`, `INC_UP` and `INC_DW` - and the table explains four of them.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If AC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 90~110V. Replace fuse. Replace controller. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| SPEED | RPM sensor indicator | The speed sensor didn't detect signal completely. | Check the gap between speed sensor and magnet. | To keep the gap-distance less than 3 mm. |

**90~110V is a figure no other page of this book uses** - the cover says AC 120V, the safety page asks for a 120-volt outlet, the matrix for 110-120V. Treat it as this table's own number and check the machine's rating plate. The LEDs the table does not explain are used elsewhere: the LOW SPEED flow chart watches `PWM` and `POWER` (`ct850-2016-low-speed-solution-flow-chart`), the matrix names the `Shut_DOWN` light (`ct800-2016-errors-low-speed-after-ten-seconds`), and the incline tables watch `UP` and `DOWN` (`ct800-2016-errors-incline-err-during-incline-action`).

The XT books print five LEDs including a limit-current one (`spirit-xt-2023-errors-controller-led-debugging-five-leds`); the CT900ENT and CT1000ENT print six (`ct900ent-errors-controller-led-debugging-six-leds-110-120-v`).

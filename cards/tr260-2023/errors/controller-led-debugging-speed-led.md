---
id: tr260-2023-errors-controller-led-debugging-speed-led
title: 'Reading the one controller LED the book names: the SPEED LED blinks as the
  sensor reads speed during calibration'
kind: troubleshooting
question: What does the SPEED LED on the lower controller mean on an Xterra tr260-2023
  treadmill?
asked_as:
- tr260 controller speed led
- speed led not blinking during calibration
- lights on the tr260 driver board
keywords:
- controller led
- indicator led
- speed led
- calibration
- speed sensor
- blink
- driver board
- led debugging
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- trx2500-2024-errors-controller-led-debugging-three-leds
- spirit-xt-2023-errors-controller-led-debugging-five-leds
see_also:
- xterra-treadmill-errors-e1-check-rpm-sensor-procedure
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM Controller Indicator LED debugging, PDF p. 24; text.md lines 336-349
  extracted_at: '2026-09-11'
---

The TR260 service manual's *Controller Indicator LED debugging* table has a single row, and its *Driver Board LED Indicator Locations* page marks only that LED:

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| SPEED LED | Detected speed, for calibration | In the calibration, when the sensor reads a speed signal, the speed LED will blink. If no blink, the sensor is probably bad, or the drive has a problem | In normal use the speed sensor is not used, but in calibration it is necessary; the speed LED shows whether the speed reading is normal | If the LED doesn't blink: 1. probably a SPEED sensor problem; 2. the drive may be broken |

No POWER, INFO or PWM LED is named on this page - yet the book's E1 chart asks the reader to watch "the PWM LED on the controller" and whether "only POWER LEDs" are on (`xterra-treadmill-errors-e1-solution-flow-chart-pwm-led`), and its check list mentions an "MD light" (`tr260-2023-errors-err-code-troubleshooting-check-list`). Those LEDs are not located or explained anywhere in the book.

The other Dyaco books name more LEDs: `trx1400-2023-errors-controller-led-debugging-power-and-info-leds`, `trx2500-2024-errors-controller-led-debugging-three-leds`, `xterra-trx-errors-controller-led-debugging-info-and-power-220-v`, `trx5500-2024-errors-controller-led-debugging-power-led-only`.

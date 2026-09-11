---
id: trx2500-2024-errors-controller-led-debugging-three-leds
title: 'Reading the three controller LEDs: a communication LED that flashes, a power
  LED that stays on, a speed LED that flashes only in calibration'
kind: troubleshooting
question: What do the three LEDs on the lower controller mean on an Xterra trx2500-2024
  treadmill?
asked_as:
- trx2500 controller leds
- led1 not flashing on the trx2500 controller
- which led is the speed led trx2500
keywords:
- controller led
- indicator led
- led1
- led2
- led3
- communication
- power led
- speed led
- fuse
- led debugging
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx2500-2024
  applies_to:
  - trx2500-2024
  section: errors
  code: '*'
  model_number:
  - '125817'
authority: 3
not_to_be_confused_with:
- xterra-trx-errors-controller-led-debugging-info-and-power-220-v
- tr260-2023-errors-controller-led-debugging-speed-led
- spirit-xt-2023-errors-controller-led-debugging-five-leds
see_also:
- xterra-treadmill-errors-e5-console-controller-communication-poor
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 6.6 Controller Indicator LED debugging, PDF p. 29 (printed 28);
    text.md lines 455-479; TRX2500 SM 6.5 Driver Board LED Indicator Locations, PDF
    p. 28 (printed 27); text.md lines 424-455
  extracted_at: '2026-09-11'
---

The TRX2500 service manual names three LEDs on the driver board:

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| LED1 | Communication directive LED | Normal: the LED flashes | During signal communication from console to lower controller, LED1 flashes | If it is not flashing, communication is poor: check the main control wires; replace the upper controller; replace the lower controller |
| LED2 | Power LED | If the DC voltage is normal it is always ON. If off, a fault condition exists | Voltage is not correct. Fuse is blown. Transformer is not good | Check the supply voltage is **220 V (110 V)**. Replace fuse. Replace controller |
| LED3 | SPEED LED | Only happens in the calibration | The speed feedback: when the speed signal is output the LED flashes | Happens in the calibration: check or replace the speed sensor; replace the lower controller |

The 6.5 locations page describes the same three, but its LED3 caption ends "the LED2 will be flashed" - a misprint for LED3. The book's E1 chart asks about a "PWM LED" and "POWER and PWM LEDs" (`xterra-treadmill-errors-e1-solution-flow-chart-pwm-led`) and its matrix about a "Shut_D light" (`xterra-trx-errors-e1-after-10-seconds-belt-not-running-eight-causes`); neither name appears in this table. LED1 dark is the hardware view of E5; LED3 dark during calibration is the hardware view of E1.

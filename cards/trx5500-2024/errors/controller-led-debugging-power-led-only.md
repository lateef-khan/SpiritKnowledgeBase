---
id: trx5500-2024-errors-controller-led-debugging-power-led-only
title: 'Reading the one controller LED the book names: POWER stays on when the DC
  supply is right, checked against 120 V or 230 V'
kind: troubleshooting
question: What does the POWER LED on the lower controller mean on an Xterra trx5500-2024
  treadmill?
asked_as:
- trx5500 controller power led
- power led off on the trx5500 driver board
- trx5500 led debugging
keywords:
- controller led
- indicator led
- power led
- fuse
- transformer
- 120v
- 230v
- led debugging
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx5500-2024
  applies_to:
  - trx5500-2024
  section: errors
  code: '*'
  model_number:
  - '155810'
authority: 3
not_to_be_confused_with:
- trx2500-2024-errors-controller-led-debugging-three-leds
- xterra-trx-errors-controller-led-debugging-info-and-power-220-v
see_also:
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
- spirit-xt-ent-errors-controller-power-led-only
source:
  ref: xterra-treadmill-trx5500-2024-service-manual
  locator: TRX5500 SM 6-4 Controller Indicator LED debugging, PDF p. 29 (printed 28);
    text.md lines 455-465
  extracted_at: '2026-09-11'
---

The TRX5500 service manual's *Controller Indicator LED debugging* table has one row:

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If the DC voltage is normal it is always ON. If off, a fault condition exists | Voltage is not correct. Fuse is blown. Transformer is no good | Check the supply voltage is **120 V (230 V)**. Replace fuse. Replace controller |

The 6-3 locations page marks the same LED ("Power directive LED. When treadmill power, LED will be blazed"). This is the only Dyaco book in the wave that quotes 120 V rather than 110 V. The book's E1 chart nevertheless asks the reader to watch a "PWM LED" and whether "only POWER and PWM LEDs" are on (`xterra-treadmill-errors-e1-solution-flow-chart-pwm-led`); no PWM LED is located or explained in the book. The Spirit ENT twin is `spirit-xt-ent-errors-controller-power-led-only`.

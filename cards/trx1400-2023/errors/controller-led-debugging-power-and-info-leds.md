---
id: trx1400-2023-errors-controller-led-debugging-power-and-info-leds
title: 'Reading the two controller LEDs: POWER stays on when the DC supply is right,
  INFO lights when the lower board hears the console'
kind: troubleshooting
question: What do the POWER and INFO LEDs on the lower controller mean on an Xterra
  trx1400-2023 treadmill?
asked_as:
- trx1400 controller leds
- info led not lit on the driver board
- power led off on the trx1400 controller
keywords:
- controller led
- indicator led
- power led
- info led
- fuse
- transformer
- main control wires
- 110v
- 220v
- led debugging
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: errors
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- xterra-trx-errors-controller-led-debugging-info-and-power-220-v
- spirit-xt-errors-controller-led-debugging-power-and-limit-only
see_also:
- xterra-treadmill-errors-e5-console-controller-communication-poor
- xterra-trx-errors-controller-led-debugging-info-and-power-220-v
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM 6.6 Controller Indicator LED debugging, PDF p. 32 (printed 30);
    text.md lines 464-484
  extracted_at: '2026-09-11'
---

The TRX1400 service manual locates two LEDs on the driver board (a Power LED and an INFO LED, section 6.5) and explains them in 6.6:

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If the DC voltage is normal it is always ON. If off, a fault condition exists | Voltage is not correct. Fuse is blown. Transformer is no good | Check the supply voltage is **110 V (or 220 V)**. Replace fuse. Replace controller |
| INFO | Whether the lower control board links to the upper console control board | If the lower control board does not link to the upper console board, the INFO LED does not light | It is a signal-indicating LED; unlit, it means the lower control board has not received the upper console board's signal | Check the main control wires, which may be broken. Replace the controller or the upper console board |

The TRX3500/TRX4500 book prints the same two rows with the supply voltage given as 220 V only (`xterra-trx-errors-controller-led-debugging-info-and-power-220-v`). An unlit INFO LED is the hardware view of E5 (`xterra-treadmill-errors-e5-console-controller-communication-poor`).

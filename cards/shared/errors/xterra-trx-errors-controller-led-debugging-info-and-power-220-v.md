---
id: xterra-trx-errors-controller-led-debugging-info-and-power-220-v
title: 'Reading the two controller LEDs on the 220 V table: INFO lights when the lower
  board hears the console, POWER stays on when the DC supply is right'
kind: troubleshooting
question: What do the INFO and POWER LEDs on the lower controller mean on an Xterra
  trx3500-2024 or trx4500-2024 treadmill?
asked_as:
- trx3500 controller leds
- trx4500 info led
- power led on the driver board 220v
keywords:
- controller led
- indicator led
- info led
- power led
- fuse
- transformer
- main control wires
- 220v
- led debugging
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- trx1400-2023-errors-controller-led-debugging-power-and-info-leds
- trx2500-2024-errors-controller-led-debugging-three-leds
see_also:
- xterra-treadmill-errors-e5-console-controller-communication-poor
- trx1400-2023-errors-controller-led-debugging-power-and-info-leds
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: TRX3500/TRX4500 SM 6.6 Controller Indicator LED debugging, PDF p. 34 (printed
    33); text.md lines 508-525; TRX3500/TRX4500 SM 6.5 Driver Board LED Indicator
    Locations, PDF p. 33 (printed 32); text.md lines 492-508
  extracted_at: '2026-09-11'
---

The TRX3500/TRX4500 service manual's *Controller Indicator LED debugging* table:

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| INFO | Whether the lower control board links to the upper console control board | If the lower control board does not link to the upper console board, the INFO LED does not light | A signal-indicating LED; unlit, the lower control board has not received the upper console board's signal | Check the main control wires, which may be broken. Replace the controller or the upper console board |
| POWER | Controller power | If the DC voltage is normal it is always ON. If off, a fault condition exists | Voltage is not correct. Fuse is blown. Transformer is no good | Check the supply voltage is **220 V**. Replace fuse. Replace controller |

The 6.5 locations page labels the power LED "LED3: Power directive LED. When treadmill power, LED will be blazed" and repeats the INFO text. The TRX1400 book prints the same two rows with "110V (or 220V)" (`trx1400-2023-errors-controller-led-debugging-power-and-info-leds`); the same book's circuit diagrams are drawn for both 120 V (GT90D-NT024) and 220 V (GT90C-NT023 CEGS) builds, so the 220 V figure here is the book's, not necessarily the machine's. An unlit INFO LED is the hardware view of E5.

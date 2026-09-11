---
id: spirit-xt-ent-errors-controller-power-led-only
title: The ENT lower controller has one indicator LED, power, and it needs the console
  connected and the safety key in to read
kind: troubleshooting
question: What does the LED on the lower controller mean on a Spirit XT485ENT or XT685ENT
  treadmill?
asked_as:
- only one light on the ent treadmill controller
- power led off on the lower board
- how to check the controller led on the touchscreen treadmill
keywords:
- controller led
- indicator led
- power led
- fuse
- transformer
- 120vac
- safety key
- ent
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt485ent-2023
  - xt685ent-2023
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- spirit-xt-errors-controller-led-debugging-power-and-limit-only
see_also:
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
source:
  ref: spirit-treadmill-xt485ent-2023-service-manual
  locator: XT485ENT 2023 service manual 6.5 Driver Board LED Indicator Locations and
    6.6 Controller Indicator LED debugging, PDF p. 27-28, text.md lines 371-399; XT685ENT
    2023 service manual 6.6 and 6.7, PDF p. 17, text.md lines 251-272
  extracted_at: '2026-09-11'
---

The XT485ENT and XT685ENT service manuals print a one-row LED table, and their LED-locations page carries a note the other XT books do not: **the power LED must be checked with the console connected and the safety key set** - *IT'S MUST BE CONNECT CONSOLE AND SET SAFETY KEY TO CHECK*.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 120 Vac (on 220 Vac electronic power system need 220 Vac). Replace fuse. Replace controller. |

There is no limit-current, incline or speed LED to read on these boards. The incline test steps that ask whether the up/down lights on the board light (`spirit-xt-errors-e3-incline-test-procedure-nine-steps`) therefore fall back on the relay click on an ENT machine.

The other XT boards carry two or five LEDs: `spirit-xt-errors-controller-led-debugging-power-and-limit-only`, `spirit-xt-2023-errors-controller-led-debugging-five-leds`.

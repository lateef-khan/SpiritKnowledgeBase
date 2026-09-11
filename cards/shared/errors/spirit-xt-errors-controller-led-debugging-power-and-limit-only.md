---
id: spirit-xt-errors-controller-led-debugging-power-and-limit-only
title: Reading the two controller LEDs, power and limit current, on the boards that
  have no incline or speed LEDs
kind: troubleshooting
question: What do the two LEDs on the lower controller mean on a Spirit XT185 or XT285
  treadmill, 2015 or 2023?
asked_as:
- what do the two lights on the treadmill controller mean
- limit current led is on
- power led off on the lower board
keywords:
- controller led
- indicator led
- power led
- limit current
- over current
- fuse
- transformer
- silicone oil
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps
- f63-2023-controller-led-debugging
see_also:
- spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
source:
  ref: spirit-treadmill-xt185-2023-service-manual
  locator: XT185 2023 service manual 6.7 Controller Indicator LED debugging, PDF p.
    16, text.md lines 275-305; XT285 2023 service manual 6.7 Controller Indicator
    LED debugging, PDF p. 17, text.md lines 277-307; XT185 2015 service manual 6.7
    Controller Indicator LED debugging, PDF p. 31, text.md lines 451-472; XT285 2015
    service manual 6.7 Controller Indicator LED debugging, PDF p. 32 (printed 31),
    text.md lines 520-541
  extracted_at: '2026-09-11'
---

The XT185 and XT285 service manuals, 2015 and 2023 alike, print a two-row LED table. Their driver board carries a Power LED and a Limit current LED and nothing else; there are no incline up/down or speed LEDs to read on these machines.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110 VAC or 230 VAC. Replace fuse. Replace controller. |
| Limit current | Over current protection warning light | When the lower board detects over current, the LED will be lit. | Protection of lower board and motor. | Replace controller. Replace motor. Do not block belt running. Between belt and running board need to smear silicone oil. |

No current threshold is printed. The XT385, XT485 and XT685 boards carry three more LEDs (`spirit-xt-2023-errors-controller-led-debugging-five-leds`, `spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps`), so the incline steps that say *do the Up/down lights on the controller light?* (`spirit-xt-errors-e3-incline-test-procedure-nine-steps`) have no LED to look at on an XT185 or XT285 - listen for the relay click instead.

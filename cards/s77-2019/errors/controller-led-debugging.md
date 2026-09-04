---
id: s77-2019-controller-led-debugging
title: Reading the indicator lights on the lower controller
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Sole S77-2019 treadmill?
asked_as:
- what do the lights on my treadmill controller mean
- s77 limit led is on
- power led on the driver board
keywords:
- led
- indicator
- power led
- limit current
- driver board
- over current
- fuse
- transformer
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- s77-2019-e2-over-current
- s77-2019-e1-no-rpm-signal
- s77-2019-lower-controller-replacement
source:
  ref: sole-tm-s77-2019-service-manual
  locator: Section 6.7 Controller Indicator LED debugging, page 30
  extracted_at: '2026-09-04'
---

**Two indicators on the driver board of this machine.**

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | Always on when the DC voltage is normal. Off means a fault. | Voltage is not correct; fuse is blown; transformer is no good | Check the supply voltage is **110 VAC or 230 VAC**; replace the fuse; replace the controller |
| LIMIT current | Over current protection warning light | Lights when the lower board detects over current | Protecting the lower board and the motor | Replace the controller; replace the motor; do not block the belt while running; smear silicone oil between the belt and the running board |

**The earlier ST725 manual for this machine family shows five LEDs** - POWER, LIMIT, UP, DOWN and SPEED - and gives current thresholds of 18 A on a 220 Vac machine and 28 A on a 120 Vac machine. This manual shows only the two above and gives no threshold. Read the board in front of you rather than either list.

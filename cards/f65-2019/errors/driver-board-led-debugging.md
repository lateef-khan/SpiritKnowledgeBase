---
id: f65-2019-driver-board-led-debugging
title: Controller indicator LED debugging
kind: spec
question: What do the LEDs on the lower controller of a Sole f65-2019 treadmill mean?
asked_as:
- what does the power led on the treadmill controller mean
- limit current light on my treadmill board
- controller lights on a sole treadmill
keywords:
- led
- power led
- limit current
- over current
- controller
- fuse
- transformer
- silicone oil
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2019
  applies_to:
  - f65-2019
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2019-e2-over-current
- f65-2019-lower-controller-replacement
source:
  ref: sole-tm-f65-2019-service-manual
  locator: Section 6.7, Controller Indicator LED debugging
  extracted_at: '2026-09-04'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110VAC or 230VAC. Replace fuse. Replace controller. |
| Limit current | Over current protection warning light | When the lower board detects over current, the LED will light. | Protection of lower board and motor. | Replace controller. Replace motor. Do not block belt running. Smear silicone oil between the belt and the running board. |

Section 6.6 places the **Limit current LED** and the **Power LED** on the driver board.

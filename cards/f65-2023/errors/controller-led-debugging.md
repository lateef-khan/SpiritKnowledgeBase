---
id: f65-2023-controller-led-debugging
title: Controller indicator LED debugging
kind: troubleshooting
question: What do the indicator LEDs on the controller of a Sole f65-2023 treadmill
  mean?
asked_as:
- what do the lights on the treadmill controller mean
- power led is off on the controller
- over current light on the treadmill board
keywords:
- controller led
- power led
- limit current
- over current protection
- fuse
- transformer
- silicone oil
- indicator light
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2023
  applies_to:
  - f65-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2023-e2-over-current
- f65-2023-error-code-list
source:
  ref: sole-tm-f65-2023-service-manual
  locator: Section 6.8 Controller Indicator LED debugging, page 18
  extracted_at: '2026-09-04'
---

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If the DC voltage is normal it is always ON. If it is off, a fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110VAC or 230VAC. Replace the fuse. Replace the controller. |
| Limit current | Over current protection warning light | The LED lights when the lower board detects over current. | Protection of the lower board and motor. | Replace the controller. Replace the motor. Do not block the belt running. Smear silicone oil between the belt and the running board. |

The over current warning light and the **E2** error code are the same protection acting.

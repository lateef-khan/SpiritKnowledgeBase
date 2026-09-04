---
id: f63-2019-controller-led-debugging
title: Reading the two indicator LEDs on the controller
kind: troubleshooting
question: What do the LEDs on the controller mean on a Sole F63-2019?
asked_as:
- what do the lights on the controller mean
- power led is off on my treadmill board
- limit current light on the controller
keywords:
- led
- power led
- limit current
- indicator
- controller
- fuse
- transformer
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2019
  applies_to:
  - f63-2019
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2019-e2-error-code
source:
  ref: sole-tm-f63-2019-service-manual
  locator: page 31, 6.7 Controller Indicator LED debugging
  extracted_at: '2026-09-04'
---

The driver board carries two indicator LEDs: a Power LED and a Limit current LED.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If the DC voltage is normal it is always ON. If it is off, a fault exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110VAC or 230VAC. Replace the fuse. Replace the controller. |
| Limit current | Over current protection warning light | When the lower board detects over current the LED lights. | Protection of the lower board and the motor. | Replace the controller. Replace the motor. Do not block the belt running. Smear silicone oil between the belt and the running board. |

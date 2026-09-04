---
id: f63-2026-controller-power-led
title: Reading the power LED on the controller
kind: troubleshooting
question: What does the LED on the controller mean on a Sole F63-2026?
asked_as:
- what does the light on the controller mean
- power led is off on my treadmill board
- controller light on my 2026 treadmill
keywords:
- led
- power led
- indicator
- controller
- fuse
- transformer
- dc voltage
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2026
  applies_to:
  - f63-2026
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2026-e05-error-code
- f63-2026-e06-error-code
source:
  ref: sole-tm-f63-2026-service-manual
  locator: pages 31 to 32, 5.5 and 5.6 Driver Board LED locations and debugging
  extracted_at: '2026-09-04'
---

This controller carries **one** indicator LED, a power directive LED. It lights when the treadmill is powered. The earlier F63 controller had a second Limit current LED; this one does not.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If the DC voltage is normal it is always ON. If it is off, a fault exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110VAC or 230VAC. Replace the fuse. Replace the controller. |

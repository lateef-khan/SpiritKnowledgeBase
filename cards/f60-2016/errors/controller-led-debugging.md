---
id: f60-2016-controller-led-debugging
title: Reading the three indicator LEDs on the controller
kind: troubleshooting
question: What do the LEDs on the controller mean on a Sole F60-2016?
asked_as:
- what do the lights on the controller mean
- power led is off on my treadmill board
- which led shows speed output
keywords:
- led1
- led2
- led3
- indicator
- communication led
- speed output
- power led
- controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f60-2016-e5-error-code
- f60-2016-e1-error-code
source:
  ref: sole-tm-f60-2016-service-manual
  locator: pages 30 to 31, 6.5 and 6.6 Driver Board LED Indicator Locations and debugging
  extracted_at: '2026-09-04'
---

The driver board carries three indicator LEDs.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| LED 1 | Communication directive LED | Flashes while a signal passes from the console to the lower controller | Flashing means communication is normal. Otherwise it is at fault | Check the main control wire and pins, whether broken or not inserted. Replace the console. Replace the controller. |
| LED 2 | Speed output | Flashes when START is pressed, in the normal state | Flashing means the speed signal output is normal. Otherwise it is at fault | Check the fast/slow wires of the 5-PIN connector. Replace the controller. Replace the console. |
| LED 3 | Controller power | Always ON if the DC voltage is normal. If it is off, a fault exists | Voltage is not correct. Fuse is blown. Transformer is no good | Check the supply voltage is 110V or 220V. Replace the fuse. Replace the controller. |

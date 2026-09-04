---
id: s77-2016-controller-led-debugging
title: Reading the indicator lights on the lower controller
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Sole S77-2016 treadmill?
asked_as:
- what do the lights on my treadmill controller mean
- s77 limit led is on
- power led on the driver board
keywords:
- led
- indicator
- power led
- limit led
- up
- down
- speed led
- driver board
- 18a
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2016
  applies_to:
  - s77-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- s77-2016-e2-over-current
- s77-2016-e1-no-rpm-signal
- s77-2016-speed-sensor-check
source:
  ref: sole-tm-s77-2016-service-manual
  locator: Section 6.7 Controller Indicator LED debugging, page 31
  extracted_at: '2026-09-04'
---

Five indicators on the driver board.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | Always on when the DC voltage is normal. Off means a fault. | Voltage is not correct; fuse is blown; transformer is no good | Check the supply is 220 Vac (110 Vac on a 120 Vac machine); replace the fuse; replace the controller |
| LIMIT | Limits DC motor current, shuts the controller down | Lights when the motor current passes **18 A** on a 220 Vac machine, or **28 A** on a 120 Vac machine. If the LIMIT light is bright for 3 to 5 seconds, the LIMIT LED turns on. | Loading too high on the belt; operation not correct, motor locked | Lubricate the belt and deck; check the mechanical drive system is not locked or jammed; replace the controller; replace the motor |
| UP | Incline motor motion up | Motion is up | Transistor was broken; relay failed | Replace the controller |
| DOWN | Incline motor motion down | Motion is down | Transistor was broken; relay failed | Replace the controller |
| SPEED | RPM sensor indicator | The speed sensor did not detect the signal completely | Check the gap between the speed sensor and the magnet | Keep the gap less than **3 mm** |

**The printed table says "the LCD will turn on" for the LIMIT current thresholds.** From the rest of the row, which describes the LIMIT LED lighting, read this as the LED.

The later ST728 manual for this machine family shows only two LEDs on its driver board, POWER and LIMIT, and gives no current thresholds.

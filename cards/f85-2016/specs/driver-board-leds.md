---
id: f85-2016-driver-board-leds
title: Driver board indicator lights and what they mean
kind: spec
question: What do the indicator LEDs on the driver board of a Sole F85-2016 treadmill
  mean?
asked_as:
- what are the lights on the treadmill controller
- limit light is on my treadmill board
- power led off on the controller
keywords:
- driver board
- indicator led
- power led
- limit led
- over current
- incline up light
- speed sensor light
- controller lights
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2016
  applies_to:
  - f85-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2016-e2-over-current
- f85-2016-speed-sensor-check
- f85-2016-lower-controller-replacement
source:
  ref: sole-tm-f85-2016-service-manual
  locator: section 6.7 Controller Indicator LED debugging, printed page 31
  extracted_at: '2026-09-04'
---

Five indicator LEDs sit on the driver board: POWER, LIMIT, UP (INC_UP), DOWN (INC_DW) and SPEED.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | On whenever the DC voltage is normal. Off means a fault. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 220Vac (on a 120Vac system it needs 110Vac). Replace the fuse. Replace the controller. |
| LIMIT | Limits the DC motor current and shuts the controller down | Lights when the motor current exceeds **18A** on a 220Vac system, or **28A** on a 120Vac system. If the light is bright for 3 to 5 seconds, the LIMIT LED latches on. | Loading is too high on the belt. Operation is not correct, motor lock. | Lubricate the belt and deck. Check the mechanical drive system is not locked or jammed. Replace the controller. Replace the motor. |
| UP | Motion of incline motor | Incline motor is moving up. | Transistor was broken. Relay failed. | Replace the controller. |
| DOWN | Motion of incline motor | Incline motor is moving down. | Transistor was broken. Relay failed. | Replace the controller. |
| SPEED | RPM sensor indicator | The speed sensor did not detect the signal completely. | Check the gap between the speed sensor and the magnet. | Keep the gap under 3 mm. |

**Source wording.** The LIMIT row says "the LCD will turn on" at both current thresholds. The row is about an LED on the driver board, not about the console LCD.

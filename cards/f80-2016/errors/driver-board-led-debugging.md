---
id: f80-2016-driver-board-led-debugging
title: Controller indicator LED debugging
kind: spec
question: What do the LEDs on the lower controller of a Sole f80-2016 treadmill mean?
asked_as:
- what does the limit led mean on my treadmill controller
- controller lights on a sole treadmill
- what current trips the treadmill controller
keywords:
- led
- power led
- limit
- 18a
- 28a
- inc_up
- inc_dw
- speed led
- controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2016
  applies_to:
  - f80-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2016-e2-over-current
- f80-2016-lower-controller-replacement
- f80-2016-speed-sensor-check
source:
  ref: sole-tm-f80-2016-service-manual
  locator: Section 6.7, Controller Indicator LED debugging
  extracted_at: '2026-09-04'
---

| Indicator LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If DC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 220Vac (on a 120Vac electronic power system it needs 110Vac). Replace fuse. Replace controller. |
| LIMIT | Limit the current of the DC motor. Controller shut down. | The LCD turns on when motor current exceeds **18A** on a 220Vac electronic power system, or **28A** on a 120Vac electronic system. If the LIMIT light is bright for 3 to 5 seconds, the LIMIT LED will turn on. | Loading is too high on the belt. Operation is not correct, motor lock. Motor lock makes the LIMIT light bright for 3 to 5 seconds first. | Belt/deck lubrication. Check the mechanical drive system is not locked or jammed. Replace controller. Replace motor. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| SPEED | RPM sensor indicator | The speed sensor didn't detect signal completely. | Check the gap between speed sensor and magnet. | Keep the gap-distance less than 3 mm. |

Section 6.6 places the **LIMIT, POWER, INC_UP, INC_DW and SPEED** LEDs on the driver board.

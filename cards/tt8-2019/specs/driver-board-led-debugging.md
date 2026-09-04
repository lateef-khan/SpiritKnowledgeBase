---
id: tt8-2019-driver-board-led-debugging
title: Reading the controller indicator LEDs
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Sole tt8-2019 treadmill?
asked_as:
- what does the limit light mean on my treadmill
- controller leds on the treadmill board
- power led is off on the controller
keywords:
- led
- power led
- limit led
- speed led
- inc_up
- inc_dw
- 18a
- 28a
- controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2019
  applies_to:
  - tt8-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- tt8-2019-e2-error-code
- tt8-2019-speed-sensor-check
source:
  ref: sole-tm-tt8-2019-service-manual
  locator: Section 6.7 Controller Indicator LED debugging, page 30
  extracted_at: '2026-09-04'
---

**DC model: TT8 2019 ST928-YT035, DC drive motor. The AC inverter TT8 2019 (ST928A-YT037) is a different machine and this card does not apply to it.**

The DC driver board carries five indicator LEDs: **POWER, LIMIT, INC_UP, INC_DW and SPEED**.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | Always on when DC voltage is normal. Off means a fault exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 220 Vac (110 Vac on a 120 Vac electronic power system). Replace the fuse. Replace the controller. |
| LIMIT | Limits DC motor current; the controller shuts down | Lights when motor current exceeds **18 A on a 220 Vac system**, or **28 A on a 120 Vac system**. If the LIMIT light is bright for 3 to 5 seconds, the LIMIT LED turns on. | Loading too high on the belt. Operation not correct, motor locked. | Belt/deck lubrication. Check the mechanical drive system is not locked or jammed. Replace the controller. Replace the motor. |
| UP | Motion of incline motor | Incline motor is going up | Transistor broken. Relay failed. | Replace the controller. |
| DOWN | Motion of incline motor | Incline motor is going down | Transistor broken. Relay failed. | Replace the controller. |
| SPEED | RPM sensor indicator | The speed sensor did not detect signal completely | Check the gap between speed sensor and magnet | Keep the gap under **3 mm**. |

The AC-inverter TT8 2019 (ST928A-YT037) has no equivalent table — its faults come out as inverter
codes instead.

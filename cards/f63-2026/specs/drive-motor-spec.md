---
id: f63-2026-drive-motor-spec
title: Brushless drive motor voltage and wiring
kind: spec
question: What are the drive motor specifications for a Sole F63-2026?
asked_as:
- what motor does my 2026 treadmill have
- which motor wire goes where on my sole
- is the 2026 treadmill motor brushless
keywords:
- brushless motor
- drive motor
- u v w
- hall sensor
- red black white
- 0-90 volt
- 0-180 volt
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2026
  applies_to:
  - f63-2026
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2026-e02-error-code
- f63-2026-e04-error-code
- f63-2026-drive-motor-replacement
source:
  ref: sole-tm-f63-2026-service-manual
  locator: pages 11 to 12 and 29, GENERAL INFORMATION and 5.3 Driver Board Wire Connections
  extracted_at: '2026-09-04'
---

**This is a brushless DC motor**, not the brushed motor with M+ and M- terminals used on earlier F63 machines. The controller drives it with **0 to 90 volts (or 0 to 180 volts)** to raise or lower the speed of the running belt.

**Three wire connection: red, black and white.**

| Wire | Terminal |
|---|---|
| Red | **U** |
| Black | **V** |
| White | **W** |

The higher the voltage, the faster the motor turns.

Speed feedback comes from a **Hall sensor on a 5-pin connection** to the controller, not from a reed switch and magnet.

**Note**: the general information section lists three motor wires and no ground, but the motor replacement procedure says to reconnect the ground wire along with W, U and V.

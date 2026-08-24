---
id: ctsbs900-le1-inverter-low-voltage
title: Error LE1 — inverter low voltage
kind: troubleshooting
question: What does error LE1 mean on a CTSBS900 and how do I fix it?
asked_as:
- console shows le1
- error le1 what does it mean
- le 1 error code
keywords:
- le1
- inverter low voltage
- mains voltage too low
- filter failure
- choke failure
facets:
  product_line: treadmill
  model: ctsbs900
  applies_to:
  - ctsbs900
  section: errors
  code: le1
authority: 3
not_to_be_confused_with:
- ctsbs900-lp-inverter-low-voltage-warning
- ctsbs900-ntcf-inverter-temperature-sensor-fault
see_also:
- ctsbs900-lp-inverter-low-voltage-warning
- ctsbs900-electrical-safety
- ctsbs900-electrical-requirements
- ctsbs900-troubleshooting-common-problems
source:
  ref: ctsbs900-om
  locator: p. 46
  extracted_at: '2026-08-24'
---

**LE1** is not the same as **LP** (inverter low voltage *warning* — a related but separate code, see [errors/lp-inverter-low-voltage-warning.md](lp-inverter-low-voltage-warning.md)) and is not **NTCF** (temperature sensor fault).

| Possible Cause | Corrective Action |
|---|---|
| Mains voltage too low | Check if mains voltage meets inverter requirement |
| Inverter failure | Replace inverter |
| Filter failure | Replace filter |
| Choke failure | Replace Choke |

Low incoming voltage can also cause the symptom described in [maintenance/troubleshooting-common-problems.md](../maintenance/troubleshooting-common-problems.md) ("only achieves ~7mph but shows higher on the display"). See [safety/electrical-safety.md](../safety/electrical-safety.md) for the 10% voltage-variance warning and [specs/electrical-requirements.md](../specs/electrical-requirements.md) for the required circuit.

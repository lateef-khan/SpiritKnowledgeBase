---
id: ct900-ol2-motor-overload-warning
title: Inverter warning oL2 - Motor overload
kind: troubleshooting
question: What does inverter warning oL2 mean on a CT900 and how do I fix it?
asked_as:
- what does ol2 mean on the inverter display
- motor overload warning
keywords:
- ol2
- motor overload warning
- kpc-cc01
- inverter warning
- over-torque detection
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: ol2
authority: 3
not_to_be_confused_with:
- ct900-e4-motor-overload
see_also:
- ct900-e4-motor-overload
source:
  ref: ct900-om
  locator: p. 46
  extracted_at: '2026-08-24'
---

**This is the inverter's oL2 warning code (warning #6), not the console's [E4 MOTOR OVERLOAD](e4-motor-overload.md) error code** - same concept, different code namespace; oL2 has a stated fix while E4 does not. Press RESET to clear any Warning Code.

**Corrective actions**:
1. Reduce the motor load.
2. Adjust the over-torque detection setting to an appropriate setting (Pr04-15 ~Pr04-17).
3. Clear the fault and then press RESET button.

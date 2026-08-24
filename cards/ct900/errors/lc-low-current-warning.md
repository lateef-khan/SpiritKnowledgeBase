---
id: ct900-lc-low-current-warning
title: Inverter warning LC - Low Current Warning
kind: troubleshooting
question: What does inverter warning LC mean on a CT900 and how do I fix it?
asked_as:
- what does lc mean on the inverter display
- low current warning
keywords:
- lc
- low current warning
- kpc-cc01
- inverter warning
facets:
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: lc
authority: 3
not_to_be_confused_with:
- ct900-e22-low-current
see_also:
- ct900-e22-low-current
source:
  ref: ct900-om
  locator: p. 47
  extracted_at: '2026-08-24'
---

**This is the inverter's LC warning code (warning #11), not the console's [E22 LOW CURRENT](e22-low-current.md) error code** - same concept, different code namespace; LC has a stated fix while E22 does not. Press RESET to clear any Warning Code.

**Corrective actions**:
1. Verify the wiring between the motor and the motor drive.
2. Verify the settings of Pr04-18 ~Pr04-20.

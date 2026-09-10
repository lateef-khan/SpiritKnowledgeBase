---
id: ce800ent-flywheel-and-induction-brake
title: Flywheel, induction brake and the resistance voltage wire
kind: spec
question: What is on the flywheel of a Spirit ce800ent elliptical, and where does
  the resistance voltage go?
asked_as:
- where is the induction brake on the ce800
- what wire changes resistance on the elliptical
- ce800ent flywheel parts
- resistance voltage wire elliptical
keywords:
- flywheel
- induction brake
- resistance voltage
- brake coil
- magnet
- resistance
- generator
- chi hua
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800ent
  applies_to:
  - ce800ent
  section: specs
  code: '*'
  model_number: '800054'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-unit-block-diagram
- ce800ent-electronic-parts-locations
- ce800ent-no-resistance
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: p. 23 (printed 23), section 6 'Flywheel definition function'
  extracted_at: '2026-09-08'
---

The page photographs the flywheel from the side and calls out two things:

- **Induction Brake** - the coil pack bolted to the bracket at the edge of the flywheel
- **Resistance Voltage** - the two-wire lead leaving that coil pack

Changing resistance means changing the voltage on that lead; the controller drives it, and the
block diagram on p. 16 runs **Controller (resistance control) -> Induction brake** with nothing in
between. The bracket carries a **CHI HUA** label reading K500054 / FB44H008 above a per-unit
serial.

The manual prints **no coil resistance, no voltage range and no level table** for this brake.

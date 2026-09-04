---
id: sole-e8-error
title: 'E8 error: controller EEPROM fault'
kind: troubleshooting
question: What does an E8 error mean on a Sole treadmill?
asked_as:
- e8 error on my treadmill
- what is error e8
keywords:
- e8
- e8 error
- eeprom
- controller
- recalibration
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - f63
  - f63-2013
  - f65
  - f80
  - f83
  - f85
  - f85-2020
  - f89
  - tt8
  - tt8-2020
  section: errors
  code: e8
authority: 3
not_to_be_confused_with: []
see_also:
- sole-install-motor-controller
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-console-error-code-list
  locator: DC digital controller table
  extracted_at: '2026-09-03'
---

**Meaning**: the motor controller EEPROM has failed.

Replace the controller. A new controller always needs a calibration afterwards.

**Scope.** This card is the fallback for the Sole treadmills that have no service manual in this knowledge base. Every machine listed in `applies_to` is one of those. A machine with a service manual has its own card for this code, or its manual shows the code does not exist on it — check the model's own cards first. AC inverter machines (ST90, TT9, the AC TT8 variants), the F63 2026 and the C80 use different code families and are deliberately excluded.

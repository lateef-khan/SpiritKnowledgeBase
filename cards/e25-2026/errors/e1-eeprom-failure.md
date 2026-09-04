---
id: e25-2026-e1-eeprom-failure
title: E1 EEPROM failure
kind: troubleshooting
question: What does error E1 mean on a Sole e25-2026 elliptical and how is it fixed?
asked_as:
- my sole elliptical says e1
- e1 on the display and nothing works
- what is error code e1 on an e25 2026
keywords:
- e1
- e-1
- eeprom
- error code
- display board pcb
- all windows off
- outputs stop
- elliptical
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2026
  applies_to:
  - e25-2026
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- e25-2026-e2-tension-motor-failure
- e25-2026-e3-ramp-error
see_also: []
source:
  ref: sole-elliptical-e25-2026-service-manual
  locator: 'Section 8.1, Error Message: E1, page 23'
  extracted_at: '2026-09-04'
---

**This is E1, not E2 (tension motor) and not E3 (incline VR).**

Definition: when the EEPROM is damaged or there is a problem with access, **all windows go OFF and all outputs STOP**. The **LEVEL Window displays "E1"**.

Troubleshooting: since the EEPROM is faulty, **replace the Display Board PCB directly**. The manual gives no other step for E1.

The error code list prints the meaning as "EEPROM failure".

**The repair named here changed.** The 2019 E25 manual answered E1 with "replace the upper controller"; this manual names the Display Board PCB.

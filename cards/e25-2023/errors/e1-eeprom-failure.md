---
id: e25-2023-e1-eeprom-failure
title: E1 EEPROM failure
kind: troubleshooting
question: What does error E1 mean on a Sole e25-2023 elliptical and how is it fixed?
asked_as:
- my sole elliptical says e1
- e-1 on the display and nothing works
- what is error code e1 on an e25
keywords:
- e1
- eeprom
- error code
- blank screen
- display board
- outputs stop
- console board
- elliptical
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2023
  applies_to:
  - e25-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- e25-2023-e2-gear-motor-failure
- e25-2023-e3-ramp-error
see_also: []
source:
  ref: sole-elliptical-e25-2023-service-manual
  locator: Error code list and section 8.1, pages 18-19
  extracted_at: '2026-09-04'
---

**This is E1, not E2 (gear motor) and not E3 (ramp / incline VR).**

Definition: when the EEPROM is damaged or there is a problem with access, **all windows turn off, all outputs stop, and the message window displays "E1"**.

Troubleshooting: the EEPROM is abnormal, **replace the Display Board directly**. The manual gives no other step for E1.

The error code list prints the meaning as "EEPROM failure".

**This differs from the 2019 E25 manual**, which tells you to replace the *upper controller* for the same code. This manual names the Display Board.

---
id: tt8-2023-e6-error-code
title: E6 lower controller component fault
kind: troubleshooting
question: What does error E6 mean on a Sole tt8-2023 treadmill?
asked_as:
- e6 error on my treadmill
- what is error code e6
- treadmill e6 controller
keywords:
- e6
- lower controller
- controller fault
- igbt
- transistor
- control module
- replace controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2023
  applies_to:
  - tt8-2023
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- tt8-2023-safety-key-message
- tt8-2023-e1-error-code
- tt8-2023-e2-error-code
- tt8-2023-e3-error-code
- tt8-2023-e4-error-code
- tt8-2023-e5-error-code
- tt8-2023-e7-error-code
see_also:
- tt8-2023-e4-error-code
- tt8-2023-controller-replacement
source:
  ref: sole-tm-tt8-2023-service-manual
  locator: Section 8.7, page 50 of 69
  extracted_at: '2026-09-04'
---

**TT8 2023 ST738-YT066, DC drive motor.**

**This is E6, not E5 (communication) and not E0/safety-key faults.**

Definition: the lower controller component is at fault.

Cause: a controller component has failed — transistor, IGBT, control module and so on.

| Part | Troubleshooting |
|---|---|
| Controller | Insert power wire of motor. |
| Display board | Only replace the upper control board. |

The printed troubleshooting for a failed controller component still lists "insert power wire of motor" as
the controller step; that is what the manual says, and it is the same wording used for E4.

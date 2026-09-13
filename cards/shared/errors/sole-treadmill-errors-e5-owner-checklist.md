---
id: sole-treadmill-errors-e5-owner-checklist
title: 'E5 communication error: owner''s checklist'
kind: troubleshooting
question: What should I check when a Sole treadmill shows E5?
asked_as:
- e5 communication error
- console controller not talking
- treadmill shows e5
keywords:
- e5
- communication error
- console controller
- connection
- disconnected
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  section: errors
  applies_to:
  - f80-2023
  - f85-2020
  - f85-2021
  - f85-2023
  - f89-2023
  - tt8-2021
  - tt8-2023
  code: e5
authority: 3
not_to_be_confused_with:
- sole-treadmill-errors-e1-owner-checklist
- sole-treadmill-errors-e2-owner-checklist
- sole-treadmill-errors-e3-owner-checklist
- sole-treadmill-errors-e4-owner-checklist
- sole-treadmill-errors-e6-owner-checklist
- sole-treadmill-errors-e7-owner-checklist
- f63-2026-e05-error-code
see_also:
- f65-2023-e5-communication-error
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-f80-2023-owners-manual
  locator: 'ERROR MESSAGES FOR DIGITAL-CONTROL SYSTEM TREADMILLS: sole-tm-f80-2023-owners-manual
    PDF p. 31 (printed 29); sole-tm-f85-2021-owners-manual PDF p. 33 (printed 31);
    sole-tm-f85-2023-owners-manual PDF p. 31; sole-tm-f89-2023-owners-manual PDF p.
    32; sole-tm-tt8-2021-owners-manual PDF p. 33 (printed 31); sole-tm-tt8-2023-owners-manual
    PDF p. 29 (printed 27)'
  extracted_at: '2026-09-12'
---

**This is the stencil-era owner's-manual E5 (communication error), not the 2026 E05 (undervoltage) and not Spirit's E5.**

The six owner's manuals print the same ERROR MESSAGES table with OK/NG checkboxes. The F80-2023, F85-2023 and F89-2023 prints read 'E1_'..'E7_' on the OCR layer — the render shows a plain code beside the checkbox column.

| ERROR | MEANING | POSSIBLE CAUSE |
|---|---|---|
| Console showing E5 | Communication disconnected between the console and the controller or communication error. | Check and make sure of proper connection between the console and the controller. |

The service manuals' deeper E5 procedure (console-controller link) is a separate card: see `f65-2023-e5-communication-error`.

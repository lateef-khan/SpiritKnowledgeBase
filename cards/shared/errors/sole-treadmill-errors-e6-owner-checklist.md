---
id: sole-treadmill-errors-e6-owner-checklist
title: 'E6 control board failure: owner''s checklist'
kind: troubleshooting
question: What should I check when a Sole treadmill shows E6?
asked_as:
- e6 control board failure
- treadmill shows e6
- change controller
keywords:
- e6
- control board failure
- controller
- igbt
- change controller
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
  code: e6
authority: 3
not_to_be_confused_with:
- sole-treadmill-errors-e1-owner-checklist
- sole-treadmill-errors-e2-owner-checklist
- sole-treadmill-errors-e3-owner-checklist
- sole-treadmill-errors-e4-owner-checklist
- sole-treadmill-errors-e5-owner-checklist
- sole-treadmill-errors-e7-owner-checklist
- f63-2026-e06-error-code
see_also:
- f65-2023-e6-lower-controller-fault
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

**This is the stencil-era owner's-manual E6 (control board failure), not the 2026 E06 and not Spirit's E6.**

The six owner's manuals print the same ERROR MESSAGES table with OK/NG checkboxes. The F80-2023, F85-2023 and F89-2023 prints read 'E1_'..'E7_' on the OCR layer — the render shows a plain code beside the checkbox column.

| ERROR | MEANING | POSSIBLE CAUSE |
|---|---|---|
| Console showing E6 | Control board failure | Controller component failure (e.g. IGBT). Change controller. |

The service manuals' deeper E6 procedure (lower-controller components) is a separate card: see `f65-2023-e6-lower-controller-fault`.

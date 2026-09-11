---
id: spirit-xt-errors-e6-lower-controller-component-fault
title: 'E6: a component on the lower controller has failed'
kind: troubleshooting
question: What does E6 mean on a Spirit XT 2015, XT 2023 or XT ENT treadmill, and
  what does the service manual say to check?
asked_as:
- what does e6 mean on my spirit treadmill
- treadmill shows e6
- lower controller fault e6
keywords:
- e6
- lower controller
- transistor
- igbt
- control module
- controller fault
- display board
- error code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e6-drive-ovrload
- ct900-e6-external-fault
- f65-2023-e6-lower-controller-fault
- spirit-2024-errors-e6-driver-board-defective
see_also:
- spirit-xt-errors-error-code-list-eight-codes
- f65-2023-e6-lower-controller-fault
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: 'XT185 2023 service manual 8.7 Error Message: E6, PDF p. 30, text.md lines
    616-636; XT285 2023 service manual 8.7 Error Message: E6, PDF p. 31, text.md lines
    618-638; XT385 2023 service manual 8.7 Error Message: E6, PDF p. 32, text.md lines
    559-576; XT485 2023 service manual 8.7 Error Message: E6, PDF p. 32, text.md lines
    559-576; XT685 2023 service manual 8.7 Error Message: E6, PDF p. 31, text.md lines
    621-641; XT185 2015 service manual Error Message: E6, PDF p. 55, text.md lines
    1005-1039; XT285 2015 service manual Error Message: E6, PDF p. 56 (printed 55),
    text.md lines 1075-1109; XT385 2015 service manual Error Message: E6, PDF p. 56,
    text.md lines 856-875; XT485 2015 service manual Error Message: E6, PDF p. 56,
    text.md lines 859-878; XT485ENT 2023 service manual 8.7 Error Message: E6, PDF
    p. 52, text.md lines 774-793; XT685ENT 2023 service manual 8.7 Error Message:
    E6, PDF p. 36, text.md lines 602-623'
  extracted_at: '2026-09-11'
---

**This is the XT E6 - not E6 on a Spirit 7.0T or MT200, which is a drive overload (`70t-2026-errors-e6-drive-ovrload`), not the CT900's E6 external fault, and not Sole's E6 (`f65-2023-e6-lower-controller-fault`), which is the same Dyaco text filed for Sole machines.**

Definition: *The lower controller component is fault.* Cause: *The controller component is fault, like Transistor, IGBT, control module... etc.*

| Part | Troubleshooting |
|---|---|
| Controller | Insert power wire of motor. |
| Display board | Only Replace upper control board. |

That is the whole table in all eleven XT service manuals, and it does not say to replace the controller whose component it has just condemned. Read the definition as the diagnosis and the table as what the book prints; a failed transistor, IGBT or control module is a controller replacement in practice, but the book does not write that sentence.

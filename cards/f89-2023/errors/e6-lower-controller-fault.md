---
id: f89-2023-e6-lower-controller-fault
title: 'E6 error: lower controller component fault'
kind: troubleshooting
question: What does an E6 error mean on a Sole f89-2023 treadmill?
asked_as:
- e6 error on my treadmill
- treadmill throwing e6
- controller fault code on treadmill
keywords:
- e6
- e6 error
- lower controller
- igbt
- transistor
- control module
- upper control board
facets:
  brand:
  - sole
  product_line: treadmill
  model: f89-2023
  applies_to:
  - f89-2023
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- f89-2023-e5-communication-error
- ct900-e6-external-fault
- ct900-e16-eeprom-rd-err
see_also:
- f89-2023-error-code-list
- sole-e6-error
source:
  ref: sole-tm-f89-2023-service-manual
  locator: 'Section 8.7 Error Message: E6, page 46'
  extracted_at: '2026-09-04'
---

**This is E6, a failed component inside the lower controller. It is not E5 (communication between the
console and the controller).**

**Definition.** The lower controller component is at fault.

**Cause.** A controller component such as a transistor, an IGBT or a control module has failed.

| Part | Troubleshooting |
|---|---|
| Controller | Insert power wire of motor. |
| Display board | Only replace the upper control board. |

**As printed.** The controller row repeats the E4 instruction, "Insert power wire of motor", even though the
definition says a component inside the controller has failed. The manual gives no other controller step for E6.

---
id: f85-2021-e5-communication-error
title: 'E5: the console and the lower controller are not talking'
kind: troubleshooting
question: What does E5 mean on a Sole F85-2021 treadmill and how do I fix it?
asked_as:
- e5 error on my treadmill
- console not communicating with the controller
- treadmill display says e5
keywords:
- e5
- communication error
- main control wire
- console board
- lower controller
- error code
- pinched cable
- six pin
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2021
  applies_to:
  - f85-2021
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- f85-2021-e0-safety-key-message
- f85-2021-e1-no-rpm-signal
- f85-2021-e2-over-current
- f85-2021-e3-incline-vr-error
- f85-2021-e4-motor-power-wire-error
- f85-2021-e6-lower-controller-error
- f85-2021-e7-input-power-error
see_also:
- f85-2021-e6-lower-controller-error
- sole-e5-error
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: 'section 8.6 Error Message: E5, printed pages 63 to 64'
  extracted_at: '2026-09-04'
---

**This is E5, not E6 (lower controller fault) and not E4 (motor power wire).**

| Field | Value |
|---|---|
| Code | E5 |
| Cause, as printed | Communication signal error. |
| Definition | Poor communication between the console and lower controller. Almost always the main control wire, but it can also be the console board or the lower controller. |

| Part | What to do |
|---|---|
| Lower controller board | Replace main control wire. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Note on the source.** The first row of that table pairs the part "Lower controller board" with the action "Replace main control wire". That is how the manual prints it; the action does not match the part.

**This machine has two console generations**, Android 6 and Android 10, with different display boards. Confirm which console is fitted before ordering an upper control board.

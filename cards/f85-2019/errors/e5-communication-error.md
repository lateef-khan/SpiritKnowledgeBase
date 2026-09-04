---
id: f85-2019-e5-communication-error
title: 'E5: the console and the lower controller are not talking'
kind: troubleshooting
question: What does E5 mean on a Sole F85-2019 treadmill and how do I fix it?
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
  model: f85-2019
  applies_to:
  - f85-2019
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- f85-2019-e0-safety-key-error
- f85-2019-e1-no-rpm-signal
- f85-2019-e2-over-current
- f85-2019-e3-incline-vr-error
- f85-2019-e4-motor-power-wire-error
- f85-2019-e6-lower-controller-error
- f85-2019-e7-input-power-error
see_also:
- f85-2019-e6-lower-controller-error
- f85-2019-main-control-cable-pinout
- sole-e5-error
source:
  ref: sole-tm-f85-2019-service-manual
  locator: 'section 8.5 Error Message: E5, printed page 72'
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

The main control wire is the **6 pin cable into JK90** on the driver board. Its data pins are TXD and RXT.

**Note on the source.** The first row of that table pairs the part "Lower controller board" with the action "Replace main control wire". That is how the manual prints it; the action does not match the part.

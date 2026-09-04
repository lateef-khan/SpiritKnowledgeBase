---
id: f85-2023-e5-communication-error
title: 'E5 error: console and controller communication'
kind: troubleshooting
question: What does an E5 error mean on a Sole f85-2023 treadmill?
asked_as:
- e5 error on my treadmill
- console not talking to the controller
- communication error on treadmill
keywords:
- e5
- e5 error
- communication
- main control wire
- computer cable
- display board
- lower controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2023
  applies_to:
  - f85-2023
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- f85-2023-e6-lower-controller-fault
- f85-2023-e4-motor-power-wire
- ct900-e5-thermal-overload
see_also:
- f85-2023-error-code-list
- sole-e5-error
source:
  ref: sole-tm-f85-2023-service-manual
  locator: 'Section 8.6 Error Message: E5, page 45'
  extracted_at: '2026-09-04'
---

**This is E5, the communication fault. It is not E6 (a failed component inside the lower controller).**

**Definition.** The communication between the console and the controller is poor. It may be due to a faulty main
control wire, but the display board or the controller may also be malfunctioning.

**Cause.** The main control wire is possibly broken, but E5 can also come from a component of the controller or
the console.

| Part | Troubleshooting |
|---|---|
| Lower controller board | Replace main control wire. |
| Main control wires | Reinsert or replace the main control wire. |
| Display board | Replace the display board. |

**As printed.** The row headed "Lower controller board" says to replace the main control wire, not the board. That
is what the manual prints; it is repeated on the main control wire row below it.

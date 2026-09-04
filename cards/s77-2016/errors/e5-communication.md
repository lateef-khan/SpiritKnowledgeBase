---
id: s77-2016-e5-communication
title: 'E5: the console and the lower controller are not talking'
kind: troubleshooting
question: What does E5 mean on a Sole S77-2016 treadmill?
asked_as:
- e5 error on my treadmill
- communication error on my s77
- console not talking to the controller
keywords:
- e5
- communication
- main control wire
- 6 pin
- console board
- lower controller
- reseat
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2016
  applies_to:
  - s77-2016
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- s77-2016-e0-safety-key
- s77-2016-e1-no-rpm-signal
- s77-2016-e2-over-current
- s77-2016-e3-incline-vr
see_also:
- s77-2016-e1-no-rpm-signal
- s77-2016-lower-controller-replacement
- sole-e5-error
source:
  ref: sole-tm-s77-2016-service-manual
  locator: 'Section 8.5 Error Message: E5, page 55'
  extracted_at: '2026-09-04'
---

**This is E5, not E4 (motor power wire) and not E6 (lower controller fault).**

**Meaning**: poor communication between the console and the lower controller. It is almost always the **main control wire**, but a fault on the console board or in the lower controller gives the same code.

| Part | What to do |
|---|---|
| Lower controller board | Replace the main control wire |
| Main control wires | Reseat the main control wire; replace it |
| Display board | Replace the upper control board |

The speed signal travels on the TX/RX pair of the **6-pin main wire**, which is the same cable, so an E5 and an E1 can have one cause.

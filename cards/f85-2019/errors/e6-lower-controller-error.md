---
id: f85-2019-e6-lower-controller-error
title: 'E6: a part inside the lower controller has failed'
kind: troubleshooting
question: What does E6 mean on a Sole F85-2019 treadmill and how do I fix it?
asked_as:
- e6 error on my treadmill
- treadmill throwing e6
- lower controller error on the display
keywords:
- e6
- lower controller
- igbt
- transistor
- control module
- motor controller
- error code
- board failure
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- f85-2019-e0-safety-key-error
- f85-2019-e1-no-rpm-signal
- f85-2019-e2-over-current
- f85-2019-e3-incline-vr-error
- f85-2019-e4-motor-power-wire-error
- f85-2019-e5-communication-error
- f85-2019-e7-input-power-error
see_also:
- f85-2019-e5-communication-error
- f85-2019-lower-controller-replacement
- sole-e6-error
source:
  ref: sole-tm-f85-2019-service-manual
  locator: 'section 8.6 Error Message: E6, printed page 73'
  extracted_at: '2026-09-04'
---

**This is E6, not E5 (communication) and not E0 (safety key).**

| Field | Value |
|---|---|
| Code | E6 |
| Cause, as printed | Lower controller error. |
| Definition | The lower controller component is fault. |
| Cause of E6 | A component of the lower controller has failed, such as a transistor, an IGBT or a control module. |

| Part | What to do |
|---|---|
| Lower controller | Replace the lower controller board. |
| Display board | Only replace the upper control board. |

The 2016 manual for the earlier machine prints "Insert power wire of motor" in the lower controller row here, which is the E4 action. This manual prints the action that matches the fault.

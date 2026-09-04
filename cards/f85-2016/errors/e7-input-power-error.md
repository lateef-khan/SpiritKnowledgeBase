---
id: f85-2016-e7-input-power-error
title: 'E7: the incoming mains supply is wrong or unstable'
kind: troubleshooting
question: What does E7 mean on a Sole F85-2016 treadmill and how do I fix it?
asked_as:
- e7 error on my treadmill
- treadmill shows e7 on a power strip
- input power error on the console
keywords:
- e7
- input power
- wall outlet
- unstable voltage
- multimeter
- lower controller
- error code
- brownout
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2016
  applies_to:
  - f85-2016
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- f85-2016-e0-safety-key-error
- f85-2016-e1-no-rpm-signal
- f85-2016-e2-over-current
- f85-2016-e3-incline-vr-error
- f85-2016-e4-motor-power-wire-error
- f85-2016-e5-communication-error
- f85-2016-e6-lower-controller-error
see_also:
- f85-2016-electrical-requirements
- sole-e7-error
source:
  ref: sole-tm-f85-2016-service-manual
  locator: 'section 8.7 Error Message: E7, printed page 57'
  extracted_at: '2026-09-04'
---

**This is E7, not E1 (no RPM signal) and not E2 (over current).**

| Field | Value |
|---|---|
| Code | E7 |
| Cause, as printed | Input power error. |
| Definition | Input power anomaly, possibly too low or too high or unstable. |
| Cause of E7 | The wall outlet is unstable, so the treadmill's working power is not stable. The power section of the lower controller board may also be broken. |

| Part | What to do |
|---|---|
| Wall outlet | Set the multimeter to AC 1000V and check whether the outlet reads 110VAC or 220VAC, and whether the voltage is stable. |
| Lower controller board | Replace the lower controller board. |

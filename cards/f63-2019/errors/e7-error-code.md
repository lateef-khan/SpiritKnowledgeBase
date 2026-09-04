---
id: f63-2019-e7-error-code
title: 'E7 error: input power anomaly'
kind: troubleshooting
question: What does an E7 error mean on a Sole F63-2019?
asked_as:
- e7 error on my treadmill
- treadmill shows e7 on a power strip
- what is error e7 on my sole
keywords:
- e7
- e7 error
- input power
- wall outlet
- unstable voltage
- multi-meter
- lower controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2019
  applies_to:
  - f63-2019
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- f63-2019-e0-error-code
- f63-2019-e1-error-code
- f63-2019-e2-error-code
- f63-2019-e3-error-code
- f63-2019-e4-error-code
- f63-2019-e5-error-code
- f63-2019-e6-error-code
see_also:
- f63-2019-error-code-list
- f63-2019-power-outlet-requirements
source:
  ref: sole-tm-f63-2019-service-manual
  locator: page 56, 8.7 Error Message E7
  extracted_at: '2026-09-04'
---

**This is E7, not E1 and not E0.**

**Definition**: input power anomaly, possibly too low, too high or unstable.

**Cause**: the wall outlet may be unstable, so the working power of the treadmill is not stable. The other possibility is that the power part of the lower controller board is broken.

| Part | Troubleshooting |
|---|---|
| Wall outlet | Set the multi-meter to AC 1000V and check whether the outlet is 110VAC or 220VAC, and whether the voltage is stable. |
| Lower controller board | Replace the lower controller board. |

The power path drawn with this error is: wall outlet, overload protection, power switch, lower controller. A CE unit or a 220V unit also has the filter and choke in that path.

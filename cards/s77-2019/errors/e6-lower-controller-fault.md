---
id: s77-2019-e6-lower-controller-fault
title: 'E6: a component inside the lower controller has failed'
kind: troubleshooting
question: What does E6 mean on a Sole S77-2019 treadmill?
asked_as:
- e6 error on my treadmill
- s77 throwing e6
- lower controller error on my treadmill
keywords:
- e6
- lower controller
- transistor
- igbt
- control module
- component failure
- replace controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- s77-2019-e0-safety-key
- s77-2019-e1-no-rpm-signal
- s77-2019-e2-over-current
- s77-2019-e3-incline-vr
see_also:
- s77-2019-lower-controller-replacement
- s77-2019-calibration-procedure
- sole-e6-error
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Section 8.6 Error Message: E6, page 55'
  extracted_at: '2026-09-04'
---

**This is E6, not E5 (communication) and not E0 (safety key).**

**Meaning**: a component inside the lower controller is at fault - the manual names the transistor, the IGBT and the control module.

| Part | What to do |
|---|---|
| Lower controller | **Replace the lower controller board** |
| Display board | Only replace the upper control board |

**Calibrate after fitting a new lower controller.**

The earlier ST725 manual for this machine family prints "Insert power wire of motor" in this row, which is the E4 remedy and does not match the fault. This manual corrects it.

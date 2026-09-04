---
id: s77-2019-e7-input-power
title: 'E7: the incoming supply is out of range'
kind: troubleshooting
question: What does E7 mean on a Sole S77-2019 treadmill?
asked_as:
- e7 error on my treadmill
- input power error on my s77
- treadmill shows e7 on a power strip
keywords:
- e7
- input power
- wall outlet
- unstable voltage
- multimeter
- lower controller
- supply
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- s77-2019-e0-safety-key
- s77-2019-e1-no-rpm-signal
- s77-2019-e2-over-current
- s77-2019-e3-incline-vr
see_also:
- s77-2019-power-outlet-requirements
- sole-voltage-test
- sole-e7-error
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Section 8.7 Error Message: E7, page 56'
  extracted_at: '2026-09-04'
---

**This is E7, not E4 (motor power wire) and not E2 (over current).**

**Meaning**: input power anomaly - too low, too high, or unstable. The wall outlet may be unstable, or the power section of the lower controller board may be broken.

| Part | What to do |
|---|---|
| Wall outlet | Set a multimeter to **AC 1000V** and check whether the outlet reads 110 VAC or 220 VAC, and whether the voltage is stable |
| Lower controller board | Replace the lower controller board |

The manual's safety section forbids a GFCI outlet on this machine and asks for a dedicated grounded circuit; both are common causes of an unstable reading.

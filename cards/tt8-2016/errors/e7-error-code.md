---
id: tt8-2016-e7-error-code
title: E7 input power out of range
kind: troubleshooting
question: What does error E7 mean on a Sole tt8-2016 treadmill?
asked_as:
- e7 error code on treadmill
- treadmill shows e7 power
- what does e7 mean
keywords:
- e7
- input power
- wall outlet
- unstable voltage
- low voltage
- high voltage
- lower controller
- multimeter
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016
  applies_to:
  - tt8-2016
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- tt8-2016-e0-error-code
- tt8-2016-e1-error-code
- tt8-2016-e2-error-code
- tt8-2016-e3-error-code
- tt8-2016-e4-error-code
- tt8-2016-e5-error-code
- tt8-2016-e6-error-code
see_also:
- tt8-2016-electrical-power-requirements
- tt8-2016-error-code-list
source:
  ref: sole-tm-tt8-2016-service-manual
  locator: Section 8.7, page 58
  extracted_at: '2026-09-04'
---

**DC model: TT8 2016 ST925-YT021, DC drive motor. The AC inverter TT8 2016 (ST925A-YT030) is a different machine and this card does not apply to it.**

**This is E7, not E1 (no RPM signal) and not E2 (over current).**

Definition: input power anomaly — possibly too low, too high or unstable.

Cause: the wall outlet may be unstable, so the treadmill's working power is not stable. The other
possibility is that the power section of the lower controller board is broken.

| Part | Troubleshooting |
|---|---|
| Wall outlet | Set the multi-meter to AC 1000 V and check whether the outlet reads 110 VAC or 220 VAC, and whether the voltage is stable. |
| Lower controller board | Replace the lower controller board. |

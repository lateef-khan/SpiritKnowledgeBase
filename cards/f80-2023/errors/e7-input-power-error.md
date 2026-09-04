---
id: f80-2023-e7-input-power-error
title: 'E7 error: input power anomaly'
kind: troubleshooting
question: What does an E7 error mean on a Sole f80-2023 treadmill?
asked_as:
- e7 error on my treadmill
- treadmill shows e7 on a power strip
- input power error on treadmill
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
  model: f80-2023
  applies_to:
  - f80-2023
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- f80-2023-e6-lower-controller-fault
- f80-2023-e4-motor-power-wire
- ct900-e7-eeprom-wr-err
- ct900-e17-ext-base-block
see_also:
- f80-2023-error-code-list
- f80-2023-electrical-power-requirements
- sole-e7-error
- sole-voltage-test
source:
  ref: sole-tm-f80-2023-service-manual
  locator: 'Section 8.8 Error Message: E7, page 46'
  extracted_at: '2026-09-04'
---

**This is E7, the input power fault. It is not E4 (motor power wire) and not E6 (a failed lower
controller component).**

**Definition.** Input power anomaly, possibly too low, too high or unstable.

**Cause.** The wall outlet may be unstable, so the treadmill's working power is not stable. The power section of
the lower controller board may also be broken.

| Part | Troubleshooting |
|---|---|
| Wall outlet | Set a multi-meter to AC 1000V and check whether the wall outlet reads 110VAC or 220VAC, and whether that voltage is stable. |
| Controller | Replace the lower controller board. |

**Two figures are in circulation.** This manual names 110VAC or 220VAC at the outlet. The company-wide E7 card,
written from support notes, tells a technician to expect about 120V AC all the way to the motor controller.
Establish which supply the machine is on before judging a reading.

---
id: s77-2019-e4-motor-power-wire
title: 'E4: the drive motor power wire'
kind: troubleshooting
question: What does E4 mean on a Sole S77-2019 treadmill?
asked_as:
- e4 error on my treadmill
- s77 shows e4 and stops
- motor wire error on my treadmill
keywords:
- e4
- motor power wire
- lower controller
- m plus
- m minus
- replace motor
- display board
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e4
authority: 3
not_to_be_confused_with:
- s77-2019-e0-safety-key
- s77-2019-e1-no-rpm-signal
- s77-2019-e2-over-current
- s77-2019-e3-incline-vr
see_also:
- s77-2019-drive-motor-spec
- s77-2019-motor-replacement
- sole-e4-error
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Section 8.4 Error Message: E4, page 53'
  extracted_at: '2026-09-04'
---

**This is E4, not E5 (communication) and not E7 (input power).**

**Meaning**: motor power wire error. The manual's stated cause is that **the power wire of the motor is not inserted into the lower controller**.

| Part | What to do |
|---|---|
| Lower controller | Insert the power wire of the motor, **or replace the lower controller board** |
| Motor | Replace the motor |
| Display board | Replace the upper control board |

The motor runs on three wires: **red into M+, black into M-, green is ground**. Check the M+ and M- terminals at the lower controller first.

The earlier ST725 manual for this machine family gives the lower controller row as "Insert power wire of motor" only, with no option to replace the board.

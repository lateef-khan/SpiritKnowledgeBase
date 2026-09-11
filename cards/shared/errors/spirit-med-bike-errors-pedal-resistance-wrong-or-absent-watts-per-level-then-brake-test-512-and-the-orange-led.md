---
id: spirit-med-bike-errors-pedal-resistance-wrong-or-absent-watts-per-level-then-brake-test-512-and-the-orange-led
title: Pedal resistance that feels wrong is the watts-per-level setting, defaulting
  to 5 watts per level; no resistance at all is the brake coil cable, then a Brake
  Test at 512 watching the orange LED on the control board
kind: troubleshooting
question: What do I check when the pedal resistance on a Spirit Medical 7.0R or 7.0U
  bike feels too hard, too easy or is missing altogether?
asked_as:
- 7.0r pedals feel harder than before
- no resistance on my rehab bike
- watts per level setting 7.0u
- brake test 512 spirit medical bike
keywords:
- pedal resistance
- no resistance
- watts per level
- 5 watts
- brake test
- '512'
- orange led
- brake coil
- control board
- rehabilitation bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode
- spirit-med-stepper-errors-one-pedal-has-no-resistance-drive-cable
see_also:
- spirit-med-bike-errors-symmetry-incorrect-unit-type-sensor-test-crank-calibration
source:
  ref: spirit-bike-70r-2025-service-manual
  locator: '7.0R (MR490-SB018-03) service manual 5.2.4 Troubleshooting, 5. Pedal Resistance
    Problem, PDF p. 13-14, text.md lines 158-187, and 5.2.1 ix Brake Test, PDF p.
    8, lines 92-120. 7.0U (MU470-SB018) service manual 5.2.4, 5., PDF p. 13-14, text.md
    lines 209-234. Owner''s manual row: ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48
    (printed 46); text.md lines 1328-1377; 7.0U 2025 owner''s manual ERROR MESSAGE
    & TROUBLESHOOTING, PDF p. 46 (printed 44); text.md lines 1285-1329; Dyaco MED
    7.0R 2021 owner''s manual (Rev. 1.2.1) Error messages and Troubleshooting, PDF
    p. 84-85; text.md lines 2642-2730'
  extracted_at: '2026-09-11'
---

Two symptoms, two answers, printed together.

## Resistance feels different - the setting

The owner's manuals:

> **Pedal resistance seems harder/different than before**
> Check the watts per level setting in the Set Up menu. **The default setting from the factory is 5 watts per level.**

The service manuals say the same in one line: *Resistance too strong/weak - Check the resistance/level setting in the SETUP.* A level on this bike is a watt step, so a facility that has set 10 watts per level has doubled every level; the Dyaco MED 2021 edition points to its page 22 for the menu.

## No resistance at all - the brake

The service manuals only:

> ii. **No any resistance**
> 1. Open the cover and make sure the cable that connect control board and coil on the brake are plugging properly at both ends. Go to next step if the connection was good.
> 2. Run the **Brake Test** in Maintenance mode and set to **maximum resistance (512)**. **Replace the control board if the orange LED on the control board didn't light.**

**The orange LED is the test.** The Brake Test drives the induction brake one bit at a time up to 512, and the Maintenance Mode page warns *don't stay in high level (more than 400) for too long*. At 512 the control board should be pushing full current into the coil and its orange LED lit; dark at 512 with the coil cable good means the board is not driving the brake. The book stops there - it does not say what a lit LED with no resistance means, and it never names the coil or the brake as a replacement part on this page.

The 7.0S/7.5S steppers answer a missing resistance with the `Motor Error` message and a motor-armature ohm reading instead (`spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode`) - a different mechanism, do not carry it here.


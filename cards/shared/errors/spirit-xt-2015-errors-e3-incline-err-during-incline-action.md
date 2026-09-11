---
id: spirit-xt-2015-errors-e3-incline-err-during-incline-action
title: E3 or INCLINE ERR raised because the VR reading does not change while the incline
  is being driven
kind: troubleshooting
question: What does E3 / INCLINE ERR mean when I press the incline keys on a Spirit
  XT 2015 treadmill?
asked_as:
- e3 when i press incline up on my spirit treadmill
- incline does not move and shows e3
- incline err on the xt
keywords:
- e3
- incline err
- vr value
- up down keys
- incline motor
- incline cable
- lower control board
- stuck
- gears cracked
- recalibrate
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt285-2015
  - xt385-2015
  - xt485-2015
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- xt485ent-2023-errors-e3-incline-err-during-incline-action
- ct850-2016-incline-err-during-incline-action
- ct850-2020-incline-err
see_also:
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
- spirit-xt-2015-errors-incline-window-shows-e3-power-cycle-then-calibrate
- spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate
source:
  ref: spirit-treadmill-xt485-2015-service-manual
  locator: 'XT185 2015 service manual Error Message: E3 / INCLINE ERR, PDF p. 50-52,
    text.md lines 876-929; XT285 2015 service manual Error Message: E3 / INCLINE ERR,
    PDF p. 51-53 (printed 50-52), text.md lines 945-999; XT385 2015 service manual
    Error Message: E3 / INCLINE ERR, PDF p. 51-53, text.md lines 776-820; XT485 2015
    service manual Error Message: E3 / INCLINE ERR, PDF p. 51-53, text.md lines 780-823'
  extracted_at: '2026-09-11'
---

**The 2015 XT service manuals define E3 twice, and this is the second definition.** The first, on `spirit-xt-2015-errors-e3-incline-vr-out-of-range`, is the reading being out of range at power on. This one is the reading not *changing* while the incline is driven, and the section is headed `Error Message: E3 / INCLINE ERR`.

Definition: *During incline action, the display board CPU cannot read the VR value, so E3 appears.*

Cause of INCLINE E3: *Press the incline UP/DOWN key. The incline doesn't operate. E3 appears on the display.* Explanation: *When press incline key, the display board CPU reads the incline VR value. If there is no VR value change to the CPU, the incline is not operating, and then appear E3 appears on the display.*

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline keys, see the display whether a value appears or not. If no values, check whether keys are stuck, or replace upper control board. |
| Incline cable | 1. Inspect whether the incline power wire and incline VR cable is connected well. |
| Driver board | 1. View the lower control board whether it has components of the incline part with obvious and serious damage. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Recalibrate the incline set. |

The action flow chart on the page between them, a picture read from the render, checks in order: display board - does pressing UP or DOWN act? driver board - during the UP action does the UP LED light and the incline voltage increase, and in the DOWN action does the DOWN LED light and the voltage decrease? incline motor - does the incline rise with the UP LED and lower with the DOWN LED? Any *no* shows the E3 / INCLINE ERR message; all *yes* means no error message.

The XT485ENT prints this same second definition with a five-row table (`xt485ent-2023-errors-e3-incline-err-during-incline-action`). **The 2023 XT books print only the first definition**; the matrix row those books keep for `INCLINE ERR, INCLINE window displays E3` is on `spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate`.

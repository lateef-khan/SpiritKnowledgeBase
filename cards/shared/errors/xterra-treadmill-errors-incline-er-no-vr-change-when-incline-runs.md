---
id: xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs
title: 'INCLINE ER: the UP or DOWN key lights the driver board LED but the VR value
  does not change, so the console decides the incline is not moving'
kind: troubleshooting
question: What does INCLINE ER mean on an Xterra tr260-2023 or trx2500-2024 treadmill,
  and what should I check?
asked_as:
- incline er on my xterra treadmill
- incline does not move and shows er
- incline er up led lights but no movement
keywords:
- incline er
- incline
- vr value
- up led
- down led
- driver board
- 5-pin cable
- incline motor stuck
- gears cracked
- re-calibrate
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr260-2023
  - trx2500-2024
  section: errors
  code: incline-er
authority: 3
not_to_be_confused_with:
- xterra-trx-errors-incline-err-no-vr-change-when-incline-runs
- trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs
- trx5500-2024-errors-incline-e3-no-vr-change-when-incline-runs
- f60-2016-incline-er-message
see_also:
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- trx2500-2024-errors-er-incline-vr-out-of-range
- xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
- xterra-treadmill-errors-incline-buttons-not-working-incline-cable-six-checks
- spirit-xt-2015-errors-e3-incline-err-during-incline-action
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM Error Message: INCLINE ER, Cause of INCLINE ER and Troubleshooting,
    PDF pp. 50-52 (printed 49-51); text.md lines 846-897; TR260 SM 8-6, the INCLINE
    ER description and action flow chart, PDF p. 42; text.md lines 639-652'
  extracted_at: '2026-09-11'
---

**This is INCLINE ER, the error raised while the incline is being driven** - the second half of the incline sections in the TR260 and TRX2500 books. The TRX3500/TRX4500 print it INCLINE ERR, the TRX1400 INCLINE Err and the TRX5500 INCLINE E3. The error raised at power-on, before any key is pressed, is E3 / ER (`xterra-treadmill-errors-e3-incline-vr-out-of-range`, `trx2500-2024-errors-er-incline-vr-out-of-range`).

*Definition.* During incline action, the display board CPU cannot read the VR value, so INCLINE ER appears.

*Cause.* Press the incline UP/DOWN key; the incline doesn't operate; INCLINE ER appears. *Explanation:* pressing the incline UP or DOWN key lights the driver board's UP or DOWN indicator; the incline operates, moving the VR, which changes the VR value; the display board CPU reads the incline VR value. If there is no VR value change, to the CPU the incline is not operating when it should be, and INCLINE ER appears. The action flow chart walks: press incline UP or DOWN -> driver board UP LED lights, incline voltage increases? -> DOWN LED lights, incline voltage decreases? -> incline motor: UP LED lights, incline rises? DOWN LED lights, incline lowers? -> no error message, or show INCLINE ERR message.

*Troubleshooting (TRX2500)*

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press the incline UP key: the driver board UP LED lights. 2. Press the incline DOWN key: the driver board DOWN LED lights. 3. If not as above, inspect the cable and connections |
| 5-pin cable | 1. Inspect whether the 5-pin cable is connected well. 2. Test by replacing the cable with a good one |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press the incline UP or DOWN key again, making the incline motor return to its position. 2. If the error still appears, re-calibrate the incline set |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set |

The **TR260 book prints the description, explanation and flow chart but no troubleshooting table for this half**; the VR table on its previous page is the E3 one. Its matrix row "INCLINE ERR, INCLINE window displays INCLINE ERR - position sensor value of incline motor is wrong - turn off the AC switch and turn on power again" is on `xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate`.

---
id: xterra-trx-errors-incline-err-no-vr-change-when-incline-runs
title: 'INCLINE ERR: the UP or DOWN key lights the driver board LED but the VR value
  does not change, so the console decides the incline is not moving'
kind: troubleshooting
question: What does INCLINE ERR mean on an Xterra trx3500-2024 or trx4500-2024 treadmill,
  and what should I check?
asked_as:
- incline err on my trx3500
- trx4500 incline err
- incline does not move and shows err
keywords:
- incline err
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
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs
- trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs
- trx5500-2024-errors-incline-e3-no-vr-change-when-incline-runs
- ct850-2020-incline-err
see_also:
- xterra-trx-errors-err-incline-vr-out-of-range
- xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
- xterra-treadmill-errors-incline-buttons-not-working-incline-cable-six-checks
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: 'TRX3500/TRX4500 SM Error Message: INCLINE ERR, Cause of INCLINE ERR and
    Troubleshooting, PDF pp. 55-58 (printed 54-57); text.md lines 887-942'
  extracted_at: '2026-09-11'
---

**This is INCLINE ERR, the error raised while the incline is being driven**, on the TRX3500 and TRX4500. The TR260 and TRX2500 print it INCLINE ER, the TRX1400 INCLINE Err and the TRX5500 INCLINE E3. The error raised at power-on, before any key is pressed, is ERR (`xterra-trx-errors-err-incline-vr-out-of-range`).

*Definition.* During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears. The book adds a page captioned "LCD show Err on the incline window".

*Cause.* Press the incline UP/DOWN key; the incline doesn't operate; INCLINE ERR appears. *Explanation:* pressing the incline UP or DOWN key lights the driver board's UP or DOWN indicator; the incline operates, moving the VR, which changes the VR value; the display board CPU reads the incline VR value. If there is no VR value change, to the CPU the incline is not operating when it should be, and INCLINE ERR appears.

*Troubleshooting*

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press the incline UP key: the driver board UP LED lights. 2. Press the incline DOWN key: the driver board DOWN LED lights. 3. If not as above, inspect the cable and connections |
| 5-pin cable | 1. Inspect whether the 5-pin cable is connected well. 2. Test by replacing the cable with a good one |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press the incline UP or DOWN key again, making the incline motor return to its position. 2. If the error still appears, re-calibrate the incline set |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set |

The matrix row "INCLINE ERR, INCLINE window displays ERR" is on `xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate`; the incline buttons that do nothing at all are on `xterra-treadmill-errors-incline-buttons-not-working-incline-cable-six-checks`.

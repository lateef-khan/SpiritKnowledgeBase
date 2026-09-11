---
id: trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs
title: 'INCLINE Err: pressing an incline key produces no VR change, checked at the
  keys, the incline cables, the driver board and the motor'
kind: troubleshooting
question: What does INCLINE Err mean on an Xterra trx1400-2023 treadmill, and what
  should I check?
asked_as:
- trx1400 incline err
- incline key does nothing err trx1400
- incline motor stuck err
keywords:
- incline err
- incline
- vr value
- incline keys
- incline cable
- driver board
- incline motor stuck
- gears cracked
- recalibrate
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: errors
  code: incline-err
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs
- xterra-trx-errors-incline-err-no-vr-change-when-incline-runs
- ct800-2016-errors-incline-err-during-incline-action
see_also:
- trx1400-2023-errors-err-or-e3-incline-vr-out-of-range
- trx1400-2023-errors-incline-test-procedure-nine-steps
- xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
- trx1400-2023-errors-incline-buttons-not-working-vr-wires-keys-motor-gears
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: 'TRX1400 SM Error Message: Err (during incline action), Cause of INCLINE
    Err and Troubleshooting, PDF pp. 51-53 (printed 50-52); text.md lines 865-919'
  extracted_at: '2026-09-11'
---

**This is INCLINE Err on the TRX1400, the error raised while the incline is being driven**; the error raised at power-on is Err / E3 (`trx1400-2023-errors-err-or-e3-incline-vr-out-of-range`). The other Dyaco books print a different troubleshooting table for this fault (`xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs`).

*Definition.* During incline action, the display board CPU cannot read the VR value, so Err appears. The drawing shows the incline UP/DOWN keys, the incline VR voltage and the incline UP/DOWN signal over the main control line, the driver board's incline drive power to the motor, and the INCLINE VR SET.

*Cause.* Press the incline UP/DOWN key; the incline doesn't operate; Err appears. *Explanation:* when an incline key is pressed the display board CPU reads the incline VR value; if there is no VR value change, the incline is not operating and Err appears. The action flow chart: press incline UP or DOWN -> driver board UP LED lights, incline voltage increases? DOWN LED lights, incline voltage decreases? -> incline motor: UP LED lights, incline rises? DOWN LED lights, incline lowers? -> no error message, or show INCLINE ERR message.

*Troubleshooting*

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press the incline keys and see whether the display shows a value. If no values, check whether the keys are stuck, or replace the upper control board |
| Incline cable | 1. Inspect whether the incline power wires and incline VR cable are connected well |
| Driver board | 1. Look at the lower control board for obvious, serious damage to the incline components |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Recalibrate the incline set |

The nine-step voltage test that precedes this section is `trx1400-2023-errors-incline-test-procedure-nine-steps`. The matrix row "INCLINE ERR, INCLINE window displays Err" is `xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate`, and the incline buttons row with the motor and gear checks is `trx1400-2023-errors-incline-buttons-not-working-vr-wires-keys-motor-gears`.

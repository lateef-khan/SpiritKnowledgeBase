---
id: cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
title: Err in the LEVEL window means the tension motor feedback is missing or abnormal, and the cable is checked first
kind: troubleshooting
question: What does Err in the LEVEL window mean on a Spirit CS800-2024 stepper?
asked_as:
- my stepper level window says err
- no resistance and err on my spirit stepper
- what does err mean on a spirit stepper
keywords:
- err
- level window
- tension motor
- feedback signal
- control cable
- replug
- no resistance
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2024
  applies_to:
  - cs800-2024
  section: errors
  code: err
  model_number: '800625'
authority: 3
not_to_be_confused_with:
- ce850-2024-errors-err-tension-motor-failure
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
- cs800-2024-errors-eeprom-error-replace-the-console
- cvc800-e-2-tension-motor-error
see_also:
- cs800-2024-errors-eeprom-error-replace-the-console
- cvc800-tension-motor-voltage-test
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: ERROR CODES, printed page 37. That page is a flat picture with no text layer
    and was read from the rendered page.
  extracted_at: '2026-09-10'
---

> When the tension motor feedback signal is abnormal or no feedback to the console, all the outputs
> will stop and all the display windows are blank but the LEVEL window will show "Err".
>
> Troubleshooting:
> 1. Check the control cable and replug it.
> 2. Check the tension motor.

**The message appears in the LEVEL window while every other window is blank.** That is what tells it
apart from `EEPROM ERROR`, which blanks the windows and writes its message in the **Main** window
(`cs800-2024-errors-eeprom-error-replace-the-console`).

**The cable is checked before the motor**, and the manual names no part to replace and no voltage to
measure.

**This is not the CE850 2024's `ERR`.** That elliptical prints the message in capitals in an error
table, defines it as `Tension motor is failure` and gives no remedy at all
(`ce850-2024-errors-err-tension-motor-failure`). Same three letters, a different console and a
different amount of help.

**The CRS800S 2024 semi-recumbent stepper, sold beside this machine, has no `Err` at all.** It
prints the same fault as the word `MOTOR ERROR` with no troubleshooting line
(`crs800s-2024-errors-motor-error-tension-motor-signal-wrong`).

The Spirit CVC800 climber is the only document that says what to measure at a tension motor:
`cvc800-tension-motor-voltage-test`.

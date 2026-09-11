---
id: cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
title: Err in the LEVEL window means the tension motor feedback is missing or abnormal,
  and the cable is checked first
kind: troubleshooting
question: What does Err in the LEVEL window mean on a Spirit CS800 stepper?
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
  model: '*'
  applies_to:
  - cs800-2021
  - cs800-2024
  section: errors
  code: err
authority: 3
not_to_be_confused_with:
- ce850-2024-errors-err-tension-motor-failure
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
- cs800-2024-errors-eeprom-error-replace-the-console
- cvc800-e-2-tension-motor-error
- cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable
- spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
see_also:
- cs800-2024-errors-eeprom-error-replace-the-console
- cvc800-tension-motor-voltage-test
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
- cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer
- cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable
- spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: ERROR CODES, printed page 37. That page is a flat picture with no text
    layer and was read from the rendered page; CS800 (2020) service manual 7-1 Error
    Codes and 7-4 Error Message Err, with 7-4-1 Tension Motor Operation and 7-4-2
    Tension Motor Troubleshooting, PDF p. 26-28 (printed 25-27), text.md lines 373-456
    - the CS800 2024 definition word for word
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

## The CS800 (2020) service manual prints the definition word for word and adds the drive figures

Its `7-1 Error Codes` table reads `Err | Tension Motor failure`, and `7-4 Error Message: Err` repeats the definition and the two-step remedy above, so the 2020-book CS800 (`cs800-2021`) and the 2024 CS800 are one console here. The service manual goes on:

**7-4-1 Tension Motor Operation.** Key signal travels to the display; the main program IC then sends a command signal to the drive board. Console directly controls the motor. Level UP: **+4~5VDC**; Level DOWN: **-4~5VDC**.

**7-4-2 Tension Motor Troubleshooting.** Console: if the key beeps when pressed, assume that the signal was sent. Inspect console power output to the motor - Level Up is +4~5VDC, Level DOWN is -4~5VDC. If there is power to the motor but the motor does not operate, **replace it**. If there is no power output, inspect whether the **transformer** has power. Data cable: inspect the cable and connections.

**So "check the tension motor" means: is it getting 4 to 5 V when a level key is pressed?** With the voltage there and no movement the motor is replaced; with no voltage the transformer is checked. The measurement itself is `cs800-2021-errors-tension-motor-voltage-test-4-to-5-vdc-then-the-transformer`. The console-to-driver connector on this machine is 14 pins, `MTR-` and `MTR+` on pins 1 and 2 and the feedback `MTR_AD` on pin 4.

**The 2016 CS800 prints this fault as `E2`** with 5 V and a 10-pin cable (`cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable`), and the XS895 as `E2` with 5 V from a separate drive board (`spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor`).

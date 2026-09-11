---
id: spirit-xs895-errors-error-code-table-three-codes
title: 'Every code the incline stepper can show: three codes for the EEPROM, the tension
  motor and the incline motor'
kind: spec
question: What error codes can a Spirit XS895 stepper display and what does each one
  mean?
asked_as:
- xs895 error code list
- spirit incline stepper error codes
- what codes does the xs895 show
keywords:
- error code
- error code table
- list
- index
- incline stepper
- three codes
- step error
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-errors-no-error-codes-printed
- csc900-2024-errors-error-code-table
- cvc800-e-1-ram-error
see_also:
- spirit-xs895-errors-e1-eeprom-defective-replace-the-display-board
- spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
- spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr
- spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
- spirit-xs895-errors-incline-position-does-not-match-the-console-calibrate
- spirit-xs895-errors-incline-buttons-do-not-work-cable-connectors-and-the-switch
- spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 7-1 Error Codes, PDF p. 26 (printed 25); text.md lines 360-366
  extracted_at: '2026-09-11'
---

**The XS895 owner's manuals (2018 and 2021) print no error code** (`spirit-climber-errors-no-error-codes-printed`). The service manual, `XS300B-YS006`, prints three:

| Error Code | CAUSE |
|---|---|
| E1 | EEPROM is defective or operate abnormal. |
| E2 | Tension motor is failure |
| E3 | Incline motor error |

- `E1` is answered with a new display board (`spirit-xs895-errors-e1-eeprom-defective-replace-the-display-board`).
- `E2` is the resistance motor: replug the control cable, check the motor, then a voltage test with a 5.5 to 6.0 V band, a fuse and a drive-board LED (`spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor`).
- `E3` is the incline potentiometer reading missing or out of range; the display also shows the words `STEP ERROR` and the matrix calls it `INCLINE ERR` (`spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr`).

**Written `E` and one digit, with no hyphen** - the CVC800 climber writes `E-1` and `E-2`, and the CSC900 and CSC880 stair climbers write `ER` and two digits; none of those lists is this one. `E3` in particular exists on no other Spirit stepper, because no other Spirit stepper has a powered incline.

**The same three digits mean other things on other product lines** - `E1` to `E3` on the Spirit treadmills are motor and speed faults - and Sole's SC200 2019 stepper prints `E1` and `E2` from the same Dyaco template with its own figures. Establish the machine before reading a code back.

Rows in the matrix that carry no code - a dim or dead display with a two-band supply check, an incline that does not match the console, incline keys that do nothing, and the pulse rows - are carded on their own and linked below.

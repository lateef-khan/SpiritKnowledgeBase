---
id: ce850-2024-errors-err-tension-motor-failure
title: ERR in the error message table means the tension motor has failed
kind: troubleshooting
question: What does ERR mean on a Spirit CE850-2020 or CE850-2024 elliptical?
asked_as:
- my spirit elliptical says err
- what does err mean on the console
- elliptical showing err
keywords:
- err
- tension motor
- resistance motor
- error message
- elliptical
- failure
- no resistance
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2020
  - ce850-2024
  section: errors
  code: err
authority: 3
not_to_be_confused_with:
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- ce900-2025-errors-eeprom-error-replace-upper-controller
- cvc800-e-2-tension-motor-error
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- xe395ent-2021-errors-e2-tension-motor-does-not-move
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback
see_also:
- ce900-2025-errors-eeprom-error-replace-upper-controller
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- cvc800-e-2-tension-motor-error
- spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
source:
  ref: spirit-elliptical-ce850-2024-owners-manual
  locator: 'TROUBLE SHOOTING - CONTINUED & ERROR CODES, printed page 39. That page
    is a flat picture with no text layer and was read from the rendered page; CE850
    (2020) service manual Error code items, 8-2 Error Message: Err, Tension Motor
    Operation / Troubleshooting and Tension Motor Voltage Test Procedure, PDF p. 32-36,
    text.md lines 546-624'
  extracted_at: '2026-09-10'
---

| Error Message | Explain |
|---|---|
| ERR | Tension motor is failure |

**That is the whole of what this manual says about `ERR`.** It prints no definition of what the
console does when the message appears, no window to look in, and no troubleshooting step. The
EEPROM row of the same table gets three lines of definition and a remedy; this row gets four words.

**This is not the CS800 2024 stepper's `Err`.** That machine prints the message in lower case in its
`LEVEL` window, defines it as the tension motor feedback being absent or abnormal, and gives two
checks - the control cable and the motor
(`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`). Use that machine's checks on
that machine only.

The other two rows of this table are `EEPROM ERROR`, which is the one row with a full definition
(`ce900-2025-errors-eeprom-error-replace-upper-controller`), and `---`, which is the stride motor
(`ce850-2024-errors-stride-window-dashes-stride-motor-failure`).

The nearest thing the manual gives to a procedure is the `STRIDE ERR` row of its troubleshooting
matrix, and that is about the **stride** motor, not this one:
`ce850-2024-errors-stride-err-position-sensor-wrong`.

**The CE850 (2020) service manual prints the same three-row table and then the section the owner's manual leaves out.** Its `8-2 Error Message: Err` reads: *When you press the Level Up or Down key, the motor does not move. "Err" appears on the display.* The configuration drawing shows the level keys feeding the display board, the display board driving the tension motor, and the motor's VR signal returning.

How the parts are meant to work (*Tension Motor Operation*):

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive Board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

How to find the fault (*Tension Motor Troubleshooting*):

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive Board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor, but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The numbered multi-meter test that follows - **blue and green wires, 5 to 6.0 VDC** - is `spirit-ce850-2016-errors-tension-motor-voltage-test-blue-and-green-5-to-6-vdc`, the same test the CE850 2016 prints for the same motor under the message `--` (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`). The XE395ENT 2021 prints the same section under `E2` with brown and black wires (`xe395ent-2021-errors-e2-tension-motor-does-not-move`).

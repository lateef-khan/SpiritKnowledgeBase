---
id: ce850-2024-errors-err-tension-motor-failure
title: ERR in the error message table means the tension motor has failed
kind: troubleshooting
question: What does ERR mean on a Spirit CE850-2024 elliptical?
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
  model: ce850-2024
  applies_to:
  - ce850-2024
  section: errors
  code: err
  model_number: '850025'
authority: 3
not_to_be_confused_with:
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- ce900-2025-errors-eeprom-error-replace-upper-controller
- cvc800-e-2-tension-motor-error
see_also:
- ce900-2025-errors-eeprom-error-replace-upper-controller
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- cvc800-e-2-tension-motor-error
source:
  ref: spirit-elliptical-ce850-2024-owners-manual
  locator: TROUBLE SHOOTING - CONTINUED & ERROR CODES, printed page 39. That page is a
    flat picture with no text layer and was read from the rendered page.
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

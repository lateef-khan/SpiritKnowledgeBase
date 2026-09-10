---
id: ce850-2024-errors-stride-window-dashes-stride-motor-failure
title: Three dashes in place of a stride number mean the stride motor has failed
kind: troubleshooting
question: What do the dashes in the stride window mean on a Spirit CE850-2024
  elliptical?
asked_as:
- my elliptical shows dashes instead of stride length
- stride window shows lines not numbers
- elliptical stride display is blank dashes
keywords:
- dashes
- stride motor
- stride window
- error message
- stride length
- elliptical
- failure
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce850-2024
  applies_to:
  - ce850-2024
  section: errors
  code: dashes
  model_number:
  - '850025'
authority: 3
not_to_be_confused_with:
- ce850-2024-errors-err-tension-motor-failure
- ce850-2024-errors-stride-err-position-sensor-wrong
see_also:
- ce850-2024-errors-stride-err-position-sensor-wrong
- ce850-2024-errors-err-tension-motor-failure
- ce900-2025-errors-eeprom-error-replace-upper-controller
source:
  ref: spirit-elliptical-ce850-2024-owners-manual
  locator: TROUBLE SHOOTING - CONTINUED & ERROR CODES, printed page 39. That page is a
    flat picture with no text layer and was read from the rendered page.
  extracted_at: '2026-09-10'
---

| Error Message | Explain |
|---|---|
| `---` | Stride motor is failure |

**The message is three dashes, not a word and not a code.** A reader looking for letters or a number
will not find one; the `STRIDE` window simply shows `---` where a stride length should be.

**That is the whole of what this manual says about it.** No definition, no window named beyond the
table, and no troubleshooting step.

**The troubleshooting matrix of the same manual describes the same display and gives it a name and a
remedy.** Its row reads `STRIDE ERR, STRIDE window displays "---"`, blames a wrong position sensor
value on the stride motor and asks for a power cycle and then a calibration. That is the half of
this fact with something to do in it:
`ce850-2024-errors-stride-err-position-sensor-wrong`. **Neither half is complete on its own** - the
error table names the failed part, the matrix names the remedy - and nothing in the manual joins
them up.

The other two rows of the error table are `EEPROM ERROR`
(`ce900-2025-errors-eeprom-error-replace-upper-controller`) and `ERR`, which is the **tension**
motor rather than the stride motor (`ce850-2024-errors-err-tension-motor-failure`).

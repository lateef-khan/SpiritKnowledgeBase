---
id: ce900-2025-errors-eeprom-error-replace-upper-controller
title: EEPROM ERROR blanks every window and stops all output, and the fix is a new
  upper controller
kind: troubleshooting
question: What does EEPROM ERROR mean on a Spirit CE800-2024, CE850-2024 or CE900-2025
  elliptical or a CR800-2024, CR900-2025, CU800-2024 or CU900-2025 bike?
asked_as:
- what does eeprom error mean on my spirit elliptical
- elliptical console showing eeprom error
- screen went blank and says eeprom
keywords:
- eeprom error
- eeprom failure
- message window
- upper controller
- console memory
- blank windows
- outputs stop
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce800-2024
  - ce850-2024
  - ce900-2025
  - cr800-2024
  - cr900-2025
  - cu800-2024
  - cu900-2025
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- ces880-2025-errors-eeprom-error-replace-display-board
- cu900ent-eeprom-err
- ce800ent-e5-console-controller-communication
see_also:
- ces880-2025-errors-eeprom-error-replace-display-board
- cu900ent-eeprom-err
source:
  ref: spirit-elliptical-ce900-2025-owners-manual
  locator: 'ERROR CODES: CE900 2025 printed page 33; CR900 2025 printed page 35; CU900
    2025 printed page 34'
  extracted_at: '2026-09-09'
---

| Error Code | Cause |
|---|---|
| EEPROM | EEPROM failure |

Displayed in the MW window as **"EEPROM ERROR"**.

> When the EEPROM is damaged or accesses a problem, all the windows are OFF, all outputs are STOP,
> MW displays "EEPROM ERROR".

**Troubleshooting - replace the upper controller.**

**The CE900 2025 elliptical, the CR900 2025 recumbent bike and the CU900 2025 upright bike print
this page word for word**, table and all.

This is the only error code any of the three owner's manuals prints. Their other fault content is a
symptom table with no codes at all, on the facing page.

The CU800ENT 2024 bike is the other way round: it prints no EEPROM message and its only code is
`E5` - `ce800ent-e5-console-controller-communication`.

**The CES880 2025 manual prints the same message with a different fix** - it says to replace the
**display board**, not the upper controller. Do not carry one answer to the other machine:
`ces880-2025-errors-eeprom-error-replace-display-board`.

The CU900ENT bike prints the message as `EEPROM ERR` and gives no fix at all:
`cu900ent-eeprom-err`.

**Four of the 2024 New Black machines print this page word for word too** - the CE800 2024 and
CE850 2024 ellipticals, the CR800 2024 recumbent bike and the CU800 2024 upright bike. Every one
prints the `Error Code | CAUSE` table with the single row `EEPROM | EEPROM failure`, the same
three-line definition and the same one-line remedy. Their ERROR CODES pages are flat pictures with
no text layer and were read from the rendered page: CE800 2024 printed page 38, CE850 2024 printed
page 39, CR800 2024 printed page 38, CU800 2024 printed page 38.

**On the CE850 2024 it is no longer the only code.** That manual's table carries two further rows
the other six do not - `ERR` for a tension motor failure and `---` for a stride motor failure. See
`ce850-2024-errors-err-tension-motor-failure` and
`ce850-2024-errors-stride-window-dashes-stride-motor-failure`. On the CE800 2024, CR800 2024 and
CU800 2024 the EEPROM row is still the whole table.

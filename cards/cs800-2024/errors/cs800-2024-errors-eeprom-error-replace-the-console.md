---
id: cs800-2024-errors-eeprom-error-replace-the-console
title: EEPROM ERROR blanks every window and stops all output, and the fix is a new console
kind: troubleshooting
question: What does EEPROM ERROR mean on a Spirit CS800-2024 stepper?
asked_as:
- my spirit stepper says eeprom error
- stepper console went blank and says eeprom
- what does eeprom error mean
keywords:
- eeprom error
- main window
- console replacement
- memory access
- blank windows
- outputs stop
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2024
  applies_to:
  - cs800-2024
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- ce900-2025-errors-eeprom-error-replace-upper-controller
- ces880-2025-errors-eeprom-error-replace-display-board
- cu900ent-eeprom-err
- crs800s-2024-errors-ram-error-replace-the-display-board
see_also:
- ce900-2025-errors-eeprom-error-replace-upper-controller
- ces880-2025-errors-eeprom-error-replace-display-board
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: ERROR CODES, printed page 37. That page is a flat picture with no text layer
    and was read from the rendered page.
  extracted_at: '2026-09-10'
---

> When EEPROM is defective or has memory access problems, the console will shut all display windows
> off and stop all the outputs. The Main Window will show "EEPROM ERROR".
>
> Troubleshooting: The console requires replacement.

**This machine names a third part for the same message.** Three Spirit manuals define `EEPROM ERROR`
in these words and each condemns something different:

| Machine | Part the manual names |
|---|---|
| CS800 2024 stepper | The **console** |
| CE800 2024, CE850 2024, CE900 2025 ellipticals and CR800 2024, CR900 2025, CU800 2024, CU900 2025 bikes | The **upper controller** (`ce900-2025-errors-eeprom-error-replace-upper-controller`) |
| CES880 2025 suspension elliptical | The **display board** (`ces880-2025-errors-eeprom-error-replace-display-board`) |

On a console of this shape the upper controller and the display board are boards inside the console,
so all three end at the same assembly in practice - but the manuals order three different parts.
**Order the part the customer's own manual names.**

The CU900ENT bike prints the message as `EEPROM ERR` and gives no fix at all (`cu900ent-eeprom-err`).

The other message this manual carries is `Err` in the LEVEL window, for the tension motor:
`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`.

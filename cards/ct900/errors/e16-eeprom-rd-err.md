---
id: ct900-e16-eeprom-rd-err
title: Error E16 - EEPROM RD ERR (read error)
kind: troubleshooting
question: What does error E16 EEPROM RD ERR mean on a CT900 and how do I fix it?
asked_as:
- what does e16 mean on the treadmill
- error 16 eeprom read
keywords:
- e16
- eeprom read error
- eeprom rd err
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e16
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e7-eeprom-wr-err
- ct900-e34-console-eeprom-error
see_also:
- ct900-e7-eeprom-wr-err
- ct900-e34-console-eeprom-error
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E16, the EEPROM READ error - not E7, the EEPROM WRITE error, and not E34 (CONSOLE EEPROM ERROR, a distinct fault with its own stated fix).**

Note: E15 does not appear in the source manual's error code table - it is skipped between E14 and E16, exactly as printed.

The manual's Error Codes table gives no distinct description or solution for E16 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 16** is this code. The inverter's own keypad (KPC-CC01) displays it as `cF2 - EEPROM read err`. The table says to press RESET to clear an error code.

Error description, word for word: *Internal EEPROM cannot be programmed.*

Corrective actions, in the order printed:

1. Check if the power board and control board inside the motor are properly installed. Press RESET key and set up the parameters as factory setting.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

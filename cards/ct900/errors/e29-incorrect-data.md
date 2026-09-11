---
id: ct900-e29-incorrect-data
title: Error E29 - Incorrect Data
kind: troubleshooting
question: What does error E29 Incorrect Data mean on a CT900 and how do I fix it?
asked_as:
- what does e29 mean on the treadmill
- error 29 incorrect data
keywords:
- e29
- incorrect data
- console error
- e29 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e29
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with: []
see_also: []
source:
  ref: ct900-om
  locator: p. 45; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

The manual's Error Codes table gives no distinct description or solution for E29 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 29** is this code. The inverter's own keypad (KPC-CC01) displays it as `cE03 - PC err data`. The table says to press RESET to clear an error code.

Error description, word for word: *Incorrect data value*

Corrective actions, in the order printed:

1. Verify if the Modbus' data value fits the communication specification of the motor drive.
2. Verify the quality of the communication cable and the communication.
3. Clear the fault and then press RESET button.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

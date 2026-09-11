---
id: ct900-e23-over-slip
title: Error E23 - Over Slip
kind: troubleshooting
question: What does error E23 Over Slip mean on a CT900 and how do I fix it?
asked_as:
- what does e23 mean on the treadmill
- error 23 over slip
keywords:
- e23
- over slip
- console error
- e23 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e23
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-osl-over-slip-warning
see_also:
- ct900-osl-over-slip-warning
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is the console's E23 error code, not the inverter's separate oSL (Over Slip Warning) code**, which is in a different code namespace and does have a stated corrective action.

The manual's Error Codes table gives no distinct description or solution for E23 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

See [oSL - Over Slip Warning](osl-over-slip-warning.md) for the inverter code of the same concept, which has a stated fix.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 23** is this code. The inverter's own keypad (KPC-CC01) displays it as `oSL - Over slip error`. The table says to press RESET to clear an error code.

Error description, word for word: *Over slip detection*

Corrective actions, in the order printed:

1. Verify if there's an overload.
2. Verify the setting of Pr04-21~ Pr03-23.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

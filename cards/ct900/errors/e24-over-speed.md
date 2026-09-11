---
id: ct900-e24-over-speed
title: Error E24 - Over Speed
kind: troubleshooting
question: What does error E24 Over Speed mean on a CT900 and how do I fix it?
asked_as:
- what does e24 mean on the treadmill
- error 24 over speed
keywords:
- e24
- over speed
- console error
- e24 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e24
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-osp-over-speed-warning
see_also:
- ct900-osp-over-speed-warning
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is the console's E24 error code, not the inverter's separate oSP (Over Speed Warning) code**, which is in a different code namespace and does have a stated corrective action.

The manual's Error Codes table gives no distinct description or solution for E24 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

See [oSP - Over Speed Warning](osp-over-speed-warning.md) for the inverter code of the same concept, which has a stated fix.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 24** is this code. The inverter's own keypad (KPC-CC01) displays it as `oSP - Over speed error`. The table says to press RESET to clear an error code.

Error description, word for word: *Over speed detection*

Corrective actions, in the order printed:

1. Verify if the frequency command is bigger than the maximum value of main communication frequency.
2. Verify the setting of Pr03-12~ Pr03-14)

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

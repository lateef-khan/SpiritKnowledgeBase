---
id: ct900-e4-motor-overload
title: Error E4 - Motor Overload
kind: troubleshooting
question: What does error E4 Motor Overload mean on a CT900 and how do I fix it?
asked_as:
- what does e4 mean on the treadmill
- error 4 motor overload
keywords:
- e4
- motor overload
- console error
- e4 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e4
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e5-thermal-overload
- ct900-ol2-motor-overload-warning
see_also:
- ct900-e5-thermal-overload
- ct900-ol2-motor-overload-warning
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E4 (MOTOR OVERLOAD), not E5 (THERMAL OVERLOAD), and not the inverter's separate oL2 warning code (also called "Motor overload" but in the inverter's own code namespace, with a stated fix).**

The manual's Error Codes table gives no distinct description or solution for E4 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

See [oL2 - Motor overload warning](ol2-motor-overload-warning.md) for the inverter code of the same name, which does have a stated corrective action.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 4** is this code. The inverter's own keypad (KPC-CC01) displays it as `oL - Over load`. The table says to press RESET to clear an error code.

Error description, word for word: *Overload: The motor drive detects excessive drive output current. The motor drive can endure 150% of rated current for 60 seconds.*

Corrective actions, in the order printed:

1. Check if the motor is overloaded.
2. Decrease the setting value at Pr01-23 to increase the output capacity of the motor drive.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

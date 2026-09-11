---
id: ct900-e3-igbt-over-temp
title: Error E3 - IGBT Over Temp
kind: troubleshooting
question: What does error E3 IGBT Over Temp mean on a CT900 and how do I fix it?
asked_as:
- what does e3 mean on the treadmill
- error 3 igbt
keywords:
- e3
- igbt over temp
- igbt overheat
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e3
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e5-thermal-overload
- ct900-e32-motor-temp
- ct900-toh-motor-over-heating-warning
see_also:
- ct900-e5-thermal-overload
- ct900-e32-motor-temp
- ct900-toh-motor-over-heating-warning
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E3 (IGBT OVER TEMP - a controller/inverter component overheating), not E5 (THERMAL OVERLOAD), not E32 (MOTOR TEMP), and not the inverter's toH (motor over-heating warning).**

The manual's Error Codes table gives no distinct description or solution for E3 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 3** is this code. The *Display on KPC-CC01* column is blank for this row; the keypad shows the number only. The table says to press RESET to clear an error code.

Error description, word for word: *Inside of motor drive is overheated and the high temperature exceeds the protection level*

Corrective actions, in the order printed:

1. Ensure that the ambient temperature falls within the specified temperature range.
2. Make sure that the ventilation holes are not obstructed.
3. Remove any foreign objects from the heatsink and check for possible dirty heat sink fins.
4. Provide enough spacing for adequate ventilation.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

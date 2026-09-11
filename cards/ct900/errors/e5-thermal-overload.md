---
id: ct900-e5-thermal-overload
title: Error E5 - Thermal Overload
kind: troubleshooting
question: What does error E5 Thermal Overload mean on a CT900 and how do I fix it?
asked_as:
- what does e5 mean on the treadmill
- error 5 thermal overload
keywords:
- e5
- thermal overload
- console error
- e5 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e5
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e3-igbt-over-temp
- ct900-e4-motor-overload
see_also:
- ct900-e3-igbt-over-temp
- ct900-e4-motor-overload
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E5 (THERMAL OVERLOAD), not E3 (IGBT OVER TEMP) and not E4 (MOTOR OVERLOAD).**

The manual's Error Codes table gives no distinct description or solution for E5 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 5** is this code. The inverter's own keypad (KPC-CC01) displays it as `oL1 - Thermal relay 1`. The table says to press RESET to clear an error code.

Error description, word for word: *Electronics thermal relay protection: Motor is overloaded.*

Corrective actions, in the order printed:

1. Check if the motor is overloaded.
2. Check if the setting of Pr00-13 <Motor Rated Current> is appropriate.
3. Check the setting of Pr04-13~ Pr04-14 <Electronic thermal relay> is appropriate.
4. Increase the capacity of the motor.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

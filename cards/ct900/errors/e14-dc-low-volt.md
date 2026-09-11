---
id: ct900-e14-dc-low-volt
title: Error E14 - DC Low Volt
kind: troubleshooting
question: What does error E14 DC Low Volt mean on a CT900 and how do I fix it?
asked_as:
- what does e14 mean on the treadmill
- error 14 low voltage
keywords:
- e14
- dc low volt
- low voltage
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e14
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e2-over-voltage
- ct900-e25-stop-over-volt
see_also:
- ct900-e2-over-voltage
- ct900-e25-stop-over-volt
- ct900-top-speed-limited-low-voltage
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E14 (DC LOW VOLT), not E2 (OVER VOLTAGE) or E25 (STOP OVER VOLT).**

The manual's Error Codes table gives no distinct description or solution for E14 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

For the related symptom of low incoming AC voltage limiting top speed, see [top speed limited / low voltage](../maintenance/top-speed-limited-low-voltage.md).

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 14** is this code. The inverter's own keypad (KPC-CC01) displays it as `Lv - Low voltage`. The table says to press RESET to clear an error code.

Error description, word for word: *DC BUS voltage is less than is too low. (printed so; a value is missing between than and is)*

Corrective actions, in the order printed:

1. Check if the input voltage is normal
2. Check for possible sudden load

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

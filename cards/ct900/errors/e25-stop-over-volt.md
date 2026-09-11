---
id: ct900-e25-stop-over-volt
title: Error E25 - Stop Over Volt
kind: troubleshooting
question: What does error E25 Stop Over Volt mean on a CT900 and how do I fix it?
asked_as:
- what does e25 mean on the treadmill
- error 25 stop over volt
keywords:
- e25
- stop over volt
- console error
- e25 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e25
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e2-over-voltage
- ct900-e14-dc-low-volt
see_also:
- ct900-e2-over-voltage
- ct900-e14-dc-low-volt
source:
  ref: ct900-om
  locator: p. 45; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E25 (STOP OVER VOLT), not E2 (OVER VOLTAGE) or E14 (DC LOW VOLT).**

The manual's Error Codes table gives no distinct description or solution for E25 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 25** is this code. The inverter's own keypad (KPC-CC01) displays it as `StoV - Ov at stop`. The table says to press RESET to clear an error code.

Error description, word for word: *DC BUS over-voltage when the motor drive is stopping.*

Corrective actions, in the order printed:

1. Check if the input voltage falls within the rated AC motor drive input voltage range.
2. Check for possible voltage transients.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

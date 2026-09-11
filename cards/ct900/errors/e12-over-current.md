---
id: ct900-e12-over-current
title: Error E12 - Over Current
kind: troubleshooting
question: What does error E12 Over Current mean on a CT900 and how do I fix it?
asked_as:
- what does e12 mean on the treadmill
- error 12 over current
keywords:
- e12
- over current
- overcurrent
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e12
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e1-over-current
- ct900-e10-accel-ovr-curr
- ct900-e11-decel-ovr-curr
see_also:
- ct900-e1-over-current
- ct900-e10-accel-ovr-curr
- ct900-e11-decel-ovr-curr
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E12, not E1 - both are printed with the identical name "OVER CURRENT" in the source table, with no further distinction given anywhere in this manual. Also not E10 (ACCEL OVR CURR) or E11 (DECEL OVR CURR), which are the acceleration/deceleration-specific variants.**

The manual's Error Codes table gives no distinct description or solution for E12 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 12** is this code. The inverter's own keypad (KPC-CC01) displays it as `ocn - Oc at normal SPD`. The table says to press RESET to clear an error code.

Error description, word for word: *Over-current during steady state operation (detected by software)*

Corrective actions, in the order printed:

1. Short-circuit at motor output: Check for possible poor insulation at the output.
2. Sudden increase in motor loading: Check for possible motor stall.
3. AC motor drive output power is too small: Replace the AC motor drive with the next higher power model.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

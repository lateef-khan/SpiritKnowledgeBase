---
id: ct900-e11-decel-ovr-curr
title: Error E11 - DECEL OVR CURR (over current during deceleration)
kind: troubleshooting
question: What does error E11 DECEL OVR CURR mean on a CT900 and how do I fix it?
asked_as:
- what does e11 mean on the treadmill
- error 11 deceleration over current
keywords:
- e11
- decel ovr curr
- deceleration over current
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e11
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e1-over-current
- ct900-e10-accel-ovr-curr
- ct900-e12-over-current
see_also:
- ct900-e1-over-current
- ct900-e10-accel-ovr-curr
- ct900-e12-over-current
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E11, over current specifically during deceleration - not E1 or E12 (both generically named "OVER CURRENT" with no phase specified), and not E10 (over current during acceleration).**

The manual's Error Codes table gives no distinct description or solution for E11 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 11** is this code. The inverter's own keypad (KPC-CC01) displays it as `ocd - Oc at decel`. The table says to press RESET to clear an error code.

Error description, word for word: *Over-current during deceleration (detected by software)*

Corrective actions, in the order printed:

1. Short-circuit at motor output: Check for possible poor insulation at the output.
2. Increase the deceleration time.
3. AC motor drive output power is too small: Replace the AC motor drive with the next higher power model.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

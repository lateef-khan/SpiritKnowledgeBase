---
id: ct900-e13-ground-fault
title: Error E13 - Ground Fault
kind: troubleshooting
question: What does error E13 Ground Fault mean on a CT900 and how do I fix it?
asked_as:
- what does e13 mean on the treadmill
- error 13 ground fault
keywords:
- e13
- ground fault
- console error
- e13 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e13
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with: []
see_also:
- ct900-grounding-instructions
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

The manual's Error Codes table gives no distinct description or solution for E13 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

If you suspect the treadmill is not properly grounded, see [Grounding Instructions](../safety/grounding-instructions.md).

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 13** is this code. The inverter's own keypad (KPC-CC01) displays it as `GFF - Ground fault`. The table says to press RESET to clear an error code.

Error description, word for word: *Ground fault. When (one of) the output terminal(s) is grounded, short circuit current is more than 50% of AC motor drive rated current, the AC motor drive power module may be damaged. NOTE: The short circuit protection is provided for AC motor drive protection, not for protecting the user.*

Corrective actions, in the order printed:

1. Check the wiring connections between the AC motor drive and motor for possible short circuits, also to ground.
2. Check whether the IGBT power module is damaged.
3. Check for possible poor insulation at the output

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

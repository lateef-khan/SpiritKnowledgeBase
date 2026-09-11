---
id: ct900-e21-safety-key
title: Error E21 - Safety Key
kind: troubleshooting
question: What does error E21 Safety Key mean on a CT900 and how do I fix it?
asked_as:
- what does e21 mean on the treadmill
- error 21 safety key
keywords:
- e21
- safety key error
- safety device fault
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e21
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with: []
see_also:
- ct900-safety-tether-cord-and-key
- ct900-safety-key-removed-treadmill-wont-stop
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

This is the formal console error code for the safety key/tether circuit - see [safety tether cord and safety key](../safety/safety-tether-cord-and-key.md) for how that device normally works.

The manual's Error Codes table gives no distinct description or solution for E21 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

If the treadmill won't stop when the key is pulled, or runs with no key at all, see the troubleshooting entry at [safety key removed - treadmill won't stop](../maintenance/safety-key-removed-treadmill-wont-stop.md), which gives an actual fix (replace the safety key device or console) not present in the Error Codes table itself.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 21** is this code. The inverter's own keypad (KPC-CC01) displays it as `SAFE - Safety switch protection`. The table says to press RESET to clear an error code.

Error description, word for word: *Safe key is removed*

Corrective actions, in the order printed:

1. Check if the safe key is properly inserted.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

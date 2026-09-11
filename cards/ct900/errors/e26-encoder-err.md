---
id: ct900-e26-encoder-err
title: Error E26 - Encoder ERR
kind: troubleshooting
question: What does error E26 Encoder ERR mean on a CT900 and how do I fix it?
asked_as:
- what does e26 mean on the treadmill
- error 26 encoder
keywords:
- e26
- encoder error
- console error
- e26 error
- treadmill fault code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e26
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-pger-pg-feedback-loss-warning
see_also:
- ct900-pger-pg-feedback-loss-warning
source:
  ref: ct900-om
  locator: p. 45; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is the console's E26 error code, not the inverter's separate PGEr (PG feedback loss warning) code**, which is a related but distinct encoder/feedback fault in the inverter's own namespace, with a stated corrective action.

The manual's Error Codes table gives no distinct description or solution for E26 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 26** is this code. The inverter's own keypad (KPC-CC01) displays it as `PGEr - PG Fbk loss`. The table says to press RESET to clear an error code.

Error description, word for word: *PG feedback loss*

Corrective actions, in the order printed:

1. Verify if the encoder works properly.
2. Verify if the wiring of PG is correct.
3. Verify if the speed of motor is over the detection range of PG terminal.
4. Verify if the setting of Pr02-31~ Pr02-39 is correct.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

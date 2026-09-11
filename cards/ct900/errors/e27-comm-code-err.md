---
id: ct900-e27-comm-code-err
title: Error E27 - COMM CODE ERR (communication code error)
kind: troubleshooting
question: What does error E27 COMM CODE ERR mean on a CT900 and how do I fix it?
asked_as:
- what does e27 mean on the treadmill
- error 27 communication code
keywords:
- e27
- comm code err
- communication code error
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e27
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e30-comm-cmd-err
- ct900-e31-comm-timeout
- ct900-ce1-communication-command-defected
see_also:
- ct900-e30-comm-cmd-err
- ct900-e31-comm-timeout
- ct900-ce1-communication-command-defected
source:
  ref: ct900-om
  locator: p. 45; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E27, not E30 (COMM CMD ERR), not E31 (COMM TIMEOUT, which has an actual stated fix), and not the inverter's own cE1 "Communication command defected" code.**

The manual's Error Codes table gives no distinct description or solution for E27 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 27** is this code. The inverter's own keypad (KPC-CC01) displays it as `cE01 - PC err command`. The table says to press RESET to clear an error code.

Error description, word for word: *Communication code is incorrect.*

Corrective actions, in the order printed:

1. Verify the function code of the ModBus fits the communication specifications of the motor drive.
2. Verify the quality of the communication cable and the communication.
3. Clear the fault then press RESET button

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

---
id: ct900-e28-data-addrs-flt
title: Error E28 - DATA ADDRS FLT (data address fault)
kind: troubleshooting
question: What does error E28 DATA ADDRS FLT mean on a CT900 and how do I fix it?
asked_as:
- what does e28 mean on the treadmill
- error 28 data address fault
keywords:
- e28
- data addrs flt
- data address fault
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e28
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-ce2-address-of-data-defected
see_also:
- ct900-ce2-address-of-data-defected
source:
  ref: ct900-om
  locator: p. 44; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is the console's E28 error code, not the inverter's cE2 "Address of data defected" warning code**, which is a similar concept in the inverter's own namespace, with a stated corrective action.

The manual's Error Codes table gives no distinct description or solution for E28 beyond its name. Per the table: "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table" for both description and solution.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 28** is this code. The inverter's own keypad (KPC-CC01) displays it as `cE02 - PC err address`. The table says to press RESET to clear an error code.

Error description, word for word: *Incorrect data address*

Corrective actions, in the order printed:

1. Verify if the Modbus' data address fits the communication specification of the motor drive.
2. Verify the quality of the communication cable and the communication.
3. Clear the fault and then press RESET button.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

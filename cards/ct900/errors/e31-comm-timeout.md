---
id: ct900-e31-comm-timeout
title: Error E31 - COMM TIMEOUT (communication timeout)
kind: troubleshooting
question: What does error E31 COMM TIMEOUT mean on a CT900 and how do I fix it?
asked_as:
- what does e31 mean on the treadmill
- error 31 communication timeout
keywords:
- e31
- comm timeout
- communication timeout
- console inverter connection
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e31
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e27-comm-code-err
- ct900-e30-comm-cmd-err
- ct900-ce10-modbus-transmission-timeout
see_also:
- ct900-e27-comm-code-err
- ct900-e30-comm-cmd-err
- ct900-ce10-modbus-transmission-timeout
source:
  ref: ct900-om
  locator: p. 45; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E31, not E27 (COMM CODE ERR) or E30 (COMM CMD ERR).**

**Description**: The communication transmission timeout error between the console and the inverter.

**Solution**: Check each connector/wire for good [connection].

Compare with the inverter's own [cE10 - ModBus transmission time-out](ce10-modbus-transmission-timeout.md) warning code, a related but separate fault in the inverter's own code namespace.

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 31** is this code. The inverter's own keypad (KPC-CC01) displays it as `cE10 - PC time out`. The table says to press RESET to clear an error code. The *Error code items* table on page 30 also gives this code the one console-side solution in the book: *The communication transmission timeout error between the console and the inverter. Check each connector/wire for good.*

Error description, word for word: *Communication transmission time-out*

Corrective actions, in the order printed:

1. Verify the quality of the communication cable and the communication.
2. Clear the fault and then press RESET button.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

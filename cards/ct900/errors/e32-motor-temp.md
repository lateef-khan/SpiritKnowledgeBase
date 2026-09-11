---
id: ct900-e32-motor-temp
title: Error E32 - Motor Temp
kind: troubleshooting
question: What does error E32 Motor Temp mean on a CT900 and how do I fix it?
asked_as:
- what does e32 mean on the treadmill
- error 32 motor temperature
keywords:
- e32
- motor temp
- motor overheating
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e32
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e3-igbt-over-temp
- ct900-e5-thermal-overload
- ct900-toh-motor-over-heating-warning
see_also:
- ct900-e3-igbt-over-temp
- ct900-e5-thermal-overload
- ct900-toh-motor-over-heating-warning
source:
  ref: ct900-om
  locator: p. 45; CT900 service manual 8. Error code items, PDF p. 29-30, text.md
    lines 366-426; CT900 service manual AC MOTOR DRIVER INVERTER VFD-TM Error and
    Warning Codes, List of Error Codes, PDF p. 40-43, text.md lines 579-841
  extracted_at: '2026-08-24'
---

**This is E32 (MOTOR TEMP), not E3 (IGBT OVER TEMP) or E5 (THERMAL OVERLOAD), and not the inverter's toH (motor over-heating warning) code.**

**Description** (as printed): "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table."

**Solution** (as printed): same generic pointer to the inverter driver's warning-code table.

See [toH - Motor over-heating warning](toh-motor-over-heating-warning.md) for the inverter's own code with a stated corrective action (verify if the motor is overheated; verify the wiring of the motor's temperature protection switch).

**Service manual remedy.** The CT900 service manual prints the VFD-TM table the owner's manual only points at - *AC MOTOR DRIVER INVERTER, VFD-TM Error and Warning Codes' Descriptions, List of Error Codes* - and its **Error Code # 32** is this code. The inverter's own keypad (KPC-CC01) displays it as `toH - Motor over heat`. The table says to press RESET to clear an error code.

Error description, word for word: *Motor overheating protection*

Corrective actions, in the order printed:

1. Verify if the motor's temperature is too high.
2. Verify if the motor's overheating protection switch is properly wired.

The `Pr` references are the drive's own parameter numbers, which only a technician at the inverter keypad can change; for a customer the actionable steps are the wiring, load, ventilation and supply checks. The Error Code # column runs 1 to 32 with 15 missing, matching the console's `E` numbering.

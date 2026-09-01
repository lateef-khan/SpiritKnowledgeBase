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
  locator: p. 45
  extracted_at: '2026-08-24'
---

**This is E32 (MOTOR TEMP), not E3 (IGBT OVER TEMP) or E5 (THERMAL OVERLOAD), and not the inverter's toH (motor over-heating warning) code.**

**Description** (as printed): "Please follow to AC MOTOR DRIVER inverter VFD-TM Error and Warning codes' descriptions corresponding table."

**Solution** (as printed): same generic pointer to the inverter driver's warning-code table.

See [toH - Motor over-heating warning](toh-motor-over-heating-warning.md) for the inverter's own code with a stated corrective action (verify if the motor is overheated; verify the wiring of the motor's temperature protection switch).

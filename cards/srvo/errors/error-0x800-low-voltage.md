---
id: srvo-error-0x800-low-voltage
title: 'Error 0x800: low voltage'
kind: troubleshooting
question: What does error code 0x800 mean on the SOLE SRVO?
asked_as:
- what does 0x800 mean on the srvo
- srvo low voltage error
- srvo showing 0x800
keywords:
- error code
- hex code
- low voltage
- undervoltage
- utility power
- mains
- control module
- brownout
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x800'
authority: 3
not_to_be_confused_with:
- srvo-error-0x40-power-module-low-voltage
- srvo-error-0x80-fo-control-error
- srvo-error-0x400-high-voltage
- srvo-error-0x80000-encoder-value-error
- srvo-error-0x800000-voltage-unstable
see_also:
- srvo-error-code-table
source:
  ref: sole-srvo-service-manual
  locator: page 44, section 9 Error Messages & Troubleshooting
  extracted_at: '2026-09-04'
---

**This is 0x800, the low voltage code. It is not 0x40 (Power module low voltage), 0x80 (FO control error), 0x400 (High voltage), 0x80000 (Encoder value error) and 0x800000 (Voltage unstable).**

| Field | Value |
|---|---|
| Error code | `0x800` |
| Error message | Low voltage |
| Probable cause | Voltage too low for control module |
| Suggested action | Turn off machine. Check utility power voltage. |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

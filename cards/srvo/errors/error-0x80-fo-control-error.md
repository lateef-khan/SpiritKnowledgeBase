---
id: srvo-error-0x80-fo-control-error
title: 'Error 0x80: fo control error'
kind: troubleshooting
question: What does error code 0x80 mean on the SOLE SRVO?
asked_as:
- what does 0x80 mean on the srvo
- srvo fo control error
- srvo showing 0x80
keywords:
- error code
- hex code
- fo control
- short circuit
- power module
- fault
- shut down
- control fault
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x80'
authority: 3
not_to_be_confused_with:
- srvo-error-0x800-low-voltage
- srvo-error-0x80000-encoder-value-error
- srvo-error-0x800000-voltage-unstable
see_also:
- srvo-error-code-table
source:
  ref: sole-srvo-service-manual
  locator: page 44, section 9 Error Messages & Troubleshooting
  extracted_at: '2026-09-04'
---

**This is 0x80, the FO control error code. It is not 0x800 (Low voltage), 0x80000 (Encoder value error) and 0x800000 (Voltage unstable).**

| Field | Value |
|---|---|
| Error code | `0x80` |
| Error message | FO control error |
| Probable cause | Power module defective/low voltage/ or short circuit |
| Suggested action | Turn off machine |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

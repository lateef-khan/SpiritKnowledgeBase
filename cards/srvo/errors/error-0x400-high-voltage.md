---
id: srvo-error-0x400-high-voltage
title: 'Error 0x400: high voltage'
kind: troubleshooting
question: What does error code 0x400 mean on the SOLE SRVO?
asked_as:
- what does 0x400 mean on the srvo
- srvo high voltage error
- srvo showing 0x400
keywords:
- error code
- hex code
- high voltage
- overvoltage
- bleeder resistor
- control module
- mains
- fault
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x400'
authority: 3
not_to_be_confused_with:
- srvo-error-0x40-power-module-low-voltage
- srvo-error-0x800-low-voltage
- srvo-error-0x40000-encoder-offset-error
- srvo-error-0x400000-encoder-not-connected
- srvo-error-0x4000000-uvw-cord-error
- srvo-error-0x40000000-electrical-load
see_also:
- srvo-error-code-table
source:
  ref: sole-srvo-service-manual
  locator: page 44, section 9 Error Messages & Troubleshooting
  extracted_at: '2026-09-04'
---

**This is 0x400, the high voltage code. It is not 0x40 (Power module low voltage), 0x800 (Low voltage), 0x40000 (Encoder off set error), 0x400000 (Encoder not connected), 0x4000000 (UVW cord error) and 0x40000000 (Electrical load).**

| Field | Value |
|---|---|
| Error code | `0x400` |
| Error message | High voltage |
| Probable cause | Voltage too high for control module |
| Suggested action | Turn off machine, check bleeder resistor. |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

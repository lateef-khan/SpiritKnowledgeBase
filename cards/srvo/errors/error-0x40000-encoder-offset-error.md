---
id: srvo-error-0x40000-encoder-offset-error
title: 'Error 0x40000: encoder off set error'
kind: troubleshooting
question: What does error code 0x40000 mean on the SOLE SRVO?
asked_as:
- what does 0x40000 mean on the srvo
- srvo encoder offset error
- srvo showing 0x40000
keywords:
- error code
- hex code
- encoder
- offset
- off set
- loose contact
- position sensor
- fault
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x40000'
authority: 3
not_to_be_confused_with:
- srvo-error-0x40-power-module-low-voltage
- srvo-error-0x400-high-voltage
- srvo-error-0x80000-encoder-value-error
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

**This is 0x40000, the encoder off set error code. It is not 0x40 (Power module low voltage), 0x400 (High voltage), 0x80000 (Encoder value error), 0x400000 (Encoder not connected), 0x4000000 (UVW cord error) and 0x40000000 (Electrical load).**

| Field | Value |
|---|---|
| Error code | `0x40000` |
| Error message | Encoder off set error |
| Probable cause | Defective encoder or loose contact |
| Suggested action | Turn off machine and check encoder |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

All three encoder codes carry the same probable cause and the same suggested action in the manual. The code is the only thing that tells them apart.

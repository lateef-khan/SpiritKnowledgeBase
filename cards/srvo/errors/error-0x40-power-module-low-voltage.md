---
id: srvo-error-0x40-power-module-low-voltage
title: 'Error 0x40: power module low voltage'
kind: troubleshooting
question: What does error code 0x40 mean on the SOLE SRVO?
asked_as:
- what does 0x40 mean on the srvo
- srvo power module low voltage error
- srvo showing 0x40
keywords:
- error code
- hex code
- power module
- low voltage
- utility power
- brownout
- restart
- fault
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x40'
authority: 3
not_to_be_confused_with:
- srvo-error-0x400-high-voltage
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

**This is 0x40, the power module low voltage code. It is not 0x400 (High voltage), 0x800 (Low voltage), 0x40000 (Encoder off set error), 0x400000 (Encoder not connected), 0x4000000 (UVW cord error) and 0x40000000 (Electrical load).**

| Field | Value |
|---|---|
| Error code | `0x40` |
| Error message | Power module low voltage |
| Probable cause | Defective power module/ Utility power low voltage |
| Suggested action | Restart machine. Replace module if issue not resolved. |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

The suggested action names a part to replace. **The knowledge base also holds a policy card saying individual parts are not replaced on the SRVO and that a whole new unit is sent.** The two have not been reconciled; check the current service policy before ordering anything.

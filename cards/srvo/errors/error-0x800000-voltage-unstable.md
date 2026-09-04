---
id: srvo-error-0x800000-voltage-unstable
title: 'Error 0x800000: voltage unstable'
kind: troubleshooting
question: What does error code 0x800000 mean on the SOLE SRVO?
asked_as:
- what does 0x800000 mean on the srvo
- srvo voltage unstable error
- srvo showing 0x800000
keywords:
- error code
- hex code
- voltage unstable
- current sampling
- motor control board
- flickering
- erratic
- fault
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x800000'
authority: 3
not_to_be_confused_with:
- srvo-error-0x80-fo-control-error
- srvo-error-0x800-low-voltage
- srvo-error-0x80000-encoder-value-error
- srvo-error-0x400-high-voltage
see_also:
- srvo-error-code-table
source:
  ref: sole-srvo-service-manual
  locator: page 44, section 9 Error Messages & Troubleshooting
  extracted_at: '2026-09-04'
---

**This is 0x800000, the voltage unstable code. It is not 0x80 (FO control error), 0x800 (Low voltage), 0x80000 (Encoder value error) and 0x400 (High voltage).**

| Field | Value |
|---|---|
| Error code | `0x800000` |
| Error message | Voltage unstable |
| Probable cause | Current sampling unstable voltage |
| Suggested action | Restart machine. Replace motor control board if issue is not resolved. |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

The suggested action names a part to replace. **The knowledge base also holds a policy card saying individual parts are not replaced on the SRVO and that a whole new unit is sent.** The two have not been reconciled; check the current service policy before ordering anything.

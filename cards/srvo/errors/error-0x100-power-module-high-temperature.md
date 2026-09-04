---
id: srvo-error-0x100-power-module-high-temperature
title: 'Error 0x100: power module high temperature'
kind: troubleshooting
question: What does error code 0x100 mean on the SOLE SRVO?
asked_as:
- what does 0x100 mean on the srvo
- srvo power module too hot
- srvo overheating error
keywords:
- error code
- hex code
- overheat
- high temperature
- overload
- power module
- cool down
- thermal
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '0x100'
authority: 3
not_to_be_confused_with:
- srvo-error-0x10000000-braking-control-error
- srvo-error-0x40000000-electrical-load
see_also:
- srvo-error-code-table
source:
  ref: sole-srvo-service-manual
  locator: page 44, section 9 Error Messages & Troubleshooting
  extracted_at: '2026-09-04'
---

**This is 0x100, the power module high temperature code. It is not 0x10000000 (Braking control error) and 0x40000000 (Electrical load).**

| Field | Value |
|---|---|
| Error code | `0x100` |
| Error message | Power module high temperature |
| Probable cause | Power module overload |
| Suggested action | Turn off machine to cool down |

Every code in the manual's table is a single bit in a hexadecimal word. The manual does not say whether two faults can be reported together, and it does not say where the code is shown: it names no display, no app screen and no debug output, so this card cannot tell you where to read it.

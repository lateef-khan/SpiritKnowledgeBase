---
id: srvo-error-code-table
title: The full list of servo fault codes
kind: troubleshooting
question: What are all the error codes on the SOLE SRVO?
asked_as:
- list of srvo error codes
- what error codes does the srvo have
- srvo fault code chart
keywords:
- error codes
- fault codes
- hex
- hexadecimal
- list
- chart
- troubleshooting
- diagnostics
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- srvo-error-0x40-power-module-low-voltage
- srvo-error-0x80-fo-control-error
- srvo-error-0x100-power-module-high-temperature
- srvo-error-0x400-high-voltage
- srvo-error-0x800-low-voltage
- srvo-error-0x40000-encoder-offset-error
- srvo-error-0x80000-encoder-value-error
- srvo-error-0x400000-encoder-not-connected
source:
  ref: sole-srvo-service-manual
  locator: page 44, section 9 Error Messages & Troubleshooting
  extracted_at: '2026-09-04'
---

Every code has its own card, because several of them differ only in the number of zeroes. Use this table to find the right one, then read that card.

| Error code | Error message | Probable cause | Suggested action |
|---|---|---|---|
| `0x40` | Power module low voltage | Defective power module/ Utility power low voltage | Restart machine. Replace module if issue not resolved. |
| `0x80` | FO control error | Power module defective/low voltage/ or short circuit | Turn off machine |
| `0x100` | Power module high temperature | Power module overload | Turn off machine to cool down |
| `0x400` | High voltage | Voltage too high for control module | Turn off machine, check bleeder resistor. |
| `0x800` | Low voltage | Voltage too low for control module | Turn off machine. Check utility power voltage. |
| `0x40000` | Encoder off set error | Defective encoder or loose contact | Turn off machine and check encoder |
| `0x80000` | Encoder value error | Defective encoder or loose contact | Turn off machine and check encoder |
| `0x400000` | Encoder not connected | Defective encoder or loose contact | Turn off machine and check encoder |
| `0x800000` | Voltage unstable | Current sampling unstable voltage | Restart machine. Replace motor control board if issue is not resolved. |
| `0x4000000` | UVW cord error | Cord loose contact | Turn off machine, plug in all cords securely. |
| `0x10000000` | Braking control error | Bleeder resistor overload | Turn off machine. Turn machine back on when motor is cooled. |
| `0x40000000` | Electrical load | Electrical load overload | Turn off machine. Turn machine back on when motor is cooled. |

The codes differ only in the number of zeroes: `0x40`, `0x400`, `0x40000`, `0x400000`, `0x4000000` and `0x40000000` are six different faults, and so are `0x80`, `0x800`, `0x80000` and `0x800000`. Count the zeroes before you act.

The manual does not say where these codes are displayed.

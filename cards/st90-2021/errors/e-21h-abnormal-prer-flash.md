---
id: st90-2021-e-21h-abnormal-prer-flash
title: 'E-21H on the inverter: abnormal prer flash'
kind: troubleshooting
question: What does E-21H mean on a Sole ST90-2021 treadmill?
asked_as:
- what does e-21h mean on my treadmill
- treadmill showing e-21h
- how do i fix e-21h
keywords:
- e-21h
- e21h
- abnormal prer flash
- inverter
- error code
- treadmill
- slat belt
facets:
  brand:
  - sole
  product_line: treadmill
  model: st90-2021
  applies_to:
  - st90-2021
  section: errors
  code: e-21h
authority: 3
not_to_be_confused_with:
- st90-2021-e-0ah-motor-overload
- st90-2021-e-22h-eeprom-error
see_also:
- sole-inverter-error-code-list
- st90-2021-inverter-error-code-list
source:
  ref: sole-tm-st90-2021-service-manual
  locator: Section 7-1 Error Codes, pages 29-30
  extracted_at: '2026-09-04'
---

**This is E-21H on the AC inverter, and it is not any other code that starts with the same characters.** PrEr is the inverter's flash memory. **The printed fix does not match the fault.** The manual answers a flash memory error with `Please lubricate running belt or check for bad bearing`, which is the same line it prints against the two overload codes. That is what the manual says; it is very likely a copy of the row above it. E-22H is the EEPROM error and is answered with `contact your dealer`.

| Field | Value |
|---|---|
| Code | E-21H |
| Description | Abnormal PrEr Flash |

The manual's cause column, word for word:

> Please lubricate running belt or check for bad bearing

The whole printed table is on the card `st90-2021-inverter-error-code-list`. This machine runs a Rhymebus AC inverter, so it does not use the E1 to E8 code set of the DC digital controller fitted to the F63, F65, F80, F85, F89 and TT8.

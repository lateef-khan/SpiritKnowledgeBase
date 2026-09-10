---
id: ct850-2020-e-21h-flash-program-defective
title: 'E-21H: flash program defective'
kind: troubleshooting
question: What does E-21H mean on a Spirit CT850-2020, CT850-2024 or CT850ENT-2024 treadmill?
asked_as:
- what does e-21h mean on my treadmill
- treadmill showing e-21h
- how do i fix e-21h
keywords:
- e-21h
- e21h
- prer
- flash
- firmware
- console replacement
- error code
- reboot
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct850-2020
  - ct850-2024
  - ct850ent-2024
  section: errors
  code: e-21h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-22h-eeprom-defective
- ct850-2020-e-26h-driver-setting-abnormal
see_also:
- st90-2021-e-21h-abnormal-prer-flash
- ct850-2020-inverter-error-code-list
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36)
  extracted_at: '2026-09-08'
---

**This is E-21H, and it is not any other code printed with the same characters.** `PrEr` is the short form the inverter itself shows. This is flash program memory; E-22H is the EEPROM.

| Field | Value |
|---|---|
| Code | E-21H |
| Cause, word for word | PrEr Flash program is defective. |
| Solution, word for word | Reboot the treadmill may restore or the console requires replacement. |

The whole printed table is on the card `ct850-2020-inverter-error-code-list`. The only tool section 8-2 asks for is a **multi-meter**.

**The CT850 2024 and CT850ENT 2024 owner's manuals print this row word for word**, cause
and solution alike, in the ERROR CODES table on printed page 42 of the CT850 2024 manual and
printed pages 60 and 61 of the CT850ENT 2024 manual. Both of those pages are flat pictures with
no text layer, and both were read from the rendered page. The 2024 books changed the machine
around this table but not the table: the whole twenty-three-code list is unchanged from the
2020 service manual.

---
id: st90-2023-e-51h-inter-communication-error
title: 'E-51H on the inverter: inter-communication error'
kind: troubleshooting
question: What does E-51H mean on a Sole ST90-2023 treadmill?
asked_as:
- what does e-51h mean on my treadmill
- treadmill showing e-51h
- how do i fix e-51h
keywords:
- e-51h
- e51h
- inter-communication error
- inverter
- error code
- treadmill
- slat belt
facets:
  brand:
  - sole
  product_line: treadmill
  model: st90-2023
  applies_to:
  - st90-2023
  section: errors
  code: e-51h
authority: 3
not_to_be_confused_with:
- st90-2023-e-22h-eeprom-error
- st90-2023-e-50h-communication-error
see_also:
- sole-inverter-error-code-list
- st90-2023-inverter-error-code-list
source:
  ref: sole-tm-st90-2023-service-manual
  locator: Section 7 Error Code List, page 15
  extracted_at: '2026-09-04'
---

**This is E-51H on the AC inverter, and it is not any other code that starts with the same characters.** This one is inside the console. E-50H is the console-to-inverter link and asks for a cable check; this one names no cable and sends the machine to the dealer.

| Field | Value |
|---|---|
| Code | E-51H |
| Description | Inter-communication error |

The manual's cause column, word for word:

> Internal communication error. Contact your SOLE dealer.

The whole printed table is on the card `st90-2023-inverter-error-code-list`. This machine runs an AC inverter, so it does not use the E1 to E8 code set of the DC digital controller fitted to the F63, F65, F80, F85, F89 and TT8.

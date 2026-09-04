---
id: st90-2023-e-50h-communication-error
title: 'E-50H on the inverter: communication error'
kind: troubleshooting
question: What does E-50H mean on a Sole ST90-2023 treadmill?
asked_as:
- what does e-50h mean on my treadmill
- treadmill showing e-50h
- how do i fix e-50h
keywords:
- e-50h
- e50h
- communication error
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
  code: e-50h
authority: 3
not_to_be_confused_with:
- st90-2023-e-07h-abnormal-pfc
- st90-2023-e-51h-inter-communication-error
see_also:
- sole-inverter-error-code-list
- st90-2023-inverter-error-code-list
source:
  ref: sole-tm-st90-2023-service-manual
  locator: Section 7 Error Code List, page 15
  extracted_at: '2026-09-04'
---

**This is E-50H on the AC inverter, and it is not any other code that starts with the same characters.** E-50H is the console losing the inverter. E-51H is a fault inside the console itself. The cable that carries this link is the 9-pin RM6T6A control cable between the console rack and the inverter's CONSOLE terminal.

| Field | Value |
|---|---|
| Code | E-50H |
| Description | Communication error |

The manual's cause column, word for word:

> Please check all cables.

The whole printed table is on the card `st90-2023-inverter-error-code-list`. This machine runs an AC inverter, so it does not use the E1 to E8 code set of the DC digital controller fitted to the F63, F65, F80, F85, F89 and TT8.

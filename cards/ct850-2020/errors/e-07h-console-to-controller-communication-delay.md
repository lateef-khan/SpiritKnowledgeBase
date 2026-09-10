---
id: ct850-2020-e-07h-console-to-controller-communication-delay
title: 'E-07H: console to controller communication delay'
kind: troubleshooting
question: What does E-07H mean on a Spirit CT850-2020, CT850-2024 or CT850ENT-2024 treadmill?
asked_as:
- what does e-07h mean on my treadmill
- treadmill showing e-07h
- how do i fix e-07h
keywords:
- e-07h
- e07h
- communication
- console
- controller
- delay
- error code
- wiring
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
  code: e-07h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-50h-console-controller-communication-abnormal
- ct850-2020-e-51h-communication-inside-console-abnormal
see_also:
- st90-2021-e-07h-abnormal-pfc
- ct850-2020-inverter-error-code-list
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36)
  extracted_at: '2026-09-08'
---

**This is E-07H, and it is not any other code printed with the same characters.** Sole's ST90 prints E-07H with a completely different meaning, `Abnormal PFC`. Do not carry the ST90 answer across to this machine.

| Field | Value |
|---|---|
| Code | E-07H |
| Cause, word for word | The communication from console to the controller is delay. |
| Solution, word for word | Check all the wires from the controller board to the console. |

The whole printed table is on the card `ct850-2020-inverter-error-code-list`. The only tool section 8-2 asks for is a **multi-meter**.

**The CT850 2024 and CT850ENT 2024 owner's manuals print this row word for word**, cause
and solution alike, in the ERROR CODES table on printed page 42 of the CT850 2024 manual and
printed pages 60 and 61 of the CT850ENT 2024 manual. Both of those pages are flat pictures with
no text layer, and both were read from the rendered page. The 2024 books changed the machine
around this table but not the table: the whole twenty-three-code list is unchanged from the
2020 service manual.

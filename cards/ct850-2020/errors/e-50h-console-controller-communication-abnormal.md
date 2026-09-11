---
id: ct850-2020-e-50h-console-controller-communication-abnormal
title: 'E-50H: console to controller communication abnormal'
kind: troubleshooting
question: What does E-50H mean on a Spirit CT800-2020, CT850-2020, CT850-2024, CT850ENT-2022
  or CT850ENT-2024 treadmill, and what did the service bulletin do about it?
asked_as:
- what does e-50h mean on my treadmill
- treadmill showing e-50h
- how do i fix e-50h
keywords:
- e-50h
- e50h
- communication
- console
- controller
- error code
- wiring
- abnormal
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct850-2020
  - ct850-2024
  - ct850ent-2022
  - ct850ent-2024
  section: errors
  code: e-50h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-51h-communication-inside-console-abnormal
- ct850-2020-e-07h-console-to-controller-communication-delay
see_also:
- st90-2021-e-50h-communication-error
- ct850-2020-inverter-error-code-list
- spirit-2024-errors-e5-console-to-driver-board-link-interrupted
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36); CT850ENT 2022 service
    manual 8-1 Error code items, PDF p. 31-32, text.md lines 563-618; spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGE 5 (remedy card); spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGE 4 (JK6 note); spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGES 3 and 6 (photographs)
  extracted_at: '2026-09-08'
---

**This is E-50H, and it is not any other code printed with the same characters.** E-50H is the link between the console and the controller; E-51H is inside the console; E-07H is the same link merely running late.

| Field | Value |
|---|---|
| Code | E-50H |
| Cause, word for word | The communication from console to the controller is abnormal. |
| Solution, word for word | Check all the wires from the controller board to the console. |

The whole printed table is on the card `ct850-2020-inverter-error-code-list`. The only tool section 8-2 asks for is a **multi-meter**.

**The CT850 2024 and CT850ENT 2024 owner's manuals print this row word for word**, cause
and solution alike, in the ERROR CODES table on printed page 42 of the CT850 2024 manual and
printed pages 60 and 61 of the CT850ENT 2024 manual. Both of those pages are flat pictures with
no text layer, and both were read from the rendered page. The 2024 books changed the machine
around this table but not the table: the whole twenty-three-code list is unchanged from the
2020 service manual.

**The CT850ENT 2022 service manual prints this row word for word** in its 8-1 table.

**A Spirit service bulletin is about this code on a CT800 #800840 (the CT800 2020)** - `spirit-treadmill-ct800-2020-e50h-service-bulletin`, headed *Spirit TM CT800 #800840 E-50H* and photographing a console whose dot-matrix window reads `E-50H` at start-up. Its remedy card, headed for the *New C[T800&CT850(2020)]*, reads:

> E-50H: Communication error between console and transformer. Solution: a). Checking wiring. b). Replacing a new transformer. c). Replacing a new console.

"Transformer" is the bulletin's word for the lower drive board. The bulletin then gives the repair it actually made: **the upper computer cable must be plugged into the JK6/STD red 6-pin port** on the lower controller (the note reads *The upper computer cable, SP# must be plugged into the JK6/ STD red 6-pin port*), and the console cable was replaced with a **middle computer cable with a heavier insulated jacket, plus a zip tie anchor at the right console support bracket** - photographed hanging beside the spare-parts cartons. So the field fix for E-50H on that machine was the console cable and its routing, before any board.

The CT800 2020 service manual's own pin table names JK11 as the *STD Main Connector (for CT800(2020))* and JK9 as the *RM6T3 Main Connector (for CT850(2020))*; the bulletin's `JK6/STD` is the connector on the driver board end. That manual prints only the seven DC codes and no E-50H, so for the CT800 2020 this code rests on the bulletin.

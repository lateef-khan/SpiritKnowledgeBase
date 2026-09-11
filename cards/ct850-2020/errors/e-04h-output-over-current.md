---
id: ct850-2020-e-04h-output-over-current
title: 'E-04H: output over current'
kind: troubleshooting
question: What does E-04H mean on a Spirit CT800-2020, CT850-2020, CT850-2024, CT850ENT-2022
  or CT850ENT-2024 treadmill?
asked_as:
- what does e-04h mean on my treadmill
- treadmill showing e-04h
- how do i fix e-04h
keywords:
- e-04h
- e04h
- over current
- overcurrent
- motor stuck
- inverter
- error code
- drive belt
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
  code: e-04h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-0ah-motor-overcurrent
- ct850-2020-e-0bh-inverter-overcurrent
- ct850-2020-e-0ch-system-overcurrent
- ct850-2020-e-41h-system-overload
see_also:
- st90-2021-e-04h-overcurrent
- ct850-2016-running-deck-belt-and-cushion-replacement
- ct850-2020-inverter-error-code-list
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36); CT850ENT 2022 service
    manual 8-1 Error code items, PDF p. 31-32, text.md lines 563-618; spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGE 2 (AC list, "For A/C Transforming System")
  extracted_at: '2026-09-08'
---

**This is E-04H, and it is not any other code printed with the same characters.** This is the code for something physically jamming the drive train.

| Field | Value |
|---|---|
| Code | E-04H |
| Cause, word for word | Output over current. |
| Solution, word for word | Check if the motor, driver belt, rollers, and running belt cause the motor stuck. |

The whole printed table is on the card `ct850-2020-inverter-error-code-list`. The only tool section 8-2 asks for is a **multi-meter**.

The deck, belt and roller work this solution asks for is on `ct850-2016-running-deck-belt-and-cushion-replacement`.

**The CT850 2024 and CT850ENT 2024 owner's manuals print this row word for word**, cause
and solution alike, in the ERROR CODES table on printed page 42 of the CT850 2024 manual and
printed pages 60 and 61 of the CT850ENT 2024 manual. Both of those pages are flat pictures with
no text layer, and both were read from the rendered page. The 2024 books changed the machine
around this table but not the table: the whole twenty-three-code list is unchanged from the
2020 service manual.

**The CT850ENT 2022 service manual prints this row word for word** in its 8-1 Error code items table, so the 2024 books inherited it from there.

**A Spirit service bulletin on the CT800 #800840 (`spirit-treadmill-ct800-2020-e50h-service-bulletin`) photographs the same list under a card headed *ERROR MESSAGE of New CT800&CT850(2020) - For A/C Transforming System***, with a shorter label for this code - *E-04H: (OC) Transformer over output current* - and one solution for the whole list: *all above are related with transformer error, so please check the wiring first before replace a new transformer.* "Transformer" is the bulletin's word for the inverter. On the strength of that heading the card carries the CT800 2020 as well; note that the CT800 2020 service manual itself prints the seven-code DC list and none of these (`spirit-2024-errors-seven-code-table-with-no-hyphen`), so for the CT800 2020 this code rests on the bulletin's heading alone.

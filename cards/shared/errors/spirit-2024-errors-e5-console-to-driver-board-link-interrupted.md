---
id: spirit-2024-errors-e5-console-to-driver-board-link-interrupted
title: E5 means the link between console and driver board is interrupted, and the
  remedy is every wire in it
kind: troubleshooting
question: What does E5 mean on a Spirit CT800-2020, CT800-2024, CT800ENT-2022 or CT800ENT-2024
  treadmill?
asked_as:
- what does e5 mean on my spirit treadmill
- treadmill showing e5
- how do i fix e5 on a spirit treadmill
keywords:
- e5
- communication
- console
- driver board
- controller
- wires
- interrupted
- error code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct800-2024
  - ct800ent-2022
  - ct800ent-2024
  - ct850-2020
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- ce800ent-e5-console-controller-communication
- ces880-2025-errors-e5-console-to-controller-connection
- ct850-2020-e-50h-console-controller-communication-abnormal
- ct850-2020-e-07h-console-to-controller-communication-delay
- f65-2016-e5-communication-error
see_also:
- spirit-2024-errors-seven-code-table-with-no-hyphen
source:
  ref: spirit-treadmill-ct800-2024-owners-manual
  locator: ERROR CODES, printed page 42 of the CT800 2024 owner's manual and printed
    page 60 of the CT800ENT 2024 owner's manual. Both pages are flat pictures with
    no text layer and were read from the rendered page; CT800 2020 service manual
    8-1 Error Codes, PDF p. 35 (printed 34), text.md lines 467-474; CT800ENT 2022
    service manual 8-1 Error code items, PDF p. 31, text.md lines 574-599; spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGE 1 (DC list headed "ERROR MESSAGE of New CT800&CT850(2020)")
  extracted_at: '2026-09-10'
---

| Field | CT800 2024 | CT800ENT 2024 |
|---|---|---|
| Cause | The communication from console to the controller is defective. | The connection between Console and Driver Board is interrupted or abnormal. |
| Solution | Check all the wires from the controller board to the console. | Check all wires are connecting well and not damaged. |

**Neither book names a board to replace.** The whole remedy is the wiring between the two boards.

**Other Spirit machines print `E5` for a communication fault, and none of them means quite this.**
The CE800ENT, CE800ENT 2024, CR800ENT 2024 and CU800ENT 2024 define it as *poor* communication and
name the main control wire as the first suspect
(`ce800ent-e5-console-controller-communication`); the CES880 2025 defines it as an abnormal
connection and prints a parts table
(`ces880-2025-errors-e5-console-to-controller-connection`). The CT850 2024 and CT850ENT 2024 of this
same 2024 family have no `E5` at all - their inverter table splits the same fault into `E-07H` for a
delay and `E-50H` for an abnormality
(`ct850-2020-e-07h-console-to-controller-communication-delay`,
`ct850-2020-e-50h-console-controller-communication-abnormal`).

Sole uses `E5` for a communication error on its treadmills too, on a different controller
(`f65-2016-e5-communication-error`).

**The two service manuals print these rows word for word.** The CT800 2020 service manual's 8-1 Error Codes table carries the CT800 2024 wording, and the CT800ENT 2022 service manual's 8-1 Error code items table carries the CT800ENT 2024 wording, so both readings of E5 are two generations old.

**A Spirit service bulletin on the CT800 #800840 (`spirit-treadmill-ct800-2020-e50h-service-bulletin`) photographs an error card headed *ERROR MESSAGE of New CT800&CT850(2020)* that lists this code under *For D/C Motor Controlling System*.** Its wording is shorter than either manual's: *E5: Communication error between console/control board.* The bulletin's page 4 adds a wiring note for the CT800 #800840: *The upper computer cable, SP# must be plugged into the JK6/STD red 6-pin port* on the lower controller. On the strength of that heading the card carries both the CT800 2020 and the CT850 2020; note that the CT850 2020 service manual itself prints only the twenty-three `E-xxH` inverter codes and no DC-controller list (`ct850-2020-inverter-error-code-list`), so for the CT850 2020 this code rests on the bulletin's heading alone.

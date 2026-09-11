---
id: spirit-2024-errors-e6-driver-board-defective
title: E6 says the driver board is defective, and yet both books only ask you to check
  its wiring
kind: troubleshooting
question: What does E6 mean on a Spirit CT800-2020, CT800-2024, CT800ENT-2022 or CT800ENT-2024
  treadmill?
asked_as:
- what does e6 mean on my spirit treadmill
- treadmill showing e6
- how do i fix e6 on a spirit treadmill
keywords:
- e6
- driver board
- controller board
- defective
- wires
- replace
- error code
- lower board
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
  code: e6
authority: 3
not_to_be_confused_with:
- f85-2019-e6-lower-controller-error
- spirit-2024-errors-e5-console-to-driver-board-link-interrupted
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
| Cause | The controller board is defective. | Driver Board is defective. |
| Solution | Check all the wires of the controller board | Check all wires are connecting well and not damaged. |

**The cause and the solution do not agree, in both books.** The cause condemns the board outright;
the solution asks only that its wiring be checked, and neither manual says what to do when the
wiring is sound. Read it as: check the wiring first, and treat a board replacement as the unstated
next step.

The neighbouring code `E5` covers the wiring *between* console and driver board
(`spirit-2024-errors-e5-console-to-driver-board-link-interrupted`); this one is about the board
itself.

Sole's F85 uses `E6` for a lower controller error (`f85-2019-e6-lower-controller-error`).

**The two service manuals print these rows word for word.** The CT800 2020 service manual's 8-1 Error Codes table carries the CT800 2024 wording, and the CT800ENT 2022 service manual's 8-1 Error code items table carries the CT800ENT 2024 wording, so both readings of E6 are two generations old.

**A Spirit service bulletin on the CT800 #800840 (`spirit-treadmill-ct800-2020-e50h-service-bulletin`) photographs an error card headed *ERROR MESSAGE of New CT800&CT850(2020)* that lists this code under *For D/C Motor Controlling System*.** Its wording is shorter than either manual's: *E6: Control board malfunction.*. On the strength of that heading the card carries both the CT800 2020 and the CT850 2020; note that the CT850 2020 service manual itself prints only the twenty-three `E-xxH` inverter codes and no DC-controller list (`ct850-2020-inverter-error-code-list`), so for the CT850 2020 this code rests on the bulletin's heading alone.

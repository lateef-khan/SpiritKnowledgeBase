---
id: spirit-2024-errors-e4-drive-motor-input-voltage-abnormal
title: E4 means the drive motor input voltage is abnormal or its wires are not connected
kind: troubleshooting
question: What does E4 mean on a Spirit CT800-2020, CT800-2024, CT800ENT-2022 or CT800ENT-2024
  treadmill?
asked_as:
- what does e4 mean on my spirit treadmill
- treadmill showing e4
- how do i fix e4 on a spirit treadmill
keywords:
- e4
- motor voltage
- abnormal voltage
- motor wires
- controller board
- connector
- error code
- drive motor
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
  code: e4
authority: 3
not_to_be_confused_with:
- f85-2019-e4-motor-power-wire-error
- ct850-2020-e-23h-low-voltage
- spirit-2024-errors-e7-abnormal-ac-input-voltage
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
| Cause | The voltage of the motor abnormal or the wires of the motor doesn't connect. | Drive motor input voltage is abnormal or the connection of Drive motor wires is not well. |
| Solution | Check the wires of the motor and replug to the controller board. | Check all wires are connecting well and not damaged. |

**Both books answer it entirely at the motor wiring**, and neither asks for a voltage measurement
even though the cause names a voltage. The CT800 2024 is the more specific of the two: it names the
**controller board** as the end to re-plug.

**This is about the motor's supply, not the wall supply.** The wall supply has its own code in the
same table - `E7` (`spirit-2024-errors-e7-abnormal-ac-input-voltage`).

Sole's F85 uses `E4` for a motor power wire error, which is the same kind of fault on a different
machine (`f85-2019-e4-motor-power-wire-error`).

**The two service manuals print these rows word for word.** The CT800 2020 service manual's 8-1 Error Codes table carries the CT800 2024 wording, and the CT800ENT 2022 service manual's 8-1 Error code items table carries the CT800ENT 2024 wording, so both readings of E4 are two generations old.

**A Spirit service bulletin on the CT800 #800840 (`spirit-treadmill-ct800-2020-e50h-service-bulletin`) photographs an error card headed *ERROR MESSAGE of New CT800&CT850(2020)* that lists this code under *For D/C Motor Controlling System*.** Its wording is shorter than either manual's: *E4: Abnormal voltage input to motor or wrong wiring between motor/control board.*. On the strength of that heading the card carries both the CT800 2020 and the CT850 2020; note that the CT850 2020 service manual itself prints only the twenty-three `E-xxH` inverter codes and no DC-controller list (`ct850-2020-inverter-error-code-list`), so for the CT850 2020 this code rests on the bulletin's heading alone.

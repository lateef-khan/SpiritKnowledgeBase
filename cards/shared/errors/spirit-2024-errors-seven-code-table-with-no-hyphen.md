---
id: spirit-2024-errors-seven-code-table-with-no-hyphen
title: Every error code these treadmills can show, a seven-row table numbered without
  a hyphen
kind: spec
question: What error codes can a Spirit CT800-2020, CT800-2024, CT800ENT-2022 or CT800ENT-2024
  treadmill display and what does each one mean?
asked_as:
- list of error codes for my spirit treadmill
- what do the e codes mean on a ct800
- spirit treadmill error code table
keywords:
- error code
- error code table
- list
- index
- console
- treadmill
- seven codes
- diagnosis
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
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-inverter-error-code-list
- ct900-error-code-table
- ct850-2016-error-code-items-list
see_also:
- spirit-2024-errors-e1-no-speed-sensor-signal
- spirit-2024-errors-e1-drive-motor-no-output-signal
- spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
- spirit-2024-errors-e3-incline-motor-wires-then-calibration
- spirit-2024-errors-e4-drive-motor-input-voltage-abnormal
- spirit-2024-errors-e5-console-to-driver-board-link-interrupted
- spirit-2024-errors-e6-driver-board-defective
- spirit-2024-errors-e7-abnormal-ac-input-voltage
- spirit-2024-errors-replace-safety-key-message
- spirit-2024-errors-safety-lock-child-mode
- ct850-2020-inverter-error-code-list
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

Seven codes, each with its own card; this table is only the index. **Both books number them `E1` to
`E7`, with no hyphen and no trailing `H`** - which is what tells them apart from the CT850's codes at
a glance.

**CT800 2024, word for word:**

| Code | Cause | Solution |
|---|---|---|
| E1 | The console does not receive signal from the speed sensor. | 1. Check and plug the wires of the motor. 2. Check and plug the wire of speed sensor. 3. Replace the speed sensor. |
| E2 | The overcurrent of the controller to the motor. | The running belt is worn need lubricate or replacement. |
| E3 | The incline motor can't work normally. | 1. Check and plug all the wires of the incline motor to the controller board. 2. Doing the calibration procedure. |
| E4 | The voltage of the motor abnormal or the wires of the motor doesn't connect. | Check the wires of the motor and replug to the controller board. |
| E5 | The communication from console to the controller is defective. | Check all the wires from the controller board to the console. |
| E6 | The controller board is defective. | Check all the wires of the controller board |
| E7 | Abnormal AC input voltage. | Check the AC input voltage is stable 100~120V. |

**CT800ENT 2024, word for word:**

| Code | Cause | Troubleshooting |
|---|---|---|
| E1 | Drive motor didn't send output signal during workout. | Check all the wires which from Drive motor connect well. |
| E2 | Drive motor current is overload to trigger the protection of Driver Board. | Check the situation of Running Belt and Deck; try to apply Lube between Running Belt and Running Deck. |
| E3 | Incline motor did not work correctly. | To do the Calibration Procedure and check Incline motor wires connection. |
| E4 | Drive motor input voltage is abnormal or the connection of Drive motor wires is not well. | Check all wires are connecting well and not damaged. |
| E5 | The connection between Console and Driver Board is interrupted or abnormal. | Check all wires are connecting well and not damaged. |
| E6 | Driver Board is defective. | Check all wires are connecting well and not damaged. |
| E7 | The AC input voltage is abnormal. | Check whether the wall socket provides a stable voltage of about 100~120V. |

Three things to know before using either table.

- **The two books do not mean the same thing by `E1`.** The CT800 2024 blames the speed sensor and
  offers it as a replacement part; the CT800ENT 2024 blames the drive motor's output signal and asks
  only about wiring. They are two cards for that reason.
- **The CT800ENT 2024 table carries two further rows that are not codes** - `Replace Safety Key` and
  `SAFETY LOCK`. They are on `spirit-2024-errors-replace-safety-key-message` and
  `spirit-2024-errors-safety-lock-child-mode`. The CT800 2024 table stops at E7.
- **`LS` is not in either table.** It is the code the same books print in their TROUBLESHOOTING
  chapter for a motor that does not respond, and nothing joins the two chapters up.

**The CT850 2024 and CT850ENT 2024 of the same 2024 family use a completely different family of
codes** - twenty-three of them, written `E-01H` through `E-52H` plus a bare `E3`
(`ct850-2020-inverter-error-code-list`). Only `E3` exists in both, and it means the incline motor in
both, with a different remedy in each. Never answer a CT850 from this table or a CT800 from that one.

**Both tables were printed in the service manuals two years earlier, word for word.** The CT800 2020 service manual's 8-1 Error Codes table is the CT800 2024 table above, cause and solution alike; the CT800ENT 2022 service manual's 8-1 Error code items table is the CT800ENT 2024 table, and it already carries the `Replace Safety Key` and `SAFETY LOCK` rows. So the two meanings of `E1` are two generations old, not a 2024 change.

**A Spirit service bulletin adds a third, shorter wording.** The photographed card in `spirit-treadmill-ct800-2020-e50h-service-bulletin`, headed *ERROR MESSAGE of New CT800&CT850(2020) - For D/C Motor Controlling System*, lists: E1 No out put from motor; E2 Overloading protection; E3 Incline Error; E4 Abnormal voltage input to motor or wrong wiring between motor/control board; E5 Communication error between console/control board; E6 Control board malfunction; E7 Abnormal voltage input to control board from house power. The same card's second half is the CT850's `E-xxH` list. Its heading is the only document that puts this DC list on a CT850 2020; that machine's own service manual prints the inverter list and nothing else.

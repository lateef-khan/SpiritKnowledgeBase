---
id: xterra-treadmill-errors-owner-error-messages-seven-codes-incline-printed-three-ways
title: The seven Error Messages in the owner's manual, with the incline error printed
  as a plain code, Er or ERR depending on the book
kind: spec
question: What error messages can an Xterra tr300-2021, trx2500-2024, trx3500-2024
  or trx4500-2024 treadmill show, and what does each mean?
asked_as:
- xterra error messages list
- what does er mean on my xterra treadmill
- trx error code meanings
keywords:
- error messages
- error code list
- safety key
- speed signal
- rated current
- incline error
- motor voltage
- communication
- power malfunction
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr300-2021
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- trx1400-2023-errors-owner-error-code-guide-seven-codes
- spirit-xt-errors-error-code-list-eight-codes
see_also:
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
- xterra-treadmill-errors-owner-checklist-seven-codes-safety-key-to-abnormal-power
source:
  ref: xterra-treadmill-trx2500-2024-owners-manual
  locator: TRX2500 OM Error Messages, PDF p. 21 (printed 19); text.md lines 695-741;
    TRX3500 OM Error Messages, PDF p. 23 (printed 21); text.md lines 818-866; TRX4500
    OM Error Messages, PDF p. 24 (printed 22); text.md lines 901-948; TR300 OM Error
    Messages, PDF p. 24 (printed 22); text.md lines 876-895
  extracted_at: '2026-09-11'
---

Four owner's manuals print a short *Error Messages* list of seven lines. The lines are the same in all four books except the incline line, whose code is printed three different ways, and the speed line, which the TR300 book words without the word "calibration".

| Code | Printed meaning | Books |
|---|---|---|
| E0 | Safety Key is not in place. A reminder to put in the safety key (TR300: "Safety switch is open. A reminder of putting on the safety key") | all four |
| E1 | Treadmill calibration did not receive a speed signal for 10 seconds (TR300: "Treadmill stops when there is no speed signal received 10 secons after start") | all four |
| E2 | Over the rated current. The controller is over the rated current for 3 seconds | all four |
| E3 / Er / ERR | Incline Error | TR300 prints **E3**; TRX2500 prints **Er**; TRX3500 and TRX4500 print **ERR** |
| E4 | Motor voltage surge or motor is disconnected | all four |
| E5 | Communication is disconnected | all four |
| E6 | Power malfunction | all four |

No E7 is printed in these four books. The TRX2500, TRX3500 and TRX4500 service manuals print an eight-code table in which **E6 is a lower control board fault and E7 is the low or unstable voltage code** - the owner's "E6 Power malfunction" does not match its own service manual; see `xterra-treadmill-errors-e6-lower-controller-component-fault`.

Detail per code: `xterra-treadmill-errors-e0-safety-switch-malfunction-owner-checks`, `xterra-treadmill-errors-e1-no-speed-signal-for-10-seconds-owner-list`, `xterra-treadmill-errors-e2-over-rated-current-for-3-seconds`, `xterra-tr-errors-e3-incline-error-owner-checks`, `trx2500-2024-errors-er-incline-vr-out-of-range`, `xterra-trx-errors-err-incline-vr-out-of-range`.

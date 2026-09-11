---
id: trx1400-2023-errors-owner-error-code-guide-seven-codes
title: 'The owner''s Error Code Guide: seven codes, with the overload trip at 6 seconds
  and ERR for a disconnected incline motor'
kind: spec
question: What error codes can an Xterra trx1400-2023 treadmill show, and what does
  each mean according to the owner's manual?
asked_as:
- trx1400 error codes
- what does err mean on the trx1400
- xterra error code guide
keywords:
- error code guide
- error code list
- safety switch
- speed signal
- overload
- power transistor
- incline motor
- communication
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: errors
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-owner-error-messages-seven-codes-incline-printed-three-ways
- spirit-xt-errors-error-code-list-eight-codes
see_also:
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
- trx1400-2023-errors-err-or-e3-incline-vr-out-of-range
source:
  ref: xterra-treadmill-trx1400-2023-owners-manual
  locator: TRX1400 OM Troubleshooting, Error Code Guide, PDF p. 39 (printed 38); text.md
    lines 1285-1305; TRX1400 SM 8. Error code items, PDF p. 37 (printed 35); text.md
    lines 564-591
  extracted_at: '2026-09-11'
---

The owner's manual prints an *Error Code Guide* of seven rows:

| Error number | Solution / cause printed |
|---|---|
| E0 | Safety switch is open. Put on the safety key to eliminate the error |
| E1 | Speed signal is not received during calibration. Treadmill stops automatically after 10 seconds |
| E2 | E2 Overload error. Controller detected over rated current for **6 seconds** |
| E4 | Abnormal motor voltage or motor disconnected |
| E5 | Communication disconnected |
| E6 | Power transistor failure |
| ERR | Incline motor disconnected or damaged |

Two things differ from the other Xterra owner's manuals. The overload trip is printed as 6 seconds here and 3 seconds in the TR300, TRX2500, TRX3500 and TRX4500 books. E6 is "Power transistor failure" here, "Power malfunction" in those books, and "Lower controller error" in this machine's own service manual (which also lists an E7 input-power code the owner's manual omits, and prints the incline code as **Err**).

Detail per code: `xterra-treadmill-errors-e0-safety-switch-malfunction-owner-checks`, `xterra-treadmill-errors-e1-no-speed-signal-for-10-seconds-owner-list`, `trx1400-2023-errors-e2-overload-over-rated-current-for-6-seconds`, `trx1400-2023-errors-err-or-e3-incline-vr-out-of-range`, `xterra-treadmill-errors-e4-motor-power-wires-not-in-lower-controller`, `xterra-treadmill-errors-e5-console-controller-communication-poor`, `xterra-treadmill-errors-e6-lower-controller-component-fault`.

---
id: ct800ent-2022-errors-e3-incline-vr-out-of-range-section
title: 'E3: the incline VR voltage missing or out of range, checked at the VR, the
  display board, the console cable and the incline'
kind: troubleshooting
question: What does section 8-3 say E3 means on a Spirit ct800ent-2022 treadmill,
  and what does it check?
asked_as:
- what does e3 mean on my ct800ent
- ent treadmill showing e3 incline
- incline vr voltage check on the touchscreen treadmill
keywords:
- e3
- incline
- vr voltage
- out of range
- incline vr
- display board
- console cable
- up relay
- down relay
- ent
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800ent-2022
  applies_to:
  - ct800ent-2022
  section: errors
  code: e3
  model_number:
  - '800852'
authority: 3
not_to_be_confused_with:
- ct850-2020-e3-incline-motor-cannot-work
- ct800-2020-errors-e3-incline-vr-out-of-range-printed-with-the-incline-err-table
- ct850-2020-incline-err
see_also:
- spirit-2024-errors-e3-incline-motor-wires-then-calibration
- ct850-2020-incline-err
- ct850-2016-incline-err-shown-in-incline-window
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: 'CT800ENT 2022 service manual 8-3 Error Message: E3, PDF p. 33, text.md
    lines 615-644'
  extracted_at: '2026-09-11'
---

**This is the CT800ENT 2022 service manual's E3 section.** Its 8-1 table row for E3 - *Incline motor did not work correctly / To do the Calibration Procedure and check Incline motor wires connection* - is on `spirit-2024-errors-e3-incline-motor-wires-then-calibration`, which the 2024 owner's manual inherited from this book.

Definition: *The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. "E3" appears on the display.* The configuration drawing shows the incline motor's `INCLINE VR SET` feeding the driver board and the display board, and the driver board's `INCLINE DOWN RELAY` and `INCLINE UP RELAY`.

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and console cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| Console cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Incline | Inspect the display board console cable connections. |

This is the CT850 2020's E3 table (`ct850-2020-e3-incline-motor-cannot-work`), printed here for a DC-drive machine whose 8-1 row says something shorter. No cause page and no flow chart are printed; the section is one page, with the INCLINE ERR section on the next (`ct850-2020-incline-err`). The CT800 2020 service manual, the non-touch-screen sibling, prints a different E3 section again (`ct800-2020-errors-e3-incline-vr-out-of-range-printed-with-the-incline-err-table`).

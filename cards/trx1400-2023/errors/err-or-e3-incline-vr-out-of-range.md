---
id: trx1400-2023-errors-err-or-e3-incline-vr-out-of-range
title: 'Err: the console is not reading the incline VR voltage or the incline motor
  has no power, checked at the incline keys, the incline cables and the driver board'
kind: troubleshooting
question: What does Err (the book also calls it E3) mean on an Xterra trx1400-2023
  treadmill, and what should I check?
asked_as:
- err on my trx1400
- trx1400 incline error err
- trx1400 e3 incline
keywords:
- err
- e3
- incline error
- vr voltage
- incline motor no power
- incline keys stuck
- incline power cable
- vr cable
- driver board
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: errors
  code: err
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- trx2500-2024-errors-er-incline-vr-out-of-range
- xterra-trx-errors-err-incline-vr-out-of-range
- xterra-tr-errors-e3-jkexer-poor-communication-upper-lower-controller
see_also:
- trx1400-2023-errors-incline-test-procedure-nine-steps
- trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs
- xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
- trx1400-2023-errors-owner-error-code-guide-seven-codes
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: 'TRX1400 SM 8.4 Error Message: Err or E3, Case of Err and Troubleshooting,
    PDF pp. 45-47 (printed 44-46); text.md lines 732-782; TRX1400 OM Troubleshooting,
    Error Code Guide, PDF p. 39 (printed 38); text.md lines 1285-1305'
  extracted_at: '2026-09-11'
---

**This is the TRX1400's incline VR fault, which its service manual heads "8.4 Error Message: Err or E3" and its code table lists as Err.** The owner's manual prints "ERR - Incline motor disconnected or damaged". The same fault carries a different troubleshooting table on the other Dyaco books (`xterra-treadmill-errors-e3-incline-vr-out-of-range`, `trx2500-2024-errors-er-incline-vr-out-of-range`, `xterra-trx-errors-err-incline-vr-out-of-range`).

*Definition.* The console board is not detecting the VR voltage value, or the voltage value has exceeded the range; "Err or E3" appears on the display. The code table adds "or the incline's motor no power". The incline VR signal travels over TX/RX of the main control lines.

*Case of Err.* The incline VR value exceeds the range and Err appears: the incline motor is not operating up or down, making the VR value exceed the range; after turning on the unit, the display board detects that the incline VR voltage exceeds the range, so Err appears. Action flow chart: incline VR -> driver board (VR voltage?) -> cable -> display board -> display operates normally, or ERR appears.

*Troubleshooting*

| Part | Troubleshooting |
|---|---|
| Display board | 1. Check whether the incline keys are stuck |
| Incline power cable and incline VR cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again |
| Driver board | 1. Replace the driver board |

The book then prints the console-to-driver-board pin definition (1 SW, 2 VDD, 3 TXD, 4 RXD, 5 GND), the incline motor leads (COM white, UP red, DOWN black) and the 3-pin VR wires (GND, sensor pin AD, +5 V VCC), followed by a nine-step test procedure with voltages - `trx1400-2023-errors-incline-test-procedure-nine-steps`. The error raised while the incline is moving is `trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs`.

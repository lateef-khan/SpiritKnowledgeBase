---
id: trx2500-2024-errors-er-incline-vr-out-of-range
title: 'ER: the console is not reading the incline VR voltage, or it is out of range,
  with the VR, display board, 5-pin cable and driver board checks'
kind: troubleshooting
question: What does ER (or Er) mean on an Xterra trx2500-2024 treadmill, and what
  should I check?
asked_as:
- er on my trx2500
- trx2500 shows er incline
- er incline error xterra
keywords:
- er
- incline error
- vr voltage
- position sensor
- potentiometer
- 5-pin cable
- driver board
- incline up led
- incline down led
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx2500-2024
  applies_to:
  - trx2500-2024
  section: errors
  code: er
  model_number:
  - '125817'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- xterra-trx-errors-err-incline-vr-out-of-range
- trx1400-2023-errors-err-or-e3-incline-vr-out-of-range
see_also:
- xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs
- xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
- xterra-treadmill-errors-owner-error-messages-seven-codes-incline-printed-three-ways
- f60-2016-incline-er-message
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM 8.4 Error Message: ER, Case of ER, Troubleshooting and Test
    Configuration, PDF pp. 46-49 (printed 45-48); text.md lines 762-846; TRX2500 OM
    Error Messages, PDF p. 21 (printed 19); text.md lines 695-741'
  extracted_at: '2026-09-11'
---

**This is ER, the TRX2500's label for the incline VR fault.** The owner's manual prints it as "Er Incline Error". The same fault is E3 on the TR260 and TRX5500, ERR on the TRX3500 and TRX4500, and "Err or E3" on the TRX1400 - see the cards named below; the procedure is the same on all of them.

*Definition.* The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. "ER" appears on the display.

*Cause.* The incline VR value exceeds the range. The incline motor is not operating up or down, making the VR value exceed the range; after turning on the unit, the display board detects that the incline VR voltage exceeds the range, so ER appears. The action flow chart draws: incline VR -> driver board (VR voltage?) -> cable (VR voltage?) -> display board -> the display operates normally, or ERR appears on the display.

*Troubleshooting*

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect the VR wires. 2. Inspect whether the incline wires are broken or disconnected |
| Display board | 1. Inspect the incline wire and 5-pin cable connections. 2. Test whether the VR voltage varies at the incline wire terminal |
| 5-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again |
| Driver board | Inspect the display board 5-pin connections |

*Test configuration - incline motor control parts.* The incline motor's power leads are **COM white, DOWN black, UP red**. The position sensor (VR) wires are **red = ground, white = position signal, black = 5 V DC**, the signal reading 0 to 5 V depending on incline position. The 5-pin main control connector is 1 SW, 2 +12V, 3 TXD, 4 RXD, 5 GND.

The error raised while the incline is moving is INCLINE ER: `xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs`. The matrix row "INCLINE ER, INCLINE window displays ER" is `xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate`.

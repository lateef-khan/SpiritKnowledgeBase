---
id: xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
title: 'Err in the incline window: the incline VR voltage is out of range at power-on
  or does not change during an incline move, checked at the VR wires, the 14-pin cable,
  the boards and the incline motor'
kind: troubleshooting
question: What does Err mean on a Spirit xe395-2016 elliptical, and how is it fixed?
asked_as:
- xe395 shows err
- incline wont move and the console says err
- err in the incline window spirit elliptical
- incline error on my xe395
keywords:
- err
- incline err
- incline motor
- incline vr
- position sensor
- 14-pin cable
- driver board
- calibrate
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395-2016
  applies_to:
  - xe395-2016
  section: errors
  code: err
  model_number:
  - '395015'
authority: 3
not_to_be_confused_with:
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- ce850-2024-errors-err-tension-motor-failure
- xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback
- xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
see_also:
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395-2016-errors-incline-err-incline-window-err
- xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v
- ct850-2016-incline-err-vr-out-of-range
- e25-2016-e3-ramp-error
- xe395-2018-errors-incline-calibration-three-key-hold
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: 'XE395 2016 (XE539S-SE019-01) service manual Error code items, Error Message:
    Err, Case of Err, Troubleshooting, Error Message: Err, Cause of Err and Troubleshooting,
    PDF p. 40-53, text.md lines 640-908'
  extracted_at: '2026-09-11'
---

**This is the XE395 2016's `Err`, its incline VR fault. It is not `EEPROM ERR` or `--`, the other two rows on its table; it is not the CE850 (2020)'s `Err`, which is that machine's tension motor; and it is not the XG400 2016's `Err`, which is a gear motor.** The XE395ENT 2021 prints this same fault as `E3`.

| Error Message | Explain |
|---|---|
| Err | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

**The book prints Err twice, for two different cases.** Both are Err.

**Case 1 - incline VR value out of range (the `Case of Err` page).** *Incline VR value exceeds the range. Err appears on the display. Incline motor isn't operation up or down, making the VR value exceed the range. After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so Err appears.*

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and 14-pin cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| 14-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 14-pin connections. |

**Case 2 - no VR change during incline action (the `Cause of Err` page).** *During incline action, the display board CPU cannot read the VR value, so Err appears. Press the incline UP/DOWN key. The incline doesn't operate. Err appears on the display.* Explanation: pressing the incline UP or DOWN key lights the driver board UP or DOWN indicator, and the incline operates and moves the VR, and the VR value changes; if the display board CPU sees no VR value change, the incline is not operating when it should be, and Err appears.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP LED lights. 2. Press incline DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 14-pin cable | 1. Inspect whether the 14-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If INCLINE Err still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

Between the two cases the book prints the console-to-driver-board 14-pin definition (`1 MTR-, 2 MTR+, 3 +5V, 4 MPOS, 5 GND, 6 RPM1, 7 GND, 8 RPM2, 9 GND, 10 +12V, 11 GND, 12 INC+, 13 INC-, 14 IPOS`), the position-sensor wire colours (*1. Red = Ground, 2. White = Position signal, 3. Black = 5vdc, 0~5v depending on incline position*) and the nine-step test: `xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`.

**The troubleshooting matrix gives a shorter answer**, printed as `INCLINE ERR, INCLINE window displays "Err"`: turn the AC switch off and on again, then calibrate the monitor - `xe395-2016-errors-incline-err-incline-window-err`. The incline calibration is a five-second hold on Stop, Level and Start together (`xe395-2018-errors-incline-calibration-three-key-hold`).

The driver board's POWER, UP and DOWN LEDs, and what each means when it is dark, are on `xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v`. Spirit treadmills print the same two cases as `INCLINE ERR` (`ct850-2016-incline-err-vr-out-of-range`), and Sole's E25, E35 and E55 2016 as `E3` (`e25-2016-e3-ramp-error`). Different machines; separate cards.

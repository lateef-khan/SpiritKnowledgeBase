---
id: xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
title: 'E3: the incline VR voltage is out of range at power-on or does not change
  during an incline move, checked at the VR wires, the 6-pin cable, the boards and
  the incline motor'
kind: troubleshooting
question: What does E3 mean on a Spirit xe395ent-2021 elliptical, and how is it fixed?
asked_as:
- xe395ent shows e3
- incline wont move e3 spirit elliptical
- ramp error on the ent elliptical
- e3 incline error
keywords:
- e3
- incline motor
- incline vr
- position sensor
- 6-pin cable
- ramp error
- incline err
- driver board
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- xe395ent-2021-errors-e2-tension-motor-does-not-move
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- e25-2023-e3-ramp-error
see_also:
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
- xe395ent-2021-errors-incline-err-incline-window-e3
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- ct850-2016-incline-err-vr-out-of-range
- e25-2023-e3-ramp-error
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: 'XE395ENT 2021 (XE539S-SE025-01) service manual Error code items, Error
    Message: E3, Case of RAMP ERROR, Troubleshooting, Error Message: E3, Cause of
    E3 and Troubleshooting, PDF p. 26-38, text.md lines 308-541'
  extracted_at: '2026-09-11'
---

**This is the XE395ENT 2021's `E3`, its incline VR fault. It is not `E2`, the only other row on its table (the tension motor), and it is not the CE850 2016's `E3`, which is that machine's stride VR over a 14-pin cable.** The XE395 2016 prints this same incline fault as `Err`.

| Error Message | Explain |
|---|---|
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

**The book prints E3 twice, for two different cases, and its first definition names a message it never uses**: *"RAMP ERROR" appears on the display*, in a section whose own heading, case page and table all say `E3`. Nothing in the book shows `RAMP ERROR` on a screen; the message is `E3`.

**Case 1 - incline VR value out of range (the `Case of RAMP ERROR` page).** *Incline VR value exceeds the range. E3 appears on the display. Incline motor isn't operation up or down, making the VR value exceed the range. After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so E3 appears.*

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and 6-pin cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| 6-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 6-pin connections. |

**Case 2 - no VR change during incline action (the `Cause of E3` page).** *During incline action, the display board CPU cannot read the VR value, so E3 appears. Press the incline UP/DOWN key. The incline doesn't operate. E3 appears on the display.* Explanation: pressing the incline UP or DOWN key lights the driver board UP or DOWN indicator, and the incline operates and moves the VR, and the VR value changes; if the display board CPU sees no VR value change, the incline is not operating when it should be, and E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | If not as above, inspect the cable and connections. |
| 6-pin cable | 1. Inspect whether the 6-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If E3 still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

**The cable between the two boards is 6-pin on this machine**, where every other Spirit elliptical printing of these tables says 14-pin. The console-to-driver-board definition printed between the two cases is `1 12V, 2 GND, 3 TXD, 4 RXD, 5 EUP, 6 DMK` - a serial link, not the motor and sensor lines the 2016 books carry - and the driver board's own motor connector reads `1 MTR-, 2 MTR+, 3 VREF, 4 MPOS, 5 GND`. The position-sensor wire colours are the usual *Red = Ground, White = Position signal, Black = 5vdc*. The nine-step test follows: `xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`.

**The troubleshooting matrix gives a shorter answer**, printed as `INCLINE ERR, INCLINE window displays "E3"`: turn the AC switch off and on again, then calibrate the monitor - `xe395ent-2021-errors-incline-err-incline-window-e3`. On this console the calibration is an `Incline Calibration` entry in the engineer mode's Factory Setting page.

Spirit treadmills print the same two cases as `INCLINE ERR` or `E3` (`ct850-2016-incline-err-vr-out-of-range`), and Sole's E25 2023 as `E3 ramp error` (`e25-2023-e3-ramp-error`). Different machines; separate cards.

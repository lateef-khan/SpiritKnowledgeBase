---
id: spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
title: 'E3: the stride VR voltage is out of range at power-on or does not change during
  a stride move, checked at the VR wires, the 14-pin cable, the boards and the stride
  motor'
kind: troubleshooting
question: What does E3 mean on a Spirit CE850-2016 or XE895-2016 elliptical, and how
  is it fixed?
asked_as:
- e3 on my spirit ce850 elliptical
- stride wont move and shows e3
- elliptical stride error e3
- ramp error e3 spirit elliptical
keywords:
- e3
- stride motor
- stride vr
- position sensor
- 14-pin cable
- ramp error
- stride err
- driver board
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe895-2016
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-errors-e1-eeprom-failure-replace-upper-controller
- spirit-ce850-2016-errors-e2-table-label-tension-motor
- xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- e95s-2016-e3-stride-error
see_also:
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
- spirit-ce850-2016-errors-stride-err-stride-window-e3
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- e95s-2016-e3-stride-error
- spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850 2016 (XE898-SE011) service manual 8-2 Error Message: E2 (the section
    is the E3 stride VR case), Case of RAMP ERROR, Troubleshooting, 8-3 Error Message:
    E3, Cause of E3 and Troubleshooting, PDF p. 44-52, text.md lines 731-914; XE895
    2016 (XE895-SE022) service manual 8-2 Error Message: E2 (the section is the E3
    stride VR case), Case of RAMP ERROR, Troubleshooting, 8-3 Error Message: E3, Cause
    of E3 and Troubleshooting, PDF p. 45-53, text.md lines 727-915'
  extracted_at: '2026-09-11'
---

**This is E3, the stride VR fault of the CE850 2016 (XE898-SE011) and XE895 2016 (XE895-SE022) books. It is not E1 (EEPROM) and not the `--` tension-motor fault the table lists as E2.** On this machine the VR belongs to the **stride** mechanism; the manual's headings still say `RAMP ERROR` and its flow charts say `INCLINE`, because the pages were built from an incline-elliptical template.

| Error Message | Explain |
|---|---|
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

**The books print E3 twice, for two different cases, under two mis-numbered headings.** The first case sits under `8-2 Error Message: E2` (whose definition nevertheless ends *"E3" appears on the display*), the second under `8-3 Error Message: E3`. Both are E3.

**Case 1 - stride VR value out of range (the `Case of RAMP ERROR` page).** *Stride VR value exceeds the range. E3 appears on the display. Stride motor isn't operation up or down, making the VR value exceed the range. After turning on the unit, the display board detects that the stride VR voltage exceeds the range, so E3 appears.*

| Part | Troubleshooting |
|---|---|
| Stride VR | 1. Reconnect VR wires. 2. Inspect whether the stride wires are broken or disconnected. |
| Display board | 1. Inspect the stride wire and 14-pin cable connections. 2. Test whether the VR voltage varies at the stride wire terminal. |
| 14-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 14-pin connections. |

**Case 2 - no VR change during stride action (the `Cause of E3` page).** *During stride action, the display board CPU cannot read the VR value, so E3 appears. Press the stride UP/DOWN key. The stride doesn't operate. E3 appears on the display.* Explanation: pressing the stride UP or DOWN key lights the driver board UP or DOWN indicator, and the stride operates and moves the VR, and the VR value changes; if the display board CPU sees no VR value change, the stride is not operating when it should be, and E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press stride UP key. The driver board UP LED lights. 2. Press stride DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 14-pin cable | 1. Inspect whether the 14-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press stride UP or DOWN key again, making the stride motor return to its position. 2. If E3 still appears, re-calibrate the stride set. |
| Stride motor | 1. Inspect whether the stride motor is stuck. 2. Inspect whether the stride gears are cracked. 3. Test whether the stride motor has a broken circuit. 4. Re-calibrate the stride set. |

Between the two cases the books print the console-to-driver-board 14-pin definition (`1 MTR-, 2 MTR+, 3 +5V, 4 MPOS, 5 GND, 6 RPM1, 7 GND, 8 RPM2, 9 GND, 10 +12V, 11 GND, 12 INC+, 13 INC-, 14 IPOS`), the position-sensor wire colours (*1. Red = Ground, 2. White = Position signal, 3. Black = 5vdc, 0~5v depending on incline position*) and a nine-step test that follows the fault from the relays to the console: `spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`.

**The troubleshooting matrix gives a shorter answer for the same display**, printed as `STRIDE ERR, STRIDE window displays "E3"`: turn the AC switch off and on again, then calibrate the monitor - `spirit-ce850-2016-errors-stride-err-stride-window-e3`. The stride calibration itself is a five-second hold on the Stride key and Start.

The CE850 (2020) and CE850 2024 books print the same two cases with the message written as three dashes, `---` (`ce850-2024-errors-stride-window-dashes-stride-motor-failure`). The XE395 2016 prints them as `Err` about its incline (`xe395-2016-errors-err-incline-vr-out-of-range-or-not-read`) and the XE395ENT 2021 as `E3` about its incline over a 6-pin cable (`xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read`) - a different axis, and on the ENT a different connector. **Sole's E95S 2016 is this book's twin page for page**, with an 11-pin cable in place of the 14-pin: `e95s-2016-e3-stride-error`. Different brand; separate card.

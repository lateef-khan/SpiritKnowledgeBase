---
id: e95-2016-e3-ramp-error
title: E3 ramp error, incline VR not read
kind: troubleshooting
question: What does error E3 mean on a Sole e95-2016 elliptical and how is it fixed?
asked_as:
- e3 ramp error on my sole elliptical
- incline error e3 wont go up
- my sole machine shows e3 when i turn it on
keywords:
- e3
- ramp error
- incline
- vr
- potentiometer
- position sensor
- error code
- calibration
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95-2016
  applies_to:
  - e95-2016
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e95-2016-e1-eeprom-failure
- e95-2016-e2-tension-motor-failure
see_also:
- e95-2016-incline-motor-test-procedure
- e95-2016-incline-calibration
- e95-2016-console-to-driver-board-pinout
- e95-2016-incline-position-mismatch
source:
  ref: sole-elliptical-e95-2016-service-manual
  locator: Section 8-3 and its repeat, pages 45-47 and 51-53
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (tension motor).**

The error table definition: "The console board is not detecting the VR voltage value, or the voltage value has exceeded the range." **The section heading and definition write it as "E-3"; the case text and the troubleshooting matrix write "E3".**

The manual prints E3 twice, for two different cases. Both are E3.

**Case 1 - VR value out of range.** The incline motor is not operating up or down, so the VR value goes outside its range. After turning the unit on, the display board detects that the incline VR voltage exceeds the range, so E3 appears.

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and 11-pin cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| 11-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 11-pin connections. |

**Case 2 - no VR change during incline action.** During incline action the display board CPU cannot read the VR value, so E3 appears. Press the incline UP/DOWN key, the incline does not operate, E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP LED lights. 2. Press incline DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 14-pin cable | 1. Inspect whether the 14-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If E3 still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

The troubleshooting matrix adds a shorter answer for the same symptom: turn the AC switch off and on again, then calibrate the monitor.

**The two cases name different cables.** Case 1 blames an **11-pin** cable and case 2 blames a **14-pin** cable. The console to driver board connector drawn in this manual has 11 pins, so treat the 14-pin row in case 2 as carried over from the E25, E35 and E55 manuals.

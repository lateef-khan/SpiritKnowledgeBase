---
id: e95s-2016-e3-stride-error
title: E3 stride error, stride VR not read
kind: troubleshooting
question: What does error E3 mean on a Sole e95s-2016 elliptical and how is it fixed?
asked_as:
- e3 on my sole e95s
- stride error e3 wont adjust
- what is error code e3 on a sole elliptical
keywords:
- e3
- stride
- vr
- potentiometer
- position sensor
- error code
- calibration
- 11-pin cable
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2016
  applies_to:
  - e95s-2016
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e95s-2016-e1-eeprom-failure
- e95s-2016-e2-tension-motor-failure
see_also:
- e95s-2016-stride-motor-test-procedure
- e95s-2016-stride-calibration
- e95s-2016-console-to-driver-board-pinout
- e95s-2016-stride-position-mismatch
source:
  ref: sole-elliptical-e95s-2016-service-manual
  locator: Section 8-3 and its repeat, pages 45-47 and 51-53
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (tension motor).**

The error table definition: "The console board is not detecting the VR voltage value, or the voltage value has exceeded the range." **"E3" appears on the display.**

**On this machine E3 is about the stride mechanism, not an incline ramp.** The section heading in the source still reads "Case of RAMP ERROR", but every troubleshooting row says stride.

The manual prints E3 twice, for two different cases. Both are E3.

**Case 1 - stride VR value out of range.** The stride motor is not operating up or down, so the VR value goes outside its range. After turning the unit on, the display board detects that the stride VR voltage exceeds the range, so E3 appears.

| Part | Troubleshooting |
|---|---|
| Stride VR | 1. Reconnect VR wires. 2. Inspect whether the stride wires are broken or disconnected. |
| Display board | 1. Inspect the stride wire and 11-pin cable connections. 2. Test whether the VR voltage varies at the stride wire terminal. |
| 11-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 11-pin connections. |

**Case 2 - no VR change during stride action.** During stride action the display board CPU cannot read the VR value, so E3 appears. Press the stride UP/DOWN key, the stride does not operate, E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press stride UP key. The driver board UP LED lights. 2. Press stride DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 11-pin cable | 1. Inspect whether the 11-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press stride UP or DOWN key again, making the stride motor return to its position. 2. If E3 still appears, re-calibrate the stride set. |
| Stride motor | 1. Inspect whether the stride motor is stuck. 2. Inspect whether the stride gears are cracked. 3. Test whether the stride motor has a broken circuit. 4. Re-calibrate the stride set. |

The troubleshooting matrix adds a shorter answer for the same symptom, printed as "STRIDE ERR, STRIDE window displays E3": turn the AC switch off and on again, then calibrate the monitor.

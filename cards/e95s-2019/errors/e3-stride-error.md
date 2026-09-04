---
id: e95s-2019-e3-stride-error
title: E3 stride VR not read
kind: troubleshooting
question: What does error E3 mean on a Sole e95s-2019 elliptical?
asked_as:
- e3 error on sole elliptical
- stride error e3 on my e95s
- stride wont adjust and shows e3
keywords:
- e3
- stride
- vr
- potentiometer
- position sensor
- 6-pin cable
- calibration
- stride err
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2019
  applies_to:
  - e95s-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e95s-2019-e1-eeprom-failure
- e95s-2019-e2-tension-motor-failure
see_also:
- e95s-2019-stride-motor-test-procedure
- e95s-2019-stride-calibration
- e95s-2019-console-to-driver-board-pinout
- e95s-2019-stride-position-mismatch
source:
  ref: sole-elliptical-e95s-2019-service-manual
  locator: Sections 8-3 and its repeat, pages 43-45 and 49-51
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (tension motor).**

Definition: the console board is not detecting the VR voltage value, or the voltage value has exceeded the range. **"E3" appears on the display.** On this machine the axis in question is the **stride**, not the incline: the manual's troubleshooting matrix prints the symptom as "STRIDE ERR, STRIDE window displays E3".

The manual prints E3 twice, for two different cases. Both are E3.

**Case 1 - VR value out of range (page 43).** The stride motor is not operating up or down, so the stride VR value goes outside its range. After turning the unit on, the display board detects that the stride VR voltage exceeds the range, so E3 appears. The heading over this case is printed as "Case of RAMP ERROR", carried over from the fixed-stride manuals.

| Part | Troubleshooting |
|---|---|
| Stride VR | 1. Reconnect VR wires. 2. Inspect whether the stride wires are broken or disconnected. |
| Display board | 1. Inspect the stride wire and 6-pin cable connections. 2. Test whether the VR voltage varies at the stride wire terminal. |
| 6-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 6-pin connections. |

**Case 2 - no VR change during stride action (page 49).** During stride action the display board CPU cannot read the VR value, so E3 appears. Press the stride UP/DOWN key, the stride does not operate, E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | 1. If not as above, inspect the cable and connections. |
| 6-pin cable | 1. Inspect whether the 6-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press stride UP or DOWN key again, making the stride motor return to its position. 2. If E3 still appears, re-calibrate the stride set. |
| Stride motor | 1. Inspect whether the stride motor is stuck. 2. Inspect whether the stride gears are cracked. 3. Test whether the stride motor has a broken circuit. 4. Re-calibrate the stride set. |

The Display board row in case 2 is printed with only the "if not as above" line; the two preceding steps that the other manuals print (press stride UP, the driver board UP LED lights; press stride DOWN, the DOWN LED lights) are missing from the table in this manual.

The troubleshooting matrix adds a shorter answer for the same symptom: turn the AC switch off and on again, then calibrate the monitor.

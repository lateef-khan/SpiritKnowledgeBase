---
id: e98-2019-e3-incline-vr-error
title: E3 incline VR not read during incline action
kind: troubleshooting
question: What does error E3 mean on a Sole e98-2019 elliptical?
asked_as:
- e3 error on sole elliptical
- incline error e3 wont go up
- my e98 shows e3
keywords:
- e3
- incline
- vr
- potentiometer
- position sensor
- 6-pin cable
- calibration
- incline err
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2019
  applies_to:
  - e98-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e98-2019-e1-eeprom-failure
- e98-2019-e2-tension-motor-failure
see_also:
- e98-2019-incline-motor-test-procedure
- e98-2019-incline-calibration
- e98-2019-incline-position-mismatch
source:
  ref: sole-elliptical-e98-2019-service-manual
  locator: Section 8.2, pages 43-45
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (tension motor).**

The error code table definition: "The console board is not detecting the VR voltage value, or the voltage value has exceeded the range."

The body section prints the other half of the story: **during incline action the display board CPU cannot read the VR value, so E3 appears.** Press the incline UP/DOWN key, the incline does not operate, E3 appears. When the driver board UP or DOWN indicator lights the incline operates and moves the VR, changing the VR value; if the CPU sees no VR change it concludes the incline is not operating.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP LED lights. 2. Press incline DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 6-pin cable | 1. Inspect whether the 6-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If E3 still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

The troubleshooting matrix adds a shorter answer for the same symptom, printed as "INCLINE ERR, INCLINE window displays E3": turn the AC switch off and on again, then calibrate the monitor.

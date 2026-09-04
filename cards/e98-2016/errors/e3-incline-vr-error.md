---
id: e98-2016-e3-incline-vr-error
title: E3 incline VR error
kind: troubleshooting
question: What does error E3 mean on a Sole e98-2016 elliptical and how is it fixed?
asked_as:
- e3 on my sole e98
- incline error e3 wont go up
- what is error code e3 on a sole elliptical
keywords:
- e3
- incline
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
  model: e98-2016
  applies_to:
  - e98-2016
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e98-2016-e1-eeprom-failure
- e98-2016-e2-tension-motor-failure
see_also:
- e98-2016-incline-motor-test-procedure
- e98-2016-incline-calibration
- e98-2016-console-to-driver-board-pinout
- e98-2016-incline-position-mismatch
source:
  ref: sole-elliptical-e98-2016-service-manual
  locator: Section 8-2, pages 45-47
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (tension motor).**

The error code table definition: "The console board is not detecting the VR voltage value, or the voltage value has exceeded the range."

The body section prints the other half of the story: **during incline action the display board CPU cannot read the VR value, so E3 appears.** Press the incline UP/DOWN key, the incline does not operate, E3 appears. When the driver board UP or DOWN indicator lights the incline operates and moves the VR, changing the VR value; if the CPU sees no VR change it concludes the incline is not operating.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP LED lights. 2. Press incline DOWN key. The driver board DOWN LED lights. 3. If not as above, inspect the cable and connections. |
| 11-pin cable | 1. Inspect whether the 11-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN LED is lit. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If E3 still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

**This manual prints only one E3 case.** The E25, E35, E55 and E95 manuals of the same year print two, adding a first case for the VR value being out of range at power-on. This manual has no such section.

The troubleshooting matrix adds a shorter answer for the same symptom, printed as "INCLINE ERR, INCLINE window displays E3": turn the AC switch off and on again, then calibrate the monitor.

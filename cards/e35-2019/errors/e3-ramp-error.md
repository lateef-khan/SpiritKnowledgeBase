---
id: e35-2019-e3-ramp-error
title: E3 ramp error, incline VR out of range
kind: troubleshooting
question: What does error E3 or RAMP ERROR mean on a Sole e35-2019 elliptical?
asked_as:
- e3 ramp error on sole elliptical
- incline error e3 wont go up
- my e35 shows e3 when i turn it on
keywords:
- e3
- ramp error
- incline
- vr
- potentiometer
- position sensor
- 14-pin cable
- calibration
facets:
  brand:
  - sole
  product_line: elliptical
  model: e35-2019
  applies_to:
  - e35-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e35-2019-e1-eeprom-failure
- e35-2019-e2-tension-motor-failure
see_also:
- e35-2019-incline-motor-test-procedure
- e35-2019-incline-calibration
- e35-2019-console-to-driver-board-pinout
- e35-2019-incline-position-mismatch
source:
  ref: sole-elliptical-e35-2019-service-manual
  locator: Section 8.3, pages 44-46
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (tension motor).**

Definition: the console board is not detecting the VR voltage value, or the voltage value has exceeded the range. **"RAMP ERROR" appears on the display.**

Case of E3: the incline VR value exceeds the range. The incline motor is not operating up or down, making the VR value exceed its range. After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so E3 appears.

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and 14-pin cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| 14-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 14-pin connections. |

The troubleshooting matrix adds a shorter answer for the same symptom: turn the AC switch off and on again, then calibrate the monitor.

This manual prints only the power-on, out-of-range case. The E25, E55 and E98 manuals of the same year also print a second E3 case, where the CPU sees no VR change during an incline movement. Do not assume this machine lacks that behaviour; the manual is simply silent on it.

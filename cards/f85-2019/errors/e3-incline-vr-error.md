---
id: f85-2019-e3-incline-vr-error
title: 'E3: the incline VR value is missing or out of range'
kind: troubleshooting
question: What does E3 mean on a Sole F85-2019 treadmill and how do I fix it?
asked_as:
- e3 error on my treadmill
- incline err on the display
- treadmill will not incline and shows e3
keywords:
- e3
- incline err
- incline vr
- potentiometer
- position sensor
- incline motor
- calibration
- error code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- f85-2019-e0-safety-key-error
- f85-2019-e1-no-rpm-signal
- f85-2019-e2-over-current
- f85-2019-e4-motor-power-wire-error
- f85-2019-e5-communication-error
- f85-2019-e6-lower-controller-error
- f85-2019-e7-input-power-error
see_also:
- f85-2019-incline-motor-and-position-sensor-test
- f85-2019-incline-position-sensor-pinout
- sole-e3-error
source:
  ref: sole-tm-f85-2019-service-manual
  locator: 'sections 8.3 Error Message: E3 and Error Message: E3 / INCLINE ERR, printed
    pages 62 to 70, and the section 8.10 matrix on page 78'
  extracted_at: '2026-09-04'
---

**This is E3, not E2 (over current) and not E0 (safety key).**

| Field | Value |
|---|---|
| Code | E3 |
| Cause, as printed | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

**The manual prints E3 twice, as two different moments.**

1. **At power on.** After the unit is turned on, the display board reads the incline VR voltage, finds it outside the range, and shows E3. The incline motor not moving up or down is what pushes the VR value out of range.
2. **During an incline action** (printed as *E3 / INCLINE ERR*). The user presses incline UP or DOWN, the incline does not move, the display board CPU sees no change in the VR value, and E3 appears.

**Troubleshooting for the power-on case**

| Part | What to do |
|---|---|
| Display board | Check the incline keys for a stuck key. |
| Incline power cable and incline VR cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Driver board | Replace the driver board. |

**Troubleshooting for the INCLINE ERR case**

| Part | What to do |
|---|---|
| Display board | Press the incline keys and watch for a value on the display. No value means a stuck key, or replace the upper control board. |
| Incline cable | Inspect whether the incline power wire and the incline VR cable are connected well. |
| Driver board | Look at the lower control board for obvious and serious damage to the incline parts. |
| Incline motor | Inspect whether the motor is stuck. Inspect whether the incline gears are cracked. Test whether the motor has a broken circuit. Recalibrate the incline set. |

The section 8.10 matrix gives a third short answer for **INCLINE ERR with E3 in the incline window**: the position sensor value of the incline motor is wrong. Turn the AC switch off and turn the power on again, then calibrate the monitor.

The full nine step bench test for the incline motor and its potentiometer is in its own card.

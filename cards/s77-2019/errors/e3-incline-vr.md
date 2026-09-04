---
id: s77-2019-e3-incline-vr
title: 'E3: the console cannot read the incline position sensor'
kind: troubleshooting
question: What does E3 mean on a Sole S77-2019 treadmill?
asked_as:
- e3 error on my treadmill
- incline error on my s77
- treadmill says e3 and will not incline
keywords:
- e3
- incline err
- vr
- potentiometer
- position sensor
- incline motor
- out of range
- calibration
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- s77-2019-e0-safety-key
- s77-2019-e1-no-rpm-signal
- s77-2019-e2-over-current
- s77-2019-e4-motor-power-wire
see_also:
- s77-2019-incline-position-sensor-test
- s77-2019-incline-sensor-pinout
- s77-2019-calibration-procedure
- sole-e3-error
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Sections 8.3 Error Message: E3 and Error Message: E3 / INCLINE ERR, pages
    44-52'
  extracted_at: '2026-09-04'
---

**This is E3, not E2 (over current) and not E0 (safety key).**

**Meaning**: the console board is not detecting the incline VR voltage value, or the value has gone outside its range.

**The manual describes E3 in two places, and they are two different symptoms of the same code.**

**1. At power on, or with the machine sitting still.** The incline motor did not move up or down, so the VR value drifted outside the range. After the unit is turned on the display board reads the incline VR voltage, finds it out of range, and shows E3.

**2. During an incline movement (INCLINE ERR).** You press the incline UP or DOWN key and the incline does not operate. The display board CPU reads the incline VR value, sees no change, and shows E3.

**Troubleshooting, in the manual's order**

| Part | What to do |
|---|---|
| Display board | Press the incline keys and watch for a value on the display. If nothing appears, check whether a key is stuck; otherwise replace the upper control board. |
| Incline power cable and incline VR cable | Inspect the wire connections. Inspect whether the wires are broken or crimped. **Replace the wires and test again.** |
| Driver board | Replace the driver board. |
| Incline motor | Check whether the motor is stuck. Check whether the incline gears are cracked. Test whether the motor has a broken circuit. Recalibrate the incline. |

The nine-step measurement procedure that goes with this is on the card `s77-2019-incline-position-sensor-test`.

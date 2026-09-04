---
id: f80-2019-e3-incline-error
title: 'E3 error: incline VR value not read'
kind: troubleshooting
question: What does an E3 or INCLINE ERR error mean on a Sole f80-2019 treadmill?
asked_as:
- e3 error on my treadmill
- incline err on the treadmill display
- treadmill will not incline and shows e3
keywords:
- e3
- incline err
- incline
- vr
- potentiometer
- position sensor
- calibration
- error code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2019
  applies_to:
  - f80-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- f80-2019-e2-over-current
- f80-2019-e4-motor-power-wire-error
see_also:
- f80-2019-incline-motor-test-procedure
- f80-2019-calibration-procedure
- f80-2019-incline-position-sensor-wiring
- sole-e3-error
source:
  ref: sole-tm-f80-2019-service-manual
  locator: 'Sections 8.3 and Error Message: E3 / INCLINE ERR'
  extracted_at: '2026-09-04'
---

**This is E3, not E2 (over current) and not E4 (motor power wire).**

The error table definition: "The console board is not detecting the VR voltage value, or the voltage value has exceeded the range."

The manual prints E3 twice, for two different cases. Both are E3.

**Case 1 - VR value out of range.** The incline motor is not operating up or down, which makes the VR value exceed its range. After the unit is turned on the display board detects that the incline VR voltage is out of range, so E3 appears. The incline VR signal is sent and received through TX/RX of the main control lines.

| Part | Troubleshooting |
|---|---|
| Display board | Check whether an incline key is stuck. |
| Incline power cable & incline VR cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Replace the driver board. |

**Case 2 - INCLINE ERR, no VR change while inclining.** Press the incline UP/DOWN key, the incline does not operate, E3 appears. During the incline action the display board CPU cannot read the VR value.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline keys and see whether a value appears. If no values, check whether keys are stuck, or replace the upper control board. |
| Incline cable | Inspect whether the incline power wire and incline VR cable are connected well. |
| Driver board | Look at the lower control board for obvious and serious damage to the incline components. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Recalibrate the incline set. |

---
id: f63-2019-e3-error-code
title: 'E3 error: incline VR voltage'
kind: troubleshooting
question: What does an E3 error mean on a Sole F63-2019?
asked_as:
- e3 error on my treadmill
- incline err on my sole treadmill
- treadmill will not incline and shows e3
keywords:
- e3
- e3 error
- incline err
- incline vr
- potentiometer
- incline motor
- vr voltage
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2019
  applies_to:
  - f63-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- f63-2019-e0-error-code
- f63-2019-e1-error-code
- f63-2019-e2-error-code
- f63-2019-e4-error-code
- f63-2019-e5-error-code
- f63-2019-e6-error-code
- f63-2019-e7-error-code
see_also:
- f63-2019-error-code-list
- f63-2019-incline-position-sensor-test
- f63-2019-console-to-controller-pinout
source:
  ref: sole-tm-f63-2019-service-manual
  locator: pages 44 to 46 (8.3) and page 50 (E3 / INCLINE ERR)
  extracted_at: '2026-09-04'
---

**This is E3, not E0 and not E7.** The manual describes E3 twice, and the two descriptions are different faults with the same code.

**E3 at power on (section 8.3)**: the console board is not detecting the VR voltage value, or the voltage value has exceeded the range. The incline motor is not operating up or down, so the VR value goes out of range. After the unit is switched on the display board sees the incline VR voltage out of range and shows E3.

| Part | Troubleshooting |
|---|---|
| Display board | Check the incline keys, whether a key is stuck or not. |
| Incline power cable and incline VR cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Driver board | Replace the driver board. |

**E3 / INCLINE ERR during an incline (page 50)**: during incline action the display board CPU cannot read the VR value. Press the incline UP or DOWN key, the incline does not operate, and E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline keys and see whether the display shows a value. If there is no value, check whether the keys are stuck, or replace the upper control board. |
| Incline cable | Inspect whether the incline power wire and the incline VR cable are connected well. |
| Driver board | Look at the lower control board for obvious and serious damage to the incline components. |
| Incline motor | Inspect whether the incline motor is stuck. Inspect whether the incline gears are cracked. Test whether the incline motor has a broken circuit. Recalibrate the incline set. |

The nine step voltage test that goes with this error is on its own card.

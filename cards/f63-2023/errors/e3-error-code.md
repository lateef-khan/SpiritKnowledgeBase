---
id: f63-2023-e3-error-code
title: 'E3 error: incline VR voltage'
kind: troubleshooting
question: What does an E3 error mean on a Sole F63-2023?
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
- vr resistor
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2023
  applies_to:
  - f63-2023
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- f63-2023-e0-error-code
- f63-2023-e1-error-code
- f63-2023-e2-error-code
- f63-2023-e4-error-code
- f63-2023-e5-error-code
- f63-2023-e6-error-code
- f63-2023-e7-error-code
see_also:
- f63-2023-error-code-list
- f63-2023-incline-position-sensor-test
- f63-2023-incline-motor-spec
source:
  ref: sole-tm-f63-2023-service-manual
  locator: pages 25 to 28, 8.4 Error Message E3
  extracted_at: '2026-09-04'
---

**This is E3, not E2 (over current) and not E7 (input power).**

**Definition**: the console board is not detecting the VR voltage value, or the voltage value has exceeded the range. E3 appears on the display.

**Cause**: the incline VR resistor value exceeds the range.

- The incline motor is not operating up or down, so the VR value goes out of range.
- After the unit is switched on the display board detects that the incline VR voltage is out of range, and E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline keys and see whether the display shows a value. If there is no value, check whether the keys are stuck, or replace the display board. |
| Incline power cable and incline VR cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Controller | Replace the controller. |
| Incline motor | Inspect whether the incline motor is stuck. Inspect whether the incline gears are cracked. Test whether the incline motor has a broken circuit. Recalibrate the incline set. |

The troubleshooting matrix adds a fourth cause: a connector that has fallen off. Check the connector of the cable, then calibrate the console.

The nine step voltage test that goes with this error is on its own card.

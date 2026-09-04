---
id: f89-2023-e3-incline-vr-voltage
title: 'E3 error: incline VR voltage out of range'
kind: troubleshooting
question: What does an E3 error mean on a Sole f89-2023 treadmill?
asked_as:
- e3 error on my treadmill
- incline error on the treadmill
- treadmill shows e3 and will not incline
keywords:
- e3
- e3 error
- incline
- vr voltage
- potentiometer
- position sensor
- incline motor
- calibration
facets:
  brand:
  - sole
  product_line: treadmill
  model: f89-2023
  applies_to:
  - f89-2023
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- f89-2023-e2-over-current
- ct900-e3-igbt-over-temp
- ct900-e31-comm-timeout
- ct900-e33-incline-err
see_also:
- f89-2023-error-code-list
- f89-2023-incline-position-sensor-test
- f89-2023-incline-sensor-connector-pinout
- sole-e3-error
source:
  ref: sole-tm-f89-2023-service-manual
  locator: 'Section 8.4 Error Message: E3, pages 40-41'
  extracted_at: '2026-09-04'
---

**This is E3, the incline VR fault. It is not E2 (over current). On a Sole machine built before 2016 the
incline fault is printed as E2 instead.**

**Definition.** The console board is not detecting the VR voltage value, or the voltage value has exceeded the
range.

**Cause.** The incline VR resistor value is outside its range.

- The incline motor is not running up or down, so the VR value leaves its range.
- After the unit is turned on, the display board detects that the incline VR voltage is out of range and E3
  appears.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline keys and see whether a value appears on the display. If there is no value, check whether a key is stuck, or replace the display board. |
| Incline power cable and incline VR cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Controller | Replace the controller. |
| Incline motor | Inspect whether the incline motor is stuck. Inspect whether the incline gears are cracked. Test whether the incline motor has a broken circuit. Recalibrate the incline set. |

**The troubleshooting matrix prints this code a second time**, as "INCLINE ERR, INCLINE window displays E3", with
two causes: a connector has fallen off (check the connector of the cable), and the incline motor position sensor
value is wrong (calibrate the console).

The nine-step voltage test the manual gives for this code is on its own card.

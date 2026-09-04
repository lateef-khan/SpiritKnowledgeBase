---
id: f60-2020-e3-error-code
title: 'E3 error: incline VR voltage'
kind: troubleshooting
question: What does an E3 error mean on a Sole F60-2020?
asked_as:
- e3 error on my treadmill
- my treadmill will not incline and shows e3
- e3 in the incline window
keywords:
- e3
- e3 error
- incline err
- incline vr
- potentiometer
- 5-pin cable
- incline motor
- vr voltage
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2020
  applies_to:
  - f60-2020
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- f60-2020-e0-error-code
- f60-2020-e1-error-code
- f60-2020-e2-error-code
- f60-2020-e4-error-code
- f60-2020-e5-error-code
- f60-2020-e6-error-code
see_also:
- f60-2020-error-code-list
- f60-2020-incline-position-sensor-wiring
- f60-2020-incline-motor-spec
source:
  ref: sole-tm-f60-2020-service-manual
  locator: pages 42 to 49, 8.4 Error Message E3
  extracted_at: '2026-09-04'
---

**This is E3, not E2 (over current) and not E6.** E3 appears in the **incline window**.

The manual describes E3 twice, and the two descriptions are different faults with the same code.

**E3 at power on (section 8.4)**: the console board is not detecting the VR voltage value, or the value has exceeded the range. The incline motor is not operating up or down, so the VR value goes out of range. After the unit is switched on, the display board detects the incline VR voltage out of range and E3 appears.

| Part | Troubleshooting |
|---|---|
| Incline VR | Reconnect the VR wires. Inspect whether the incline wires are broken or disconnected. |
| Display board | Inspect the incline wire and the 5-pin cable connections. Test whether the VR voltage varies at the incline wire terminal. |
| 5-pin cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Driver board | Inspect the display board 5-pin connections. |

**INCLINE E3 during an incline (page 46)**: press the incline UP or DOWN key and the incline does not operate. The driver board UP or DOWN indicator lights, the incline should move the VR and change the VR value. If the CPU sees no VR value change, INCLINE E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline UP key, the driver board UP LED lights. Press the incline DOWN key, the driver board DOWN LED lights. If it is not as above, inspect the cable and connections. |
| 5-pin cable | Inspect whether the 5-pin cable is connected well. Test by replacing the cable with a good one. |
| Driver board | Check whether the driver board UP/DOWN LED is lit. Press incline UP or DOWN again to make the incline motor return to its position. If the error still appears, re-calibrate the incline set. |
| Incline motor | Inspect whether the incline motor is stuck. Inspect whether the incline gears are cracked. Test whether the incline motor has a broken circuit. Re-calibrate the incline set. |

The troubleshooting matrix adds: a wrong position sensor value on the incline motor. Turn the AC switch off and on again, then calibrate the monitor.

**Note on the printed text**: the section 8.4 heading reads "INCLINE E3" but its definition sentence still ends "so INCLINE ER appears", wording left over from the older manual. There is no ER code on this machine.

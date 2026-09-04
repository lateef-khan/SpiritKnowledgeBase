---
id: f60-2016-incline-er-message
title: 'INCLINE ER: no incline feedback signal'
kind: troubleshooting
question: What does INCLINE ER mean on a Sole F60-2016?
asked_as:
- incline er on my treadmill
- my treadmill will not incline and shows er
- er in the incline window
keywords:
- incline er
- er
- incline error
- incline vr
- potentiometer
- 5-pin cable
- incline motor
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: errors
  code: incline-er
authority: 3
not_to_be_confused_with:
- f60-2016-e0-error-code
- f60-2016-e1-error-code
- f60-2016-e2-error-code
- f60-2016-e4-error-code
- f60-2016-e5-error-code
- f60-2016-e6-error-code
see_also:
- f60-2016-error-code-list
- f60-2016-incline-position-sensor-test
- f60-2016-incline-motor-spec
source:
  ref: sole-tm-f60-2016-service-manual
  locator: pages 46 to 53, 8.3 Error Message INCLINE ER
  extracted_at: '2026-09-04'
---

**On this machine the incline fault is ER in the incline window, not E3.** This model has no E3 code at all. Do not confuse it with E2 (over current) or E6 (lower controller).

**The treadmill still runs with this error.** The manual says the console did not receive the incline feedback signal, ER appears at the incline window, but the treadmill is able to be operated.

The manual describes ER twice.

**ER at power on (section 8.3)**: the console board is not detecting the VR voltage value, or the value has exceeded the range. The incline motor is not operating up or down, so the VR value goes out of range. After the unit is switched on, the display board detects the incline VR voltage out of range and INCLINE ER appears.

| Part | Troubleshooting |
|---|---|
| Incline VR | Reconnect the VR wires. Inspect whether the incline wires are broken or disconnected. |
| Display board | Inspect the incline wire and the 5-pin cable connections. Test whether the VR voltage varies at the incline wire terminal. |
| 5-pin cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Driver board | Inspect the display board 5-pin connections. |

**ER during an incline (page 51)**: press the incline UP or DOWN key and the incline does not operate. The driver board UP or DOWN indicator lights, the incline should move the VR and change the VR value. If the CPU sees no VR value change, INCLINE ER appears.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline UP or DOWN key. If there is no action, inspect the cable and connections. |
| 5-pin cable | Inspect whether the 5-pin cable is connected well. Test by replacing the cable with a good one. |
| Driver board | Press incline UP or DOWN again to make the incline motor return to its position. If ER still appears, re-calibrate the incline set. |
| Incline motor | Inspect whether the incline motor is stuck. Inspect whether the incline gears are cracked. Test whether the incline motor has a broken circuit. Recalibrate the incline set. |

The troubleshooting matrix adds: a wrong position sensor value on the incline motor. Turn the AC switch off and on again, then calibrate the monitor.

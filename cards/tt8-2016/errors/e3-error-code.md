---
id: tt8-2016-e3-error-code
title: E3 incline VR voltage out of range
kind: troubleshooting
question: What does error E3 mean on a Sole tt8-2016 treadmill?
asked_as:
- e3 incline error on treadmill
- grade window shows e3
- incline will not move e3
keywords:
- e3
- incline err
- vr
- potentiometer
- position sensor
- incline motor
- calibration
- grade window
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016
  applies_to:
  - tt8-2016
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- tt8-2016-e0-error-code
- tt8-2016-e1-error-code
- tt8-2016-e2-error-code
- tt8-2016-e4-error-code
- tt8-2016-e5-error-code
- tt8-2016-e6-error-code
- tt8-2016-e7-error-code
- tt8-2016-ac-e3-error-code
see_also:
- tt8-2016-incline-vr-test-procedure
- tt8-2016-incline-position-sensor-wiring
- tt8-2016-calibration-procedure
source:
  ref: sole-tm-tt8-2016-service-manual
  locator: Sections 8.3 and Error Message E3 / INCLINE ERR, pages 46-54
  extracted_at: '2026-09-04'
---

**DC model: TT8 2016 ST925-YT021, DC drive motor. The AC inverter TT8 2016 (ST925A-YT030) is a different machine and this card does not apply to it.**

**This is E3, not E1 (no RPM signal) and not E7 (input power).**

Definition: the console board is not detecting the VR voltage value, or the voltage value has exceeded the
range, so "E3" appears on the display.

The manual states E3 in two places and the halves are different, so read both:

- **Out of range at power on.** The incline motor is not operating up or down, which lets the VR value run
  outside its range; after turning the unit on, the display board sees the incline VR voltage out of range
  and E3 appears.
- **INCLINE ERR during incline action.** Press the incline UP/DOWN key and the incline does not move. The
  display board CPU reads the incline VR value; if the value does not change, the CPU concludes the incline
  is not operating and E3 appears.

| Part | Troubleshooting |
|---|---|
| Display board | Press the incline keys and see whether the display shows a value. If not, check whether a key is stuck, or replace the upper control board. |
| Incline power cable & incline VR cable | Inspect the wire connections. Inspect whether wires are broken or crimped. |
| Driver board | Replace the driver board. Look for obviously and seriously damaged incline components on the lower control board. |
| Incline motor | Inspect whether the incline motor is stuck. Inspect whether the incline gears are cracked. Test whether the incline motor has a broken circuit. Recalibrate the incline set. |

The troubleshooting matrix gives a shorter route for the same symptom, printed as "GRADE window displays
E3": check the cable connector, calibrate the console, then replace the incline motor or the decline motor.

The AC-inverter TT8 2016 (ST925A-YT030) also prints a bare **E3**, but there it means the **rear
incline motor**. Do not carry this answer across to that machine.

---
id: e25-2023-e3-ramp-error
title: E3 ramp error, incline VR not read
kind: troubleshooting
question: What does error E3 or RAMP ERROR mean on a Sole e25-2023 elliptical?
asked_as:
- e3 ramp error on sole elliptical
- incline error e3 wont go up
- my e25 shows e3 when i turn it on
keywords:
- e3
- ramp error
- incline err
- incline
- vr
- potentiometer
- 14-pin cable
- calibration
- error code
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2023
  applies_to:
  - e25-2023
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e25-2023-e1-eeprom-failure
- e25-2023-e2-gear-motor-failure
see_also:
- e25-2023-incline-calibration
- e25-2023-incline-buttons-not-working
- e25-2023-incline-motor-spec
source:
  ref: sole-elliptical-e25-2023-service-manual
  locator: Error code list, section 8.3 and the troubleshooting matrix, pages 18,
    22-24, 28
  extracted_at: '2026-09-04'
---

**This is E3, not E1 (EEPROM) and not E2 (gear motor).**

Definition, as the error code list prints it: "The console is not detecting the incline motor VR voltage, or the voltage has exceeded the range." Section 8.3 words it as "The console board is not detecting the VR voltage value, or the voltage value has exceeded the range." **"RAMP ERROR" appears on the display.**

**Case the manual describes.** The incline VR value exceeds the range. The incline motor is not operating up or down, so the VR value goes outside its range. After the unit is turned on the display board detects that the incline VR voltage exceeds the range, so E3 appears.

| Part | Troubleshooting |
|---|---|
| Incline VR | Reconnect VR wires. Inspect whether the incline wires are broken or disconnected. |
| Display board | Inspect the incline wire and 14-pin cable connections. Test whether the VR voltage varies at the incline wire terminal. |
| 14-pin cable | Inspect the wire connections. Inspect whether wires are broken or crimped. Replace the wires and test again. |
| Driver board | Inspect the display board 14-pin connections. |

The troubleshooting matrix carries a second, shorter answer for the same fault, listed there as **"INCLINE ERR, INCLINE window shows E3 error code"** with the reason "Position sensor value of incline motor is wrong":

1. Turn off the AC switch and turn on power again.
2. Follow the section 8.6 calibration procedure to calibrate the incline motor.

Unlike the 2019 E25 manual, this manual prints E3 only once in section 8. It has no second E3 case for "no VR change during incline action".

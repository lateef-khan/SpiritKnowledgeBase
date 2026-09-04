---
id: e98-2023-incline-err
title: INCLINE ERR on the display
kind: troubleshooting
question: What does INCLINE ERR mean on a Sole e98-2023 elliptical?
asked_as:
- my sole elliptical says incline err
- incline error on the e98 touchscreen
- elliptical incline stopped working and shows an error
keywords:
- incline err
- e3
- position sensor
- incline motor
- ac switch
- calibration
- error code
- matrix
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2023
  applies_to:
  - e98-2023
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- e98-2023-eeprom-err
- e98-2023-lwr-not-found
- e98-2023-lwr-not-match
see_also:
- e98-2023-incline-calibration
- e98-2023-incline-buttons-not-working
source:
  ref: sole-elliptical-e98-2023-service-manual
  locator: Troubleshooting procedure matrix, page 24
  extracted_at: '2026-09-04'
---

The troubleshooting matrix row reads: **"INCLINE ERR, INCLINE window shows 'E3' error code."**

| Reason | Solve |
|---|---|
| Position sensor value of incline motor is wrong. | 1. Turn off the AC switch and turn on power again. 2. Follow the section 8.6 calibration procedure to calibrate the incline motor. |

**This manual contradicts itself about the code.** The error code list in section 8 has only three entries - EEPROM ERR, LWR not found, LWR not match - and **E3 is not one of them**. The matrix row is the only place in the manual that mentions E3, and it is a leftover from the older keypad-console manuals, where E3 was the ramp error. Do not tell a customer this console displays E3 unless they have read it off the screen themselves.

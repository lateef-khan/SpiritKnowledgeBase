---
id: e25-2026-e2-tension-motor-failure
title: E2 tension motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole e25-2026 elliptical and how is it fixed?
asked_as:
- my sole elliptical shows e2
- resistance will not change and it says e2
- what is error code e2 on an e25 2026
keywords:
- e2
- tension motor
- gear motor
- drive board
- resistance
- level up
- level down
- error code
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2026
  applies_to:
  - e25-2026
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- e25-2026-e1-eeprom-failure
- e25-2026-e3-ramp-error
see_also:
- e25-2026-tension-motor-voltage-test
- e25-2026-tension-motor-spec
source:
  ref: sole-elliptical-e25-2026-service-manual
  locator: 'Section 8.2, Error Message: E2, pages 24-25'
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (incline VR).**

Definition: when you press the **Level Up or Down key the motor does not move**, and **"E2" appears on the LEVEL windows**. The error code list prints the meaning as "Tension motor is failure".

How the circuit is meant to work:

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive Board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

Troubleshooting:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive Board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The numbered voltage test that confirms this is in a separate card.

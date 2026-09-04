---
id: e35-2019-e2-tension-motor-failure
title: E2 tension motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole e35-2019 elliptical and how is it diagnosed?
asked_as:
- e2 on my sole elliptical
- resistance wont change and it shows e2
- level up does nothing e2 error
keywords:
- e2
- tension motor
- resistance
- level up
- level down
- drive board
- error code
- elliptical
facets:
  brand:
  - sole
  product_line: elliptical
  model: e35-2019
  applies_to:
  - e35-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- e35-2019-e1-eeprom-failure
- e35-2019-e3-ramp-error
see_also:
- e35-2019-tension-motor-voltage-test
- e35-2019-tension-motor-connector-pinout
- e35-2019-tension-motor-spec
source:
  ref: sole-elliptical-e35-2019-service-manual
  locator: Section 8.2, pages 41-42
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (ramp / incline VR).**

Definition: when you press the Level Up or Down key the motor does not move; **"E2" appears on the display**. The error table prints the meaning as "Tension motor is failure".

How the circuit is meant to work:

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

Troubleshooting:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The numbered voltage test that confirms this is in a separate card.

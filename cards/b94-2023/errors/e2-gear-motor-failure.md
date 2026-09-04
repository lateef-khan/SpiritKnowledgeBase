---
id: b94-2023-e2-gear-motor-failure
title: E2 gear motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole B94-2023 bike and how is it diagnosed?
asked_as:
- e2 on my 2023 sole bike
- resistance wont change and it shows e2
- level up does nothing e2 error b94
keywords:
- e2
- gear motor
- resistance
- level up
- level down
- drive board
- error code
- upright bike
facets:
  brand:
  - sole
  product_line: bike
  model: b94-2023
  applies_to:
  - b94-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- b94-2023-e1-eeprom-failure
see_also:
- b94-2023-gear-motor-voltage-test
- sole-bike-tension-motor-error
source:
  ref: sole-bike-b94-2023-service-manual
  locator: 'Section 8 Error Code List and Section 8.2 Error Message: E2, page 18'
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM). Those are the only two codes this bike has.**

Definition: you press the Level Up or Level Down key, the motor does not move, and **"E2" appears on the display**. The error table prints the meaning as "Gear motor is failure".

How the parts are meant to work:

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive Board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

How to find the fault:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive Board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The numbered voltage test that confirms this is in a separate card. A multi-meter is the only tool the manual asks for.

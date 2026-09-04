---
id: e25-2023-e2-gear-motor-failure
title: E2 gear motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole e25-2023 elliptical and how is it fixed?
asked_as:
- sole elliptical shows e2
- resistance wont change and it says e2
- what is e2 on a sole e25
keywords:
- e2
- gear motor
- resistance
- level up
- level down
- drive board
- error code
- data cable
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2023
  applies_to:
  - e25-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- e25-2023-e1-eeprom-failure
- e25-2023-e3-ramp-error
see_also:
- e25-2023-gear-motor-voltage-test
- e25-2023-gear-motor-spec
source:
  ref: sole-elliptical-e25-2023-service-manual
  locator: Error code list and section 8.2, pages 18, 20-21
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (ramp / incline VR).**

Definition: **when you press the Level Up or Down key the motor does not move, and "E2" appears on the display.** The error code list prints the meaning as "Gear motor is failure".

How the parts are supposed to behave:

| Part | Description |
|---|---|
| Display | The key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive board | Receives the signal and responds by putting out power to the motor. Level UP: **+5VDC**; Level DOWN: **-5VDC**. |

Troubleshooting:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive board | Inspect the drive board power output to the motor: Level Up is **+5VDC**, Level Down is **-5VDC**. If there is power to the motor but the motor does not operate, replace the motor. If there is no power output, inspect whether the drive board has power. |

The meter procedure that produces those readings is a separate card.

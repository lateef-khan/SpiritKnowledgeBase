---
id: e95-2016-e2-tension-motor-failure
title: E2 tension motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole e95-2016 elliptical and how is it fixed?
asked_as:
- my sole machine shows e2
- resistance wont change and it says e2
- what is error code e2 on a sole elliptical
keywords:
- e2
- e-2
- tension motor
- resistance
- level up
- drive board
- error code
- gear motor
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95-2016
  applies_to:
  - e95-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- e95-2016-e1-eeprom-failure
- e95-2016-e3-ramp-error
see_also:
- e95-2016-tension-motor-voltage-test
- e95-2016-tension-motor-spec
- e95-2016-tension-motor-connector-pinout
source:
  ref: sole-elliptical-e95-2016-service-manual
  locator: Section 8-2, pages 42-44
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (ramp / incline VR).**

Definition: when you press the Level Up or Level Down key the motor does not move, and **"E-2"** appears on the display. The error table prints the meaning as "Tension motor is failure".

**Tension motor operation**

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Drive board | Drive board receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

**Tension motor troubleshooting**

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Drive board | Inspect drive board power output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

The multimeter procedure is in its own card.

Note the printing: the error code table lists this fault as **E2**, while the section heading and the definition both write **E-2**. They are the same fault.

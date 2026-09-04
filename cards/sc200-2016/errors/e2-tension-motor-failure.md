---
id: sc200-2016-e2-tension-motor-failure
title: E2 tension motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole sc200-2016 climber and how is it fixed?
asked_as:
- my sole sc200 shows e2
- resistance wont change and it says e2
- what is error code e2 on a sole climber
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
  model: sc200-2016
  applies_to:
  - sc200-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- sc200-2016-e1-eeprom-failure
see_also:
- sc200-2016-tension-motor-voltage-test
- sc200-2016-tension-motor-spec
- sc200-2016-tension-motor-connector-pinout
source:
  ref: sole-elliptical-sc200-2016-service-manual
  locator: Section 8-2, pages 37-40
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM) and not E3 (ramp / incline VR).**

Definition: when you press the Level Up or Level Down key the motor does not move, and **"E2"** appears on the display. The error table prints the meaning as "Tension motor is failure".

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

**This manual names the tension motor where the elliptical manuals name a drive board.** Its tables read:

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Tension motor | The tension motor receives the signal and responds by putting out power to the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

and for troubleshooting:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Tension motor | Inspect display board output to the motor. Press the Level Up is +5VDC; Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

A second table names the cable:

| Part | Troubleshooting |
|---|---|
| Display board | 1. Inspect the 8-pin cable connections. |
| 8-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Tension motor | Inspect the display board 8-pin connections. |

**This machine has no E3.** The error table lists only E1 and E2.

---
id: sc200-2019-e2-tension-motor-failure
title: E2 tension motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole sc200-2019 and how is it diagnosed?
asked_as:
- e2 on my sole climber
- resistance wont change and it shows e2
- level up does nothing e2 error
keywords:
- e2
- tension motor
- resistance
- level up
- level down
- 8-pin cable
- error code
- climber
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2019
  applies_to:
  - sc200-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- sc200-2019-e1-eeprom-failure
see_also:
- sc200-2019-tension-motor-voltage-test
- sc200-2019-tension-motor-connector-pinout
- sc200-2019-tension-motor-spec
- sc200-2019-console-connector-pinout
source:
  ref: sole-elliptical-sc200-2019-service-manual
  locator: Section 8-2, pages 34-37
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM). This machine has only two error codes.**

Definition: when you press the Level Up or Down key the motor does not move; **"E2" appears on the display**. The error table prints the meaning as "Tension motor is failure".

How the circuit is meant to work:

| Part | Description |
|---|---|
| Display | Key signal travels to the display. The main program IC then sends a command signal to the drive board. |
| Tension motor | Tension motor receives the signal and responds by putting out power to the motor. Level UP: **+2.5VDC**; Level DOWN: **-2.5VDC**. |

Troubleshooting:

| Part | Description |
|---|---|
| Display | If the key beeps when pressed, assume that the signal was sent. |
| Data cable | Inspect the cable and connections. |
| Tension motor | Inspect display board output to the motor. Press the Level Up is +2.5VDC; Level DOWN is -2.5VDC. If there is power to the motor but the motor does not operate, replace it. If there is no power output, inspect whether the drive board has power. |

A second table names the cable to check:

| Part | Troubleshooting |
|---|---|
| Display board | 1. Inspect the 8-pin cable connections. |
| 8-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Tension motor | Inspect the display board 8-pin connections. |

**The drive voltage on this machine is +/-2.5VDC, not the +/-5VDC of the 2019 Sole ellipticals.** Do not carry the elliptical figure over. The numbered voltage test is in a separate card.

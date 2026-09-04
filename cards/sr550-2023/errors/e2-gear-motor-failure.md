---
id: sr550-2023-e2-gear-motor-failure
title: E2 gear motor failure
kind: troubleshooting
question: What does error E2 mean on a Sole sr550-2023 rower and how is it fixed?
asked_as:
- my sole rower says e2
- resistance will not change and it shows e2
- what is error code e2 on an sr550
keywords:
- e2
- gear motor
- error code
- resistance
- level up
- level down
- data cable
- transformer
- rower
facets:
  brand:
  - sole
  product_line: rower
  model: sr550-2023
  applies_to:
  - sr550-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- sr550-2023-gear-motor-voltage-test
- sr550-2023-gear-motor-spec
- sr550-2023-resistance-will-not-adjust
- sole-rower-e2-part-to-replace
source:
  ref: sole-rower-sr550-2023-service-manual
  locator: Section 8, error code list page 16, and section 8.1 page 17
  extracted_at: '2026-09-04'
---

**E2 is the only error code this manual documents.** The error code list has one row: E2, "Gear motor is failure". There is no E1 in this manual.

Definition: when you press the **Level Up or Down key the motor does not move**, and **"E2" appears on the display**.

How the circuit is meant to work:

| Part | Description |
|---|---|
| Console | Key signal travels to the display. The main program IC then sends a command signal to the gear motor. The console directly controls the motor. Level UP: +5VDC; Level DOWN: -5VDC. |

Troubleshooting:

| Part | Description |
|---|---|
| Console | If the key beeps when pressed, assume that the signal was sent. Inspect console power output to the motor: Level Up is +5VDC, Level Down is -5VDC. **If there is power to the motor but the motor does not operate, replace it.** If there is no power output, **inspect whether the transformer has power**. |
| Data cable | Inspect the cable and connections. |

**The manual is not consistent about what drives the motor.** The tables above say the console controls the motor directly, but the voltage test tells you to probe "on the drive board", and the test configuration page is titled "The console to driver board connector pin define function". Expect a driver board in the circuit whichever table you read.

The numbered voltage test is in a separate card.

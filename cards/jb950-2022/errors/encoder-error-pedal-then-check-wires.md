---
id: jb950-2022-errors-encoder-error-pedal-then-check-wires
title: 'ENCODER ERROR: keep pedalling and reset, then check the console-to-controller
  wire, the motor wire and the brake assembly'
kind: troubleshooting
question: What does ENCODER ERROR mean on a Spirit jb950-2022 Johnny G bike and how
  is it fixed?
asked_as:
- johnny g bike says encoder error
- jb950 encoder error on the console
- spirit indoor bike encoder sensor not reading
- encoder error after pedalling slowly
keywords:
- encoder error
- encoder sensor
- capacitor voltage
- motor wire
- controller
- brake assembly
- reset console
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: encoder-error
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-using-default-setup-reset-then-mcu-board
- jb950-2022-errors-hr-sensor-error-reset-console
see_also:
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- spirit-jb950-errors-limit-sensor-test-after-motor-error
- jb950-2022-errors-error-message-table-four-messages
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.1 Error Messages table, PDF p. 37, text.md
    lines 564-593
  extracted_at: '2026-09-11'
---

**This is `ENCODER ERROR`, one of four messages the JB950 console prints. It is not `MOTOR ERROR`, the row above it, where the encoder *does* read and the brake fails to home.**

| Explanation | Troubleshooting |
|---|---|
| 1. Capacitor voltage is too low, causing ENCODER SENSOR not to read. | 1. Continue to pedal and press Play and + Key to Reset Console to see if it has been remedied |
| 2. Bad Wire connection causing ENCODER SENSOR not to read | 2. Check if the wire between the console & controller is seated properly. |
| 3. MOTOR wire is disconnected, MOTOR does not operate, ENCODER SENSOR has no signal | 3. Check if the MOTOR wire is seated properly. 4. Check if brake assembly is malfunctioning. |

The first cause is electrical starvation: the bike is generator powered and the encoder cannot be read until the capacitor has charged, so the first fix is to **keep pedalling and reset** (`PLAY` and `+` together). Only then does the book go to the 9-pin system cable between console and controller, the motor wire at the brake, and the brake assembly itself.

The encoder is the optical wheel and sensor on the DC motor encoder board inside the brake assembly, and its count is shown live in the maintenance-mode brake test (`spirit-jb950-errors-limit-sensor-test-after-motor-error`). An encoder that reads but a brake that never homes is `jb950-2022-errors-motor-error-brake-does-not-reach-home`.

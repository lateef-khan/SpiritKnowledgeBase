---
id: jb950-2022-errors-motor-error-brake-does-not-reach-home
title: 'MOTOR ERROR: the encoder reads but the brake never reaches home, so check
  the cables, then the brake assembly, then the limit sensor board and controller'
kind: troubleshooting
question: What does MOTOR ERROR mean on a Spirit jb950-2022 Johnny G bike and how
  is it fixed?
asked_as:
- johnny g bike says motor error
- jb950 brake motor error
- spirit indoor bike motor error and no resistance
- brake wont go to home position on the jb950
keywords:
- motor error
- brake
- home position sensor
- encoder
- brake position flag
- limit sensor board
- controller
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: motor-error
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- jb950-2022-errors-using-default-setup-reset-then-mcu-board
- jb950-2022-errors-hr-sensor-error-reset-console
see_also:
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- spirit-jb950-errors-limit-sensor-test-after-motor-error
- jb950-2022-errors-no-resistance-control-board-wiring-then-brake-test
- jb950-2022-errors-error-message-table-four-messages
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.1 Error Messages table, PDF p. 37, text.md
    lines 564-593
  extracted_at: '2026-09-11'
---

**This is `MOTOR ERROR`, one of four messages the JB950 console prints. It is not `ENCODER ERROR`, the next row down, even though both concern the brake.**

| Explanation | Troubleshooting |
|---|---|
| 1. ENCODER is read, but motor does not reach home position. | 1. Make sure cables aren't broken or shorted to other pins or the frame. 2. Brake position flag may have crashed into, or traveled past the home position sensor. Replace brake assembly. 3. Replace the Limit SENSOR BOARD & controller |

The order is the book's: cables first, then the brake assembly (whose position flag can strike or overrun the home position sensor), and the limit sensor board together with the controller last.

The brake here is a gear-motor-driven magnetic brake with a closed-loop encoder and two optical limit sensors - home and upper - on a limit sensor board, all named in the wiring chapter of the same book. The `LIMIT SENSOR` screen inside the maintenance-mode brake test, which shows the home sensor, the end sensor and the encoder count while you drive the brake with `+` and `-`, is the check the book says to run **only after a motor error**: `spirit-jb950-errors-limit-sensor-test-after-motor-error`.

An encoder that gives no reading at all is the other message: `jb950-2022-errors-encoder-error-pedal-then-check-wires`. No resistance with no message on the screen is a matrix row: `jb950-2022-errors-no-resistance-control-board-wiring-then-brake-test`.

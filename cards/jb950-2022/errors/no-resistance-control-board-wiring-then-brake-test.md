---
id: jb950-2022-errors-no-resistance-control-board-wiring-then-brake-test
title: 'No resistance: the control board, the brake wiring, then the brake test in
  maintenance mode'
kind: troubleshooting
question: Why is there no resistance on a Spirit jb950-2022 Johnny G bike?
asked_as:
- no resistance on the johnny g bike
- jb950 pedals spin free with no load
- spirit indoor bike brake not working
- jb950 level up does nothing
keywords:
- no resistance
- control board
- brake wiring
- brake test
- maintenance mode
- magnetic brake
- gear motor
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: no-code
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- ce800ent-no-resistance
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
see_also:
- spirit-jb950-errors-limit-sensor-test-after-motor-error
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- ce800ent-no-resistance
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.4 Troubleshooting procedure matrix, PDF p.
    45, text.md lines 839-868
  extracted_at: '2026-09-11'
---

The condition is printed as `No resistance`.

| Reason | Solving |
|---|---|
| 1. Control board malfunction. 2. Brake wiring bad connection. | 1. Replace with new Control board. 2. Please check wiring. 3. Run brake test in Maintenance mode. |

**The third step is a test, not a part.** `BRAKE TEST` in maintenance mode drives the magnetic brake from L-1 to L-20 and back automatically, or to a target you set, and shows the encoder count and the limit-sensor state (1 = home, 2 = active range, 3 = end) while it does - the book's own tool for telling a dead brake from a dead controller. The test is a console fact; the screen inside it that the book says to run after a motor error is `spirit-jb950-errors-limit-sensor-test-after-motor-error`.

The brake here is a gear motor moving neodymium magnets against an aluminium flywheel, with an encoder and two limit sensors on the brake assembly; the control board is the lower controller under the chain covers. **No resistance with a message on the screen is a different entry**: `MOTOR ERROR` (`jb950-2022-errors-motor-error-brake-does-not-reach-home`) or `ENCODER ERROR` (`jb950-2022-errors-encoder-error-pedal-then-check-wires`).

The generator-brake commercial bikes answer the same row with a control board, a resistance-voltage wire and a driver IC in the console (`ce800ent-no-resistance`); none of those parts is on this machine.

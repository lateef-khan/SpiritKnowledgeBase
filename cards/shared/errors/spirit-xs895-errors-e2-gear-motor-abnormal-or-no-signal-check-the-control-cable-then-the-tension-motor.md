---
id: spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
title: 'E2 on the incline stepper means the gear motor is abnormal or the display
  board gets no signal from it: the control cable, then the tension motor, then 5
  volts at the drive board'
kind: troubleshooting
question: What does E2 mean on a Spirit XS895 stepper?
asked_as:
- xs895 shows e2
- incline stepper resistance motor error
- what does e2 mean on my spirit stepper
keywords:
- e2
- gear motor
- tension motor
- control cable
- replug
- drive board
- 5vdc
- incline stepper
- error code
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- spirit-xs895-errors-e1-eeprom-defective-replace-the-display-board
- spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr
- cs800-2016-errors-e2-tension-motor-failure-5-volts-and-the-10-pin-cable
- cvc800-e-2-tension-motor-error
- crw800-2024-errors-e2-cable-tension-communication-error
see_also:
- spirit-xs895-errors-error-code-table-three-codes
- spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- sc200-2019-e2-tension-motor-failure
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 7-1 Error Codes, PDF p. 26 (printed 25), text.md lines 360-366; 7-4 Error
    Message E2, 7-4-1 Tension Motor Operation and 7-4-2 Tension Motor Troubleshooting,
    PDF p. 27-29 (printed 26-28), text.md lines 388-437
  extracted_at: '2026-09-11'
---

| Error Code | CAUSE |
|---|---|
| E2 | Tension motor is failure |

**7-4 Error Message: E2.** Definition: Gear motor operate abnormal or display board can't receive signal from gear motor. Troubleshooting: 1. Check the control cable and replug it. 2. Check the tension motor.

**The book calls the same part a gear motor and a tension motor on one page.** It is the motor that pulls the resistance cable; the drawing shows the display board sending a *level up/down signal* and receiving a *level count signal* back, with a separate *motor voltage* line from the driver board.

**7-4-1 Tension Motor Operation.** Display: key signal travels to the display; the main program IC then sends a command signal to the drive board. Drive Board: receives the signal and responds by putting out power to the motor. Level UP: **+5VDC**; Level DOWN: **-5VDC**.

**7-4-2 Tension Motor Troubleshooting.** Display: if the key beeps when pressed, assume that the signal was sent. Data cable: inspect the cable and connections. Drive Board: inspect drive board power output to the motor - Level Up is +5VDC, Level DOWN is -5VDC. If there is power to the motor but the motor does not operate, **replace it**. If there is no power output, inspect whether the drive board has power.

**On this machine the motor is driven from a separate drive board**, not from the console as on the CS800 (2020) and CRS800S; that is where the probes go for the voltage test, which passes a band of 5.5 to 6.0 V rather than the 5 V these tables quote (`spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led`).

The CS800 (2020) and 2024 print this fault as `Err` in the LEVEL window with the same two-step remedy (`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`). Sole prints this code for its SC200 2019 (`sc200-2019-e2-tension-motor-failure`).

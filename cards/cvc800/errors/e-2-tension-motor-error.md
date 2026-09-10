---
id: cvc800-e-2-tension-motor-error
title: 'E-2: the tension motor is faulty or sending the wrong signal'
kind: troubleshooting
question: What does E-2 mean on a Spirit CVC800 climber?
asked_as:
- what does e-2 mean on my spirit climber
- climber showing e2
- no resistance and an error on my climber
keywords:
- e-2
- e2
- motor error
- tension motor
- level vr
- resistance
- display board
- error code
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: errors
  code: e2
  model_number: '800440'
authority: 3
not_to_be_confused_with:
- cvc800-e-1-ram-error
- e25-2016-e2-tension-motor-failure
- sole-bike-tension-motor-error
see_also:
- cvc800-tension-motor-voltage-test
- cvc800-e-1-ram-error
- e25-2016-e2-tension-motor-failure
- sole-bike-tension-motor-error
source:
  ref: spirit-climber-cvc800-service-manual
  locator: 'Section 8-2 Error Message: E-2, pages 29-30'
  extracted_at: '2026-09-08'
---

**This is E-2, not E-1, and not Sole's E2.** The CVC800 prints its codes with a hyphen.

Definition, word for word:

> MOTOR ERROR:
> Tension Motor operates abnormal or provide wrong signal to the console.

The signal path the manual draws: the `+/- KEYS` and `LEVEL +/- KEYS` feed the display board; the
display board sends a `Level +/- Signal` to the tension motor, and the motor returns a
`Level VR Signal`.

**Tension Motor Operation**

| Part | Description |
|---|---|
| Console | Key signal travels to the display. The main program IC then sends a command signal to the drive board. Console directly controls the motor. Level UP: +2.5VDC; Level DOWN: -2.5VDC |

**Tension Motor Troubleshooting**

| Part | Description |
|---|---|
| Console | If the key beeps when pressed, assume that the signal was sent. Inspect console power output to the motor. Press the Level Up is +4.5VDC; Level DOWN is -4.5VDC. If there is power to the motor, but the motor does not operate, replace it. If there is no power output, inspect whether the transformer has power. |
| Data cable | Inspect the cable and connections. |

**These two tables print two different voltages for the same signal.** The operation table says the
console drives the motor at +/-2.5 VDC; the troubleshooting table on the same page says to expect
+/-4.5 VDC at the console output, and the voltage test procedure on the next page says +4 to 5.5 V.
The manual never reconciles them. Measure against the **+4 to 5.5 V** band from the test procedure,
which is the only one given as a range with a pass condition attached - see
`cvc800-tension-motor-voltage-test`.

If the key beeps, the console did its part; the fault is downstream.

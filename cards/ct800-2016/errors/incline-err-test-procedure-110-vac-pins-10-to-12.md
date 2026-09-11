---
id: ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12
title: 'Measuring the incline circuit when the incline will not run: ~110 VAC at the
  motor and the sensor on pins 10 to 12'
kind: procedure
question: How do I test the incline motor and position sensor on a Spirit ct800-2016
  treadmill?
asked_as:
- how to test the incline motor on a spirit treadmill
- incline potentiometer voltage test
- incline calibration keeps failing
keywords:
- incline motor
- potentiometer
- position sensor
- relay
- incline board
- vr
- 5vdc
- pin 10 pin 11 pin 12
- 110 vac
- jk13
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: errors
  code: incline-err
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-test-procedure
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
see_also:
- ct850-2016-incline-err-vr-out-of-range
- ct800-2016-errors-incline-err-during-incline-action
- ct800-2016-errors-incline-calibration-fails-checks-wire-colours
- ct800-2016-errors-controller-led-debugging-90-to-110-v
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: CT800 2016 service manual Test configuration, Pin definition and Test Procedure,
    PDF p. 43-47 (printed 42-46), text.md lines 729-900
  extracted_at: '2026-09-11'
---

Nine steps, in the manual's order. A multi-meter is the only tool named.

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor doesn't move: with the incline light and relay activated, check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire, whichever way the motor should be travelling. **It should be about the mains voltage, ~110 VAC.** Voltage present and no movement means the motor is bad.
   - If the light is on but the relay does not click on, the incline board needs replacing (bad relay, most likely).
5. If the motor moves, is there a sensor reading on the console? After the speed calibration ends the INCLINE window shows the computer incline setting, **15 for maximum and 0 for lowest**; the window is a counter showing the actual position sensor output. Motor moving and no count means the position sensor wiring or circuitry.
   - A count that still fails calibration: the potentiometer may be loose and giving false readings - it should not be able to rotate. Remove the cover from the rear of the motor and try it; check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. All tight means the potentiometer could be bad.
   - No count: check the voltage at the potentiometer - **5 Vdc between the black and red wires**, and **about 4.5 to 4.7 Vdc between the red and white wires with the motor at its lowest position**. Voltage on the white wire that changes as the motor moves, with no count, means a bad wire between the potentiometer and the console.
6. Check the potentiometer voltage at the 3-pin connector on the incline board. None means the wire from the motor to the connector is faulty.
7. If there is voltage, check the output connector to the console at the bottom of the incline board. None means a fault on the incline board - no electronic components sit in this signal path, only circuit connections, so a bad solder joint or broken track.
8. Voltage at the output connector but none at the console: check the whole cable from incline board to console for cuts or bad connections at the inline connectors.
9. Voltage at the console connector and no count while the motor moves: the console.

**The console connector pins are numbered 10 to 12 on this machine**, the same at the incline board and at the console:

| Pin | Signal |
|---|---|
| 10 | 5 Vdc |
| 11 | position signal 0~5 Vdc |
| 12 | ground |

That matches the 12-pin JK13/JK1 pin definitions printed two pages earlier - **P10 +VCC, P11 VR IN, P12 GND** - and the 3-pin JK4 incline VR connector, **P1 +VCC, P2 VR IN, P3 GND**. The motor power connector JK2 is **black = DOWN, white = COM, red = UP**, and the motor connector is **white = M-, red = M+**.

**The CT850 2016 service manual prints the same nine steps with ~230 VAC and a 3-pin console connector numbered 1 to 3** (`ct850-2016-incline-err-test-procedure`). The XT books print ~110 VAC (230 VAC) and pins 1 to 3 (`spirit-xt-errors-e3-incline-test-procedure-nine-steps`). The calibration-fails page later in this book repeats the pin list with wire colours (`ct800-2016-errors-incline-calibration-fails-checks-wire-colours`).

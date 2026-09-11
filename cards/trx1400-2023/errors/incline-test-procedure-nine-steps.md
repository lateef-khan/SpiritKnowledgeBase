---
id: trx1400-2023-errors-incline-test-procedure-nine-steps
title: 'Testing the incline after an Err in nine steps: lights and relay, ~110 VAC
  across the motor leads, 5 V DC and 4.5 to 4.7 V DC at the potentiometer, then the
  count in the INCLINE window'
kind: procedure
question: How do I test the incline motor and position sensor after an Err on an Xterra
  trx1400-2023 treadmill?
asked_as:
- trx1400 incline test procedure
- incline motor voltage test 110vac
- potentiometer 5 volt test incline treadmill
keywords:
- err
- incline motor
- potentiometer
- position sensor
- relay
- 110vac
- 5vdc
- 4.5 to 4.7 vdc
- incline window count
- pin 1 5vdc
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: errors
  code: err
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-test-procedure
see_also:
- trx1400-2023-errors-err-or-e3-incline-vr-out-of-range
- trx1400-2023-errors-incline-err-no-vr-change-when-incline-runs
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM Test configuration and Test Procedure for Err, PDF pp. 48-50
    (printed 47, 49, 59); text.md lines 782-865
  extracted_at: '2026-09-11'
---

The TRX1400 service manual follows its Err section with a *Test Procedure* that no other Xterra book prints:

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - If the relay clicks but the motor doesn't move: with the incline light and relay activated, check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire, whichever direction the board's Up/Down light says the motor should travel. It should be about mains voltage, **~110 VAC (230 VAC)**. If the voltage is present but the motor doesn't move, the motor is bad.
   - If the light is on but the relay does not click, the incline board needs replacing (bad relay most likely).
5. If the motor moves, is there a sensor reading on the console?
   - The INCLINE window shows the computer's incline setting after speed calibration ends - **15 for maximum incline, 0 for lowest**. During the test the Incline window is a counter showing the actual position sensor output. Motor moving with no count in the window means a problem in the position sensor wiring or circuitry.
   - A count that still fails calibration: the potentiometer could be loose, giving false readings (it should not be able to rotate). Remove the cover from the rear of the motor and see if the potentiometer is loose; check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. If everything is tight, the potentiometer could be bad.
   - No count: check the voltage at the potentiometer. There should be **5 V DC between the black and red wires**, and a voltage between red and white of **about 4.5 to 4.7 V DC at the lowest position** (the figure is not critical). If the white-wire voltage changes as the motor moves but the counter does not register, suspect a bad wire between the potentiometer and the console.
6. Check the potentiometer voltage at the 3-pin connector on the incline board. None: the wires from the motor to the connector are faulty.
7. If there is voltage, check at the output connector to the console at the bottom of the incline board. None: the problem is on the incline board - there are no electronic components in this path, only circuit connections, so only a bad solder joint or a broken track is possible.
   - Console connector wiring, the same at the incline board and at the console: **pin 1 = 5 V DC, pin 2 = position signal 0 to 5 V DC, pin 3 = ground.**
8. Voltage at the output connector but none at the console: check the whole cable from incline board to console for cuts or a bad inline connector.
9. Voltage at the console connector but no count in the INCLINE window while the motor moves: the problem is the console.

The "15 for max incline" figure is the book's; the same book's calibration procedure sets maximum elevation to 10. The Spirit XT books print this procedure word for word (`spirit-xt-errors-e3-incline-test-procedure-nine-steps`).

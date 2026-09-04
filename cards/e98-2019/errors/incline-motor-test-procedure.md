---
id: e98-2019-incline-motor-test-procedure
title: Incline motor and position sensor test procedure
kind: procedure
question: How do I test the incline motor and its position sensor on a Sole e98-2019
  elliptical?
asked_as:
- incline motor not moving on sole elliptical how to test
- how do i check the incline potentiometer
- incline counter not changing on the console
keywords:
- incline motor
- potentiometer
- position sensor
- relay
- 115vac
- incline board
- calibration
- test
facets:
  brand:
  - sole
  product_line: elliptical
  model: e98-2019
  applies_to:
  - e98-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- e98-2019-e3-incline-vr-error
- e98-2019-incline-calibration
- e98-2019-incline-motor-spec
source:
  ref: sole-elliptical-e98-2019-service-manual
  locator: Test Procedure, page 42
  extracted_at: '2026-09-04'
---

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor does not move: with the incline light and relay activated, check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire, depending on which direction the motor is supposed to travel according to the Up/Down lights on the board. It should be about the same as the mains voltage, **~115VAC**. If the voltage is present but the motor does not move, the motor is bad.
   - If the light is on but the relay does not click on, the incline board needs to be replaced (bad relay most likely).
5. If the motor moves, is there a sensor reading on the console?
   - The INCLINE window shows the computer incline setting after speed calibration ends; **20 for max incline, 0 for lowest incline**. If the motor is moving and there is no count in the Incline window, there is a problem in the position sensor wiring or circuitry.
   - If there is a count but calibration fails, the potentiometer could be loose (it should not be able to rotate). Remove the cover from the rear of the motor and check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. If everything is tight the potentiometer could be bad.
   - If there is no count, check the voltage at the potentiometer. There should be **5vdc between the black and red wire**, and a voltage between the red and white wire of about **4.5~4.7 Vdc when the motor is at the lowest position** (the number is not critical). If the white-wire voltage changes as the motor moves but the counter does not register, there may be a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage is present there is a problem on the incline board. There are no electronic components on the board for this signal, only circuit connections, so the only possible faults are a bad solder joint or a broken circuit.
   Console connector wiring, the same on the incline board and at the console: **Pin 3 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 1 = ground.**
8. If there is voltage at the output connector to the console, check the voltage at the console. If there is none there but there is at the incline board, check the entire cable for cuts or bad connections at the inline connectors.
9. If there is voltage at the console connector but no count in the Incline window when the motor is moving, the problem is with the console.

The incline motor drawing labels the three mains leads **white = COM, red = UP, black = DOWN**, on a 6-way connector.

---
id: e95s-2019-stride-motor-test-procedure
title: Stride motor and position sensor test procedure
kind: procedure
question: How do I test the stride motor and its position sensor on a Sole e95s-2019
  elliptical?
asked_as:
- stride motor not moving on my sole elliptical
- how do i check the stride potentiometer
- stride counter not changing on the console
keywords:
- stride motor
- potentiometer
- position sensor
- relay
- 115vac
- stride board
- calibration
- test
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2019
  applies_to:
  - e95s-2019
  section: errors
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- e95s-2019-e3-stride-error
- e95s-2019-stride-calibration
- e95s-2019-stride-motor-spec
source:
  ref: sole-elliptical-e95s-2019-service-manual
  locator: Test Procedure, page 48
  extracted_at: '2026-09-04'
---

1. Run calibration again.
2. Does the stride motor move at all?
3. If no, do the Up/Down lights on the stride board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor does not move: with the stride light and relay activated, check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire, depending on which direction the motor is supposed to travel according to the Up/Down lights on the board. It should be about the same as the mains voltage, **~115VAC**. If the voltage is present but the motor does not move, the motor is bad.
   - If the light is on but the relay does not click on, the stride board needs to be replaced (bad relay most likely).
5. If the motor moves, is there a sensor reading on the console?
   - The window shows the computer stride setting after speed calibration ends; **20 for max stride, 0 for lowest stride**. If the motor is moving and there is no count in the Stride window, there is a problem in the position sensor wiring or circuitry. (The manual writes "The INCLINE window will display the computer stride setting"; on this machine the window is the stride window.)
   - If there is a count but calibration fails, the potentiometer could be loose (it should not be able to rotate). Remove the cover from the rear of the motor and check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. If everything is tight the potentiometer could be bad.
   - If there is no count, check the voltage at the potentiometer. There should be **5vdc between the black and red wire**, and a voltage between the red and white wire of about **4.5~4.7 Vdc when the motor is at the lowest position** (the number is not critical). If the white-wire voltage changes as the motor moves but the counter does not register, there may be a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the 3-pin connector on the stride board. If there is no voltage the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the stride board. If no voltage is present there is a problem on the stride board. There are no electronic components on the board for this signal, only circuit connections, so the only possible faults are a bad solder joint or a broken circuit.
   Console connector wiring, the same on the stride board and at the console: **Pin 3 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 1 = ground.**
8. If there is voltage at the output connector to the console, check the voltage at the console. If there is none there but there is at the stride board, check the entire cable for cuts or bad connections at the inline connectors.
9. If there is voltage at the console connector but no count in the Stride window when the motor is moving, the problem is with the console.

The position sensor wires are **red = ground, white = position signal, black = 5vdc**. The motor mains leads are **white = COM, red = UP, black = DOWN**.

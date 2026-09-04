---
id: f65-2016-incline-motor-test-procedure
title: Incline motor test procedure
kind: procedure
question: How do I test the incline motor and position sensor on a Sole f65-2016 treadmill?
asked_as:
- how do i test the incline motor on a treadmill
- incline will not move what do i check
- treadmill potentiometer test
keywords:
- incline motor
- potentiometer
- position sensor
- relay
- calibration
- 4.5 vdc
- incline board
- counter
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2016
  applies_to:
  - f65-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2016-e3-incline-error
- f65-2016-incline-position-sensor-wiring
- f65-2016-incline-motor-spec
source:
  ref: sole-tm-f65-2016-service-manual
  locator: Test Procedure, incline motor control function
  extracted_at: '2026-09-04'
---

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - **Relay clicks but the motor does not move**: with the incline light and relay activated, measure between the neutral (white) wire and the Up (red) or Down (black) wire, whichever direction the Up/Down lights say the motor should travel. It should be about the same as the mains voltage, ~110VAC (230VAC). If the voltage is present but the motor does not move, the motor is bad.
   - **Light on but the relay does not click**: replace the incline board (most likely a bad relay).
5. If the motor moves, is there a sensor reading on the console?
   - The INCLINE window shows the computer incline setting after the speed calibration ends: **15 for max incline, 0 for lowest**. That window is a counter showing the actual position sensor output. Motor moving with no count means a problem in the position sensor wiring or circuitry.
   - Count present but calibration fails: the potentiometer may be loose and giving false readings; it should not be able to rotate. Remove the cover from the rear of the motor and check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. If everything is tight, the potentiometer could be bad.
   - No count: check the voltage at the potentiometer. There should be **5vdc between the black and red wire**, and a voltage between the red and white wire of about **4.5~4.7 Vdc when the motor is at the lowest position**. If the white wire voltage changes as the motor moves but the counter does not register, there may be a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the **3-pin connector on the incline board**. No voltage there means the wire from the motor to the connector is faulty.
7. If there is voltage, check the output connector to the console at the bottom of the incline board. No voltage there means a problem on the incline board - there are no electronic components on the board for this signal, only circuit connections, so the only possible faults are a bad solder joint or a broken circuit.
   - Console connector wiring, the same on the incline board and at the console: **Pin 1 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 3 = ground**.
8. If the output connector has voltage but the console does not, check the whole cable from the incline board to the console for cuts or bad connections at the in-line connectors.
9. Voltage at the console connector but no count in the Incline window while the motor moves means the problem is in the console.

---
id: f63-2016-incline-position-sensor-test
title: Voltage test for the incline position sensor
kind: procedure
question: How do I test the incline position sensor on a Sole F63-2016?
asked_as:
- how do i test the incline potentiometer
- incline motor moves but no count on console
- incline calibration keeps failing
keywords:
- incline
- position sensor
- potentiometer
- vr
- relay
- incline board
- voltage test
- counter
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2016
  applies_to:
  - f63-2016
  section: errors
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2016-e3-error-code
- f63-2016-incline-motor-spec
source:
  ref: sole-tm-f63-2016-service-manual
  locator: pages 49 to 59, Test Procedure under 8.3
  extracted_at: '2026-09-04'
---

This is the nine step test the manual gives for an incline fault.

1. Run the calibration again.
2. Does the incline motor move at all?
3. If it does not, do the Up and Down lights on the incline board light?
4. If they light, do the relays click on?
   - **Relay clicks but the motor does not move**: with the incline light and the relay activated, measure between the neutral (white) wire and the Up (red) or Down (black) wire, whichever direction the board's lights say the motor should travel. It should read about the mains voltage, ~110VAC (230VAC). If the voltage is there and the motor still does not move, the motor is bad.
   - **Light on but the relay does not click**: replace the incline board. A bad relay is the likely cause.
5. If the motor moves, is there a sensor reading on the console? After the speed calibration ends the INCLINE window shows the computer incline setting, **15 for maximum incline and 0 for the lowest**. That window is a counter showing the actual position sensor output.
   - **Motor moves, no count**: a problem in the position sensor wiring or circuitry.
   - **Count but calibration fails**: the potentiometer may be loose and giving false readings. It should not be able to rotate. Take the cover off the rear of the motor, grab the potentiometer and check the two Phillips screws holding it to the motor casting. If it still feels loose, the nut holding it to its black mounting bracket may be loose. If everything is tight, the potentiometer may be bad.
   - **No count at all**: measure at the potentiometer. There should be **5vdc between the black and red wire**, and a voltage between the red and white wire. That reading is about **4.5 to 4.7 Vdc when the motor is at its lowest position**. The exact number is not critical. If the white wire voltage changes as the motor moves but the counter never registers, there may be a bad wire connection between the potentiometer and the console.
6. Measure the potentiometer voltage at the 3-pin connector on the incline board. No voltage means the wire from the motor to the connector is faulty.
7. If it is there, measure at the output connector to the console at the bottom of the incline board. No voltage there means a problem on the incline board itself. There are no electronic components on the board for this signal, only circuit connections from the potentiometer connector to the console connector, so only a bad solder joint or a broken circuit is possible.
8. If the voltage is present at that output connector, measure at the console. Voltage at the board but not at the console means the cable between them has a cut or a bad connection.
9. Voltage at the console connector but no count in the Incline window while the motor moves means the console is the problem.

**Console connector wiring**, the same on the incline board and at the console:

| Pin | Signal |
|---|---|
| 1 | 5vdc |
| 2 | position signal 0~5vdc |
| 3 | ground |

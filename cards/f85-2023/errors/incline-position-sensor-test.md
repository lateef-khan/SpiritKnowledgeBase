---
id: f85-2023-incline-position-sensor-test
title: Testing the incline motor, relays and position sensor
kind: procedure
question: How do I test the incline motor and its position sensor on a Sole f85-2023
  treadmill?
asked_as:
- how do i test the incline motor
- incline potentiometer test on a treadmill
- no count in the incline window
keywords:
- incline test
- potentiometer
- position sensor
- relay
- up down lights
- 5vdc
- incline counter
- e3
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2023
  applies_to:
  - f85-2023
  section: errors
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2023-e3-incline-vr-voltage
- f85-2023-incline-sensor-connector-pinout
- f85-2023-incline-motor-spec
- f85-2023-calibration-procedure
source:
  ref: sole-tm-f85-2023-service-manual
  locator: Section 8.4 Test procedure, pages 42-43
  extracted_at: '2026-09-04'
---

This is the manual's own test for an E3 incline fault. Work through it in order.

1. Run calibration again.
2. Does the incline motor move at all?
3. If not, do the Up/Down lights on the controller light?
4. If they light, do the relays click on?
   - **Relay clicks but the motor does not move**: with the incline light and relay activated, check the voltage
     between the neutral (white) wire and the Up (red) or Down (black) wire, whichever direction the Up/Down
     lights call for. It should be about the same as the mains voltage, ~110VAC (230VAC). If the voltage is there
     and the motor does not move, the motor is bad.
   - **Light on but the relay does not click**: the controller needs to be replaced, most likely a bad relay.
5. If the motor moves, is there a sensor reading on the console?
   - The INCLINE window shows the computer incline setting after the speed calibration ends: **15 for max incline,
     0 for lowest incline**. That window is a counter showing the actual position sensor output. If the motor
     moves and the count does not change, the problem is in the position sensor wiring or circuitry.
   - **Count changes but calibration fails**: the potentiometer may be loose and giving false readings. It should
     not be able to rotate. Remove the cover from the rear of the motor and try to move the potentiometer by hand.
     Check the two Phillips screws holding it to the motor casting. If it still feels loose, the nut holding the
     potentiometer to its black mounting bracket could be loose. If everything is tight, the potentiometer could
     be bad.
   - **No count**: check the voltage at the potentiometer. There should be **5vdc between the black and red wire**,
     and a voltage between the red and white wire. That voltage is about **4.5~4.7 Vdc when the motor is at the
     lowest position** (the exact number is not critical). If the white wire has voltage that changes as the motor
     moves but the counter still does not register, there may be a bad wire connection between the potentiometer
     and the console.
6. Check the voltage from the potentiometer at the **3-pin connector on the controller**. If there is no voltage,
   the wire from the motor to the connector is faulty.
7. If there is voltage, check the output connector to the console at the bottom of the controller. If no voltage
   is present, the problem is on the controller. There are no electronic components on the board for this signal,
   only circuit connections from the potentiometer connector to the console connector, so the only possible
   problems are a bad solder joint or a broken circuit on the board.
8. If voltage is present at the output connector to the console, check the voltage at the console. Voltage at the
   controller but none at the console means the whole cable from controller to console needs checking for cuts and
   bad connections at the input wire connectors.
9. If there is voltage at the console connector but no count in the INCLINE window while the motor moves, the
   problem is the console.

The three console connector pins are on the pinout card. They are the same at the controller and at the console.

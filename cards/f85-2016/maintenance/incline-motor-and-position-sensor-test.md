---
id: f85-2016-incline-motor-and-position-sensor-test
title: Bench testing the incline motor and its potentiometer
kind: procedure
question: How do I test the incline motor and position sensor on a Sole F85-2016 treadmill?
asked_as:
- how do i test the incline motor
- incline will not move on my treadmill
- how do i check the incline potentiometer
keywords:
- incline test
- potentiometer
- relay
- incline board
- position sensor
- mains voltage
- counter
- calibration fails
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2016
  applies_to:
  - f85-2016
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2016-e3-incline-vr-error
- f85-2016-incline-position-sensor-pinout
- f85-2016-incline-motor
source:
  ref: sole-tm-f85-2016-service-manual
  locator: section 8.3 Test Procedure, printed page 50
  extracted_at: '2026-09-04'
---

This is the manual's nine step test for an incline complaint or a failing calibration. The steps only make sense in order.

1. **Run calibration again.**
2. Does the incline motor move at all?
3. If it does not, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - **Relay clicks but the motor does not move**: with the incline light and relay activated, measure between the neutral (white) wire and the Up (red) or Down (black) wire, whichever direction the board is calling for. It should read about mains voltage, **~110VAC (230VAC)**. Voltage present and no movement means the motor is bad.
   - **Light on but the relay does not click**: replace the incline board. A bad relay is the most likely cause.
5. If the motor moves, is there a sensor reading on the console? The INCLINE window shows the computer incline setting after the speed calibration ends: **15 for maximum incline, 0 for lowest**. That window is a counter showing the actual position sensor output.
   - **Motor moving, no count**: the fault is in the position sensor wiring or circuitry.
   - **Count present but calibration fails**: the potentiometer may be loose and giving false readings. It should not be able to rotate. Remove the cover from the rear of the motor, grab the potentiometer and check it. Check the two Phillips screws holding it to the motor casting, and the nut holding it to its black mounting bracket. If everything is tight, the potentiometer could be bad.
   - **No count**: check the voltage at the potentiometer. There should be **5 vdc between black and red**, and a voltage between red and white of about **4.5 to 4.7 Vdc at the lowest motor position**. If the white wire voltage changes as the motor moves but the counter never registers, suspect a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the **3 pin connector on the incline board**. No voltage means the wire from the motor to that connector is faulty.
7. If there is voltage, check at the **output connector to the console** at the bottom of the incline board. No voltage there means a problem on the incline board itself. The board carries no electronic components for this signal, only circuit connections, so the only possible faults are a bad solder joint or a broken track. Console connector wiring, the same on the incline board and at the console: **pin 1 ground, pin 2 position signal 0~5vdc, pin 3 5vdc**.
8. If there is voltage at the output connector, check at the console. Voltage at the board but not at the console means the cable between them is cut or badly connected at the in-wire connectors.
9. Voltage at the console connector but no count in the incline window while the motor moves means the problem is the console.

---
id: spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
title: 'Stride motor and position sensor test, nine steps: relays, about 115 VAC at
  the motor, 5 VDC and 4.5 to 4.7 VDC at the potentiometer, and 20 for the longest
  stride'
kind: procedure
question: How do I test the stride motor and its position sensor on a Spirit CE850-2016,
  CE850-2020 or XE895-2016 elliptical?
asked_as:
- how to test the stride motor on a spirit elliptical
- stride potentiometer voltage check
- stride wont move relay click
- ce850 stride sensor test
keywords:
- stride motor
- position sensor
- potentiometer
- relay
- 115 vac
- stride board
- calibration
- test procedure
- e3
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  - xe895-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
see_also:
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- ce850-2024-errors-stride-window-dashes-stride-motor-failure
- e95s-2016-stride-motor-test-procedure
- ct850-2016-incline-err-test-procedure
- spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual Test Procedure, nine steps, PDF
    p. 49, text.md lines 834-870; CE850 (2020) service manual Test Procedure, nine
    steps, PDF p. 42, text.md lines 718-754; XE895 2016 (XE895-SE022) service manual
    Test Procedure, nine steps, PDF p. 50, text.md lines 835-871
  extracted_at: '2026-09-11'
---

**This is the stride machines' test.** The stride motor is a 115 volt AC motor with four wires - red (UP), black (DOWN), white (COM, neutral) and green (ground) - and a 3-pin position-sensor cable. The stride board is the driver board with the two relays and the UP and DOWN LEDs on it (`spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds`).

1. Run calibration again.
2. Does the stride motor move at all?
3. If no, do the Up/down lights on the stride board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor doesn't move: with the stride light and relay activated check the voltage between the neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel according to the Up/Down lights on the board. **It should be about the same as the mains voltage, ~115VAC.** If the voltage is present but the motor doesn't move, then the motor is bad.
   - If the light is on, but the relay does not click on, then the stride board needs to be replaced (bad relay most likely).
5. If the motor moves, is there a sensor reading on console?
   - The STRIDE window will display the computer stride setting (after speed cal. ends); **20 for max stride, 0 for lowest stride**. The STRIDE window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count occurring in the STRIDE window then there is a problem in the position sensor wiring or circuitry.
   - If there is a count, but the calibration fails, then the position sensor (potentiometer) could be loose, creating false readings (it should not be able to rotate). Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting. If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
   - If there is no count then check the voltage at the potentiometer. **There should be 5vdc between the black and red wire** and there should be a voltage between the red and white wire. **This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position** (the number isn't too critical, as long as it's somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the 3-pin connector on the stride board. If there is no voltage then the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the stride board. If no voltage present then there is a problem on the stride board. There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector. The only problems that are possible are a bad solder joint or broken circuit on the board. Console connector wiring, the same on the stride board and at the console: **Pin 3 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 1 = ground.**
8. If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there, but is there at the stride board, then check the entire cable from stride board to console for cuts or bad connection at the inline connectors.
9. If there is voltage at the console connector, but no count in the STRIDE window when the motor is moving, then there is a problem with the console.

**Three books print these nine steps in the same words** - the CE850 2016 and XE895 2016 under `E3` (`spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read`) and the CE850 (2020) under `---` (`ce850-2024-errors-stride-window-dashes-stride-motor-failure`). The 20-for-max figure agrees with those books' console pages, which set the stride from 18 to 24 inches in half-inch steps. The position-sensor wire colours printed beside the test are *Red = Ground, White = Position signal, Black = 5vdc* on the 2016 books; the 2020 book drops the colours and prints only *1. Ground, 2. Position signal, 3. 5Vdc*.

**The XE395 2016 and XE395ENT 2021 print the same nine steps about their incline motor** with their own figures - about 120 VAC and 15 for max incline on the XE395 2016 (`xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`), about 115 VAC and 20 on the ENT (`xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`). Spirit treadmills print it for their incline motor (`ct850-2016-incline-err-test-procedure`), and Sole's E95S 2016 for its stride with the same figures (`e95s-2016-stride-motor-test-procedure`). Different machines; separate cards.

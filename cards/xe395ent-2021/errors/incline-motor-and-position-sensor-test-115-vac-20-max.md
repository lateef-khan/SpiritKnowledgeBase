---
id: xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
title: 'Incline motor and position sensor test, nine steps: relays, about 115 VAC
  at the motor, 5 VDC and 4.5 to 4.7 VDC at the potentiometer, and 20 for the highest
  incline'
kind: procedure
question: How do I test the incline motor and its position sensor on a Spirit xe395ent-2021
  elliptical?
asked_as:
- how to test the incline motor on the xe395ent
- incline potentiometer voltage check ent elliptical
- incline wont move relay click e3
- xe395ent incline sensor test
keywords:
- incline motor
- position sensor
- potentiometer
- relay
- 115 vac
- incline board
- calibration
- test procedure
- e3
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
see_also:
- xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
- ct850-2016-incline-err-test-procedure
- e25-2023-e3-ramp-error
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: XE395ENT 2021 (XE539S-SE025-01) service manual Test Procedure, nine steps,
    PDF p. 35, text.md lines 461-497
  extracted_at: '2026-09-11'
---

**This is the XE395ENT 2021's test.** The incline motor is a 115 volt AC motor with four wires - red (UP), black (DOWN), white (COM, neutral) and green (ground) - and a 3-pin position-sensor cable. The incline board is the driver board with the two relays and the UP and DOWN LEDs.

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/down lights on the incline board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor doesn't move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel according to the Up/Down lights on the board. **It should be about the same as the mains voltage, ~115VAC.** If the voltage is present but the motor doesn't move, then the motor is bad.
   - If the light is on, but the relay does not click on, then the incline board needs to be replaced (bad relay most likely).
5. If the motor moves, is there a sensor reading on console?
   - The INCLINE window will display the computer incline setting (after speed cal. ends); **20 for max incline, 0 for lowest incline**. The INCLINE window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count occurring in the INCLINE window then there is a problem in the position sensor wiring or circuitry.
   - If there is a count, but the calibration fails, then the position sensor (potentiometer) could be loose, creating false readings (it should not be able to rotate). Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting. If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
   - If there is no count then check the voltage at the potentiometer. **There should be 5vdc between the black and red wire** and there should be a voltage between the red and white wire. **This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position** (the number isn't too critical, as long as it's somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the incline board. There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector. The only problems that are possible are a bad solder joint or broken circuit on the board. Console connector wiring, the same on the incline board and at the console: **Pin 3 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 1 = ground.**
8. If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there, but is there at the incline board, then check the entire cable from incline board to console for cuts or bad connection at the inline connectors.
9. If there is voltage at the console connector, but no count in the INCLINE window when the motor is moving, then there is a problem with the console.

This is the test the `E3` chapter ends on (`xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read`). **The XE395 2016 prints the same nine steps with ~120VAC and 15 for max incline** (`xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`); the stride machines print ~115VAC and 20 for the longest stride (`spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`). Spirit treadmills print it for their incline (`ct850-2016-incline-err-test-procedure`), and Sole's E25 2023 for its ramp (`e25-2023-e3-ramp-error`).

---
id: xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
title: 'Incline motor and position sensor test, nine steps: relays, about 120 VAC
  at the motor, 5 VDC and 4.5 to 4.7 VDC at the potentiometer, and 15 for the highest
  incline'
kind: procedure
question: How do I test the incline motor and its position sensor on a Spirit xe395-2016
  elliptical?
asked_as:
- how to test the incline motor on the xe395
- incline potentiometer voltage check elliptical
- incline wont move relay click
- xe395 incline sensor test
keywords:
- incline motor
- position sensor
- potentiometer
- relay
- 120 vac
- incline board
- calibration
- test procedure
- err
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395-2016
  applies_to:
  - xe395-2016
  section: errors
  code: '*'
  model_number:
  - '395015'
authority: 3
not_to_be_confused_with:
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
see_also:
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v
- e25-2016-incline-motor-test-procedure
- ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: XE395 2016 (XE539S-SE019-01) service manual Test Procedure, nine steps,
    PDF p. 50, text.md lines 828-864
  extracted_at: '2026-09-11'
---

**This is the XE395 2016's test, and two of its figures are its own.** The incline motor is a 120 volt AC motor with four wires - red (UP), black (DOWN), white (COM, neutral) and green (ground) - and a 3-pin position-sensor cable. The incline board is the driver board with the two relays and the POWER, UP and DOWN LEDs (`xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v`).

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/down lights on the incline board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor doesn't move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel according to the Up/Down lights on the board. **It should be about the same as the mains voltage, ~120VAC.** If the voltage is present but the motor doesn't move, then the motor is bad.
   - If the light is on, but the relay does not click on, then the incline board needs to be replaced (bad relay most likely).
5. If the motor moves, is there a sensor reading on console?
   - The INCLINE window will display the computer incline setting (after speed cal. ends); **15 for max incline, 0 for lowest incline**. The INCLINE window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count occurring in the INCLINE window then there is a problem in the position sensor wiring or circuitry.
   - If there is a count, but the calibration fails, then the position sensor (potentiometer) could be loose, creating false readings (it should not be able to rotate). Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting. If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
   - If there is no count then check the voltage at the potentiometer. **There should be 5vdc between the black and red wire** and there should be a voltage between the red and white wire. **This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position** (the number isn't too critical, as long as it's somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
6. Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the incline board. There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector. The only problems that are possible are a bad solder joint or broken circuit on the board. Console connector wiring, the same on the incline board and at the console: **Pin 3 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 1 = ground.**
8. If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there, but is there at the incline board, then check the entire cable from incline board to console for cuts or bad connection at the inline connectors.
9. If there is voltage at the console connector, but no count in the INCLINE window when the motor is moving, then there is a problem with the console.

**Two figures differ from every other Spirit printing of this page.** The mains voltage to expect at the motor is **~120VAC** (the stride books and the XE395ENT say ~115VAC), and the top of the counter is **15 for max incline** - while the same book's console pages put the incline range at 0 to 20 in half steps. The book does not reconcile the two; treat 15 as the counter figure this test expects and 20 as the console's display range.

This is the test the `Err` chapter ends on (`xe395-2016-errors-err-incline-vr-out-of-range-or-not-read`). The XE395ENT 2021 prints the same nine steps with ~115VAC and 20 (`xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`); the stride machines with ~115VAC and 20 for the longest stride (`spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`). Spirit treadmills print it for their incline (`ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12`), and Sole's E25, E35, E55, E95 and E98 2016 for theirs (`e25-2016-incline-motor-test-procedure`).

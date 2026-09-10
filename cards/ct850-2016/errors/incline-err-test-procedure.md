---
id: ct850-2016-incline-err-test-procedure
title: Measuring the incline circuit when the incline will not run
kind: procedure
question: How do I test the incline motor and position sensor on a Spirit CT850-2016
  treadmill?
asked_as:
- how to test the incline motor on a spirit treadmill
- incline potentiometer voltage test
- incline calibration keeps failing
keywords:
- incline motor
- potentiometer
- position sensor
- relay
- incline board
- vr
- 5vdc
- voltage test
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: incline-err
  model_number: '850845'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-incline-err-vr-out-of-range
- ct850-2016-incline-err-during-incline-action
- ct850-2016-incline-calibration-fails-checks
- ct850-2016-incline-motor-replacement
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Test Procedure, page 43 (printed 42)
  extracted_at: '2026-09-08'
---

Nine steps, in the manual's order. A multi-meter is the only tool named.

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - If the relay clicks on but the motor doesn't move: with the incline light and relay activated,
     check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire,
     depending on which direction the motor is supposed to travel according to the Up/Down lights on
     the board. **The manual says it should be about the same as the mains voltage, ~230VAC.** If the
     voltage is present but the motor doesn't move, the motor is bad.
   - If the light is on but the relay does not click on, the incline board needs to be replaced (bad
     relay most likely).
5. If the motor moves, is there a sensor reading on the console? The INCLINE window shows the
   computer incline setting after speed calibration ends: **15 for maximum incline, 0 for lowest**.
   That window is a counter showing the actual position sensor output. If the motor is moving and no
   count occurs, the problem is in the position sensor wiring or circuitry.
   - If there is a count but calibration fails, the position sensor (potentiometer) could be loose
     and creating false readings; it should not be able to rotate. Remove the cover from the rear of
     the motor and check whether it is loose, and check the two Phillips screws holding it to the
     motor casting. If it still feels loose, the nut holding the potentiometer to its black mounting
     bracket could be loose. If everything is tight, the potentiometer could be bad.
   - If there is no count, check the voltage at the potentiometer. There should be **5 Vdc between
     the black and red wire**, and a voltage between the red and white wire. That voltage is about
     **4.5 to 4.7 Vdc when the motor is at its lowest position** - the number is not critical as long
     as it is in that neighbourhood. If the white wire has voltage that changes as the motor moves
     but the counter still does not register, there may be a bad wire connection between the
     potentiometer and the console.
6. Check the voltage from the potentiometer at the 3-pin connector on the incline board. No voltage
   means the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the incline
   board. No voltage there means a problem on the incline board. There are no electronic components
   on the board for this signal, only circuit connections from the potentiometer connector to the
   console connector, so the only possible faults are a bad solder joint or a broken circuit.
8. If there is voltage at the output connector to the console, check the voltage at the console. If
   there is none at the console but there is at the incline board, check the whole cable from
   incline board to console for cuts or bad connections at the inline connectors.
9. If there is voltage at the console connector but no count in the INCLINE window while the motor
   moves, the problem is with the console.

Console connector wiring - the same at the incline board and at the console:

| Pin | Signal |
|---|---|
| 1 | 5 Vdc |
| 2 | position signal 0~5 Vdc |
| 3 | ground |

**Read the 230 VAC figure with care.** The cover of this manual reads `ST8100-CT001 Treadmill
Service Manual (110V)`, and every other electrical instruction in it calls for a 120-volt supply.
Measure against the supply the machine is actually on.

Step 4 ends `then the motor is bad`; the replacement procedure is on
`ct850-2016-incline-motor-replacement`.

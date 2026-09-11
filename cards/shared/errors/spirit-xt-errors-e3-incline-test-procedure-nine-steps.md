---
id: spirit-xt-errors-e3-incline-test-procedure-nine-steps
title: 'Measuring the incline circuit in nine steps: relay click, mains at the motor,
  5 Vdc at the potentiometer, then the console connector'
kind: procedure
question: How do I test the incline motor and position sensor after an E3 on a Spirit
  XT 2015, XT 2023 or XT ENT treadmill?
asked_as:
- how to test the incline motor on my spirit treadmill
- incline potentiometer voltage test
- incline calibration keeps failing with e3
keywords:
- e3
- incline motor
- potentiometer
- position sensor
- relay
- up down lights
- 5vdc
- 4.5 to 4.7 vdc
- pin 1 pin 2 pin 3
- mains voltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-test-procedure
see_also:
- spirit-xt-2023-errors-e3-incline-vr-out-of-range
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- xt485ent-2023-errors-e3-incline-vr-out-of-range
- spirit-xt-errors-e3-action-flow-chart
- ct850-2016-incline-err-test-procedure
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT185 2023 service manual Test procedure, PDF p. 26-27, text.md lines 519-572;
    XT285 2023 service manual Test procedure, PDF p. 27-28, text.md lines 521-574;
    XT385 2023 service manual Test procedure, PDF p. 28-29, text.md lines 471-521;
    XT485 2023 service manual Test procedure, PDF p. 28-29, text.md lines 471-521;
    XT685 2023 service manual Test procedure, PDF p. 27-28, text.md lines 524-576;
    XT185 2015 service manual Test Procedure, PDF p. 49 (printed 59), text.md lines
    826-876; XT285 2015 service manual Test Procedure, PDF p. 50 (printed 59), text.md
    lines 895-945; XT385 2015 service manual Test Procedure, PDF p. 50, text.md lines
    738-776; XT485 2015 service manual Test Procedure, PDF p. 50, text.md lines 742-780;
    XT485ENT 2023 service manual Test Configuration and Test Procedure, PDF p. 44-46,
    text.md lines 621-697; XT685ENT 2023 service manual TEST PROCEDURE, PDF p. 32-33,
    text.md lines 509-557
  extracted_at: '2026-09-11'
---

Nine steps, printed word for word in all eleven XT service manuals (2015 XT185 to XT485, 2023 XT185 to XT685, XT485ENT and XT685ENT). The 2023 books say *controller*; the 2015 books and the XT485ENT say *incline board* for the same board.

1. Run calibration again.
2. Does the incline motor move at all?
3. If not, do the Up/down lights on the controller light?
4. If they light, do the relays click on?
   - If the relay clicks but the motor does not move: with the incline light and relay activated, check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire, whichever way the motor should be travelling. **It should be about the mains voltage, ~110 VAC (230 VAC).** Voltage present and no movement means the motor is bad.
   - If the light is on but the relay does not click, the controller needs replacing (bad relay, most likely).
5. If the motor moves, is there a sensor reading on the console? After the speed calibration ends the INCLINE window shows the computer incline setting, **15 for maximum and 0 for lowest**, and that window is a counter showing the actual position sensor output. Motor moving with no count means the position sensor wiring or circuitry.
   - A count that still fails calibration: the potentiometer may be loose and giving false readings - it should not be able to rotate. Remove the cover from the rear of the motor and try it; check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. All tight means the potentiometer could be bad.
   - No count: check the voltage at the potentiometer. **5 Vdc between the black and red wires**, and a voltage between the red and white wires of **about 4.5 to 4.7 Vdc with the motor at its lowest position** - the number is not critical, so long as it is in that neighbourhood. Voltage on the white wire that changes as the motor moves, with no count, means a bad wire between the potentiometer and the console.
6. Check the potentiometer voltage at the 3-pin connector on the controller. None means the wire from the motor to the connector is faulty.
7. If there is voltage, check the output connector to the console at the bottom of the controller. None means a fault on the controller - there are no electronic components on the board for this signal, only circuit connections, so a bad solder joint or a broken track.
8. Voltage at the output connector but none at the console: check the whole cable from controller to console for cuts or bad connections at the inline connectors.
9. Voltage at the console connector and no count while the motor moves: the console.

**The console connector pin order is printed two ways.** The 2015 XT385 and XT485, all five 2023 books and both ENT books print *Pin 1 = ground, Pin 2 = position signal 0~5 Vdc, Pin 3 = 5 Vdc*. **The 2015 XT185 and XT285 print the reverse: Pin 1 = 5 Vdc, Pin 2 = position signal, Pin 3 = ground.** Nothing reconciles them; identify the 5 V and ground pins with the meter before trusting either list.

**The sensor wire colours are printed two ways as well.** The 2023 XT185, XT285, XT385, XT485 and XT685 drawings label the position sensor wires *P1 GND (Red), P2 Position signal (White), P3 +5 Vcc (Black)*. The 2015 XT385 and XT485, the XT485ENT and the XT685ENT label them *Black = Ground, White = Position signal, Red = 5 Vdc*. Step 5 of the text above, common to all, measures 5 Vdc "between the black and red wire" and the signal "between the red and white wire", which fits the black-ground reading. Measure rather than trust a colour.

The CT850 2016 prints the same nine steps against ~230 VAC and its own pin order (`ct850-2016-incline-err-test-procedure`).

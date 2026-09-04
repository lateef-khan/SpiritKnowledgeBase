---
id: s77-2019-incline-position-sensor-test
title: Measuring the incline position sensor
kind: procedure
question: How do I test the incline position sensor on a Sole S77-2019 treadmill?
asked_as:
- how do i test the incline potentiometer on my treadmill
- s77 incline motor moves but the display does not count
- measuring the incline vr on my treadmill
keywords:
- position sensor
- potentiometer
- vr
- relay
- incline board
- 5vdc
- counter
- calibration
- loose
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- s77-2019-e3-incline-vr
- s77-2019-incline-sensor-pinout
- s77-2019-incline-motor-spec
source:
  ref: sole-tm-s77-2019-service-manual
  locator: E3 test procedure, pages 48-49
  extracted_at: '2026-09-04'
---

Work down this list; each step assumes the one before it passed.

1. Run the calibration again.
2. **Does the incline motor move at all?**
3. If it does not, do the **Up/Down lights on the incline board** light?
4. If they light, **do the relays click**?
   - **Relay clicks but the motor does not move**: with the incline light and relay active, measure between the neutral (white) wire and the Up (red) or Down (black) wire, whichever direction the board is calling for. It should be about the mains voltage, ~110 VAC (230 VAC). **Voltage present and the motor still still: the motor is bad.**
   - **Light on but no relay click**: replace the incline board. Most likely a bad relay.
5. **If the motor moves, is there a sensor reading on the console?** The INCLINE window counts the actual position sensor output, 15 at maximum incline and 0 at the lowest.
   - **Motor moving, no count**: a problem in the position sensor wiring or circuitry.
   - **Count present but calibration fails**: the potentiometer may be loose and giving false readings; it should not be able to rotate. Remove the cover at the rear of the motor and try to move it. Check the two Phillips screws holding it to the motor casting, and the nut holding it to its black mounting bracket. If everything is tight, the potentiometer may be bad.
   - **No count**: measure at the potentiometer. There should be **5 V DC between the black and red wires**, and a voltage between the **red and white** wires of about **4.5 to 4.7 V DC with the motor at its lowest position** - the exact figure is not critical. If the white wire voltage changes as the motor moves but the counter does not register, there may be a bad wire connection between the potentiometer and the console.
6. Measure at the **3-pin connector on the incline board**. No voltage means the wire from the motor to the connector is faulty.
7. Measure at the **output connector to the console** at the bottom of the incline board. No voltage there means the fault is on the incline board itself. There are no electronic components on that path, only circuit connections, so the only possible faults are a bad solder joint or a broken track.
8. If there is voltage at the board output but none at the console, check the whole cable from incline board to console for cuts and bad connections at the in-wire connectors.
9. If there is voltage at the console connector but no count in the INCLINE window while the motor moves, the problem is the console.

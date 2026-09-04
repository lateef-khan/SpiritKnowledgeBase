---
id: tt8-2016-ac-incline-vr-test-procedure
title: Testing the incline position sensor step by step
kind: procedure
question: How do I test the incline position sensor and its wiring on a Sole tt8-2016-ac
  treadmill?
asked_as:
- how do i test the incline potentiometer
- incline motor moves but console shows nothing
- check the incline position sensor voltage
keywords:
- incline vr
- potentiometer
- position sensor
- 5vdc
- relay clicks
- incline counter
- 3-pin connector
- calibration fails
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016-ac
  applies_to:
  - tt8-2016-ac
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- tt8-2016-incline-vr-test-procedure
see_also:
- tt8-2016-ac-e-52h-error-code
- tt8-2016-ac-e-53h-error-code
- tt8-2016-ac-incline-position-sensor-wiring
source:
  ref: sole-tm-tt8-2016-ac-service-manual
  locator: VR Test Procedure, page 35
  extracted_at: '2026-09-04'
---

**AC model: TT8 2016 ST925A-YT030, AC drive motor driven by an inverter. The DC drive motor TT8 2016 (ST925-YT021) is a different machine and this card does not apply to it.**

The manual heads this "VR Test Procedure" and places it before the code table. Run it when the incline
misbehaves or calibration fails — it is the detail behind E-52H, E-53H and E3.

1. Run calibration again.
2. Does the incline/decline motor move at all?
3. If not, do the Up/Down lights on the incline board light?
4. If they light, do the relays click on?
   - **Relay clicks but the motor does not move**: with the incline light and relay activated, measure
     between the neutral (**white**) wire and the Up (**red**) or Down (**black**) wire, whichever
     direction the Up/Down lights call for. It should be about mains voltage, **~110 VAC (230 VAC)**. If
     the voltage is there and the motor still does not move, the motor is bad.
   - **Light on but the relay does not click**: replace the incline board — most likely a bad relay.
5. If the motor moves, is there a sensor reading on the console? The INCLINE window shows the computer
   incline setting after speed calibration ends — **15 for max incline, 0 for lowest**. That window is a
   counter showing the actual position sensor output.
   - Motor moving, no count: the fault is in the position sensor wiring or circuitry.
   - Count present but calibration fails: the potentiometer may be loose and giving false readings — it
     should not be able to rotate. Remove the cover from the rear of the motor and check the two Phillips
     screws holding it to the motor casting, then the nut holding it to its black mounting bracket. If
     everything is tight, the potentiometer could be bad.
   - No count at all: measure at the potentiometer. There should be **5 Vdc between the black and red
     wire**, and a voltage between the red and white wire that reads about **4.5 to 4.7 Vdc at the lowest
     position** (the exact figure is not critical). If the white wire has voltage that changes as the motor
     moves but the counter does not register, suspect a bad wire connection between the potentiometer and
     the console.
6. Check the voltage from the potentiometer at the **3-pin connector** on the incline board. No voltage
   means the wire from the motor to the connector is faulty.
7. If there is voltage, check the output connector to the console at the bottom of the incline board. No
   voltage there means the fault is on the incline board itself. There are no electronic components on the
   board for this signal — only circuit connections — so the only possibilities are a bad solder joint or a
   broken circuit.
   Console connector wiring, the same at the incline board and at the console:
   - Pin 1 = ground
   - Pin 2 = position signal 0~5 Vdc
   - Pin 3 = 5 Vdc
8. If there is voltage at the output connector, check at the console. Voltage at the incline board but none
   at the console means the cable between them has a cut or a bad connection.
9. Voltage at the console connector but no count in the Incline window while the motor moves means the
   problem is the console.

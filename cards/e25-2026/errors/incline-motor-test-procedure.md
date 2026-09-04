---
id: e25-2026-incline-motor-test-procedure
title: Incline motor and position sensor test procedure
kind: procedure
question: How do I test the incline motor and its position sensor on a Sole e25-2026
  elliptical?
asked_as:
- how do i test the incline motor on a sole elliptical
- incline moves but the display does not count
- e25 2026 potentiometer test
keywords:
- incline motor
- relay
- position sensor
- potentiometer
- ad value
- distance window
- incline board
- 115vac
- counter
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2026
  applies_to:
  - e25-2026
  section: errors
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- e25-2026-e3-ramp-error
- e25-2026-incline-position-sensor-pinout
- e25-2026-incline-calibration
source:
  ref: sole-elliptical-e25-2026-service-manual
  locator: Section 8.3, Test Procedure steps 1-8, page 32
  extracted_at: '2026-09-04'
---

1. Run calibration again.
2. Does the incline motor move at all?
3. If no, do the relays click on?
   - If the relay clicks on but the motor does not move: check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire. It should be about the same as the mains voltage, **~115VAC**. If the voltage is present but the motor does not move, the motor is bad.
   - If you press the Incline +/- key but the relay does not click on, the **incline board needs to be replaced** (bad relay most likely).
4. If the motor moves, is there a sensor reading on the console?
   - **The Distance window displays the computer incline setting.** The **AD value corresponding to the maximum incline is approximately 40**, and the **AD value corresponding to the minimum incline is approximately 924**. The Distance window is a counter showing the actual position sensor output. If the motor is moving and there is no count in the Distance window, there is a problem in the position sensor wiring or circuitry.
   - If there is a count but calibration fails, the potentiometer could be loose, creating false readings; it should not be able to rotate. Remove the cover from the rear of the motor and check the two Phillips screws holding it to the motor casting, then the nut holding it to its black mounting bracket. If everything is tight the potentiometer could be bad.
   - If there is no count, check the voltage at the potentiometer. There should be **5vdc between the black and red wire**, and a voltage between the red and white wire of about **4.5~4.7 Vdc at the lowest position** (the number is not critical). If the white-wire voltage changes as the motor moves but the counter does not register, there may be a bad wire connection between the potentiometer and the console.
5. Check the voltage from the potentiometer at the **3-pin connector on the incline board**. If there is no voltage the wire from the motor to the connector is faulty.
6. If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage is present there is a problem on the incline board. There are no electronic components on the board for this signal, only circuit connections, so the only possible faults are a bad solder joint or a broken circuit. Console connector wiring, the same on the incline board and at the console: **Pin 1 = 5vdc, Pin 2 = position signal 0~5vdc, Pin 3 = ground.**
7. If there is voltage at the output connector to the console, check the voltage at the console. If there is none there but there is at the incline board, check the entire cable for cuts or bad connections at the inline connectors.
8. If there is voltage at the console connector but no count in the Incline window when the motor is moving, the problem is with the console.

**Which window holds the count is printed both ways.** Step 4 says the count appears in the **Distance** window; step 8 says the **Incline** window. Watch both while the motor runs.

**The numbers changed from the 2019 manual**, which read the count in the Incline window as 20 for maximum incline and 0 for lowest. This manual reads an AD value of about 40 at maximum and about 924 at minimum, so a high number here means a low incline.

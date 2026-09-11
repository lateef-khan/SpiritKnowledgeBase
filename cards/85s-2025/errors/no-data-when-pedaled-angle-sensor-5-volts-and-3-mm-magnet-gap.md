---
id: 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
title: 'A program that starts but registers nothing when pedaled is the angle sensor
  on the brake: 5 volts on pins 2 and 9, and a 3 mm gap to the magnet on the brake
  shaft'
kind: troubleshooting
question: Why does a Spirit 85s-2025 recumbent stepper start a program but register
  no data when it is pedaled?
asked_as:
- 8.5s stepper shows zero rpm when i pedal
- nothing counts on my spirit rehab stepper
- 8.5s angle sensor gap
- stepper crank sensors test no reading
keywords:
- no data
- no rpm
- angle sensor
- reed
- magnet
- 3mm gap
- pin 2 and pin 9
- 5v dc
- brake shaft
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: errors
  code: no-code
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
see_also:
- spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 5. Troubleshooting (Electronic), 5-3 No revolutions, "Program Starts But
    No Data Registers When Stepper is Pedaled", items 7-10 of the page's continued
    numbering, PDF p. 21; text.md lines 301-305
  extracted_at: '2026-09-11'
---

**The 7.5S reads its speed from an optical RPM sensor watching the flywheel bolts; the 8.5S reads it from an angle sensor and a magnet on the brake shaft.** The 7.5S procedure - a 1 to 2 mm gap to a bolt head, the PULSE window - is a different machine (`spirit-med-stepper-errors-no-data-when-pedaled-sensor-test`). This is the 8.5S's own.

The book prints these as items 7 to 10, continuing the numbering of the step-graph procedure above them on the same page:

7. *Program Starts But No Data Registers When Stepper is Pedaled* (the heading).
8. Make sure all the cables in the back of console are plugged in properly.
9. Run the Sensor Test in Maintenance mode. Go to step iii if **ANGLE** didn't display correct RPM, go to step iv if **REED** didn't work properly.
10. Open the cover and measure the **pin 2 and pin 9** at the cable that connect to the angle sensor for **5V DC**. Check the magnet on the shaft of brake. The magnet should be in the center of the shaft and have **3mm gap** between magnet and angle sensor. Replace the angle sensor if correct but there is no RPM.

**Two readouts, one page.** The Maintenance Mode item on this console is *Crank Sensors*, listed with two entries - *Crank Index Magnet Sensor* and *Crank RPM Angle Sensor* - which are the REED and ANGLE the procedure refers to. Step 9 sends you to "step iii" and "step iv", which do not exist on the page; read them as step 10's two halves - the 5 V measurement and the magnet gap for the angle sensor, the magnet itself for the reed.

**The pass conditions:** 5 V DC between pins 2 and 9 of the angle sensor cable, the magnet centred on the brake shaft, 3 mm from the sensor. A sensor that has its 5 V, its magnet and still no RPM is replaced. The book prints no remedy for a REED that fails beyond the magnet check.

The wiring diagram of the same book labels the part *#085, Brake and Angle Sensor*; it is on the brake, not on the pedal cranks, and the *Crank Calibration* item in Maintenance Mode (right crank at 6 o'clock, then press the button) is the console-side procedure that follows a sensor replacement.

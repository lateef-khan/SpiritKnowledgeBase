---
id: spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm
title: 'A wrong left or right step graph is worked through the step sensor board:
  5 volts on its cable, the Sensor Test counters at about 17, and a 7 to 9 mm gap'
kind: troubleshooting
question: What do I check when the left/right step graph reads wrong on a Spirit 7.5S
  or 8.5S recumbent stepper?
asked_as:
- stepper step graph is wrong on one side
- left right bars dont match on my spirit stepper
- how to adjust the step sensor on a recumbent stepper
- reflector sensor gap on the 7.5s
keywords:
- step graph
- step sensor board
- reflector sensor
- sensor test
- 5v dc
- 7-9mm
- pin 1 and pin 3
- symmetry
- recumbent stepper
- encoder wheel
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-5s-med
  - 85s-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
- spirit-med-stepper-errors-optical-sensor-board-gap-7-to-9-mm-abnormal-spm-or-no-response
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
source:
  ref: spirit-stepper-7-5s-med-service-manual
  locator: 7.5S (RS9600-SS021) service manual 5.2.3 Troubleshooting and Problem Solving,
    "Left/Right Step Graph Incorrect", PDF p. 17; text.md lines 166-184. 8.5S (MS2000-SB036-01)
    service manual 5-3 No revolutions, "Left/Right Step Graph Incorrect", PDF p. 20;
    text.md lines 281-300 - the same six steps word for word
  extracted_at: '2026-09-11'
---

**The owner's manuals answer a wrong symmetry or watt reading with one line - run the Sensor Test** (`spirit-med-stepper-errors-symmetry-or-watt-reading-wrong`). The service manuals print the procedure behind it, and both print it in the same words:

1. Make sure all the cables in the back of console are plugged in properly.
2. Open the left shroud and make sure the cable is connected to the step sensor board properly.
3. Measure between **pin 1 and pin 3** of the cable that connects to the step sensor board for **5V DC**. If there is no 5V DC, check the connection of the cable or replace the cable. Go to next step if there is 5V DC.
4. Run the **Sensor Test** in Maintenance mode.
5. The **SPM window should show ON** when the reflector sensor #1 (bottom one) aligns to the silver surface. The **CALORIES window should show ON** when the reflector sensor #2 (top one) aligns to the silver surface. The step position counter of each foot (TIME and STEPS window) should show **about 17 (15~17)** when you perform a full range step. If the value is incorrect, follow next step to adjust the sensor board.
6. Adjust the sensor to align with the center of the shaft as left picture. Make sure the surface of the sensor is parallel to the surface of the pulley and has a **7~9mm gap** between sensor and the reflective surface of the pulley. If the problem isn't resolved replace the sensor board.

**What the step sensor is.** The 7.5S book's Sensor Test description explains it: one step sensor on the front left pulley, two optical reflector sensors reading a silver-and-black encoder wheel, so that the console can tell a left step from a right one and count each foot's travel from about 0 to about 17. A wrong graph on one side is that count going wrong on one side.

**Three figures, and the order matters:** 5 V on the cable proves the board is fed; the counters at 15 to 17 prove it is reading; the 7 to 9 mm gap, with the sensor face parallel to the pulley, is the adjustment. Only a board that is fed, aligned and still wrong is replaced.

**On the 8.5S these words do not match its console.** The 8.5S book prints the six steps unchanged, but its own Maintenance Mode (a touchscreen menu entered by tapping the Wi-Fi icon and the clock) has no *Sensor Test* item and no SPM, CALORIES, TIME or STEPS windows - it has *Crank Sensors*, which displays rotational speed. The 5 V measurement and the 7 to 9 mm gap still stand for the 8.5S (its own 7-4 page repeats the gap, `spirit-med-stepper-errors-optical-sensor-board-gap-7-to-9-mm-abnormal-spm-or-no-response`); the window names are a leftover from the 7.5S book and should be read as *the sensor readout in Maintenance Mode*.

A stepper that registers nothing at all is the RPM sensor rather than the step sensor - `spirit-med-stepper-errors-no-data-when-pedaled-sensor-test` on the 7.5S, `85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap` on the 8.5S.

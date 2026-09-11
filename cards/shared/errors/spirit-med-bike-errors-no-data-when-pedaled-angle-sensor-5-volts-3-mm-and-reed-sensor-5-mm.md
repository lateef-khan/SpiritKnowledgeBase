---
id: spirit-med-bike-errors-no-data-when-pedaled-angle-sensor-5-volts-3-mm-and-reed-sensor-5-mm
title: 'The program starts but nothing registers when you pedal: the Sensor Test,
  then 5 volts and a 3 mm gap at the angle sensor or a 5 mm gap at the reed sensor'
kind: troubleshooting
question: Why does a Spirit Medical 7.0R or 7.0U bike start a program but register
  no RPM or data when it is pedalled?
asked_as:
- 7.0r no rpm when pedaling
- rehab bike program running but no data
- angle sensor gap on the 7.0u
- reed switch test spirit medical bike
keywords:
- no data
- no rpm
- sensor test
- angle sensor
- reed sensor
- reed switch
- 5v dc
- 3mm gap
- 5mm gap
- rehabilitation bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
- spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072
see_also:
- spirit-med-bike-errors-symmetry-incorrect-unit-type-sensor-test-crank-calibration
- spirit-med-bike-errors-programs-do-not-start-key-test-then-keypad
source:
  ref: spirit-bike-70r-2025-service-manual
  locator: '7.0R (MR490-SB018-03) service manual 5.2.4 Troubleshooting, 3. Program
    Starts But No Data Registers When Bike is Pedaled, steps i-v, PDF p. 12-13; text.md
    lines 141-177; 6.13.5 reed sensor gap 2 mm, PDF p. 35, lines 422-431. 7.0U (MU470-SB018)
    service manual 5.2.4, 3., PDF p. 12-13, text.md lines 192-223; 6.12.3 reed sensor
    gap 2 mm, PDF p. 33, lines 487-501. Owner''s manual row: ERROR MESSAGE & TROUBLESHOOTING,
    PDF p. 48 (printed 46); text.md lines 1328-1377; 7.0U 2025 owner''s manual ERROR
    MESSAGE & TROUBLESHOOTING, PDF p. 46 (printed 44); text.md lines 1285-1329; Dyaco
    MED 7.0R 2021 owner''s manual (Rev. 1.2.1) Error messages and Troubleshooting,
    PDF p. 84-85; text.md lines 2642-2730'
  extracted_at: '2026-09-11'
---

The owner's manuals, word for word:

> **Program starts but no data registers when the bike is pedaled**
> - Check that the connectors are properly seated in the back of the consoles.
> - Perform the Sensor tests in Maintenance mode. If one of the sensors does not work it needs replacement. If both sensors do not work, it could be a bad console or both sensors are bad.

**The count of failed sensors is the owner's diagnosis** - one dead sensor is that sensor, two dead at once is more likely the console. The service manuals print what to measure behind each:

1. Make sure all the cables in the back of console were plugged in properly.
2. Run the **Sensor Test** in Maintenance mode. Go to step 3 if **ANGLE** didn't display correct RPM, go to step 4 if **REED** didn't work properly.
3. Open the cover and measure **pin 2 and pin 9 at the cable that connect to the angle sensor for 5V DC**. Check the magnet on the shaft of brake. **The magnet should be in the center of the shaft and have 3mm gap between magnet and angle sensor.** Replace the angle sensor if correct but there is no RPM.
4. Open the cover and check the reed sensor. **Make sure the magnet on the pulley aligns to only one of the arrow of the reed sensor and have about 5mm gap.** Use meter to check the sensor if everything set up properly, the sensor should be **short when magnet pass the sensor**. Replace the sensor if it isn't short when magnet passes the sensor.
5. Check the cables if there is no problem in step 3 and 4. Replace the console if everything is good.

**Two sensors, two jobs.** The angle sensor on the brake gives speed and RPM (the Sensor Test shows it as `ANGLE`); the reed switch on the pulley counts crank revolutions for crank position (`REED`, which flips 0 to 1 once per revolution with a beep). The REED side is the one the symmetry index depends on - see `spirit-med-bike-errors-symmetry-incorrect-unit-type-sensor-test-crank-calibration`.

**The reed gap is printed twice, and differently.** The troubleshooting page says *about 5mm* at the reed sensor; the reed-sensor replacement procedure in the same books (6.13 on the 7.0R, 6.12 on the 7.0U) says *the distance between reed sensor and magnet should be 2mm*. The book does not reconcile them - set the gap to the replacement figure when you have just fitted the part, and accept the wider tolerance when you are only checking.

The 8.5S stepper prints a similar angle-sensor test with the same 5 V and 3 mm figures (`85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap`); the 8.0U/8.5R of this range use a Hall sensor and a 2-3 mm gap instead (`spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072`).


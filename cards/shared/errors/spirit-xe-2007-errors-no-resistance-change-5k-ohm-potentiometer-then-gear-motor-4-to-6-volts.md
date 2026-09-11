---
id: spirit-xe-2007-errors-no-resistance-change-5k-ohm-potentiometer-then-gear-motor-4-to-6-volts
title: 'No resistance change: listen for the gear motor, read about 5K ohms across
  the red and yellow wires and a near short across black and brown, then 4 to 6 volts
  at the motor on UP'
kind: troubleshooting
question: Why does the resistance not change on a Spirit XE100-2007, XE200-2007, XE300-2007,
  XE400-2007 or XE500-2007 elliptical, and how does the dealer manual test the gear
  motor?
asked_as:
- resistance wont change on my spirit xe300
- elliptical gear motor ohm test
- xe500 no resistance change
- how to test the gear motor on a 2007 spirit elliptical
keywords:
- no resistance
- gear motor
- potentiometer
- 5k ohms
- red wire
- yellow wire
- orange wire
- black wire
- brown wire
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe100-2007
  - xe200-2007
  - xe300-2007
  - xe400-2007
  - xe500-2007
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller
see_also:
- spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3
source:
  ref: spirit-elliptical-xe100-xe200-xe300-xe400-xe500-2007-service-manual
  locator: XE100-XE500 2007 dealer service manual Troubleshooting Guide, ELECTRONIC
    SYSTEM, PDF p. 3, text.md lines 51-98; XE100-XE500 2007 dealer service manual
    Repair Procedures, PROCEDURE 3 and PROCEDURE 4, PDF p. 6, text.md lines 170-202
  extracted_at: '2026-09-11'
---

**The 2008 dealer manual prints no error code**; its second electronic row is this one, and it ends in Procedure 3 or Procedure 5.

`No resistance change`
1. When the UP or DOWN buttons are pressed, listen for the sound of the gear motor running.
2. If you cannot hear the motor running, remove the console and set the volt meter to the ohms setting.
   - Measure between the **red and the yellow** wires; it should be around **5K ohms +/- (500 ohms)**.
   - Measure between the **red and orange** wires and then between the **yellow and orange** wires. These two measurements should add up to the measurement between the red and yellow.
   - If these measurements are correct, then the potentiometer on the gear motor is good.
   - Measure between the **black and brown** wires. The meter should read close to a short, about **1-5 ohms**.
   - If all of these readings are correct, the motor and harness are good and **the console needs to be replaced**. If any of the readings are not correct, the problem is either the harness or the gear motor; take the same measurements from the wires directly on the gear motor. (Procedure 3)
3. If you do hear the motor running, make sure the motor cable is properly connected to both the gear motor and the brake, and the cable is properly adjusted. (Procedure 5)

**Procedure 3 - test gear motor.** Take off the right shroud to access the gear motor. Set the meter to DC voltage. Check for voltage between the **yellow and the red** wires - *should be around 4.5v for 350/550*. Check between yellow and orange, then red and orange; added together they should total the yellow-to-red reading. Press START and then UP, and check between the **black and the brown** wires: **you should get 4-6 volts** (you will need a helper for this step).

So the split is: five ohm readings good = console; any ohm reading wrong at the console but right at the motor = harness; wrong at the motor = gear motor; motor audibly running = the cable to the brake, which is Procedure 5's adjustment, a care procedure the maintenance cards carry.

**Two references in Procedure 3 name machines this book does not cover**: *If unit is an XE550, go to motor test in engineering mode (Procedure 8)* - Procedure 8 in this book is the XE400/XE500 incline calibration - and *4.5v for 350/550*. The XE350 and XE550 are the 2005 models; the sentences were carried over. The engineering-mode Motor Test on the 2007 consoles is under Functions in Procedure 7.

The XBR25/XBR55 2007 bike book of the same year answers the same symptom with a DC test at the controller and no ohm figures (`spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller`). The 2016 books test a tension motor on a drive board at 5.5 to 6.0 VDC (`spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc`).

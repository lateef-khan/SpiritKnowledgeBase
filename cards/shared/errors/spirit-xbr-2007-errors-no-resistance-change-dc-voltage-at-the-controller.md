---
id: spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller
title: 'No resistance change: DC voltage on harness wires 2 and 5 must rise with the
  level, then the brake coil connector reads zero at level 1 and something above it'
kind: troubleshooting
question: Why does the resistance not change on a Spirit XBR25-2007 or XBR55-2007
  recumbent bike, and how does the dealer manual test the controller and brake coil?
asked_as:
- resistance wont change on my old spirit recumbent
- xbr55 level up does nothing
- how do i test the controller on a spirit xbr25
- brake coil test on a spirit recumbent bike
keywords:
- no resistance
- controller
- brake coil
- dc voltage
- harness
- wires 2 and 5
- level 1
- volt meter
- recumbent
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2007
  - xbr55-2007
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-errors-dashes-tension-motor-failure
- xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
see_also:
- spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console
- xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
- spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires
source:
  ref: spirit-bike-xbr25-xbr55-2007-service-manual
  locator: XBR25/XBR55 2007 dealer service manual Bike Troubleshooting guide and Procedures
    1-3, PDF p. 3, text.md lines 38-63
  extracted_at: '2026-09-11'
---

**The 2008 dealer manual for the XBR25 and XBR55 prints no error code**; its second troubleshooting row is this one, and it ends in procedure 3.

`No resistance change`

1. Remove side covers to access the controller.
2. Check for DC voltage where main harness plugs into controller. (procedure 3)

**Procedure 3 - test for DC voltage from console.**

1. Remove the cover beneath the seat to access the controller.
2. Turn the meter to DC voltage.
3. Leave the harness connected to the controller and put the leads on the **2nd and 5th wires**. (You will probably need to remove some of the glue from the back of the harness.)
4. Press start and set the resistance to level 1. **As you increase the resistance you should see the voltage reading increase as well.**
5. If the reading is not going up as you go up in resistance, **the problem is either the console or the harness.** If the readings are what they should be, go to the next step.
6. With the meter still on DC, put the leads into the back of the **2-pin connector** for the wires that go to the **brake coil**.
7. **At level 1 the voltage reading should be zero. At level 2 and above, if you get any reading the controller is working.**
8. If you don't have any voltage, **the controller needs to be replaced.** If there is voltage but still no resistance, **the brake coil needs to be replaced.**

So the split is: no rising voltage on wires 2 and 5 = console or harness; rising voltage there but nothing at the brake coil connector = controller; voltage at the coil but no resistance = the induction brake itself. **No pass/fail figure is printed for the controller output** - the book asks only that it rise with the level and that it be zero at level 1.

The 2016 residential books that replaced these machines test a tension motor instead, on a drive board, and expect 5.5 to 6.0 VDC (`spirit-xb-2016-errors-tension-motor-voltage-test-blue-and-green-wires`); the XBR95 2016 keeps an induction brake and watches a CN2 output (`xbr95-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable`). None of them prints this two-stage test. The third row of the same guide, a loose seat carriage, is a mechanical adjustment (procedure 4) and is not an errors fact.

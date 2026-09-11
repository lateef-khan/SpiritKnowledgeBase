---
id: 7-5s-med-errors-hand-pulse-problem-rear-sensor-points-shorted
title: A hand pulse problem is checked at the console connectors, then at the sensor
  whose two rear points should read shorted, then at the cables
kind: troubleshooting
question: What do I check when the hand pulse grips do not read on a Spirit 7-5s-med
  recumbent stepper?
asked_as:
- 7.5s hand pulse not reading
- grip heart rate dead on my spirit rehab stepper
- how to test the hand pulse sensor on the 7.5s
keywords:
- hand pulse
- grip pulse
- sensor points
- shorted
- bent pins
- console connector
- broken cable
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: 7-5s-med
  applies_to:
  - 7-5s-med
  section: errors
  code: no-pulse
authority: 3
not_to_be_confused_with:
- spirit-hand-pulse-not-working
see_also:
- spirit-med-stepper-errors-programs-do-not-start-keypad-test
- spirit-hand-pulse-not-working
source:
  ref: spirit-stepper-7-5s-med-service-manual
  locator: 5.2.3 Troubleshooting and Problem Solving, "Hand Pulse Problem", PDF p.
    20; text.md lines 202-212
  extracted_at: '2026-09-11'
---

**The owner's manuals of the 7.0S, 7.5S and MS300 print no hand pulse row at all.** This is the service manual's, and it is the only hand pulse procedure printed for the medical steppers.

1. Check the cables in the back of console to ensure there is a good connection and the pins in the connector are not bent. Go to next step if the problem isn't resolved.
2. Measure the hand pulse sensor as pictured below. **The two rear sensors points should be shorted** when the console is on the bike and shouldn't be shorted to the other sensors. Set the hand pulse sensor to the right setting if the setup was wrong. Go to next step if the setup is right.
3. Open the cover and check the cables connection and possible broken cables. Replace the console if everything is good.

**The test in step 2 is continuity, not voltage.** Each grip sensor has contact points on its back; the two rear points of a sensor should buzz through to each other and must not buzz through to the *other* sensor's points. A sensor wired so that the two grips are joined, or one that is open across its own rear points, is "the wrong setting" - and the remedy is to set it right, not to replace it.

**"When the console is on the bike" is printed that way.** The procedure was written for a bike console and carried onto the stepper without the noun being changed; it is one of several places this book still reads as a bike book.

**No voltage and no part number is printed**, and the fault ends at a new console. The four-cause hand pulse row the bikes and treadmills print (`spirit-hand-pulse-not-working`) was not written for this machine.

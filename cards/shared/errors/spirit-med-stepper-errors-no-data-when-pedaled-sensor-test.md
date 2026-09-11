---
id: spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
title: The program starts but nothing registers when you pedal, and the Sensor Test
  separates one bad sensor from a bad console
kind: troubleshooting
question: Why does a Spirit recumbent stepper start a program but register no data
  when it is pedaled?
asked_as:
- my stepper isnt counting anything
- program runs but no numbers on my spirit stepper
- stepper shows zero rpm when i pedal
- no data registering on the stepper console
keywords:
- no data
- does not register
- sensor test
- reflector sensor
- maintenance mode
- connectors
- console replacement
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
- csc900-2024-errors-speed-abnormal-then-data-resets
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
see_also:
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
- spirit-med-stepper-errors-no-power-outlet-and-dc-wire
- spirit-med-stepper-errors-one-pedal-has-no-resistance-drive-cable
- spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: Troubleshooting, "Program starts but no data registers", printed page 40
    (PDF page 42) of the 7.0S 2025 manual; the same text on printed page 42 (PDF page
    44) of the 7.5S 2025 manual and printed page 60 (PDF page 60) of the MS300 2021
    manual. Read from the native text layer and confirmed against a 300 dpi render
    of the 7.0S page; 7.5S (RS9600-SS021) service manual 5.2.3, "Program Starts But
    No Watts Value When Stepper is Pedaled", PDF p. 15-16, text.md lines 152-165;
    7.0S (RS9500-SS021-02) service manual 5.2.3 "Program Starts But No Watts Value
    When Stepper is Pedaled", PDF p. 15-16, text.md lines 165-184; 7.5S (RS9600-SS021-03)
    service manual 5.2.3 "Program Starts But No Watts Value When Stepper is Pedaled",
    PDF p. 15-16, text.md lines 148-167 - the 7.5S RS9600-SS021-01 page unchanged
    in both (compared with difflib on 2026-09-11)
  extracted_at: '2026-09-10'
---

The manual, word for word:

> - Check that the connectors are properly seated in the back of the consoles.
> - Perform the Sensor tests in Maintenance mode. If one of the sensors does not work it needs
>   replacement. If both sensors do not work, then it could be a bad console or both sensors are bad.

**The count of failed sensors is the diagnosis.**

| What the Sensor Test shows | What the manual concludes |
|---|---|
| One sensor dead | That sensor needs replacement |
| Both sensors dead | A bad console, **or** both sensors bad |

**Two dead sensors at once is more likely to be one console than two failures**, which is why the
manual offers the console first in that row - but it does not commit, and it gives no way to settle
it from the console. Reseat the connectors before you read anything into the result.

**The sensors this refers to are the two reflector sensors** read out in the Maintenance mode Sensor
Test: SPM window shows reflector sensor #1 as 1 or 0, CALORIES window shows reflector sensor #2, TIME
and STEPS show the left and right step position counters, and PULSE shows the speed sensor signal.
The menu itself is carded under `section: console`.

**A wrong reading is a different row from no reading.** If numbers appear but the Symmetry Index or
the watts look wrong, go to `spirit-med-stepper-errors-symmetry-or-watt-reading-wrong`.

The stair climbers read their speed from a light sensor and a grating instead, and their answer is
not this one (`csc900-2024-errors-speed-abnormal-then-data-resets`).

## The 7.5S service manual prints the procedure behind the owner's-manual row, for the RPM sensor

Its heading is *Program Starts But No Watts Value When Stepper is Pedaled*, and it is the speed sensor - not the step sensor - that it works through:

> i. Make sure all the cables in the back of console were plugged in properly.
> ii. Open the left shroud and make sure the cable is connected to the RPM sensor board properly.
> iii. Run the Sensor Test in Maintenance mode.
> iv. The **PULSE window should show ON** when the bolt is aligned to the sensor and RPM should show when the stepper is pedaled. Go to the next step if PULSE window didn't switch to ON when the bolt is aligned to the sensor.
> v. Adjust the position of the sensor to align the sensor to the bolt. Make sure the surface of the sensor is parallel to the bolt and has a **1~2mm gap** between sensor and bolt. If the problem persists, go to next step.
> vi. Measure between **pin 1 and pin 3** of the cable that connects to the RPM sensor board for **5V DC**. If there is no 5V DC, check the connection of the cable or replace the cable. Replace the sensor board if there is 5V DC.

**The RPM sensor watches the four bolt heads on the flywheel**, one pass per bolt, and the PULSE window of the Sensor Test flips ON as each bolt passes. Gap first (1 to 2 mm, sensor face parallel to the bolt), then 5 V on pins 1 and 3, then the board.

**The step sensor is the other half of "both sensors"** in the owner's-manual row, and its procedure - a 7 to 9 mm gap and the counters at about 17 - is the step-graph card (`spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm`). **The 8.5S has no RPM sensor of this kind**; its speed comes from an angle sensor and a magnet on the brake shaft with a 3 mm gap (`85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap`).

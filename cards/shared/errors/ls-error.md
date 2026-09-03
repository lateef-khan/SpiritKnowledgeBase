---
id: sole-ls-error
title: LS error on older treadmills
kind: troubleshooting
question: What does an LS error mean on a Sole treadmill?
asked_as:
- ls error on my treadmill
- old treadmill shows ls
keywords:
- ls error
- low speed
- calibration
- speed sensor
- pin test
- pwm light
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - '*'
  section: errors
  code: ls
authority: 2
not_to_be_confused_with: []
see_also:
- sole-pin-test-pre-2016
- sole-battery-test-drive-motor
source:
  ref: sole-tm-ls-error
  locator: whole document
  extracted_at: '2026-09-03'
---

**Meaning**: the machine is not reaching the speed it expects. This error only happens on 2016 and older treadmills.

A calibration often fixes it outright. It can also be caused by friction between the belt and the deck, a worn motor controller, or a motor that no longer turns.

If the error started right after assembly, just replace the computer cables.

1. Run a calibration.
   - Pass: quick start the machine. If it runs, it is fixed. If not, go to step 2.
   - Fail: go to step 2.
2. Ask: does the running belt move at all before the LS error appears?
   - **Moves for less than 10 seconds**: remove the motor hood cover and check the speed sensor alignment. If it is out, align it and calibrate again. If it is aligned, go to step 3.
   - **Moves for longer than 10 seconds**: go to step 3.
   - **Does not move**: remove the motor hood cover, press Start and watch for the PWM light on the controller.
     - Light comes on: go to step 3.
     - No light: ask whether the machine was recently assembled, taken apart or moved. If yes, replace the computer cables. If no, run a pin test. Pass, replace the upper computer cable and the display board. Fail, replace the middle and lower computer cables and the motor controller.
3. Work through the wear checks below, and run a battery test on the drive motor. If the motor fails the battery test, replace the drive motor and the motor controller.

Before you fit a new motor controller, look for the wear that kills controllers:

1. Ask how often the customer lubricates. Whether the answer is good or bad, check the running belt and running deck for wear. Slide a hand between the belt and the deck, palm up, and feel whether the texture in the middle is gone. Turn the palm down and feel the deck for damage.
   - Belt and deck good: go to step 2.
   - Belt or deck worn or damaged: replace the running belt, the running deck and the controller. Replace the deck only if it is worn or damaged.
2. Ask whether the machine is plugged straight into its own circuit on a non-GFCI outlet.
   - Yes: go to step 3.
   - No: have the customer move it to its own non-GFCI circuit and try again. If it runs, it is fixed. If it does not run, replace the motor controller.
3. Ask whether there are squeaking or knocking noises.
   - Yes: ask whether the noise is at the front or the rear, and replace the front roller or the rear roller (possibly both) together with the motor controller.
   - No: replace the motor controller.

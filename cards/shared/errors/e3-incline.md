---
id: sole-e3-error
title: 'E3 error: incline fault'
kind: troubleshooting
question: What does an E3 error mean on a Sole treadmill?
asked_as:
- e3 error on my treadmill
- incline error on treadmill
keywords:
- e3
- e3 error
- incline error
- incline motor
- calibration
- pin test
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - f63
  - f63-2013
  - f65
  - f65-2026
  - f80
  - f80-2026
  - f83
  - f83-2026
  - f85
  - f85-2020
  - f85-2026
  - f89
  - tt8
  - tt8-2020
  section: errors
  code: e3
authority: 2
not_to_be_confused_with:
- sole-e2-error
see_also:
- sole-pin-test-pre-2016
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-e3-error-treadmill
  locator: whole document
  extracted_at: '2026-09-03'
---

**This is E3, the incline fault. On a machine built before 2016 the same incline fault shows as E2, and an overcurrent fault on a newer machine also shows as E2. Check the build year before you act.**

**Meaning**: a problem with the incline motor or the motor controller.

This error can be a false positive on a brand new machine, or after a part has been replaced. A motor controller or a display board always needs a calibration after it is fitted, so always run a calibration first.

If the machine was recently assembled **and** it fails calibration, replace the computer cables.

1. Run a calibration.
   - Pass: quick start the machine and press the incline buttons. If it inclines and declines, it is fixed.
   - Still faulty, or calibration failed: go to step 2.
2. Ask whether the incline motor moved at all.
   - **Yes** - the signal back up to the console is interrupted.
     - 2016 or newer: replace the motor controller or the display board.
     - Older than 2016: run a pin test. Pass, replace the upper computer cable and the display board. Fail, replace the middle and lower computer cables and the motor controller.
   - **No** - the signal down to the motor controller is interrupted.
     - 2016 or newer: replace the motor controller or the incline motor.
     - Older than 2016: run a pin test. Most of the time this test is unnecessary and the motor controller is the answer. Pass, replace the upper computer cable and the display board. Fail, replace the middle and lower computer cables and the motor controller.

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

**Scope.** This card is the fallback for the Sole treadmills that have no service manual in this knowledge base. Every machine listed in `applies_to` is one of those. A machine with a service manual has its own card for this code, or its manual shows the code does not exist on it — check the model's own cards first. AC inverter machines (ST90, TT9, the AC TT8 variants), the F63 2026 and the C80 use different code families and are deliberately excluded.

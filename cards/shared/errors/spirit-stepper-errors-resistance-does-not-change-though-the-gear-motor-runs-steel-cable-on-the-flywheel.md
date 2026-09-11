---
id: spirit-stepper-errors-resistance-does-not-change-though-the-gear-motor-runs-steel-cable-on-the-flywheel
title: 'The console adjusts the level and the gear motor runs, but the resistance
  does not change: the steel cable has come off the flywheel'
kind: troubleshooting
question: Why does the resistance not change on a Spirit CS800 or XS895 stepper when
  the console and gear motor are working?
asked_as:
- stepper level changes but it doesnt get harder
- cs800 resistance stuck motor is moving
- xs895 no resistance but gear motor works
- steel cable off the flywheel stepper
keywords:
- resistance does not change
- gear motor
- steel cable
- flywheel
- unresponsive resistance
- cable loose
- stepper
- incline stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - cs800-2016
  - cs800-2021
  - xs895-2018
  - xs895-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-stepper-errors-noise-from-the-flywheel-friction-foreign-objects-then-replace
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- spirit-xs895-errors-incline-motor-no-function-and-no-resistance-gear-motor
- sc200-2016-no-resistance-or-flywheel-noise
- sc200-2019-no-resistance-or-flywheel-noise
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: CS800 (2020) service manual 9-2 Troubleshooting for the Flywheel, first
    situation, PDF p. 38 (printed 37), text.md lines 584-589; CS800 2016 (XS200-SS003)
    service manual 10-2 Flywheel Problem item 1, PDF p. 65, text.md lines 926-931;
    XS895 (XS300B-YS006) service manual 9-5 Troubleshooting For Flywheel and Drive
    belt, first box, PDF p. 45 (printed 44), text.md lines 689-694
  extracted_at: '2026-09-11'
---

Three books, one sentence.

- **CS800 (2020):** *The console can adjust the resistance level and gear motor operates normally, but the resistance doesn't change.* **Solve:** Check the steel cable is mounted on the flywheel.
- **CS800 2016:** *If resistance adjustment on the console is nonresponsive and Gear Motor is functioning normally, check the cable to see if the flywheel is in place properly or if the cable is loose.*
- **XS895:** *If Gear motor is operating normally, check Steel cable is mounted on Flywheel in the right way.*

**The resistance on these steppers is a magnet bracket pulled by a steel cable, and the gear motor pulls the cable.** So a motor that runs when the level changes, with no change in effort at the pedals, means the motion is not reaching the flywheel - the cable has slipped off its anchor on the flywheel side, or it is slack. There is nothing electrical to test: the console and the motor have already proved themselves.

**What it is not.** A motor that does *not* run is the tension motor page and its voltage test (`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`); the XS895 adds a page for a gear motor that has failed outright (`spirit-xs895-errors-incline-motor-no-function-and-no-resistance-gear-motor`). Noise from the flywheel is the other half of the same section in all three books (`spirit-stepper-errors-noise-from-the-flywheel-friction-foreign-objects-then-replace`).

The steel cable's route and its refitting are the flywheel replacement steps in each book - set the console to the highest level and power off before unhooking it. Sole prints this row for its SC200 steppers (`sc200-2016-no-resistance-or-flywheel-noise`, `sc200-2019-no-resistance-or-flywheel-noise`).

---
id: spirit-xs895-errors-incline-motor-no-function-and-no-resistance-gear-motor
title: An incline motor that does not work is its wires and electronics, and no resistance
  when pedaling is the console first, then the gear motor replaced
kind: troubleshooting
question: What do I check when the incline motor does nothing, or there is no resistance
  when pedaling, on a Spirit XS895 stepper?
asked_as:
- xs895 incline wont move
- no resistance at all on my spirit incline stepper
- xs895 gear motor dead
- incline motor replacement length xs895
keywords:
- incline motor
- no function
- no resistance
- gear motor
- controller board
- steel cable
- 245mm
- incline stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr
- spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor
- spirit-stepper-errors-resistance-does-not-change-though-the-gear-motor-runs-steel-cable-on-the-flywheel
- spirit-xs895-errors-incline-buttons-do-not-work-cable-connectors-and-the-switch
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 9-4 Troubleshooting For Incline motor and Controller board and Gear motor,
    PDF p. 44 (printed 43); text.md lines 667-689
  extracted_at: '2026-09-11'
---

One page, two motors.

**Incline motor is no function.** Check all the incline motor wires are plug well and all the electronic parts are good. *Incline motor needs to be adjusted to the right length when doing the replacement. Setting the motor to zero then rotate the outer tube to let the distance between two bolt holes is 245mm.*

**If there is no resistance when pedaling**, please check console is ok, first. Then check Gear motor is functional. If Gear motor is defective then unmount steel cable and replace Gear motor.

**The 245 mm figure is the one thing on this page a technician cannot guess.** A replacement incline motor is a telescoping actuator; run it to zero, then turn the outer tube until the two mounting holes are 245 mm apart, and only then fit it. A motor fitted at another length either will not reach the frame holes or will not calibrate to the console's range (`spirit-xs895-errors-incline-position-does-not-match-the-console-calibrate`). The replacement steps themselves are under `section: assembly`.

**Console before gear motor for a dead resistance.** "Check console is ok" is the `E2` page - a key that beeps has sent its signal, and the drive board's 5 V output proves the console side (`spirit-xs895-errors-e2-gear-motor-abnormal-or-no-signal-check-the-control-cable-then-the-tension-motor`). A gear motor that is fed and does not run is replaced, steel cable unhooked first. A gear motor that runs with no change in resistance is a different fault - the cable off the flywheel (`spirit-stepper-errors-resistance-does-not-change-though-the-gear-motor-runs-steel-cable-on-the-flywheel`).

An incline motor whose position reading is lost puts `STEP ERROR` on the display (`spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr`); one that never gets the command is the handlebar switch (`spirit-xs895-errors-incline-buttons-do-not-work-cable-connectors-and-the-switch`).

---
id: spirit-xs895-assembly-incline-motor-gear-motor-and-controller-board-replacement
title: 'Replacing the incline stepper incline motor, gear motor and controller board:
  resistance to MAX before the power goes off, two 17 mm wrenches on the incline motor,
  and a new incline motor set to 245 mm between its bolt holes'
kind: procedure
question: How do I replace the incline motor, the gear motor (tension motor) or the
  controller board on a Spirit XS895 incline stepper?
asked_as:
- incline motor replacement xs895
- gear motor replacement xs895 resistance to max first
- controller board cover xs895
- incline motor length 245mm xs895
keywords:
- incline motor
- gear motor
- tension motor
- controller board
- steel cable
- 245 mm
- ground wire
- box wrench
- incline stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: assembly
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xs895-assembly-side-case-replacement
- spirit-xs895-assembly-rear-rail-assembly-replacement
- spirit-xs895-assembly-idler-wheel-flywheel-and-drive-belt-replacement
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 10-8 Incline motor, Gear motor, and Controller board replacement, PDF pp.
    56-57; text.md lines 918-967; 9-4 Troubleshooting For Incline motor (the 245 mm),
    PDF p. 44; text.md lines 667-689
  extracted_at: '2026-09-11'
---

**Set the resistance to MAX before you cut the power** (step 4), and **set a new incline motor to 245 mm between
its two bolt holes** before it goes in.

1. Follow the side case replacement to take off the side case.
2. Use a screwdriver to remove the **controller board cover locking screw**, then take off the cover.
3. **Remember all wire locations before unplugging them.** Use a screwdriver to remove the controller board.
4. Before replacing the gear motor, use the console to **adjust the resistance level to MAX**, then cut off the
   power. Unmount the **steel cable** from the gear motor.
5. Use a screwdriver to remove the gear motor and unplug its wire. Then take off the gear motor.
6. Use **two 17 mm box wrenches** to remove the **incline motor locking bolts**. Cut off the wire ties and remove
   the incline motor **ground wire** with a screwdriver. Disconnect the incline motor wires from the controller
   board, then take off the incline motor.
7. Reverse the steps to install all parts.

**The incline motor length.** The troubleshooting chapter (9-4) adds what this procedure does not: *the incline
motor needs to be adjusted to the right length when doing the replacement - set the motor to zero, then rotate
the outer tube until the distance between the two bolt holes is 245 mm.* A gear motor that is not functional is
replaced after the console is checked first and the steel cable unmounted.

The incline motor is an AC motor with four wires (red UP, black DOWN, white COM, green ground) and a 3-pin
position sensor cable; those definitions are specs cards, and the incline calibration afterwards is a console
card.

The XS300B-YS006 service manual is one book for both XS895 owner's-manual printings; the two-column page is read by step number.


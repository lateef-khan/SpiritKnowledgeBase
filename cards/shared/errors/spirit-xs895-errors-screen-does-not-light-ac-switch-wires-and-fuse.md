---
id: spirit-xs895-errors-screen-does-not-light-ac-switch-wires-and-fuse
title: 'The screen does not light on the incline stepper: the AC switch, the wires
  into the console, then the fuse pulled from the AC switch'
kind: troubleshooting
question: What do I check when the console screen on a Spirit XS895 stepper does not
  light?
asked_as:
- xs895 screen dead
- spirit incline stepper no power to the console
- where is the fuse on the xs895
keywords:
- screen does not light
- ac switch
- fuse
- console wires
- no display
- no power
- incline stepper
- mains
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: no-power
authority: 3
not_to_be_confused_with:
- spirit-cs800-errors-no-display-check-the-adapter-cables-and-pinched-wires
- spirit-med-stepper-errors-no-power-outlet-and-dc-wire
see_also:
- spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led
- cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 9. Common Problems, 9-1 Troubleshooting For Console, PDF p. 41 (printed
    40); text.md lines 615-636
  extracted_at: '2026-09-11'
---

*The Screen doesn't lit.* Three photographs, three captions:

1. Check **AC Switch** is on.
2. Check all the wires that connect to Console are plug well.
3. **Unmount Fuse from AC Switch** and check it. If it is defective to do the replacement.

**The XS895 is a mains machine with a switched, fused inlet**, which is why this page differs from every other Spirit stepper's: the CS800s are adapter-powered and start at the adapter (`spirit-cs800-errors-no-display-check-the-adapter-cables-and-pinched-wires`), the medical steppers at their outlet and DC wire. Here the switch is checked first and the fuse - which lives in the AC switch housing and pulls out of it - last.

**No voltage is printed on this page.** The matrix row for a dim or incomplete display in the same book gives the supply as `110-120V or 220-240V` (`cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt`, which the XS895 shares); this page only asks whether the switch is on, the wires are in and the fuse is whole.

The same fuse is step 5 of the tension motor voltage test (`spirit-xs895-errors-tension-motor-voltage-test-5-5-to-6-vdc-then-the-fuse-and-the-drive-board-power-led`) - a blown fuse takes the resistance motor and the screen down together.

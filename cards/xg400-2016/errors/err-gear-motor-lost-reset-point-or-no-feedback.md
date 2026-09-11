---
id: xg400-2016-errors-err-gear-motor-lost-reset-point-or-no-feedback
title: Err in the message window means the gear motor has lost its reset point or
  the console gets no feedback from it, and the causes run from a chipped gear to
  weak batteries
kind: troubleshooting
question: What does Err mean on a Spirit xg400-2016 elliptical, and what causes it?
asked_as:
- xg400 shows err
- err on my spirit xg400 elliptical
- gear motor error on the elliptical
- motor error message elliptical
keywords:
- err
- motor error
- gear motor
- reset point
- feedback
- yj-9902
- cable
- console
- batteries
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xg400-2016
  applies_to:
  - xg400-2016
  section: errors
  code: err
  model_number:
  - '400415'
authority: 3
not_to_be_confused_with:
- xg400-2016-errors-er1-eeprom-power-cycle-then-replace-console
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- ce850-2024-errors-err-tension-motor-failure
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
see_also:
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc
- xg400-2016-errors-no-resistance-gear-motor-magnet-or-steel-cable
- xg400-2016-errors-er1-eeprom-power-cycle-then-replace-console
source:
  ref: spirit-elliptical-xg400-2016-service-manual
  locator: XG400 2016 (SE551-SE023-01) service manual Troubleshooting for Motor Error,
    PDF p. 41, text.md lines 628-661
  extracted_at: '2026-09-11'
---

**This is the XG400 2016's `Err`, its gear (tension) motor. It is not `Er1`, the EEPROM code on the same page, and not the `--` the same book's error chapter prints for the same motor; and it is not the XE395 2016's `Err`, which is an incline VR, or the CE850 (2020)'s `Err`.**

> When "Err" signal is shown up in the message window, it means that either gear motor has lost its original reset point or the console cannot detect the feedback signal sent by the gear motor.

Causes of Motor Error and dispositions, as printed:

| Cause | What the book says |
|---|---|
| a. Failure of the Gear Motor | The gear motor should be free from abnormal noises during operation. When there is chip out with the motor gear, it creates noises while operating. **Replace YJ-9902 gear motor** to remedy noise issue. |
| b. Defective Cable | The cable could be stuck, not properly installed or too much tension of the spring on magnets, which should cause gear motor to be overloaded and stop functioning. Rearranging the cable properly or replacing it is the usual way to remedy cable issues. |
| c. Console Malfunction / d. | The circuit failure and unable to drive the gear motor. **Replacing the console is the only way** to remedy the problem. |
| e. Insufficient Power (only in case batteries are used) | When batteries are without sufficient power and are unable to drive the gear motor, the error message comes on. Replace the batteries to resume normal operation. |

**Items c and d are one cause split by a numbering slip** - `c. Console Malfunction:` has nothing after the colon and `d.` carries its text. **Item e does not apply to this machine**: the XG400 2016 runs from a mains adaptor and has no batteries. The page is a document from another product pasted in after the matrix; `YJ-9902` is a gear-motor part number that appears nowhere else in the book.

**The same book's error chapter names the same motor fault `--`**, defines it as the motor not moving when Level Up or Down is pressed, and tests the drive board at 5.5 to 6.0 VDC on blue and green wires (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`, `spirit-xe-2016-errors-tension-motor-voltage-test-blue-and-green-5-5-to-6-vdc`). The mechanical guide two pages on gives no-resistance its own three checks (`xg400-2016-errors-no-resistance-gear-motor-magnet-or-steel-cable`).

The CS800 2024 stepper's `Err` is a tension-motor feedback fault too, in the LEVEL window, with a cable check first (`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`); the CE850 (2020) and CE850 2024 ellipticals print `ERR` for a tension motor that does not move (`ce850-2024-errors-err-tension-motor-failure`). Same three letters, different machines.

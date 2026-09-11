---
id: spirit-med-bike-errors-programs-do-not-start-key-test-then-keypad
title: 'Console programs will not start on the rehabilitation bike: cables inside
  the console, then a Key Test that condemns the keypad if it fails or cannot be reached'
kind: troubleshooting
question: Why will the console programs not start on a Spirit Medical 7.0R or 7.0U
  bike?
asked_as:
- 7.0r console wont start a program
- keys do nothing on my rehab bike
- how to test the keypad on the 7.0u
- spirit medical bike buttons not working
keywords:
- programs do not start
- key test
- keypad
- maintenance mode
- engineering mode
- console cables
- rehabilitation bike
- buttons not working
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-programs-do-not-start-keypad-test
see_also:
- spirit-med-bike-errors-no-power-90-to-240-vac-fuse-12-vdc-at-the-console-then-24-vdc-supply
- spirit-med-bike-errors-no-data-when-pedaled-angle-sensor-5-volts-3-mm-and-reed-sensor-5-mm
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48 (printed 46); text.md lines
    1328-1377; 7.0U 2025 owner's manual ERROR MESSAGE & TROUBLESHOOTING, PDF p. 46
    (printed 44); text.md lines 1285-1329; Dyaco MED 7.0R 2021 owner's manual (Rev.
    1.2.1) Error messages and Troubleshooting, PDF p. 84-85; text.md lines 2642-2730;
    7.0R (MR490-SB018-03) service manual 5.2.4 Troubleshooting, 2. Console Programs
    Do Not Start, PDF p. 12, text.md lines 141-158; 7.0U (MU470-SB018) service manual
    5.2.4, 2., PDF p. 12, text.md lines 192-209
  extracted_at: '2026-09-11'
---

The owner's manuals, word for word:

> **Console programs do not start**
> - Perform Keypad test in Maintenance mode
> - If you cannot access the test, and the keys seem to have no affect when pressed, then the keypad has malfunctioned.

The service manuals add one step before the test:

> i. **Open the cover of the console and check all cables were plugged.** After checking the cables, perform the Key Test in Maintenance mode. **Replace the keypad if the Key Test didn't pass or can't enter Maintenance mode.**

**The diagnosis is the test being unreachable as much as the test failing.** Maintenance mode is entered by holding Start, Stop and Enter together for about five seconds, which is itself three key presses - a keypad dead enough to block that entry has already answered the question. The Key Test beeps and shows a number for every key pressed and prints *Passed* when all have been pressed; a key with no beep and no number is the faulty one.

**The part named is the keypad**, not the console - the 7.0R service manual's parts list carries a *Key Board* (19-04) inside the console assembly as a separate item.

The 7.0S/7.5S steppers print the same two owner's-manual bullets (`spirit-med-stepper-errors-programs-do-not-start-keypad-test`). The Maintenance / Engineering mode menu itself is carded under `section: console`.


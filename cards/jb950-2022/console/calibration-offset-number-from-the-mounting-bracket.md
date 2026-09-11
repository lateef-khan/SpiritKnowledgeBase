---
id: jb950-2022-console-calibration-offset-number-from-the-mounting-bracket
title: The Calibration entry holds a brake offset number written on the console mounting
  bracket, which a replacement console must be given before it calibrates itself
kind: procedure
question: What is the calibration offset number on a Spirit jb950-2022 bike and how
  do I enter it on a new console?
asked_as:
- where is the calibration number on the jb950
- i replaced the jb950 console and the resistance feels wrong
- what does caliadj mean on the johnny g bike
- how do i calibrate the brake on the jb950
keywords:
- calibration
- offset number
- encoder count
- console mounting bracket
- caliadj
- home position sensor
- level 1
- dynamometer
- replacement console
- maintenance mode
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: console
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-console-calibration-do-not-enter
see_also:
- jb950-2022-console-calibration-do-not-enter
- jb950-2022-console-brake-test
- jb950-2022-console-limit-sensor-test
- jb950-2022-console-maintenance-mode-entry-and-menu
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 5.3 MAINTENANCE MENU IN CONSOLE SOFTWARE, CALIBRATION, PDF pp. 43-44 (printed
    43-44); text.md lines 815-839
  extracted_at: '2026-09-11'
---

**The owner's manual says do not enter this menu. The service manual is where the procedure lives.**

> Calibration contains sensitive settings of the braking system. Making changes will affect the
> resistance curve.

**When the console is replaced, the old console's calibration offset number must be entered into
the new one.** The number is **written on the console mounting bracket of the original console**;
write it on the new console for future reference. It was determined in the factory on a dynamometer
to compensate for standard tolerances between frames.

**What the number is:** the encoder count from when the brake moves from the home position sensor
to the **Level 1** position.

1. In Maintenance Mode, scroll to **CALIBRATION** and press **Play**. The console shows the
   calibration offset setting.
2. The screen reads, for example, **`CaliAdj 80 2`** over **`80`**. The top number is the actual
   encoder count; the bottom number is the offset adjustment number. **They should match closely but
   may be off by a few counts either way - that is normal.** The third figure is the limit sensor
   flag: **2** between the home sensor and the end-of-travel sensor, **1** at the home sensor, **3**
   at the end-of-travel sensor.
3. Use the **+ / -** keys to adjust the offset to the correct setting and press **Play**. **The brake
   automatically calibrates to the new offset number.** Calibration is complete.

**The "correct setting" is the bracket number, not a figure from this card.** The 80 is the manual's
example and no default is printed; a bike whose bracket number is lost has no documented way back.

**The owner's manual's warning still stands for everyone else** - it says only that adjustments here
"will negatively affect the bike's resistance profile" and gives no steps
(`jb950-2022-console-calibration-do-not-enter`). Testing the brake without touching this number is
`jb950-2022-console-brake-test`; the limit-sensor readings 1, 2 and 3 are the same ones that test
shows.

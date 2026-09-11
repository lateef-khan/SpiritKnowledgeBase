---
id: spirit-ct800-console-calibration-with-grade-return
title: Calibrating with Start and Fast +, through wheel size 2.98 and a grade return
  step
kind: procedure
question: How do I calibrate a Spirit CT800 treadmill?
asked_as:
- how do i calibrate my treadmill
- how do i get into factory settings on the treadmill
- treadmill speed is wrong how do i reset it
- what should the wheel size be set to
keywords:
- calibration
- factory settings
- safety key
- fast plus
- wheel size
- minimum speed
- maximum speed
- maximum elevation
- grade return
- metric
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2012
  - ct800-2016
  - ct850-2018
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- xt-2015-console-calibration-fast-plus
- ct900-calibration-procedure
- ct850-2016-calibration-procedure-metric-or-english
- ct850-2016-calibration-procedure-english-only
- ct850-2016-console-calibration-minimum-speed-0-5
- ct850-2020-console-calibration-minimum-speed-0-3
see_also:
- spirit-ct800-console-engineering-mode-menu-with-units
- ct850-2020-factory-setting-ranges
- ct800-2016-console-calibration-in-kph-with-potentiometer-readings-235-to-22
- ct800-2016-console-calibration-procedure-1-wheel-2-92-to-2-98
source:
  ref: spirit-treadmill-ct800-2012-owners-manual
  locator: 'Calibration Procedure, p. 24; the CT800 2016 owner''s manual prints the
    same nine steps on its p. 36. CT800-2016 service manual: section 8.3 PDF p. 51
    (printed 50), text.md lines 950-981; PROCEDURE 1 PDF p. 65 (printed 64), lines
    1357-1372'
  extracted_at: '2026-09-09'
---

**Nine steps, and step 8 is Grade return.** The later CT800 routine drops that step and holds Start
with **Speed Up** instead of Fast +: `ct900-calibration-procedure`. The 2015 XT routine uses the
same Start and Fast + gesture but has **no wheel size, speed or elevation step at all**:
`xt-2015-console-calibration-fast-plus`. Do not run one on the other's machine.

1. **Remove the safety key.**
2. **Press and hold Start and Fast +, and replace the safety key.** Keep holding Start and Fast
   until the window displays **"Factory settings"**, then press **Enter**.
3. Set the display to **Metric or English** (Miles vs. Kilometers) with the **up or down** key, then
   press **Enter**.
4. Make sure the **wheel size diameter is 2.98**, then press **Enter**.
5. Adjust the **minimum speed** (if needed) to **0.5**, then press **Enter**.
6. Adjust the **maximum speed** (if needed) to **12.0**, then press **Enter**.
7. Adjust the **maximum elevation** (if needed) to **15**, then press **Enter**.
8. **Grade return - On.** This allows the incline to return to zero when Stop is pressed. **For sale
   in Europe, EU standards require this to be off.**
9. **Press Start to begin calibration.** The process is automatic; **the speed will start up without
   warning, so do not stand on the belt.**

Neither manual prints an adjustable range for any of these values, and neither says what to do when
calibration fails beyond checking the speed sensor alignment, which is in the maintenance chapter.
Ranges are printed for the later console in `ct850-2020-factory-setting-ranges`; they are that
machine's figures, not these.

The 2016 manual prints "safety button" for the safety key in steps 1 and 2. That manual replaces the
word "key" with "button" throughout.

**The CT850-2018 owner's manual prints these same nine steps on its p. 40**, including the Start and
Fast + gesture, wheel size 2.98, minimum 0.5, maximum 12.0, maximum elevation 15 and the Grade
return step with its European note, so this card covers that machine. Like the CT800 2016 manual it
writes "safety button" rather than safety key.

**The 2018 manual prints the speed sensor alignment procedure immediately after these steps**,
headed by the sentence "If the calibration does not pass you may need to check the speed sensor
alignment". The CT800 manuals put the same procedure in their maintenance chapter. It is held with
the other speed sensor work at `spirit-ct800-maintenance-speed-sensor-alignment`.

**The other CT850 owner's manuals do not use this routine.** The 2016 and 2020 manuals hold Start
with **Speed Up**, have no grade return step and set a maximum of **15.0**; the ENT-2022 touchscreen
has no key gesture at all.

**The XT685 2010 routine is these nine steps with a different wheel size - 3.01, not 2.98** - and is
kept apart for that reason: `xt685-2010-console-calibration-wheel-size-3-01`.

**The CT800-2016 service manual prints two other calibration routines for the same machine, and
neither has the Grade return step.** Its section 8.3 sets **0.8 and 20.0 kph** with wheel size 2.98
and says what the incline window should read while the incline calibrates
(`ct800-2016-console-calibration-in-kph-with-potentiometer-readings-235-to-22`); its repair
procedure 1 sets 0.5 and 12.0 with a wheel size of **2.92~2.98**
(`ct800-2016-console-calibration-procedure-1-wheel-2-92-to-2-98`). Three routines for one machine;
read all three before you commit a value.


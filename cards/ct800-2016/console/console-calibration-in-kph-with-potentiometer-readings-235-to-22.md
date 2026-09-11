---
id: ct800-2016-console-calibration-in-kph-with-potentiometer-readings-235-to-22
title: 'Calibrating with Start and Fast in kilometres per hour: 0.8 to 20.0 kph, wheel
  2.98, and the incline reading that runs from about 235 to about 22'
kind: procedure
question: How do I calibrate a Spirit ct800-2016 treadmill from its service manual,
  and what should the incline window read?
asked_as:
- how do i calibrate my treadmill
- what should the incline window show during calibration
- calibration fails on the incline
- what wheel size do i enter
keywords:
- calibration
- factory settings
- fast key
- wheel size 2.98
- 0.8 kph
- 20.0 kph
- maximum elevation 15
- potentiometer
- vr reading
- incline window
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: console
  code: '*'
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- spirit-ct800-console-calibration-with-grade-return
- ct800-2016-console-calibration-procedure-1-wheel-2-92-to-2-98
- ct850-2016-calibration-procedure-metric-or-english
- ct900-calibration-procedure
see_also:
- ct800-2016-console-maintenance-menu-and-engineering-mode-as-the-service-manual-prints-them
- ct850-2016-console-data-ranges
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: Section 8.3 CALIBRATION PROCEDURE, PDF p. 51 (printed 50); text.md lines
    950-981
  extracted_at: '2026-09-11'
---

**This is the service manual's main calibration routine for the CT800-2016, in kilometres per hour,
and it is the only CT800 document that says what the incline window should read while the incline
calibrates.** The owner's manual for the same machine prints a nine-step routine in miles with a Grade
return step (`spirit-ct800-console-calibration-with-grade-return`), and the same service manual
prints a third version in its repair procedures with a wheel size range of 2.92 to 2.98
(`ct800-2016-console-calibration-procedure-1-wheel-2-92-to-2-98`). Three routines, one machine.

1. **Remove the safety key.**
2. **Press and hold down the Start and Fast (speed up) buttons with one hand and replace the safety
   key with the other.** Keep holding Start and Fast until the window displays **"Factory settings"**,
   then press **Enter**.
3. Set the display to **Metric or English** with the up or down key, then press Enter.
4. Make sure the **wheel size diameter is 2.98**, then press Enter.
5. Adjust the **minimum speed** (if needed) to **0.8 kph**, then press Enter.
6. Adjust the **maximum speed** (if needed) to **20.0 kph**, then press Enter.
7. Adjust the **maximum elevation** (if needed) to **15**, then press Enter.
8. **Press Start to begin calibration.** The process is automatic; **the speed will start up without
   warning, so do not stand on the belt.**
9. **Speed calibrates first, then incline.** When the incline starts, the **INCLINE window shows the
   actual reading from the potentiometer (VR)**. At the bottom position the reading is **about 235**.
   The Distance window shows the computer's % grade setting; the first setting is 15, so the motor
   drives the base up toward 15% grade. The Incline window reading should change as the base rises,
   from about 235 at the bottom to **around 22** at the top.

**If that number does not change at all when the incline motor moves, the console is not receiving a
reading from the potentiometer.** The E3 / INCLINE ERR test procedure in the same manual is where to
go next.

**The figures are the kilometre versions of the owner's manual's 0.5 and 12.0 mph.** 0.8 kph is 0.5
mph; 20.0 kph is about 12.4 mph, a little above 12.0. The wheel size and the elevation are the same.
**There is no Grade return step here**, where the owner's manual has one.

If the calibration does not pass, the manual prints the speed sensor alignment check immediately
after these steps; that adjustment is held with the maintenance cards.


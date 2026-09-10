---
id: ct900-calibration-procedure
title: Calibration procedure - wheel size, min/max speed, max elevation
kind: procedure
question: How do I calibrate wheel size, min/max speed and max elevation on a Spirit CT800-2020
  or CT900 treadmill?
asked_as:
- how do i calibrate the treadmill
- how do i reset the treadmill to factory settings
- what is the wheel size setting
keywords:
- calibration
- factory settings
- wheel diameter
- min speed
- max speed
- max elevation
- calibrate console
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct800-2024
  - ct850-2024
  - ct900
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-console-calibration-with-grade-return
- xt-2015-console-calibration-fast-plus
- ct850-2016-calibration-procedure-metric-or-english
- ct850-2016-console-calibration-minimum-speed-0-5
- ct850-2020-console-calibration-minimum-speed-0-3
- ct850ent-2022-console-calibration-touchscreen
- ctsbs900-factory-mode-min-max-speed
see_also:
- ct900-engineering-mode-menu
- ct900-incline-position-mismatch-e33
- ct850-2020-factory-setting-ranges
source:
  ref: ct900-om
  locator: p. 34
  extracted_at: '2026-08-24'
---

1. Remove the safety key.
2. Press and hold down the **Start** and **Speed Up** buttons and replace the safety button. Continue to hold the Start and Speed Up buttons until the window displays "Factory settings", then press the **Enter** button.
3. You will now be able to set the display to show Metric or Imperial settings (Meters vs. Miles). Press the **Up** or **Down** button to show which you want, then press **Enter**.
4. Make sure the wheel size diameter is **2.98** then press **Enter**.
5. Adjust the minimum speed (if needed) to **0.5** and then press **Enter**.
6. Adjust the maximum speed (if needed) to **12.0** and then press **Enter**.
7. Adjust the maximum elevation (if needed) to **15** and then press **Enter**.
8. Press **Start** to begin calibration. The process is automatic; the speed will start up without warning, so do not stand on the belt.

If the incline position doesn't match the console after calibration, or you see INCLINE ERR / E33, see [incline position mismatch (E33)](incline-position-mismatch-e33.md).

**The CT800-2020 owner's manual prints these eight steps word for word on its p. 38**, including the
same mix of "safety key" in step 1 and "safety button" in step 2, so this card covers that machine.

**There is no grade return step here.** The 2012 and 2016 CT800 routine has nine steps, holds Start
with **Fast +** rather than Speed Up, and ends with a Grade return setting and a European note:
`spirit-ct800-console-calibration-with-grade-return`. Running one machine's routine on the other is
the classic mistake.

**The CT800ENT-2022 manual prints no calibration procedure at all**, although it twice tells the
reader to run one - in its troubleshooting table and at the head of its speed sensor alignment
section. Nothing on this card is claimed for that machine.

Adjustable ranges for these five values are not printed in any CT800 or CT900 manual. The CT850-2020
service manual prints them for that machine: `ct850-2020-factory-setting-ranges`.

**The CTSBS900 opens factory settings with the same Start + Speed Up gesture but runs a shorter
routine.** Its Factory Mode sets units, minimum speed and maximum speed only - there is no wheel
size step, no maximum elevation step, and no automatic belt run at the end; it finishes with
FINISHED and CONSOLE RESET. Its maximum speed is also a range, 10.0-15.6 mph / 16.0-25.0 kph, not
the single 12.0 above. Do not carry any value on this card across to that machine:
`ctsbs900-factory-mode-min-max-speed`.

**The 2024 CT800 and CT850 owner's manuals print these eight steps word for word on their p. 36**,
under CALIBRATION PROCEDURE & ENGINEERING MODE MENU - the same Start and Speed Up gesture, the same
mix of "safety key" in step 1 and "safety button" in step 2, wheel size **2.98**, minimum **0.5**,
maximum **12.0** and maximum elevation **15** - so this card covers those two machines. The two 2024
books print the identical page; measured on native PDF text their calibration sections match each
other 100% word for word.

**The 2024 ENT treadmills calibrate from the touchscreen instead**, with defaults printed as a range
rather than as steps: `ct800ent-2024-console-calibration-defaults-0-5-to-12-0-mph`.

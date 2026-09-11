---
id: xt685-2023-calibration-procedure
title: Running calibration with a wheel size of 3.01
kind: procedure
question: How do I calibrate an XT685-2023 treadmill?
asked_as:
- how do i calibrate my treadmill
- what wheel size do i enter during calibration
- how do i get into factory settings
keywords:
- calibration
- factory settings
- wheel size
- '3.01'
- maximum speed
- minimum speed
- grade return
- safety key
facets:
  brand:
  - spirit
  product_line: treadmill
  model: xt685-2023
  applies_to:
  - xt685-2023
  section: console
  code: '*'
  model_number:
  - '685823'
authority: 3
not_to_be_confused_with:
- xt-2023-console-calibration-wheel-size-two-four-three
- xt-2023-console-calibration-basic
see_also:
- xt-2023-maintenance-adjusting-the-speed-sensor
- xt-2023-console-engineering-mode-menu
- xt685-2023-console-data-ranges-12-mph-20-kph-spec
source:
  ref: spirit-treadmill-xt685-2023-owners-manual
  locator: page 45, BELT AND DECK CLEANING & CALIBRATION PROCEDURE - Calibration Procedure.
    Service manual section 8.10 Calibration Procedure, PDF p. 34 (printed 34), text.md
    lines 670-681
  extracted_at: '2026-09-09'
---

**The wheel size here is 3.01. The XT385 and XT485 routine is otherwise identical but its wheel size is 2.43, and the XT185 and XT285 routine has no wheel size step at all.** Entering the wrong figure is the reason to keep these three apart.

1. **Remove the Safety Key.**
2. **Press and hold Start and Speed +** and at the same time **replace the Safety Key**. Continue to hold Start and Speed keys until the window displays **"Factory settings"**, then press the **Enter** key.
3. You can now set the display to **Metric or English** (Miles vs. Kilometers). Press the **incline +/-** key to show which you want, then press **Enter**. The maximum speed value is displayed in the speed window, and the maximum elevation value is displayed in the incline window.
4. **Adjust the maximum speed (if needed) to 12.0 mph** and then press **Enter**.
5. **Adjust the minimum speed (if needed) to 0.5 mph** and then press **Enter**.
6. **Make sure the wheel size diameter is 3.01**, then press **Enter**.
7. **Grade return - On.** This allows the incline to return to zero when the Stop button is pressed. For sale in Europe, EU standards require this to be off.
8. **Press Start to begin calibration.** The process is automatic; **the speed will start up without warning, so do not stand on the belt.**

If the calibration does not pass, check the speed sensor alignment: `xt-2023-maintenance-adjusting-the-speed-sensor`.

**The service manual prints the same eight steps with the metric figures written out**: step 2 holds
"Start and Fast +", step 4 sets the maximum to **20.0 kmph (IMPERIAL set 12.0MPH)**, step 5 the
minimum to **1.0 kmph (IMPERIAL set 0.5MPH)**, and step 6 is "Make sure the wheel size diameter is
3.01". Its grade-return step prints no EU sentence. **That service manual has no Maintenance Menu or
engineering-mode section at all** - see `xt-2023-console-engineering-mode-menu` - so the calibration
routine is the only console setting it prints.


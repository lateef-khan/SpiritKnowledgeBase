---
id: xt685ent-2023-console-calibration-behind-five-taps-on-settings
title: 'Calibrating from Settings: tap the word Settings more than five times, open
  CONTROLLER, tick Start calibrating speed and Check speed, then Reboot'
kind: procedure
question: How do I calibrate a Spirit xt685ent-2023 treadmill?
asked_as:
- how do i calibrate the touchscreen treadmill
- where is the hidden device information page
- what should the wheel diameter be on the xt685ent
- what do incline low point and high point mean
keywords:
- calibration
- settings five times
- device information
- controller
- check speed
- wheel diameter
- torque value
- pwm start
- max incline
- reboot
facets:
  brand:
  - spirit
  product_line: treadmill
  model: xt685ent-2023
  applies_to:
  - xt685ent-2023
  section: console
  code: '*'
  model_number:
  - '685523'
authority: 3
not_to_be_confused_with:
- xt485ent-2023-console-calibration-behind-the-software-version-and-password-20160620
- xt685-2023-calibration-procedure
- ct850ent-2022-console-calibration-touchscreen
- f80-2023-engineering-mode
see_also:
- xt685ent-2023-console-settings-page-ten-items-with-a-retail-sleep-mode
- spirit-xtent-console-data-ranges-12-mph-time-to-999
source:
  ref: spirit-treadmill-xt685ent-2023-service-manual
  locator: Section 8.9 Calibration Procedure, PDF pp. 39-42 (printed 39-42); text.md
    lines 628-670. The screenshots were rendered and read
  extracted_at: '2026-09-11'
---

**There is no key gesture and no password on this console; the hidden page is behind repeated taps on
the word Settings.** The XT485ENT hides the same page behind five taps on its software version and a
password (`xt485ent-2023-console-calibration-behind-the-software-version-and-password-20160620`).

1. After power on, touch the **gear icon** in the status bar to open the Settings page.
2. **Tap the word "Settings" more than 5 times in a row** to enter the DEVICE INFORMATION page.
3. On DEVICE INFORMATION, tap **CONTROLLER** to open CONTROLLER INFORMATION.
4. Set **Metric or Imperial**. **Tick "Start calibrating speed?"**, then check the wheel diameter,
   the maximum speed and the maximum incline (the manual's words: "set the wheel diameter is 75 and
   set the maximum speed (if needed) to 12.0 mph and max incline to 30...etc.").
5. Click **"Check speed"** to start calibration. The process is automatic; **the speed will start up
   without warning, so do not stand on the belt.**
6. To complete the speed and incline calibration, click **"Reboot"** to reboot the display. The
   success screen reads **"Speed calibration successfully!"** and shows an **Incline low point**
   (18 in the screenshot) and an **Incline high point** (206).

**The text and the screenshots disagree on two figures.** Step 4's sentence says wheel diameter
**75** and max incline **30**; the CONTROLLER screenshot on the next page shows **WHEEL DIAMETER 60**
and **MAX INCLINE 30 %**, and the DEVICE INFO screenshot before it shows **MAX INCLINE 15 %**. The
machine's incline range is 0 to 15 (`spirit-xtent-console-data-ranges-12-mph-time-to-999`). Read the
console's own screen; do not type 75 or 30 from this sentence.

The CONTROLLER screenshot's other values: **TORQUE VALUE 50, PWM START 1080, PWM SEGMENTATION 1007,
MIN SPEED 0.5 mph, MAX SPEED 12.0 mph**, with a **ROM Reset Factory** control at the bottom right.
The DEVICE INFO page shows MIN SPEED 0.5, MAX SPEED 12.0, MIN INCLINE 0 %, **Rom version C5A28V12**,
Total distance, a **U DISK** button, **"Set reminder to refuel time: 90 hours"**, and System
Settings, Restore Factory and Open Log buttons. Those are the demonstration machine's values, not a
spec, and the manual describes none of the buttons.

**None of these fields is the LED XT685's wheel size of 3.01** (`xt685-2023-calibration-procedure`);
that figure belongs to a different routine on a different console.


---
id: xt485ent-2023-console-calibration-behind-the-software-version-and-password-20160620
title: 'Calibrating from Settings: tap the software version five times, enter 20160620,
  then CONTROLLER, Start calibrating speed and CHECK SPEED'
kind: procedure
question: How do I calibrate a Spirit xt485ent-2023 treadmill?
asked_as:
- how do i calibrate the touchscreen treadmill
- what is the password for the calibration screen
- where is calibration on the xt485ent
- what are the wheel diameter and torque values
keywords:
- calibration
- settings
- software version
- five taps
- password 20160620
- controller
- check speed
- wheel diameter 60
- torque value 65
- reboot
facets:
  brand:
  - spirit
  product_line: treadmill
  model: xt485ent-2023
  applies_to:
  - xt485ent-2023
  section: console
  code: '*'
  model_number:
  - '485850'
authority: 3
not_to_be_confused_with:
- xt685ent-2023-console-calibration-behind-five-taps-on-settings
- xt-2023-console-calibration-wheel-size-two-four-three
- ct850ent-2022-console-calibration-touchscreen
see_also:
- xt485ent-2023-console-settings-menu
- spirit-xtent-console-data-ranges-12-mph-time-to-999
source:
  ref: spirit-treadmill-xt485ent-2023-service-manual
  locator: Section 8.10 CALIBRATION PROCEDURE, PDF pp. 55-56 (printed 55-56); text.md
    lines 828-856. The two screenshots were rendered and read
  extracted_at: '2026-09-11'
---

**There is no key gesture. The calibration screen is hidden behind the software version number and a
password.** The owner's manual's Settings card says this console holds no calibration
(`xt485ent-2023-console-settings-menu`); it holds one, here.

1. Choose **Settings** at the bottom right of the screen, then tap **Software**.
2. The screen shows the software version - the screenshot reads
   `C006_XT485_T1001B_S002_201130_EN`. **Tap the version line five times.**
3. **Enter the password 20160620** to confirm before the calibration screen opens.
4. Choose the **CONTROLLER** tab and set the units, imperial or metric.
5. **To calibrate speed as well as incline, tick "Start calibrating speed"** at the bottom left.
   Without the tick, only the incline level is calibrated. Click **CHECK SPEED** to begin.
6. The process is automatic; **the speed will start up without warning, so do not stand on the belt.**
   When the "calibration successfully" screen appears, click **reboot** to exit.

The CONTROLLER screen in the screenshot:

| Field | Value shown |
|---|---|
| UNITS | METRIC / IMPERIAL (Imperial selected) |
| WHEEL DIAMETER | 60 |
| TORQUE VALUE | 65 |
| PWM START | 0 |
| PWM SEGMENTATION | 0 |
| MIN SPEED | 0.5 mph |
| MAX SPEED | 12.0 mph |
| MAX INCLINE | 15 % |

A **ROM Reset Factory** control sits at the bottom right, and the tabs across the top are DEVICE
INFO, CONTROLLER and FREQUENCY. The manual describes none of those, gives no adjustable range for any
field, and does not say what to do when calibration fails.

**These values are not the LED XT485's.** The LED XT485-2023 enters a wheel size of **2.43** in a
Start-and-Speed routine (`xt-2023-console-calibration-wheel-size-two-four-three`); this screen's
wheel diameter is a different quantity in a different unit, and 2.43 does not belong here. The
XT685ENT screen is the same page reached a different way, with a torque value of 50 and PWM figures
in the thousands (`xt685ent-2023-console-calibration-behind-five-taps-on-settings`).

**The Settings screenshot on the same page lists seven items** - Display, WiFi, Bluetooth, Software,
Date Time, Child Lock, Units - where the owner's manual lists five and says the machine has no child
lock. See `xt485ent-2023-console-settings-menu`.


---
id: trx5500-2024-console-engineering-mode-behind-the-software-version-and-password-20160620
title: 'Engineering mode: tap the software version five times and enter 20160620'
kind: procedure
question: How do I get into engineering mode and calibrate an Xterra trx5500-2024
  treadmill?
asked_as:
- how do i calibrate the trx5500 touchscreen
- what is the service password for the trx5500
- where is the lube reminder setting
keywords:
- engineering mode
- calibration
- password 20160620
- software version
- device info
- controller
- wheel diameter 60
- check speed
- refuel reminder
- restore factory
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx5500-2024
  applies_to:
  - trx5500-2024
  section: console
  code: '*'
  model_number:
  - '155810'
authority: 3
not_to_be_confused_with: []
see_also:
- trx5500-2024-console-settings-wifi-time-software-update-brightness-bluetooth
- xt485ent-2023-console-calibration-behind-the-software-version-and-password-20160620
source:
  ref: xterra-treadmill-trx5500-2024-service-manual
  locator: 7-13 Calibration Procedure, PDF p. 60-68 (printed 59-67), text.md lines
    939-1034 and OCR supplements; Device Info and Controller pages read from a 130
    dpi render of p. 64-65
  extracted_at: '2026-09-11'
---

From the Dyaco GT90D-NT041 service manual; the owner's manual prints no engineering mode.

1. Power on and wait for the main page.
2. Touch the **Settings** icon (bottom right), then **Software**.
3. Touch the software version **5 times** to open the password page. (The screenshot shows a version string of the form `C006_TRX5500_T1001B ... 201113`.)
4. Enter the password **20160620** and touch CONFIRM. The **DEVICE INFO** page opens: MIN SPEED 0.5 mph, MAX SPEED 12.0 mph, MIN INCLINE 0 %, MAX INCLINE 15 %, a "Set reminder to refuel time" field reading **90 hours** (the lube reminder), and SYSTEM SETTINGS, RESTORE FACTORY and OPEN LOG buttons.
5. Touch **CONTROLLER** to open the speed-calibrating page: UNITS (Metric / Imperial), WHEEL DIAMETER **60**, TORQUE VALUE **65**, PWM START 0, PWM SEGMENTATION 0, MIN SPEED 0.5 mph, MAX SPEED 12.0 mph, MAX INCLINE 15 %, a "Start calibrating speed?" tick box, a CHECK SPEED button and ROM Reset Factory. A third tab is FREQUENCY.
6. Two procedures: **(a)** leave "Start calibrating speed?" unticked and touch CHECK SPEED — only the incline motor is calibrated, the belt does not move, and incline parameters are recorded (the screen shows INCLINE LOW POINT and HIGH POINT AD values); **(b)** tick "Start calibrating speed?" then touch CHECK SPEED — both incline and speed are calibrated and recorded. Touch **Reboot** when finished.

Spirit's XT485ENT uses the same five taps and the same password ([Spirit twin](../../xt485ent-2023/console/console-calibration-behind-the-software-version-and-password-20160620.md)).


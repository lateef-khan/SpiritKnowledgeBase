---
id: xe395ent-2021-console-engineer-mode-service-tests-key-motor-incline-sensor
title: 'The Service page of Engineer Mode: a Key Test, a Motor Test and an Incline
  Test each with Manual and Auto modes showing an AD value, and a Sensor Test'
kind: procedure
question: How do I test the resistance motor, incline motor, keys or sensors on a
  Spirit xe395ent-2021 elliptical?
asked_as:
- how do i test the incline motor on the xe395ent
- xe395ent motor test ad value
- xe395ent sensor test hp wp rpm
- xe395ent key test
keywords:
- service
- key test
- motor test
- incline test
- manual
- auto
- ad value
- sensor test
- bt hr
- rpm
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- xe395ent-2021-console-engineer-mode-ten-presses-on-settings-function-page-30-minute-sleep
- xe395ent-2021-console-engineer-mode-factory-setting-machine-type-blename-and-incline-calibration
- spirit-xb55ent-console-engineer-mode-service-tests-key-motor-incline-sensor
- xe395ent-2021-console-settings-menu-and-its-eight-items
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: MAINTENANCE MENU IN CONSOLE SOFTWARE, 2. Service, PDF p. 42 (printed 42);
    text.md lines 587-615, screenshot from the OCR supplement for PDF page 42
  extracted_at: '2026-09-11'
---

The Service page of Engineer Mode
(`xe395ent-2021-console-engineer-mode-ten-presses-on-settings-function-page-30-minute-sleep`)
holds four items, word for word:

**Key Test** - Click "Reset" to clear key. The screenshot shows a key count beside the RESET button.

**Motor Test**

1. **Manual**: Click "Test" to enable the tiny-move motor function, then click "+" or "-" to move
   the motor forward or backward a little. It shows the **AD value** for the current position.
2. **Auto**: Click "Test" to enable the lift test function; it moves the motor up to High-Level then
   down to Low-Level automatically. It shows the AD value for the current position, the target Level
   and the count of cycles (`CNT`).

**Incline Test** - the same two Manual and Auto tests, word for word, for "the incline Motor".

**Sensor Test** - Click "Test" to enable the sensor test; it can test **BT HR value, HP value, WP
value and RPM**. The screenshot row reads `HRS: HP: WP: 60 RPM`.

**Both motors are real on this machine.** The Motor Test drives the tensioning gear motor and the
Incline Test the 115 V AC incline motor this book describes in its electrical chapter. The XBR55ENT
and XBU55ENT bikes print the same page with an Incline Test that has nothing to drive
(`spirit-xb55ent-console-engineer-mode-service-tests-key-motor-incline-sensor`).

**The AD value is the position sensor reading.** The manual prints no target range, no pass value
and no error message for any of the four tests. HP and WP are the hand-pulse and wireless-pulse
inputs; BT HR is a Bluetooth chest strap, which pairs from the ordinary Settings page
(`xe395ent-2021-console-settings-menu-and-its-eight-items`). Incline calibration itself is on the
Factory Setting page
(`xe395ent-2021-console-engineer-mode-factory-setting-machine-type-blename-and-incline-calibration`).

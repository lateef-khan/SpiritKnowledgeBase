---
id: spirit-xb55ent-console-engineer-mode-service-tests-key-motor-incline-sensor
title: 'The Service page of Engineer Mode: a Key Test, a Motor Test and an Incline
  Test in Manual and Auto with AD values, and a Sensor Test that reads BT HR, HP,
  WP and RPM'
kind: procedure
question: How do I test the resistance motor, keys or sensors on a Spirit XBR55ENT
  or XBU55ENT bike?
asked_as:
- how do i test the resistance motor on the xbr55ent
- how do i test the buttons on the xbu55ent
- what is the ad value on the bike engineer mode
- how do i test the heart rate sensor on the xbr55ent
keywords:
- service
- key test
- motor test
- incline test
- sensor test
- ad value
- manual
- auto
- bt hr
- hand pulse
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55ent-2021
  - xbu55ent-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xb55ent-console-engineer-mode-ten-presses-on-settings-function-page-30-minute-sleep
- spirit-xb55ent-console-engineer-mode-factory-setting-machine-type-blename-and-an-incline-calibration
- xe395ent-2021-console-settings-menu-and-its-eight-items
source:
  ref: spirit-bike-xbr55ent-2021-service-manual
  locator: XBR55ENT MAINTENANCE MENU IN CONSOLE SOFTWARE, 2. Service, PDF p. 30 (printed
    30); text.md lines 362-390, screenshot from the OCR supplement for PDF page 30.
    The XBU55ENT-2021 service manual prints the same page word for word on its PDF
    p. 30, text.md lines 358-386
  extracted_at: '2026-09-11'
---

The Service page of Engineer Mode
(`spirit-xb55ent-console-engineer-mode-ten-presses-on-settings-function-page-30-minute-sleep`) holds
four items, word for word:

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

**These bikes have no incline motor.** The Incline Test is on the screen and in the text because
the page was written for the XE395ENT elliptical, whose Engineer Mode this is; on the XBR55ENT and
XBU55ENT the Motor Test is the tensioning gear motor and the Incline Test has nothing to drive. The
Factory Setting page carries the same leftover as an Incline Calibration
(`spirit-xb55ent-console-engineer-mode-factory-setting-machine-type-blename-and-an-incline-calibration`).

**The AD value is the motor position sensor reading.** The manual prints no target range, no pass
value and no error message for any of the four tests. HP and WP are the hand-pulse and wireless-pulse
inputs; BT HR is a Bluetooth chest strap, which pairs from the ordinary Settings page
(`xe395ent-2021-console-settings-menu-and-its-eight-items`).

**The Sole touchscreen ellipticals of the same generation print this page with the same four
tests**; it is Dyaco software shared across brands, but the Sole card is not evidence for these two
machines.

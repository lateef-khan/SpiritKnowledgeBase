---
id: xe395ent-2021-console-engineer-mode-factory-setting-machine-type-blename-and-incline-calibration
title: 'The Factory Setting pages: Restore Factory, First Launch, a Machine Type reading
  XE395, a BLE name, and an Incline Calibration that runs the motor up and down for
  three to six seconds each way'
kind: procedure
question: How do I calibrate the incline, restore factory settings or rename the Bluetooth
  on a Spirit xe395ent-2021 elliptical?
asked_as:
- how do i calibrate the incline on the xe395ent
- xe395ent restore factory settings
- xe395ent blename bluetooth name
- xe395ent first launch
keywords:
- factory setting
- restore factory
- first launch
- machine type
- blename
- bluetooth name
- incline calibration
- max ad
- min ad
- engineer mode
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
- xe395ent-2021-console-engineer-mode-service-tests-key-motor-incline-sensor
- spirit-xb55ent-console-engineer-mode-factory-setting-machine-type-blename-and-an-incline-calibration
- xe395-2018-errors-incline-calibration-three-key-hold
- xe395-2016-console-incline-calibration-stop-level-and-start-held-five-seconds
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: MAINTENANCE MENU IN CONSOLE SOFTWARE, 3. Factory Setting and 4. Factory
    Setting (Incline Calibration), PDF pp. 43-44 (printed 43-44); text.md lines 615-641,
    screenshot from the OCR supplement for PDF page 44
  extracted_at: '2026-09-11'
---

The Factory Setting page of Engineer Mode
(`xe395ent-2021-console-engineer-mode-ten-presses-on-settings-function-page-30-minute-sleep`)
holds four items, word for word:

| Item | What the manual says |
|---|---|
| Restore Factory | Click "Clear" to restore factory. |
| First Launch | Click "ON" to set First Launch ON, then re-power ON will process First Launch UI. |
| Machine Type | See the console machine type. The manual adds: **"Machine Type is XE395"**. |
| BLENAME | Input the new name and press SAVE to re-name the BLE device name; **re-power on**, then a phone can scan for the console under the new BLE name. "Just for developer test". |

**A fourth page, also headed Factory Setting, holds one item - Incline Calibration:**

> Click "start" to calibrate incline. The incline motor will move UP till no move any more for 3~6
> sec and move Down till no move any more for 3~6 sec then finish to calibration.

The screen shows **MAX. AD**, **MIN. AD**, **CURRENT AD** and **DIRECTION**. No target figures are
printed. This is the calibration the E3 troubleshooting pages send you back to ("Run calibration
again", "re-calibrate the incline set"); those pages are held with the error cards.

**A touchscreen button, not a key hold.** The LED XE395 of 2018 calibrates its incline by holding
Start, Level Up and Stop for five seconds (`xe395-2018-errors-incline-calibration-three-key-hold`);
the 2016 service manual holds Stop, Level and Start
(`xe395-2016-console-incline-calibration-stop-level-and-start-held-five-seconds`). Neither gesture
is printed for this machine.

**Restore Factory says nothing about what it keeps.** No odometer, account or record is named as
surviving or being cleared.

**BLENAME is the name a phone sees.** The manual gives no length limit and marks the control as a
developer test. The XBR55ENT and XBU55ENT bikes print these pages unchanged, with their own machine
types
(`spirit-xb55ent-console-engineer-mode-factory-setting-machine-type-blename-and-an-incline-calibration`).

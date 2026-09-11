---
id: spirit-xb55ent-console-engineer-mode-factory-setting-machine-type-blename-and-an-incline-calibration
title: 'The Factory Setting page: Restore Factory, First Launch, a Machine Type of
  upright or recumbent, a BLENAME for the Bluetooth name, and an Incline Calibration
  for an incline the bike does not have'
kind: procedure
question: How do I restore factory settings, set the machine type or rename the Bluetooth
  on a Spirit XBR55ENT or XBU55ENT bike?
asked_as:
- how do i factory reset the xbr55ent console
- how do i change the bluetooth name of the xbu55ent
- my xbu55ent thinks it is a recumbent bike
- what is first launch on the spirit bike engineer mode
keywords:
- factory setting
- restore factory
- first launch
- machine type
- blename
- bluetooth name
- incline calibration
- engineer mode
- xbu55 upright
- xbr55 recumbent
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
- spirit-xb55ent-console-engineer-mode-service-tests-key-motor-incline-sensor
- spirit-ent-bike-console-spirit-plus-app-from-the-top-right-icon
source:
  ref: spirit-bike-xbr55ent-2021-service-manual
  locator: XBR55ENT MAINTENANCE MENU IN CONSOLE SOFTWARE, 3. Factory Setting and 4.
    Factory Setting (Incline Calibration), PDF pp. 31-32 (printed 31-32); text.md
    lines 390-416, screenshots from the OCR supplement for PDF pages 31 and 32. The
    XBU55ENT-2021 service manual prints the same pages word for word on its PDF pp.
    31-32, text.md lines 386-412
  extracted_at: '2026-09-11'
---

The Factory Setting page of Engineer Mode
(`spirit-xb55ent-console-engineer-mode-ten-presses-on-settings-function-page-30-minute-sleep`) holds
four items, word for word:

| Item | What the manual says |
|---|---|
| Restore Factory | Click "Clear" to restore factory. |
| First Launch | Click "ON" to set First Launch ON, then re-power ON will process First Launch UI. |
| Machine Type | See the console machine type. **Machine Type is XBU55 or XBR55** - the screenshot offers **XBU55-UpRight Bike** and **XBR55-Recumbent Bike**. |
| BLENAME | Input the new name and press SAVE to re-name the BLE device name; **re-power on**, then a phone can scan for the console under the new BLE name. "Just for developer test". |

**Machine Type is the one that must be right.** The two bikes share one console software, and this
switch is what tells it which bike it is on. The manual does not say what goes wrong if it is set
to the other bike.

**BLENAME is the name the Spirit+ app sees.** The screenshot's default is "Phone's Name"; the
manual gives no length limit and marks the control as a developer test. Pairing itself is done from
the app (`spirit-ent-bike-console-spirit-plus-app-from-the-top-right-icon`).

**Restore Factory says nothing about what it keeps.** No odometer, account or record is named as
surviving or being cleared.

**A fourth page, also headed Factory Setting, holds one item - Incline Calibration:** "Click 'start'
to calibrate incline. The incline motor will move UP till no move any more for 3~6 sec and move Down
till no move any more for 3~6 sec then finish to calibration." The screen shows MAX. AD, MIN. AD,
CURRENT AD and DIRECTION. **Neither bike has an incline motor.** The page is the XE395ENT
elliptical's, printed unchanged in both bike books; on these machines there is nothing for it to
move, and no card should send an XBR55ENT or XBU55ENT owner to it. The Service page carries the same
leftover as an Incline Test
(`spirit-xb55ent-console-engineer-mode-service-tests-key-motor-incline-sensor`).

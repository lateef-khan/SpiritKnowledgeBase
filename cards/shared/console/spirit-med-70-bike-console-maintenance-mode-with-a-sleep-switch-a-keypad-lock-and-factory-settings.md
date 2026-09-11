---
id: spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings
title: 'Maintenance mode behind Start, Stop and Enter for five seconds: Key and Display
  tests, Functions with a Sleep switch, a Security keypad lock and Factory settings'
kind: procedure
question: How do I get into maintenance mode on a Spirit Medical 7.0 series bike,
  and what is in the menu?
asked_as:
- how do i switch the 7.0r to metric
- how do i turn off sleep mode on the 7.0u
- how do i reset the odometer on my spirit medical bike
- what is in engineering mode on the rehab bike
keywords:
- maintenance mode
- engineering mode
- start stop enter
- five seconds
- key test
- display test
- sleep mode
- pause mode
- units
- beep
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-40-bike-console-maintenance-mode-with-an-ant-id-a-bootloader-switch-and-a-model-setting
- spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
see_also:
- spirit-med-70-bike-console-security-lock-unlocked-with-start-and-enter-for-3-seconds
- spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration
- spirit-med-70-bike-console-unit-type-recumbent-or-upright-and-the-model-codes-the-service-manual-names
- spirit-med-70-bike-console-power-on-self-test-odometer-and-a-twenty-minute-power-down
- 70t-2026-console-maintenance-mode-menu
- spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: 7.0R OM MACHINE CARE / Console Software, PDF p. 47 (printed 45), text.md
    lines 1294-1328; 7.0U OM PDF p. 45 (printed 43), lines 1251-1285; Dyaco MED 7.0R
    (2021) "Maintenance menu in console software", PDF pp. 82-84 (printed 82-84),
    lines 2592-2659. 7.0R SM (MR490-SB018-03) 5.2.1 Maintenance Mode, PDF pp. 7-8,
    lines 73-109; 7.0U SM (MU470-SB018) 5.2.1, PDF pp. 7-8, lines 124-160.
  extracted_at: '2026-09-11'
---

**Press and hold Start, Stop and Enter together for about 5 seconds, then press Enter.** The heading
says the menu "may be called Engineering mode, depending on version" - and the books split exactly
that way: the three owner's manuals say the message window shows **"Maintenance mode"**, both service
manuals say **"Engineering mode"**. No book says to pedal first; these bikes are mains powered.

| Item | What it holds |
|---|---|
| **Key test** | Press all the keys one at a time. The service manuals add: each press beeps and shows a number; a key with no beep and no number has failed; when every key has been pressed the display shows **Passed** and the test ends by itself |
| **Display test** | Lights each LED sequentially |
| **Functions** (Enter to open) | **Sleep mode**, **Pause mode**, **Odometer reset**, **Units**, **Beep sound** - see below |
| **Security** | Locks the keypad (`spirit-med-70-bike-console-security-lock-unlocked-with-start-and-enter-for-3-seconds`) |
| **Factory settings** | **Brake Test**, **Sensor test**, **Crank position cali**, **Watts calibration (Factory use only)**, **Unit type** (`spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration`, `spirit-med-70-bike-console-unit-type-recumbent-or-upright-and-the-model-codes-the-service-manual-names`) |

**Functions, entry by entry, with the figures each book prints:**

| Entry | 2025 7.0R / 7.0U owner's manuals | Dyaco MED 7.0R (2021) | Service manuals MR490-SB018-03 / MU470-SB018 |
|---|---|---|---|
| **Sleep mode** | on = powers down after **30 minutes** of inactivity, "this is the default setting"; off = stays on until the main power switch is turned off | same wording, **20 minutes** | on = sleeps after **30 minutes**; off = "the console power is always on" |
| **Pause mode** | on = **5 minutes** of pause; off = pauses indefinitely | same, 5 minutes | on = pause lasts **30 minutes** then the console returns to idle; off = indefinite |
| **Odometer reset** | zeroes time and distance | same | "Reset odometer readings" |
| **Units** | English (imperial) or metric; **default imperial**, so bodyweight and height are in pounds and inches | same | ENGLISH or METRIC |
| **Beep sound** | speaker on or off | same | same |

**Two figures disagree across the five books and nothing settles them**: the sleep time (30 or 20) and
the pause length (5 or 30). The console chapters of all three owner's manuals separately say the console
powers down after 20 minutes
(`spirit-med-70-bike-console-power-on-self-test-odometer-and-a-twenty-minute-power-down`). Quote the
book the caller holds and say the others differ.

**Not in this menu**: no ANT ID, no Update Code, no LED brightness, no CSAFE test and no Exit item -
those are the 4.0 series
(`spirit-med-40-bike-console-maintenance-mode-with-an-ant-id-a-bootloader-switch-and-a-model-setting`).
The rehabilitation steppers' menu has a Motor test where these bikes have a Brake test
(`spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test`), and the 7.0T
treadmill's a Service Mode with incline and drive-motor tests (`70t-2026-console-maintenance-mode-menu`).

**The troubleshooting pages send you here** - "Perform Keypad test in Maintenance mode", "Perform the
Sensor tests in Maintenance mode" - and the service manuals say a console that cannot enter the menu,
or fails the Key Test, needs its keypad replaced. The one error message, EEPROM error, is with the error
cards.


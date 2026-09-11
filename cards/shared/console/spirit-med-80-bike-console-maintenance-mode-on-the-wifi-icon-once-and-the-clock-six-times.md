---
id: spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
title: Maintenance Mode on the touchscreen bikes opens on one tap of the Wi-Fi icon
  and six on the clock, and holds Odometer, Software versions, Service and a Lock
  Facility Program switch
kind: procedure
question: How do I get into maintenance mode on a Spirit Medical 8 series bike, and
  what is in it?
asked_as:
- how do i get into the service menu on the 8.0u
- where is the odometer on the 8.5r touchscreen
- how do i see the firmware version on my spirit medical bike
- what is lock facility program on the 8.0u
keywords:
- maintenance mode
- engineering mode
- wifi icon
- clock six times
- status bar
- odometer
- software version
- lcb version
- lock facility program
- machine type
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings
- spirit-med-40-bike-console-maintenance-mode-with-an-ant-id-a-bootloader-switch-and-a-model-setting
- cu1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups
see_also:
- spirit-med-80-bike-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
- spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
- spirit-med-80-bike-console-settings-menu-and-the-four-viewing-modes-with-close-up-mode
- spirit-med-80-bike-console-screen-overview-prints-a-factory-mode-banner-and-a-treadmill-tile
- 85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 85ue-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 80t-2026-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: 8.0U SM (MU2000-SB036-01) 4.2 MAINTENANCE MODE, PDF p. 10, text.md lines
    161-175 (screenshot in the OCR supplement); 4.2.1 Menu Structure, PDF p. 11, lines
    175-212; 4.2.2.1 and 4.2.2.4, PDF pp. 12 and 16, lines 214 and 311-312. 8.5R SM
    (MR2000-SB036-01) 4.2, PDF p. 9, lines 114-125; 4.2.1, PDF p. 10, lines 125-160;
    PDF pp. 11 and 15, lines 162 and 244-245.
  extracted_at: '2026-09-11'
---

**On the Home Screen, tap the Wi-Fi icon once, then tap the clock in the status bar six times.**
"Maintenance Mode is intended for troubleshooting purposes." The screenshot marks the two targets with
arrows at the top right of the Welcome page - the Age, Height and Weight wheels with the Timer and Start
buttons - where the status bar reads a Wi-Fi symbol and **12:15**; it is the same Factory-Mode
screenshot the owner's manuals print (`spirit-med-80-bike-console-screen-overview-prints-a-factory-mode-banner-and-a-treadmill-tile`).

**What the menu holds, as the book draws its tree:**

| Top level | Second level | Third level |
|---|---|---|
| **Odometer** | | |
| **Software** | Android Version, Firmware Version, LCB Version, Console APP Version | |
| **Service** | Machine Type | Treadmill, Upright Bike, Recumbent Bike, Recumbent Stepper, UBE, Rehab UBE |
| | Communication | |
| | NFC Sensor | |
| | Keypad Test | Resistance Increase, Resistance Decrease, Start/Stop, Enter |
| | Error Log | |
| | Beacon Test | White, Blue, Green, Yellow, Red Color |
| | Crank Sensors | Crank Index Magnet Sensor, Crank RPM Angle Sensor |
| | Crank Calibration | |
| **Lock Facility Program** | ON / OFF Setting | |

"The full name of LCB is Lower Control Board."

**Odometer** - "Indicates the total belt operation time and accumulated running distance." **That is
treadmill wording on a machine with no belt**; the figures are the machine's total time and distance.

**Lock Facility Program** - "When set to ON, the speed and incline profiles of the Facility program
cannot be modified." Treadmill wording again; on this machine the Facility program's resistance
profile is what the lock protects.

**Software** is where firmware, LCB and console-app updates run (`spirit-med-80-bike-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`). **Service** holds the
eight tests (`spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`).

**There is no key-hold entry and no menu the owner's manual describes.** The owner's manuals never
mention maintenance mode; Settings is the owner's menu (`spirit-med-80-bike-console-settings-menu-and-the-four-viewing-modes-with-close-up-mode`). Do not hold Start, Stop and
Enter on this console - that is the LED consoles' gesture (`spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings`).

**The 8.0U and 8.5R books print this chapter identically**, tree and all; the 8.5S stepper, the 8.5UE
ergometer and the 8.0T treadmill share the app and the gesture
(`85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`,
`85ue-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`,
`80t-2026-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`), the treadmill's
tree carrying motor and step-sensor tests instead of crank tests.


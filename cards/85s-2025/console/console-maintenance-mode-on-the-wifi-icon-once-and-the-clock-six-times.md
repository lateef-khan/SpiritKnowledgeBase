---
id: 85s-2025-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
title: Maintenance Mode opens on one tap of the Wi-Fi icon and six on the clock, and
  holds Odometer, Software versions, Service and a Lock Facility Program switch
kind: procedure
question: How do I get into maintenance mode on a Spirit 85s-2025 recumbent stepper,
  and what is in it?
asked_as:
- how do i get into the service menu on the 8.5s stepper
- where is the odometer on the 8.5s touchscreen
- how do i see the firmware version on the spirit 8.5s
- what is lock facility program on the 8.5s
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
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: console
  code: '*'
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- 85s-fit-2026-console-maintenance-mode-behind-ten-presses-on-hello-guest
- spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test
- spirit-ent-console-enter-engineering-mode
- cu1000ent-2023-console-maintenance-mode-welcome-ten-times-four-groups
see_also:
- 85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
- 85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
- 85s-2025-console-settings-and-the-four-workout-views
- 85s-2025-console-screen-overview-prints-a-factory-mode-banner
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 8.5S-785545 (MS2000-SB036-01) service manual 4-2 Maintenance Mode, PDF
    p. 7, text.md lines 99-102 (the screenshot with its two arrows was read from a
    render); 4.2.1 Maintenance Mode Menu Structure, PDF p. 8, lines 103-138, read
    against a render of the tree; 4.2.2.1, 4.2.2.2 and 4.2.2.4, PDF pp. 9 and 11,
    lines 140-141 and 187
  extracted_at: '2026-09-11'
---

**On the Home Screen, tap the Wi-Fi icon once, then tap the clock in the status bar six times.**
"Maintenance Mode is intended for troubleshooting purposes." The screenshot marks the two targets
with arrows at the top right of the Welcome page - the page with the Age, Height and Weight wheels
and the Lift, Timer and Start buttons - where the status bar reads a Wi-Fi symbol and **12:15**.

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

**Odometer** - *"Indicates the total belt operation time and accumulated running distance."* The
sentence is treadmill wording on a stepper with no belt to run; the figures are the machine's total
time and distance.

**Software** shows the four version strings and is where updates run
(`85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`). **LCB is the
Lower Control Board**, which the book says three times in footnotes.

**Service** holds the eight tests and the Machine Type switch
(`85s-2025-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`).
"This series of six models shares the same app" - the six machine types above - so the type must be
set to Recumbent Stepper for this machine.

**Lock Facility Program** - *"When set to ON, the speed and incline profiles of the Facility program
cannot be modified."* Speed and incline are again treadmill words; the setting locks the Facility
program's profile against editing.

**No units, language, beacon-on/off, standby or pause entry is here.** Those live in the user-facing
**Settings** page behind the gear icon (`85s-2025-console-settings-and-the-four-workout-views`); the
book's update screenshot shows that page listing Progress Beacon, Acceleration & Deceleration,
Language, Time & Date, WiFi, Standby, Pause Mode, Account, Units and Software.

**Not the 8.5S-Fit's gesture, and not the LED steppers' hold.** The 8.5S-Fit opens its maintenance
mode on **ten presses of Hello Guest**
(`85s-fit-2026-console-maintenance-mode-behind-ten-presses-on-hello-guest`); the 7.5S and MS300 LED
consoles hold **Start, Stop and Enter for five seconds**
(`spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test`); the ENT
touchscreens press Home or Welcome ten times. **The 8.5S owner's manual prints no maintenance mode
at all** - this service manual is the only document that opens it.


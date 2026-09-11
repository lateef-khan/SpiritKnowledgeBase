---
id: spirit-med-40-bike-console-maintenance-mode-with-an-ant-id-a-bootloader-switch-and-a-model-setting
title: 'Maintenance mode behind Start, Stop and Confirm: Key and Display tests, Functions,
  a Brake and CSAFE test, an ANT ID, an Update Code bootloader switch and a Model
  setting'
kind: procedure
question: How do I get into maintenance mode on a Spirit Medical 4.0 series bike,
  and what is in the menu?
asked_as:
- how do i switch the 4.0r to metric
- how do i turn off the beep on my spirit medical bike
- how do i reset the odometer on the 4.0u
- what is update code in the 4.0r service menu
keywords:
- maintenance mode
- engineering mode
- start stop confirm
- key test
- display test
- units
- beep
- odometer reset
- ant id
- bootloader
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40r-pt
  - 40u-2025
  - 40u-pt
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings
- spirit-ce800-console-maintenance-menu-function-and-service
- spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
see_also:
- spirit-med-40-bike-console-face-two-row-message-window-rpm-and-level-windows-and-five-program-keys
- 40t-2026-console-maintenance-mode-menu
- 40t-2026-console-pause-mode-setting
- spirit-ce800-console-maintenance-menu-function-and-service
source:
  ref: spirit-bike-40r-2025-owners-manual
  locator: 4.0R OM MACHINE CARE / Console Software, PDF p. 36 (printed 34), text.md
    lines 1017-1050; 4.0U OM PDF p. 36, lines 971-1004. 4.0R SM (FR800-SB022-03) 8-3
    MAINTENANCE MODE MENU, PDF p. 30, lines 353-382; 4.0U SM (FU800-SB022-03) 8-3
    Maintenance Mode, PDF p. 30, lines 388-409. PT 4.0 R "Maintenance mode in console
    software", PDF pp. 55-56 (printed 55-56), lines 1726-1771; PT 4.0 U PDF pp. 53-54,
    lines 1691-1735.
  extracted_at: '2026-09-11'
---

**Press and hold the Start, Stop and Confirm keys together until the message window shows
"maintenance mode", then press Confirm.** The console "has built in maintenance/diagnostic software"
that will, for example, "change the console settings from English to Metric and turn off the beeping
of the speaker when a key is pressed".

**How long to hold, and whether to pedal, depends on which book you read.**

| Book | Hold for | Pedal first? |
|---|---|---|
| 2025 owner's manuals (4.0R, 4.0U) and both Dyaco PT editions | **about 2 seconds** | not mentioned |
| Service manuals FR800-SB022-03 and FU800-SB022-03 | **about 5 seconds** | **"pedal the bike and press and hold"** |

The console is generator powered, so it is not live standing still; the service manual's "pedal the
bike" is the practical instruction, and a console that shows nothing after two seconds is worth holding
for five.

**The menu as the owner's manuals and PT editions print it:**

| Item | What it holds |
|---|---|
| **Key test** | Test all the keys; press them one at a time |
| **Display test** | Lights each LED sequentially |
| **Functions** (press Confirm to open) | **Unit** - English (imperial) or metric; **the default is imperial**, so bodyweight and height read in pounds and inches. **Pause mode** - on allows 5 minutes of pause, off pauses indefinitely. **Odometer reset** - zeroes time and distance. **Beep sound** - speaker on or off. **LED Brightness**. **Model** - "Select the kind of device" |
| **Service** | **Brake Test** - "Adjust PWM value"; **CSAFE Test** - test the CSAFE functions |
| **ANT ID** | "Adjust the ANT ID" |
| **Update Code** | "Switch bootloader on/off. **The default is off.**" |
| **Exit** | Press Confirm to leave maintenance mode and restart |

**The service manuals draw the same items in a different tree and drop one.** They print five numbered
groups - 1 Key Test, 2 Display Test, 3 FUNCTION (Units, PAUSE MODE ON/OFF, Odometer Reset, BEEP SOUND,
LED BRIGHTNESS), 4 SERVICE (Brake Test, C safe Test, **ANT ID, UPDATE CODE**), 5 EXIT - so ANT ID and
Update Code sit **inside Service** there, and **there is no Model entry**. Nothing says which tree the
console actually shows; try Service if ANT ID is not at the top level.

**Neither book explains the ANT ID beyond "adjust" it, nor says what to do once the bootloader is on.**
Nothing here describes a USB port, a file name or an update procedure - the parts lists carry a
Bluetooth board and a CSAFE board, and this is the only page that touches either. Do not promise a
firmware update path from this menu.

**Sleep mode is not in this menu.** No sleep entry and no power-down time are printed anywhere in
these books; the console is generator powered and goes dark when pedalling stops.

**The Security keypad lock, the Sensor test, the Crank position calibration and the Unit type of the
7.0 series are not here** - that is a different menu
(`spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings`).
The CR800/CU800 commercial bikes' menu has no ANT ID, no Update Code and no LED Brightness
(`spirit-ce800-console-maintenance-menu-function-and-service`).

**The only error message the service manuals print for this console, EEPROM ERR, is cleared with a
different three-key hold** - Start, Stop and Fan - and is held with the error cards.


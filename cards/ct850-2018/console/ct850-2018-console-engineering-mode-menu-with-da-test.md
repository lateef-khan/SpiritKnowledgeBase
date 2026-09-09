---
id: ct850-2018-console-engineering-mode-menu-with-da-test
title: The engineering mode menu whose Functions list holds ODO Reset and a DA Test
kind: procedure
question: How do I get into engineering mode on a Spirit CT850-2018 treadmill and what
  is in it?
asked_as:
- how do i get into the service menu on my treadmill
- how do i switch the treadmill from miles to kilometres
- how do i stop the console beeping when i press a button
- how do i reset the odometer
keywords:
- engineering mode
- diagnostic software
- button test
- lcd test
- functions
- sleep mode
- odo reset
- units
- beep
- da test
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2018
  applies_to:
  - ct850-2018
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-console-engineering-mode-menu-with-units
- ct900-engineering-mode-menu
- ct850-2016-console-engineering-mode-menu-with-units
- ct850-2016-engineering-mode-menu
see_also:
- spirit-ct800-console-calibration-with-grade-return
- ct900ent-sleep-mode-auto-shutoff
- ct850-2016-mileage-lock
- ct850-2016-reset-odometer-and-hours
source:
  ref: spirit-treadmill-ct850-2018-owners-manual
  locator: ENGINEERING MODE MENU, p. 43
  extracted_at: '2026-09-09'
---

**This menu has a DA Test and an ODO Reset, and no Grade Return.** No other Spirit treadmill menu in
this repository prints a DA Test. The menus that look closest to it are
`spirit-ct800-console-engineering-mode-menu-with-units`, which has Grade Return and Maintenance
instead, and `ct900-engineering-mode-menu`, which has GS Mode and no Units. Do not read one onto
another.

The console has built in maintenance/diagnostic software. It will, for example, change the console
settings from English to Metric and turn off the beeping of the speaker when a button is pressed.

**To enter: press and hold the Start, Stop and Enter buttons for about 5 seconds**, until the
Message Center displays **Engineering Mode Menu**, then press **Enter**.

| Item | What it does |
|---|---|
| 1. Button Test | Test all the buttons to make sure they are functioning |
| 2. LCD Test | Tests all the display functions |
| 3. Functions | Press Enter to access the settings, Up arrow to scroll |
| 4. Security | Allows the buttonpad to be locked to prevent unauthorized use |

Under **Functions**:

| Setting | What it does |
|---|---|
| a. Sleep Mode | Turn on to have the console power down automatically after **20 minutes** of inactivity |
| b. Pause Mode | Turn on to allow 5 minutes of pause, turn off to have the console pause indefinitely |
| c. ODO Reset | Resets the odometer |
| d. Units | Sets the display to readout in English or Metric display measurements |
| e. Beep | Turns off the speaker so no beeping sound is heard |
| f. DA Test | **Tests the brake resistance** |

**Unlike every other engineering menu in this family, entry needs no safety key gesture.** The
manual does not say to remove or insert the safety button, only to hold the three keys for about 5
seconds.

**The manual contradicts itself about the sleep time-out.** This menu says **20 minutes**; the
console chapter's TO TURN TREADMILL OFF section says the display goes to sleep after **30 minutes**
of inactivity (`ct900ent-sleep-mode-auto-shutoff`). Nothing in the manual resolves it; both figures
are reproduced as printed.

**The manual gives no unlock sequence for the Security item**, and prints no Child Lock. Its two
other locking features are separate: the mileage lock (`ct850-2016-mileage-lock`) and the
diagnostics screen that clears the odometer (`ct850-2016-reset-odometer-and-hours`), both entered
with the numeric buttons and the safety button rather than from this menu.

**Calibration is not in this menu.** It has its own entry gesture and its own "Factory settings"
prompt: `spirit-ct800-console-calibration-with-grade-return`.

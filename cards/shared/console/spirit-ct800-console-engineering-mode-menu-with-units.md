---
id: spirit-ct800-console-engineering-mode-menu-with-units
title: The engineering mode menu whose Functions list holds Units and Grade Return
kind: procedure
question: How do I get into engineering mode on a Spirit CT800 treadmill and what
  is in it?
asked_as:
- how do i get into the service menu on my treadmill
- how do i switch the treadmill from miles to kilometres
- how do i stop the console beeping when i press a key
- how do i reset the lube message
keywords:
- engineering mode
- diagnostic software
- key test
- display test
- security
- keypad lock
- sleep mode
- beep
- units
- maintenance reset
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2012
  - ct800-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900-engineering-mode-menu
- ct850-2016-engineering-mode-menu
- xt-2015-console-engineering-mode-menu
- ct850-2016-console-engineering-mode-menu-with-units
- ct850-2018-console-engineering-mode-menu-with-da-test
see_also:
- spirit-ct800-console-calibration-with-grade-return
- ct900ent-sleep-mode-auto-shutoff
- ct800-2016-console-maintenance-menu-and-engineering-mode-as-the-service-manual-prints-them
source:
  ref: spirit-treadmill-ct800-2012-owners-manual
  locator: 'Engineering Mode Menu, p. 24; the CT800 2016 owner''s manual prints the
    same menu on its p. 37. CT800-2016 service manual: Maintenance menu PDF p. 52
    (printed 51), text.md lines 981-1004; Engineering Mode PDF p. 69 (printed 68),
    lines 1488-1530'
  extracted_at: '2026-09-09'
---

**This menu has a Units entry and a Grade Return entry.** The later CT800 menu has neither, puts
Display Test second and adds a Child Lock: `ct900-engineering-mode-menu`. The CT850-2016 menu is
entered a different way again - SPEED and ENTER, not Start, Stop and Enter -
`ct850-2016-engineering-mode-menu`.

The console has built in maintenance/diagnostic software. It will, for example, change the console
settings from English to Metric and turn off the beeping of the speaker when a key is pressed.

**To enter: press and hold the Start, Stop and Enter keys, then insert the safety key.** Keep
holding the keys down until the Message Center displays **Engineering Mode Menu**, then press
**Enter**.

| Item | What it does |
|---|---|
| a. Key Test | Test all the keys to make sure they are functioning |
| b. Security | Allows the keypad to be locked to prevent unauthorized use |
| c. Functions | Press Enter to access the settings, Up arrow to scroll |
| d. Display Test | Tests all the display functions |

Under **Functions**:

| Setting | What it does |
|---|---|
| i. Sleep Mode | Turn on to have the console power down automatically after **20 minutes** of inactivity |
| ii. Beep | Turns off the speaker so no beeping sound is heard |
| iii. Grade Return | Returns the elevation to lowest setting when pause is pressed |
| iv. Units | Sets the display to English or Metric readings |
| v. Maintenance | Resets the lube reset message and odometer |
| vi. Pause Mode | Turn on to allow 5 minutes of pause, turn off to have the console pause indefinitely |

**The two manuals disagree with themselves about the sleep time-out.** This menu says the console
powers down after **20 minutes** of inactivity. The console operation chapter of the same two
manuals says the display goes to sleep after **30 minutes** of inactivity
(`ct900ent-sleep-mode-auto-shutoff`). Nothing in either manual resolves it; both figures are
reproduced as printed.

**The 2016 manual calls the first item Button Test.** That manual replaces the word "key" with
"button" throughout, so it also reads "insert the safety button" in the entry instruction.

**Calibration is not in this menu.** It has its own entry gesture and its own "Factory settings"
prompt: `spirit-ct800-console-calibration-with-grade-return`.

**The CT800-2016 service manual prints this menu twice more, and neither copy matches this one.** Its
"Maintenance menu" lists Key Test, Display test, Functions and Security with **Start and Enter held
together** as the unlock, and its repair-procedure "Engineering Mode" adds a Calibration sub-menu, a
separate Lube Message Reset and a "CONSOLE LOCKED" prompt; neither prints the 20-minute sleep figure.
Both are on `ct800-2016-console-maintenance-menu-and-engineering-mode-as-the-service-manual-prints-them`.


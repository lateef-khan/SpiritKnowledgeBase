---
id: ct900-engineering-mode-menu
title: Engineering Mode Menu - diagnostic and service settings
kind: procedure
question: How do I open Engineering Mode on a Spirit CT800-2020 or CT900 treadmill and what
  settings does it hold?
asked_as:
- how do i enter engineering mode
- how do i lock the keypad
- how do i change units to metric
- how do i reset the odometer
keywords:
- engineering mode
- maintenance mode
- key test
- display test
- security
- sleep mode
- pause mode
- gs mode
- beep mode
- odometer
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct900
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-console-engineering-mode-menu-with-units
- ct850-2016-engineering-mode-menu
- xt-2015-console-engineering-mode-menu
see_also:
- ct900-calibration-procedure
- ct900-pause-stop-reset
source:
  ref: ct900-om
  locator: p. 34
  extracted_at: '2026-08-24'
---

The console has built-in maintenance/diagnostic software that lets you change settings such as English to Metric units and turn off the speaker beep. To enter the Engineering Mode Menu, press and hold down the **Start**, **Stop** and **Enter** buttons, then insert the safety button. Keep holding the buttons down for about 5 seconds until the Message Center displays Engineering Mode Menu. Press **Enter** to access the menu below:

1. **Key Test** - Will allow you to test all the buttons to make sure they are functioning.
2. **Display Test** - Tests all the display functions.
3. **Security** - Allows the keypad to be locked to prevent unauthorized use. Sets the Child Lock function; this locks out the keypad until a pre-determined key sequence is pressed. Key sequence = **Incline UP** held down together until unlocked.
4. **Functions** (Press Enter to access settings, Up arrow to scroll)
   - **Sleep Mode** - Turn on to have the console power down automatically after 30 minutes of inactivity.
   - **Pause Mode** - Turn on to allow 5 minutes of pause, turn off to have the console pause indefinitely. *(This is the setting behind the "After 5 minutes the display will reset" behavior described in [Pause/Stop/Reset](../console/pause-stop-reset.md).)*
   - **Maintenance** - Reset maintenance reminder message and odometer readings.
   - **GS Mode** - Returns the elevation to lowest setting when pause is pressed.
   - **Beep Mode** - Turns the speaker (beep sound) on or off.

**The CT800-2020 owner's manual prints items 1 to 4 above word for word on its p. 41**, including the
five Functions settings and the 30 minute sleep figure, so this card covers that machine. Two
details of how it prints them:

- **It lists Security twice** - as item 3, "Allows the keypad to be locked to prevent unauthorized
  use", and again as item 5, "Sets the Child Lock function", with the same Incline UP unlock
  sequence. Item 3 above holds both descriptions.
- **It has no Units setting and no Grade Return setting under those names.** GS Mode is the grade
  return. The earlier CT800 menu does have both, along with a 20 minute sleep figure and a different
  item order: `spirit-ct800-console-engineering-mode-menu-with-units`.

**The CT800ENT-2022 manual has no engineering mode section at all**, so nothing here is claimed for
that machine.

**The Maintenance Mode sub-menu below is printed in the CT900 manual only.** No CT800 manual prints
it, so do not quote SERVICE MODE, the RPM and AMPS readout or the numbered test steps for a CT800.

## Maintenance Mode sub-menu detail

1.1 Press and hold the Start, Stop and Enter key at the same time.
1.2 The MW (Message Window) will display MAINTENANCE MODE, then PRESS ENTER.
1.3 The Maintenance Mode menu is:

- **1.3.1 KEY TEST** (Enter to run) - MW shows PRESS ALL KEYS. As the user presses keys, the MW shows the key number, e.g. "S1". When all keys are pressed, MW shows TEST PASSED for 3 seconds then exits to the next test in the menu.
- **1.3.2 DISPLAY TEST** (Enter to run) - Lights all LEDs. User presses Stop to end the test and exit to the next test.
- **1.3.3 SLEEP MODE - ON** (Enter to modify) - Default is ON. Sleep after 30 minutes.
- **1.3.4 ODOMETER** (Enter for menu) - MW shows ODOMETER _____ HRS. MW shows ENTER TO RESET; if the user presses Enter, resets the odometer and exits to the next test.
- **1.3.5 UNITS - ENGLISH** (Enter to modify) - Default is English.
- **1.3.6 SPEAKER - ON** (Enter to modify) - Default is ON.
- **1.3.7 INCLINE RETURN - ON** (Enter to Modify) - Default is ON: Incline returns to home position when Pause is pressed. OFF means the incline remains at current setting when Pause is pressed, but will return to home position when the program ends.
- **1.3.8 SERVICE MODE** (Enter for Menu)
  - **1.3.8.1 INCLINE** (Enter to run) - Use Incline keys, then MW displays: HOME POS SW - OFF. When the switch is activated, display changes to ON.
  - **1.3.8.2 DRIVE MOTOR** (Enter to run) - Use Speed keys. Each key press increases motor speed 0.1 mph/kph. MW then shows: RPM ___ AMPS___. RPM is measured from the flywheel hall sensor. The Speed window shows MPH information.

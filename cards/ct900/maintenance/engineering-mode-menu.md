---
id: ct900-engineering-mode-menu
title: Engineering Mode Menu - diagnostic and service settings
kind: procedure
question: How do I open Engineering Mode on a CT900 and what settings does it hold?
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
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with: []
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

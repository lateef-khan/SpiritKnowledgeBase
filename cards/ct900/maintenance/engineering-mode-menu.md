---
id: ct900-engineering-mode-menu
title: Engineering Mode Menu - diagnostic and service settings
kind: procedure
question: How do I open Engineering Mode on a Spirit CT800-2020 or CT900 treadmill
  and what settings does it hold?
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
  - ct800-2024
  - ct850-2020
  - ct850-2024
  - ct900
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-console-engineering-mode-menu-with-units
- ct850-2016-engineering-mode-menu
- xt-2015-console-engineering-mode-menu
- ct850-2016-console-engineering-mode-menu-with-units
- ct850-2018-console-engineering-mode-menu-with-da-test
- ctsbs900-maintenance-mode-key-and-display-test
- ctsbs900-maintenance-mode-function-settings
see_also:
- ct900-calibration-procedure
- ct900-pause-stop-reset
- ct900-console-factory-and-acceleration-settings-accel-decel-0-02
- 40t-2026-console-maintenance-mode-as-the-service-manual-prints-it
source:
  ref: ct900-om
  locator: p. 34-35. CT900 service manual, Maintenance Mode, PDF p. 38 (printed 38),
    text.md lines 537-573
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

**Of the CT800 and CT850 range, the Maintenance Mode sub-menu below is printed in the CT900 manual
only.** No CT800 manual prints it, so do not quote SERVICE MODE, the RPM and AMPS readout or the
numbered test steps for a CT800. The CT900 manual prints it as the full-page figure on p. 35, not as
running text, so a text-only extract of that manual will not contain it.

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

**The CT850-2020 owner's manual prints items 1 to 5 above word for word on its p. 41**, including
the five Functions settings, the 30 minute sleep figure and the Security entry printed twice with
the Incline UP unlock sequence, so this card covers that machine.

**The CT850-2016 owner's manual prints a sixth Functions setting, Units**, between Maintenance and
GS Mode, and is held separately: `ct850-2016-console-engineering-mode-menu-with-units`. **The
CT850-2018 menu is different again** - Button Test, LCD Test, a Functions list with ODO Reset and a
DA Test, and a 20 minute sleep figure:
`ct850-2018-console-engineering-mode-menu-with-da-test`. **The CT850ENT-2022 manual has no
engineering mode section at all.**

**The CTSBS900 has a Maintenance Mode that is entered differently and holds different items.** It
opens on Start + Stop + Enter held for **2 seconds** with no safety key to insert, and its menu is
KEY TEST, DISPLAY TEST, FUNCTION and SERVICE - it has no Security or Child Lock entry, and it adds
ODOMETER RESET, OTA AUTO and a SERVICE menu for USB and over-the-air software updates that nothing
here describes: `ctsbs900-maintenance-mode-key-and-display-test`,
`ctsbs900-maintenance-mode-function-settings`. Nothing on this card is claimed for that machine.

**The 2024 CT800 and CT850 owner's manuals print items 1 to 5 word for word on their p. 36**,
including the five Functions settings, the **30 minute** sleep figure, the Start + Stop + Enter hold
of about 5 seconds with the safety button inserted, and the Security entry printed twice with the
**Incline UP** unlock sequence - so this card covers those two machines. Like the 2020 manuals they
have no Units setting and no Grade Return under those names; GS Mode is the grade return.

**They print the menu on the same page as the calibration procedure**, under the shared heading
CALIBRATION PROCEDURE & ENGINEERING MODE MENU, with ENGINEERING MODE MENU as a sub-heading below the
eight calibration steps.

**The 2024 ENT treadmills have no key gesture at all** - their maintenance mode is opened by pressing
**Hello Guest** ten times on the touchscreen and holds five groups, not five numbered items:
`cu800ent-2024-console-maintenance-mode-and-engineering-menu`.

**The CT900 service manual prints the Maintenance Mode sub-menu above word for word on its p. 38**,
as running text, with the same KEY TEST, DISPLAY TEST, SLEEP MODE 30 minutes, ODOMETER in hours,
UNITS, SPEAKER, INCLINE RETURN and SERVICE MODE entries. **The CT800-2020 service manual prints no
engineering or maintenance menu at all**; its only console setting is the factory-settings table
(`ct850-2020-factory-setting-ranges`). The 4.0T service manual prints this same CT900-style menu
with a Confirm key (`40t-2026-console-maintenance-mode-as-the-service-manual-prints-it`).


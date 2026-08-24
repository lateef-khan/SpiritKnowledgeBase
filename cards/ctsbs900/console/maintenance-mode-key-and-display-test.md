---
id: ctsbs900-maintenance-mode-key-and-display-test
title: Maintenance Mode — entering it, Key Test, and Display Test
kind: procedure
question: How do I enter CTSBS900 Maintenance Mode and run the Key and Display tests?
asked_as:
- how do i enter the service menu
- how do i test if the console buttons work
- how do i test the console display
keywords:
- maintenance mode
- key test
- display test
- press all keys
- service menu
facets:
  product_line: treadmill
  model: ctsbs900
  applies_to:
  - ctsbs900
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ctsbs900-maintenance-mode-function-settings
- ctsbs900-maintenance-mode-software-update
- ctsbs900-factory-mode-min-max-speed
see_also:
- ctsbs900-maintenance-mode-function-settings
- ctsbs900-maintenance-mode-software-update
- ctsbs900-factory-mode-min-max-speed
source:
  ref: ctsbs900-om
  locator: p. 49
  extracted_at: '2026-08-24'
---

To enter **Maintenance Mode**, press and hold the **Start, Stop, and Enter** keys simultaneously for 2 seconds.

Maintenance Mode is operated through a menu system:
- KEY TEST
- DISPLAY TEST
- FUNCTION > (see [console/maintenance-mode-function-settings.md](maintenance-mode-function-settings.md))
- SERVICE > (see [console/maintenance-mode-software-update.md](maintenance-mode-software-update.md))
- EXIT

After entering Maintenance Mode, a long beep sounds and the Message Window (MW) displays: **"MAINTENANCE MODE MENU – PRESS ENTER."**

1. Press **Enter** to access the first main menu item, Key Test — the MW displays "KEY TEST."
2. Use the **Up/Down** keys to select each option in the main menu.
3. When Key Test is selected, the MW displays "KEY TEST." Press **Enter** to enter the Key Test, and the MW shows "PRESS ALL KEYS." Each key pressed displays its corresponding key label. After all keys have been pressed, the display shows "TEST PASSED" for 3 seconds, then returns to the main menu.
4. If Display Test is selected, the MW shows "DISPLAY TEST." Press **Enter** to enter the Display Test — a long beep sounds to begin.
   1. All LEDs turn ON for 2 seconds.
   2. All LEDs turn OFF for 2 seconds.
   3. The MW displays all characters from "0" to "9" and "A" to "Z," changing once per second. At the same time, the DM (Dot Matrix) switches one row every 0.5 seconds until all 8 rows have been displayed; then the DM switches one column every 0.5 seconds until all 24 columns have been displayed; then all LEDs display in sequence once.

---
id: e20-2026-engineering-mode
title: Entering the engineering menu and what is in it
kind: procedure
question: How do I get into the engineering mode menu on a Sole E20-2026 elliptical?
asked_as:
- how do i get into the service menu on my elliptical
- how do i reset the odometer on my sole elliptical
- how do i turn off the beep on my elliptical
- hidden menu on sole elliptical
keywords:
- engineering mode
- service menu
- maintenance menu
- diagnostic
- key test
- display test
- odo reset
- motor test
- factory set
facets:
  brand:
  - sole
  product_line: elliptical
  model: e20-2026
  applies_to:
  - e20-2026
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e20-2026-display-units
- e20-2026-sleep-mode
- e20-2026-pause-mode-setting
- e20-2026-child-lock
- e20-2026-power-up-and-odometer
source:
  ref: sole-elliptical-e20-2026-owners-manual
  locator: page 20, Engineering Mode
  extracted_at: '2026-09-04'
---

The console has **built in maintenance/diagnostic software**. It can change console settings such as **English or Metric units** and **turning off the console beeps**.

**To enter: press and hold down the Start, Stop and Enter keys. Keep holding for about five seconds.** **Press the Level Up/Down keys to navigate the menu.**

| Code | Menu item | What it does |
|---|---|---|
| F00 | KEY TEST | Test all the keys to make sure they are functioning |
| F01 | DISPLAY TEST | Automatically tests all LED |
| F02 | ODO RESET | Resets the odometer |
| F03 | UNITS | 1: English, 0: Metric - English (Imperial) or Metric display readings |
| F04 | SLEEP MODE | 1: OFF, 0: ON - console powers down automatically after 15 minutes of inactivity |
| F05 | MOTOR TEST | Continually runs the tensioning gear motor |
| F06 | MANUAL | Allows stepping of the gear motor |
| F07 | PAUSE MODE | 1: OFF, 0: ON - on allows 5 minutes of pause, off pauses indefinitely |
| F08 | KEY TONE | 1: OFF, 0: ON - the beep sound when a key is pressed |
| F09 | CHILD LOCK | 1: OFF, 0: ON - locks the keypad against unauthorized use |
| F10 | FACTORY SET | For factory use only |
| F11 | EXIT | Select to exit the Maintenance Menu |

**F10 is for factory use only** - the manual gives no further description of it.

Four of these items have their own cards because they answer questions on their own: `e20-2026-display-units`, `e20-2026-sleep-mode`, `e20-2026-pause-mode-setting` and `e20-2026-child-lock`.

**The only motor this menu tests is the tensioning gear motor** (F05, F06). There is no incline test in the list.

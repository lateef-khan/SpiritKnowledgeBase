---
id: sr500-2016-maintenance-menu
title: Engineering mode in the console software
kind: procedure
question: How do I get into engineering mode on a Sole sr500-2016 rower?
asked_as:
- how do i get into engineering mode on a sole rower
- change my rower from miles to km
- reset the odometer on an sr500
- motor test on a sole rowing machine
keywords:
- engineering mode
- maintenance menu
- fun
- key test
- odometer reset
- units
- motor test
- manual test
- diagnostic
facets:
  brand:
  - sole
  product_line: rower
  model: sr500-2016
  applies_to:
  - sr500-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sr500-2016-console-buttons
- sr500-2016-no-adjustable-resistance
source:
  ref: sole-rower-sr500-2016-service-manual
  locator: Section 7.4, Maintenance menu in the console software
  extracted_at: '2026-09-04'
---

**In IDLE MODE, long press the UP and DOWN keys together for 3 seconds** to enter engineering mode. Pressing **RESET** at any time returns to idle mode.

On entry the console runs an LCD byte display test, lighting each byte in turn, then goes straight to the main menu screen. The console window displays **"FUN"**; press **MODE** to enter the options.

| Menu | Item |
|---|---|
| FUNCTION > | KEY TEST |
| | ODOMETER RESET |
| | UNITS - ENGLISH / METRIC |
| | MOTOR TEST - correction related |
| | MANUAL |

**KEY TEST.** Press MODE to confirm entry. The console window scrolls "PRESS ALL KEYS". "KEY NUMBER" appears in the DISTANCE window as each key is pressed. When every key has been pressed the console window shows **"OK"**, and after 2 seconds it returns to KEY TEST.

**ODOMETER RESET.** Press MODE to enter; the console window shows "ODO RESET". Press **UP, then DOWN, then MODE** to clear the total mileage and total time. When cleared the display shows **"RET"**, and after 2 seconds it returns to the ODOMETER RESET submenu.

**UNITS.** Press MODE to enter the unit switching screen. The default unit is **"MI"**; press UP or DOWN to switch, and the window shows **"KM"** for metric. Press MODE to accept and return to the UNITS submenu.

**MOTOR TEST**, the automatic motor test. Press MODE and the console window shows "TEST" with **"L 01" (L01~L16)** in the DISTANCE window. Press UP, DOWN, MODE to run it: it increments to the highest level then descends to the minimum, **changing every 2 seconds**, then runs the motor drag cable test. Press RESET to end and return to the MOTOR TEST submenu.

**MANUAL**, the manual motor test. "TEST" is displayed; press MODE to enter. The DISTANCE window shows **XX, the motor COUNTER value**, and the level window shows **L1 ~ L16**. Press UP to raise the segment number to 16, DOWN to lower it to 1, and RESET to finish and return to the MANUAL submenu.

---
id: spirit-rower-console-engineering-mode-up-and-down-three-seconds-fun-menu
title: Engineering mode opens on Up and Down held three seconds, shows FUN, and holds
  a Key Test, Odometer Reset, Units, Motor Test and Manual motor test
kind: procedure
question: How do I get into engineering mode on a Spirit CRW800 or XRW600 rower, and
  what is in it?
asked_as:
- how do i get into engineering mode on the spirit rower
- how do i reset the odometer on my crw800 rower
- change the spirit rower from miles to km
- how do i test the resistance motor on the rower
keywords:
- engineering mode
- maintenance menu
- fun
- key test
- odometer reset
- units
- motor test
- manual test
- up and down three seconds
- diagnostic
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  - xrw600-2019
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-water-rower-console-engineering-mode-sound-and-odo
- spirit-stepper-console-maintenance-menu-sleep-mode-default-off-and-a-cross-reference-to-the-wrong-page
- sr500-2016-maintenance-menu
see_also:
- crw800-2024-console-button-functions
- crw800-2024-console-window-functions
- xrw600-console-screen-overview
- sr500-2016-maintenance-menu
- crw900-2021-errors-vr-setting-for-trouble-with-resistance
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: CRW800 (2020) service manual 7-4 Maintenance menu in the console software,
    PDF p. 36 (printed 35); text.md lines 506-534. CRW800-2016 (CW800-YR001) service
    manual 8.4 Maintenance menu in the console software, PDF p. 36, lines 456-486.
    XRW600-2019 (DW400-YR002) service manual 8.4, PDF p. 36, lines 447-477. CRW800-2024
    owner's manual ENGINEERING MODE, printed p. 28, lines 1398-1430. All four print
    the same nine numbered steps; the wording differences are named in the body
  extracted_at: '2026-09-11'
---

**In IDLE MODE, press and hold the UP and DOWN keys together for 3 seconds** to enter "engineering
mode one". **Pressing RESET at any time returns to IDLE MODE.**

On entry the console runs an **LCD byte display test**, lighting each byte in turn, then goes
straight to the main menu. The console window shows **"FUN"**; press **MODE** to enter the options.

| Menu | Item | What it holds |
|---|---|---|
| FUNCTION > | KEY TEST | |
| | ODOMETER RESET | |
| | UNITS > | ENGLISH / METRIC |
| | MOTOR TEST > | "Correction related" |
| | MANUAL | |

**KEY TEST.** Press MODE to confirm. The console window scrolls **"PRESS ALL KEYS"**; a **KEY NUMBER**
appears in the DISTANCE window as each key is pressed. When every key has been pressed the window
shows **"OK"**, and after 2 seconds it returns to KEY TEST.

**ODOMETER RESET.** Press MODE; the window shows **"ODO RESET"**. Press **UP, then DOWN, then MODE** to
clear the total mileage and the total time. When cleared the display shows **"RET"**, and after
2 seconds it returns to the ODOMETER RESET submenu.

**UNITS.** Press MODE to enter the unit switching screen. The default is **"MI"**; press UP or DOWN
to switch, and the window shows **"KM"** for metric. Press MODE to accept and return to the UNITS
submenu.

**MOTOR TEST**, the automatic motor test. Press MODE and the window shows **"TEST"** with **"L 01"**
(L01 to L16) in the DISTANCE window. Press UP, DOWN and MODE to run it: the level climbs to the
highest, then descends to the minimum, **changing every 2 seconds**, then runs the **motor drag
cable test**. Press RESET to end and return to the MOTOR TEST submenu.

**MANUAL**, the manual motor test. The window shows "TEST"; press MODE to enter. The DISTANCE window
shows **XX, the motor COUNTER value**, and the level window shows **L1 to L16**. UP raises the segment
number to 16, DOWN lowers it to 1, and RESET finishes and returns to the MANUAL submenu.

**Sixteen levels, on every one of these books.** The MOTOR TEST counts L01 to L16 and the MANUAL test
1 to 16, which matches the console's 1-16 LEVEL window (`crw800-2024-console-window-functions`).

**Four documents, one menu.** The CRW800 (2020) service manual says "press UP and DOWN key for 3
seconds"; the CRW800-2016, XRW600-2019 and the CRW800-2024 owner's manual say "long press". The
2016 and XRW600 books misprint the last word as "MMNUAL submenu" and print "select OK OK" in the
UNITS step; nothing behind the words differs. **The CRW800-2021 and XRW600 owner's manuals print no
engineering mode at all** - only the 2024 CRW800 owner's manual carries it, on its p. 28.

**The Sole SR500-2016 rower prints this menu word for word** in its own service manual, FUN and all
(`sr500-2016-maintenance-menu`). Same Dyaco console, different brand; that card never covers a
Spirit machine and this one never covers a Sole.

**This is not the water rowers' menu.** The CRW900 and CRW800H2O open theirs on **Reset and Enter for
two seconds** and hold only Sound and ODO (`spirit-water-rower-console-engineering-mode-sound-and-odo`);
the CRW900 also has a separate VR setting routine on Enter, Up and Down
(`crw900-2021-errors-vr-setting-for-trouble-with-resistance`). **Nor is it the steppers' menu**, which
opens on Start, Stop and Enter held five seconds
(`spirit-stepper-console-maintenance-menu-sleep-mode-default-off-and-a-cross-reference-to-the-wrong-page`).


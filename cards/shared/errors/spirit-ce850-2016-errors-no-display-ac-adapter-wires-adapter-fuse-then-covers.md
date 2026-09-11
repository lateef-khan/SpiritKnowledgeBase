---
id: spirit-ce850-2016-errors-no-display-ac-adapter-wires-adapter-fuse-then-covers
title: 'No display: seat the AC adapter, check the console wires, check the adapter
  fuse, then open the covers and look for a wrong or broken wire'
kind: troubleshooting
question: What do I check when the console shows nothing on a Spirit CE850-2016, XE895-2016,
  XE395-2016 or XE395ENT-2021 elliptical?
asked_as:
- elliptical console is dead
- no display on my spirit ce850
- xe395 screen wont come on
- elliptical wont power up what to check
keywords:
- no display
- no power
- console dead
- ac adapter
- adapter fuse
- wires
- chain covers
- console problem
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  section: errors
  code: no-display
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers
see_also:
- spirit-lcd-dim-or-incomplete
- e95s-2016-no-display
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual 9-1 Console Problem, PDF p. 59-60,
    text.md lines 1035-1059; XE895 2016 (XE895-SE022) service manual 9-1 Console Problem,
    PDF p. 60-61, text.md lines 1035-1059; XE395 2016 (XE539S-SE019-01) service manual
    9-1 Console Problem, PDF p. 60-61, text.md lines 1033-1068; XE395ENT 2021 (XE539S-SE025-01)
    service manual 9-1 Console Problem, PDF p. 49-50, text.md lines 715-749
  extracted_at: '2026-09-11'
---

Section `9-1 Console Problem`, four steps in the order printed:

1. Under normal use the console screen will display. If there is no display, first check the **AC adapter** to make sure it is in the correct position.
2. Next, check if all the wires are inserted firmly and securely on to the console.
3. Then remove the **AC adapter fuse** to check for damage; replace if damaged.
4. Remove the console cover and the left and right chain covers, check if all the wires are inserted in the correct positions and check whether the wires are broken.

**No voltage is measured anywhere in the four steps** - the book asks for the adapter to be seated, the fuse to be looked at and the wires to be traced, and names no part beyond a damaged fuse. The fuse itself is a **5A** on the motor controller on these four books (`Fuse replacement`, the page before the matrix); the CE850 (2020) prints a 10A there.

**Four service manuals print these four steps word for word** - the CE850 2016 (XE898-SE011), its residential twin the XE895 2016, the XE395 2016 and the XE395ENT 2021. **The XE195 2016 and XE295 2016 print a different list** with no fuse step and a connector check on the controller and harness instead: `spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers`. The XE795 2016, XE795 2023, XG400 2016 and the CE machines print no console-problem section at all - their answer to a dim or dark display is the matrix's display row (`spirit-lcd-dim-or-incomplete`, `ce900-2025-errors-leds-not-bright-incomplete-or-imperfect`).

If the display lights but shows `E1`, `--`, `E3`, `Err` or `E2`, the fault has a code and its own card. Sole's E95S 2016 prints these same four steps (`e95s-2016-no-display`); Spirit's 2016 residential bikes check the computer cable and meter each contact instead (`spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter`). Different machines; separate cards.

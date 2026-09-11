---
id: spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers
title: 'No display: seat the power adaptor, check every connector in the console,
  on the controller and on the harness, then open the covers and look for a wrong
  or broken wire'
kind: troubleshooting
question: What do I check when the console shows nothing on a Spirit XE195-2016 or
  XE295-2016 elliptical?
asked_as:
- xe195 console is dead
- no display on my spirit xe295
- elliptical screen wont come on
- elliptical wont power up what to check
keywords:
- no display
- no power
- console dead
- power adaptor
- connectors
- controller
- wire harness
- console problem
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  section: errors
  code: no-display
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-errors-no-display-ac-adapter-wires-adapter-fuse-then-covers
see_also:
- spirit-lcd-dim-or-incomplete
- spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3
- spirit-elliptical-errors-eeprom-err-replace-upper-controller
source:
  ref: spirit-elliptical-xe195-2016-service-manual
  locator: XE195 2016 (XE509S-SE021-01) service manual 9-1 Console Problem, PDF p.
    44-45, text.md lines 691-719; XE295 2016 (XE519S-SE020-01) service manual 9-1
    Console Problem, PDF p. 44-45, text.md lines 692-726
  extracted_at: '2026-09-11'
---

Section `9-1 Console Problem`, as printed:

1. Display: When there is no display, check with the following procedures.
2. Make sure the **power adaptor** is properly inserted.
3. Check all connectors, including those in the console, on the controller and wire harness, are connected properly.
4. Next, check if all the wires are inserted firmly and securely on to the console.
5. Remove the console cover and the left and right chain covers, check if all the wires are inserted in the correct positions and check whether the wires are broken.

**No voltage is measured and no fuse is named** - unlike the CE850 2016 / XE395 2016 version of this section, which has an AC-adapter-fuse step in the middle (`spirit-ce850-2016-errors-no-display-ac-adapter-wires-adapter-fuse-then-covers`). These two books have no fuse page either.

**The XE195 2016 and XE295 2016 service manuals print these steps word for word.** The XE795 2016 and XG400 2016 print no console-problem section; their only answer to a dark display is the matrix row (`spirit-lcd-dim-or-incomplete`, `ce900-2025-errors-leds-not-bright-incomplete-or-imperfect`). The XE100-XE500 2007 dealer manual tests the adapter and harness with a meter instead (`spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3`).

If the display lights but shows `EEPROM ERR` or `--`, the fault has a code and its own card.

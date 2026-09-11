---
id: spirit-xe-errors-no-resistance-check-console-then-replace-the-gear-motor-cable
title: 'No resistance: check the console works first, then the gear motor cable, and
  replace the steel cable if it is worn or damaged'
kind: troubleshooting
question: Why is there no resistance on a Spirit CE850-2016, XE895-2016, XE295-2016,
  XE395-2016 or XE395ENT-2021 elliptical, and what does the service manual say to
  check?
asked_as:
- no resistance on my spirit elliptical
- elliptical pedals spin free no tension
- gear motor cable elliptical
- xe395 resistance not working
keywords:
- no resistance
- gear motor
- steel cable
- tension cable
- console
- flywheel
- magnetic brake
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe295-2016
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ce800ent-no-resistance
- xg400-2016-errors-no-resistance-gear-motor-magnet-or-steel-cable
- xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable
see_also:
- spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move
- xe395ent-2021-errors-e2-tension-motor-does-not-move
- xg400-2016-errors-no-resistance-gear-motor-magnet-or-steel-cable
- e95s-2016-no-resistance-gear-motor
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual 9-4 Controller, Incline Motor,
    Tension Motor Problem item 4 and 9-5 Flywheel & Poly-V Belt Problem item 1, PDF
    p. 63-64, text.md lines 1092-1133; XE895 2016 (XE895-SE022) service manual 9-4
    Controller, Incline Motor, Tension Motor Problem item 4 and 9-5 Flywheel & Poly-V
    Belt Problem item 1, PDF p. 64-65, text.md lines 1092-1133; XE295 2016 (XE519S-SE020-01)
    service manual 9-7 Gear Motor Problem, PDF p. 51, text.md lines 808-816; XE395
    2016 (XE539S-SE019-01) service manual 9-8 Gear Motor Problem, PDF p. 69, text.md
    lines 1174-1182; XE395ENT 2021 (XE539S-SE025-01) service manual 9-8 Gear Motor
    Problem, PDF p. 58, text.md lines 855-863
  extracted_at: '2026-09-11'
---

As printed, under `Gear Motor Problem` (XE295 2016, XE395 2016, XE395ENT 2021) or as item 4 of `Controller, Incline Motor, Tension Motor Problem` (CE850 2016, XE895 2016):

> If there is no resistance, first check to see if console is functioning normally. Next check the Gear Motor cable, if worn or damaged remove the Steel Cable. Use Phillips screw driver to remove the Tapping Screw w 5x19 securing the Gear Motor cable and replace cable with new.

So the order is **console first, cable second**, and the only part the paragraph names is the cable. The gear motor is the tension motor; its coded fault - the motor does not move when Level is pressed - is `--` on the 2016 books and `E2` on the ENT (`spirit-elliptical-2016-errors-dashes-tension-motor-does-not-move`, `xe395ent-2021-errors-e2-tension-motor-does-not-move`), with a drive-board voltage test that this paragraph does not repeat.

**The CE850 2016 and XE895 2016 add a second sentence on the next page**, under `Flywheel & Poly-V Belt Problem`: *When the user uses the console to adjust the resistance, but it doesn't work and the gear motor is working, check the steel cable if it works with the flywheel or it is loose.* That is the case where the motor runs and nothing changes - the cable between the gear motor and the magnet carrier is slack or off.

**Five service manuals print the paragraph word for word.** The XE195 2016 and XG400 2016 do not; the XG400 answers the same symptom with its own three-line row - gear motor, magnet position, broken steel cable (`xg400-2016-errors-no-resistance-gear-motor-magnet-or-steel-cable`). The generator-brake CE800 books replace a control board instead (`ce800ent-no-resistance`), and the XE795 2016 watches the driver board's CN2 output (`xe795-2016-errors-resistance-does-not-change-driver-board-cn2-and-8-pin-cable`). Sole files the same paragraph for its E95S under maintenance (`e95s-2016-no-resistance-gear-motor`).

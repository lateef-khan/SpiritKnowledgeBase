---
id: spirit-xe-errors-incline-motor-not-functioning-check-wires-controller-and-power-adaptor
title: 'The incline motor does not run: check every wire, then the incline controller
  and the power adaptor, and replace what is damaged'
kind: troubleshooting
question: What do I check when the incline or stride motor does not work on a Spirit
  CE850-2016, XE895-2016, XE395-2016 or XE395ENT-2021 elliptical?
asked_as:
- incline motor not working on my spirit elliptical
- stride motor wont move ce850
- xe395 incline dead what to check
- elliptical incline controller check
keywords:
- incline motor
- stride motor
- incline controller
- power adaptor
- wires
- not functioning
- reset
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
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-xe-2007-errors-incline-does-not-work-check-the-incline-wires-and-controller
see_also:
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
- xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max
- xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- xe395-2016-errors-err-incline-vr-out-of-range-or-not-read
- xe395ent-2021-errors-e3-incline-vr-out-of-range-or-not-read
- e95s-2019-stride-motor-not-working
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: CE850 2016 (XE898-SE011) service manual 9-4 Controller, Incline Motor,
    Tension Motor Problem items 1-3, PDF p. 63, text.md lines 1092-1110; XE895 2016
    (XE895-SE022) service manual 9-4 Controller, Incline Motor, Tension Motor Problem
    items 1-3, PDF p. 64, text.md lines 1092-1110; XE395 2016 (XE539S-SE019-01) service
    manual 9-7 Controller & Incline Motor Problem, PDF p. 68, text.md lines 1160-1174;
    XE395ENT 2021 (XE539S-SE025-01) service manual 9-7 Controller & Incline Motor
    Problem, PDF p. 57, text.md lines 841-855
  extracted_at: '2026-09-11'
---

As printed, under `Controller & Incline Motor Problem` (XE395 2016, XE395ENT 2021) or `Controller, Incline Motor, Tension Motor Problem` (CE850 2016, XE895 2016):

> When incline motor is not functioning, check all the wire for secure connection, check incline controller and power adaptor is damaged or broken. Replace damaged or broken parts.

The CE850 2016 and XE895 2016 put a warning first - *Incline motor, controller and gear motor are all electronic components. Please do not disassemble it if you are unfamiliar with these parts* - and their "incline motor" is the **stride** motor; the word *stride* does not appear on that page, though it is the only motor of that kind on the machine.

**The paragraph names no measurement.** The measured version of the same check - relays, mains voltage at the motor, 5 VDC at the potentiometer - is the nine-step test in the error chapter of each book: `spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`, `xe395-2016-errors-incline-motor-and-position-sensor-test-120-vac-15-max`, `xe395ent-2021-errors-incline-motor-and-position-sensor-test-115-vac-20-max`. The coded form of the fault is `E3` / `Err` / `E3` on the three families.

**Each book then prints the reset figure for a replacement motor, and the two families differ.** CE850 2016 / XE895 2016: *turn the tubing clockwise to the end, then counterclockwise two and half circles, or let the center between two holes be 245 ±1 mm.* XE395 2016 / XE395ENT 2021: *rotate the incline barrel clockwise to the end and then counterclockwise one and a half circle; make sure the distance of two hole sites is 204±1mm.* Two and a half turns and 245 mm on the stride machines, one and a half turns and 204 mm on the incline machines - do not carry one to the other. The replacement procedure those figures belong to is the assembly chapter's.

**Four service manuals print this paragraph.** The XE195, XE295, XE795 and XG400 2016 have no powered incline or stride and print nothing like it. The XE100-XE500 2007 dealer manual's incline row is its own (`spirit-xe-2007-errors-incline-does-not-work-check-the-incline-wires-and-controller`), and Sole files the E95S version under maintenance (`e95s-2019-stride-motor-not-working`).

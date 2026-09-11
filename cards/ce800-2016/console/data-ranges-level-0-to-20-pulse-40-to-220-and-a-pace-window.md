---
id: ce800-2016-console-data-ranges-level-0-to-20-pulse-40-to-220-and-a-pace-window
title: 'Display and work ranges for each console reading on the 2016 elliptical: speed
  to 99.9, level 0 to 20, pulse 40 to 220 BPM, and a pace window'
kind: spec
question: What are the display ranges for speed, level, time and pulse on a Spirit
  ce800-2016 elliptical?
asked_as:
- how many resistance levels does the 2016 ce800 have
- what is the highest pulse the ce800 console shows
- what is pace on the spirit ce800 console
- how long can i set the countdown timer on the ce800
keywords:
- display range
- work range
- level 0 to 20
- pulse 40 to 220
- pace
- laps
- countdown
- calories
- speed
- spec
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2016
  applies_to:
  - ce800-2016
  section: console
  code: '*'
  model_number:
  - '800045'
authority: 3
not_to_be_confused_with:
- cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- spirit-ce850-2016-console-data-ranges-stride-18-to-24-and-level-1-to-20
see_also:
- ce800-2016-console-software-modes-idle-child-lock-pause-end-and-reset
- ce800-2016-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan
- cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- spirit-ce-console-quick-start-time-counts-up
- spirit-ce-specs-forty-resistance-levels
source:
  ref: spirit-elliptical-ce800-2016-service-manual
  locator: Section 4 XE890B Electrical Operation, Function, PDF pp. 15-16 (printed
    15-16); text.md lines 264-312
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in Kilometer mile per hour" - both units in one line |
| LEVEL | 0 to 999 | **0 to 20** | printed as "the incline position from 0 to 20"; preset 0 to 20; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| PACE | 00:00 to 99:99 | 00:00 to 99:99 | "Time to finish 1KM/MILE workout" |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in kilometres or miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; "if the treadmill doesn't have a signal for 8 seconds" the value becomes 0 |

**"Incline" and "treadmill" are the spec's words**, not this machine's: this is a treadmill software
specification reused for the elliptical
(`ce800-2016-console-software-modes-idle-child-lock-pause-end-and-reset`). The LEVEL row is the
resistance level; the CE800 has no powered incline.

**Zero to twenty here, and the same table on the CU800-2012 bike**
(`cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220`). The 2013 owner's manual for
the CE800 describes forty resistance levels in Quick Start (`spirit-ce-console-quick-start-time-counts-up`,
`spirit-ce-specs-forty-resistance-levels`); this table's twenty is the software spec's figure and
nothing in the book reconciles the two.

**A PACE window is a reading the LED-window CE800 of 2021 does not have**; its data windows show
Distance, Calories, Pulse, Time and then Speed, Watts, METs, Time Remaining
(`spirit-ce-console-led-data-windows-scan`).

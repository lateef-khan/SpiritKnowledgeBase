---
id: spirit-ce850-2016-console-data-ranges-stride-18-to-24-and-level-1-to-20
title: Display and work ranges for each console reading, with a stride of 18 to 24
  in half steps and a level range of 1 to 20
kind: spec
question: What are the stride, level, time and pulse ranges on a Spirit CE850-2016
  or XE895-2016 elliptical?
asked_as:
- what stride lengths does the ce850 have
- how many resistance levels does the xe895 have
- what is the highest pulse the ce850 console shows
- how long can i set the countdown on the xe895
keywords:
- display range
- work range
- stride 18 to 24
- half steps
- level 1 to 20
- pulse 40 to 220
- laps
- countdown
- spec
- eight seconds
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe895-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- xe395-2016-console-data-ranges-incline-0-to-20-in-half-steps-and-level-0-to-20
- ce800-2016-console-data-ranges-level-0-to-20-pulse-40-to-220-and-a-pace-window
see_also:
- spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset
- spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan
- ce850-2020-console-stride-length-18-to-24-inches-buttons-on-the-left-swing-arm
- xe895-2018-specs-powered-stride-set-per-segment-with-no-length-printed
- spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850-2016 (XE898-SE011) section 4 Product Operation, Function, PDF pp.
    18-19 (printed 18-19); text.md lines 339-387. XE895-2016 (XE895-SE022) PDF pp.
    18-19, lines 333-383, word for word
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in mile per hour" |
| **Stride** | 0 to 99 | **18 to 24** | "the stride position from 18 to 24"; preset 18 to 24; UP or DOWN moves it by **0.5** |
| LEVEL | 0 to 99 | **1 to 20** | printed as "the stride position from 1 to 20"; preset 1 to 20; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**The stride row is what sets these two books apart** from every other 2016 elliptical spec: a
powered stride motor set between 18 and 24, in half steps. The LEVEL row's description is a
copy-and-paste ("the stride position from 1 to 20"); the level is the resistance.

**The key table calls the same control incline and gives it a range of 0 to 20**
(`spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan`),
and the E3 troubleshooting pages say the STRIDE window counts "20 for max stride, 0 for lowest".
Three ranges for one motor in one book; the 18 to 24 here is the only one that matches the 18- to
24-inch stride the CE850-2020 owner's-style text describes
(`ce850-2020-console-stride-length-18-to-24-inches-buttons-on-the-left-swing-arm`).

**The XE895-2018 owner's manual prints no stride length at all**
(`xe895-2018-specs-powered-stride-set-per-segment-with-no-length-printed`); this 2016 service book
is the only XE895 document that gives one, and it gives it as a console range, not in inches.

**One to twenty here; zero to twenty on the XE295, XE795 and XG400 of 2016**
(`spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220`).

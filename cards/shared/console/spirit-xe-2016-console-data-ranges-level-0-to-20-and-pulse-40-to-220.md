---
id: spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
title: Display and work ranges for each console reading, with a level work range of
  0 to 20
kind: spec
question: What are the display ranges for speed, level, time and pulse on a Spirit
  XE295, XE795 or XG400 2016 elliptical?
asked_as:
- how many resistance levels does the xe795 have
- what is the highest pulse the xg400 console shows
- how long can i set the countdown on the xe295
- is there a level zero on the xe795
keywords:
- display range
- work range
- level 0 to 20
- pulse 40 to 220
- laps
- countdown
- calories
- speed
- spec
- eight seconds
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe295-2016
  - xe795-2016
  - xg400-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- xe195-2016-console-data-ranges-level-1-to-20-and-pulse-40-to-220
- spirit-ce850-2016-console-data-ranges-stride-18-to-24-and-level-1-to-20
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
see_also:
- xe195-2016-console-data-ranges-level-1-to-20-and-pulse-40-to-220
- xe395-2016-console-data-ranges-incline-0-to-20-in-half-steps-and-level-0-to-20
- spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-xe-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
- spirit-xe795-console-quick-start-with-forty-resistance-levels
- spirit-xe-console-quick-start-with-twenty-resistance-levels
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
source:
  ref: spirit-elliptical-xe295-2016-service-manual
  locator: XE295-2016 section 4 Elliptical Operation, Function, PDF pp. 18-19 (printed
    18-19); text.md lines 285-327. XG400-2016 PDF pp. 16-17, lines 226-268, word for
    word. XE795-2016 PDF pp. 18-19, lines 284-327, with the two figures named in the
    body
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in mile per hour" |
| LEVEL | 0 to 99 | **0 to 20** | "the level position from 0 to 20"; preset **1 to 20**; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**The XE795-2016 prints two figures differently in the LEVEL row**: a display range of **0 to 999**
and a preset of **0 to 20**, where the XE295 and XG400 print 0 to 99 and 1 to 20. The work range is
0 to 20 in all three.

**Zero to twenty here; one to twenty on the XE195-2016**
(`xe195-2016-console-data-ranges-level-1-to-20-and-pulse-40-to-220`). The software-spec chapter of
all three books says Quick Start starts resistance "from 1"
(`spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset`), so
whether a level 0 exists on the machine is not settled by the books.

**Twenty levels is a finding for the XE795.** Every XE795 owner's manual, 2018 to 2023, describes
**forty** resistance levels in Quick Start (`spirit-xe795-console-quick-start-with-forty-resistance-levels`);
this 2016 service book's table counts to 20, and nothing in it mentions 40. For the XE295 and XG400
the twenty agrees with their owner's manuals
(`spirit-xe-console-quick-start-with-twenty-resistance-levels`); the ranges, the 8-second pulse
drop-out and the count-down limits are printed only here.

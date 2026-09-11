---
id: xe395-2016-console-data-ranges-incline-0-to-20-in-half-steps-and-level-0-to-20
title: Display and work ranges for each console reading, with an incline of 0 to 20
  in half steps beside a level of 0 to 20
kind: spec
question: What are the incline, level, time and pulse ranges on a Spirit xe395-2016
  elliptical?
asked_as:
- how high does the incline go on the xe395
- does the xe395 incline move in half steps
- how many resistance levels does the xe395 have
- what is the highest pulse the xe395 console shows
keywords:
- display range
- work range
- incline 0 to 20
- half steps
- level 0 to 20
- pulse 40 to 220
- laps
- countdown
- spec
- eight seconds
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395-2016
  applies_to:
  - xe395-2016
  section: console
  code: '*'
  model_number:
  - '395015'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- spirit-ce850-2016-console-data-ranges-stride-18-to-24-and-level-1-to-20
see_also:
- spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan
- xe395-2016-console-incline-calibration-stop-level-and-start-held-five-seconds
- spirit-xe395-console-muscle-figure-bands-by-incline-level
- spirit-xe-2016-console-lcd-layout-calories-time-distance-incline-level-and-a-ten-character-message-window
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: Section 4 Product Operation, Function, PDF pp. 18-19 (printed 18-19); text.md
    lines 328-375
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in mile per hour" |
| **Incline** | 0 to 99.9 | **0 to 20** | "the incline position from 0 to 20"; preset 0 to 20; UP or DOWN moves it by **0.5** |
| LEVEL | 0 to 99 | **0 to 20** | "the level position from 0 to 20"; preset 0 to 20; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**The incline row is what sets this book apart** from the XE195, XE295, XE795 and XG400 of the same
year, which print no incline range (`spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220`).
The key table agrees - Incline Up and Down move 0.5, maximum 20, minimum 0
(`spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan`) -
and the message-window scan adds `ALT` and `MAX INC` for it.

**The E3 test procedure in the same book says 15.** Its step 5 reads "The INCLINE window will
display the computer incline setting (after speed cal. ends); **15 for max incline**, 0 for lowest
incline" - a treadmill sentence pasted in; the 2021 XE395ENT book prints the same sentence with 20.
The 0-to-20 range here and in the key table is the one that fits the machine; the 15 is held with
the error cards as a contradiction, not a spec.

**The 2018 owner's manual describes the ramp's muscle bands over 0-7.5 and 8-20**
(`spirit-xe395-console-muscle-figure-bands-by-incline-level`), which agrees with a 20 maximum. The
incline is calibrated by a key hold
(`xe395-2016-console-incline-calibration-stop-level-and-start-held-five-seconds`).

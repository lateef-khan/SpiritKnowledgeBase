---
id: sc200-2016-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the display ranges for the console readings on a Sole sc200-2016
  climber?
asked_as:
- how many resistance levels does the sole sc200 have
- what does spm mean on my sole climber
- what heart rate range does the console read
keywords:
- display range
- work range
- spm
- vertical
- level 20
- calories
- pulse
- bpm
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2016
  applies_to:
  - sc200-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2016-console-buttons
source:
  ref: sole-elliptical-sc200-2016-service-manual
  locator: Function, pages 18-19
  extracted_at: '2026-09-04'
---

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| SPM | 0 to 888 | 0~120 | the manual describes it as "the current speed in mile per hour" |
| LEVEL | 0 to 99 | 1 to 20 | preset value 1 to 20, each press changes by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count down setup range 10:00 to 99:00; when TIME is set the count goes to zero |
| VERTICAL | 00000 to 99999 | 0 to 99999 | the manual describes it as "the current vertical in Mile" |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | 40 to 220 BPM | hand pulse or chest belt receiver |

In RUN mode, if there is no pulse signal for **8 seconds** the displayed value becomes 0. The source writes that sentence about "the bike".

**Two unit definitions in this table look wrong and are reproduced exactly as printed.** SPM is defined as "the current speed in mile per hour" on a machine where SPM normally means steps per minute, and VERTICAL is defined as "the current vertical in Mile" with a range of 0 to 99999. Treat both units as unconfirmed.

There is no incline, stride, speed in mph, distance or laps reading on this console.

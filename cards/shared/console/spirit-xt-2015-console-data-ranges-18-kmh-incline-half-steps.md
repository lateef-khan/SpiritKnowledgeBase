---
id: spirit-xt-2015-console-data-ranges-18-kmh-incline-half-steps
title: 'Display and work ranges: 1.0 to 18.0 km/h (0.5 to 12.0 mph), incline 0.0 to
  15.0 in 0.5 steps, pulse 50 to 200 BPM'
kind: spec
question: What are the speed, incline and pulse ranges on a Spirit XT385-2015 or XT485-2015
  treadmill console?
asked_as:
- what is the top speed of my treadmill
- how many incline levels does the treadmill have
- what heart rate range does the console read
- why does the pulse show dashes
keywords:
- display range
- work range
- speed
- incline
- laps
- distance
- calories
- pulse
- bpm
- dashes
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt385-2015
  - xt485-2015
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-2015-console-data-ranges-16-kmh-incline-steps-of-1
- spirit-xt-2023-console-data-ranges-20-kmh-incline-15
see_also:
- spirit-xt-2015-console-keys-with-enter-cycling-altitude
- ct850-2016-window-display-modes
- xt-2015-console-calibration-fast-plus
source:
  ref: spirit-treadmill-xt485-2015-service-manual
  locator: XT485-2015 section 4 Product Operation, Function, PDF pp. 16-17 (printed
    16-17); text.md lines 232-289. The XT385-2015 service manual prints the same table
    on its PDF pp. 16-17, text.md lines 231-288
  extracted_at: '2026-09-11'
---

**These two consoles work between 1.0 and 18.0 km/h (0.5 to 12.0 mph) and step the incline by 0.5.**
The XT185-2015 and XT285-2015 stop at 16.0 km/h and step the incline by 1
(`spirit-xt-2015-console-data-ranges-16-kmh-incline-steps-of-1`); the 2023 XT385 and XT485 reach
20.0 km/h (`spirit-xt-2023-console-data-ranges-20-kmh-incline-15`).

| Reading | Display range | Work range | Step / note |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | **1.0 to 18.0 km/h (0.5 to 12.0 mph)** | FAST / SLOW change it by 0.1 km/h (mph) |
| INCLINE | 0 to 99 | **0.0 to 15.0**; preset value 0 to 15.0 | UP / DOWN change it by **0.5** |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | Counts up by default; counts down if the user sets a time. Count-down setup range 10:00 to 99:00 |
| LAPS | 0 to 99 | 0 to 99 | Total working laps |
| DISTANCE | 0.00 to 99.99 | 0.00 to 99.99 | Kilometres or miles |
| CALORIES | 0.0 to 9999 | 0.0 to 9999 | Cumulative |
| PULSE | 0 to 999 | **50 to 200 BPM** | Hand pulse or receiver; a chest belt must be worn to use the receiver |

In RUN Mode, with **no pulse signal for 8 seconds** the displayed pulse becomes "- - -" (three dashes, not 0).

In RUN Mode, pressing STOP saves the time value; re-entering RUN Mode continues counting from it.

The service manual's own words for these figures are "DISPLAY range" (what the window can show) and
"WORK range" (what the machine will actually do). Quote the work range as the machine's limit.

**There is no PACE row in these two books.** The XT185-2015 and XT285-2015 tables have one.


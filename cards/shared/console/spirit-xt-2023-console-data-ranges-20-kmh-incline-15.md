---
id: spirit-xt-2023-console-data-ranges-20-kmh-incline-15
title: 'Display and work ranges: 1.0 to 20.0 km/h or 0.5 to 12.0 mph, incline 0 to
  15 in 0.5 steps, pulse 50 to 200 BPM'
kind: spec
question: What are the speed, incline and pulse ranges on a Spirit XT385-2023 or XT485-2023
  treadmill console?
asked_as:
- what is the top speed of my treadmill
- how many incline levels does the treadmill have
- what heart rate range does the console read
- how many laps does the counter go to
keywords:
- display range
- work range
- speed
- 20 km/h
- incline 15
- laps
- calories
- pulse
- bpm
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt385-2023
  - xt485-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- xt185-2023-console-data-ranges-16-kmh-10-mph
- xt285-2023-console-data-ranges-18-kmh-incline-12
- xt685-2023-console-data-ranges-12-mph-20-kph-spec
- spirit-xt-2015-console-data-ranges-18-kmh-incline-half-steps
- f80-2023-console-data-ranges
see_also:
- spirit-xt-2023-console-keys-in-ready-and-run-mode
- xt-2023-console-calibration-wheel-size-two-four-three
- ct850-2016-window-display-modes
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT485-2023 section 4 Product Operation, Function, PDF pp. 7-8 (printed
    7-8); text.md lines 106-156. The XT385-2023 service manual is the same text on
    the same pages and lines
  extracted_at: '2026-09-11'
---

**These two consoles work between 1.0 and 20.0 km/h (0.5 to 12.0 miles) and incline 0 to 15.**
The XT185-2023 stops at 10 mph (`xt185-2023-console-data-ranges-16-kmh-10-mph`), the XT285-2023 at
18.0 km/h and incline 12 (`xt285-2023-console-data-ranges-18-kmh-incline-12`), and the XT685-2023
prints the same figures with a note about a 20 kph specification
(`xt685-2023-console-data-ranges-12-mph-20-kph-spec`).

| Reading | Display range | Work range | Step / note |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | **1.0 to 20.0 km, or 0.5 to 12.0 miles** | FAST / SLOW change it by 0.1 km/h (mph) |
| INCLINE | 0 to 99 | **0 to 15**; preset value 0 to 15 | UP / DOWN change it by 0.5 |
| TIME | 00:00 to 99:99 | 00:00 to 99:59 | Counts up by default; counts down if the user sets a time. Count-down setup range 10:00 to 99:00 |
| LAPS | 0 to 999 | 0 to 999 | Total working laps |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.99 | Kilometres or miles |
| CALORIES | 0 to 9999 | 0 to 999 | Cumulative |
| PULSE | 0 to 999 | **50 to 200 BPM** | Hand pulse or receiver; a chest belt must be worn to use the receiver |

In RUN Mode, with **no pulse signal for 8 seconds** the displayed pulse becomes "0".

In RUN Mode, pressing STOP saves the time value; re-entering RUN Mode continues counting from it.

The service manual's own words for these figures are "DISPLAY range" (what the window can show) and
"WORK range" (what the machine will actually do). Quote the work range as the machine's limit.

**There is no PACE row in these two books**, although the 2023 XT185 and XT285 tables have one.

The calibration routine for these two machines sets the same limits - maximum 20.0 kmph (12.0 MPH)
and minimum 1.0 kmph (0.5 MPH): `xt-2023-console-calibration-wheel-size-two-four-three`.


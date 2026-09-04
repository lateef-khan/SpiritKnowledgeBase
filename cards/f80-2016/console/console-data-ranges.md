---
id: f80-2016-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the speed, incline and pulse ranges on a Sole f80-2016 treadmill
  console?
asked_as:
- what is the top speed of my treadmill
- how high does the incline go on a sole treadmill
- what heart rate range does the treadmill console read
keywords:
- display range
- work range
- top speed
- incline
- pulse
- bpm
- calories
- distance
- lcd
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2016
  applies_to:
  - f80-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2016-console-buttons-run-mode
- f80-2016-console-modes
source:
  ref: sole-tm-f80-2016-service-manual
  locator: Section 4, Operation - Function
  extracted_at: '2026-09-04'
---

The console has a **9" LCD display**.

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 1.0~18.0 kmph (0.5 ~ 12.0 mph) | FAST/SLOW change it by 0.1 km/h (mph) per press |
| INCLINE | 0 to 99 | 0 to 15 | position shown 0 to 15, preset value 0 to 15, UP/DOWN change it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count down setup range 10:00 to 99:00 |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 | kilometres or miles |
| CALORIES | 0.0 to 999 | 0.0 to 999 | cumulative for the workout |
| PULSE | 0 to 999 | 50 to 200 BPM | hand pulse or chest belt receiver |

TIME counts up by default; if the user sets a time it counts down and runs to zero.

In RUN mode, if the treadmill has no pulse signal for **8 seconds** the displayed value becomes 0.

**The manual gives two different maximum inclines.** The Function block above says the incline work range is 0 to 15 and the incline quick keys go to 15, but the RUN MODE description says "the maximum incline position is 12". The 2019 manual for the same machine says 15 in both places.

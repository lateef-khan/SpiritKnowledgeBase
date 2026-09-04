---
id: f85-2021-console-data-ranges
title: Display and working ranges for every console window
kind: spec
question: What are the speed, incline, time and pulse ranges on the Sole F85-2021
  console?
asked_as:
- how fast does the f85 ent treadmill go
- what is the top speed and incline
- pulse range on the treadmill display
keywords:
- speed range
- incline range
- top speed
- max incline
- pulse range
- calories
- distance
- display window
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2021
  applies_to:
  - f85-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2021-console-modes-and-buttons
- f85-2021-quick-keys
- f85-2021-calibration-procedure
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: section 4 Operation, Function, printed pages 17 to 18
  extracted_at: '2026-09-04'
---

| Window | Display range | Working range | Step |
|---|---|---|---|
| SPEED | 1.0 to 22.0 km max, or 0.5 to 12.0 max in miles | 1.0 to 22.0 km/h (0.5 to 12.0 mph) | 0.1 km/h or mph |
| INCLINE | printed as "0" only | 0 to 15 (preset value 0 to 15) | 1 |
| TIME | 00:00 to 99:99 | 00:00 to 99:59 | count down setup 10:00 to 99:00 |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 | |
| CALORIES | 0 to 999 | 0 to 999 | |
| PULSE | 0 to 999 | 50 to 200 BPM | |

- TIME counts up by default. Setting a time makes it count down, and it counts to zero.
- In RUN mode, pressing STOP saves the time value; entering RUN mode again continues counting up from it.
- PULSE reads from the hand grips or from a receiver. Using the receiver needs a chest belt. If no signal arrives for **8 seconds** the window falls back to 0.
- The RUN mode page agrees on the incline limit: the UP button raises the incline to a maximum position of **15**.

**Two gaps in this page.** The INCLINE display range is printed as "DISPLAY range is 0." with nothing after it, so the upper figure is missing from the source. And this page lists **no LAPS window** at all, while the 2016 and 2019 manuals for the neighbouring builds both give LAPS a display and working range of 0 to 99.

The calibration screen enforces the same speed limits: English max 12.0 and min 0.5, metric max 22.0 and min 1.0.

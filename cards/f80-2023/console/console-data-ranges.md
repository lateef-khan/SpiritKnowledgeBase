---
id: f80-2023-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the speed, incline and pulse ranges on a Sole f80-2023 treadmill
  console?
asked_as:
- what is the top speed of this treadmill
- what is the max incline on my treadmill
- what heart rate range does the console read
keywords:
- display range
- work range
- speed
- incline
- time
- distance
- calories
- pulse
- bpm
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2023
  applies_to:
  - f80-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2023-console-buttons-ready-mode
- f80-2023-console-modes
source:
  ref: sole-tm-f80-2023-service-manual
  locator: Section 4.2 Display Function, pages 7-8
  extracted_at: '2026-09-04'
---

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| SPEED | 1.0 to 20.0 km MAX, or 0.5 to 12.0 for MILE | 1.0~20.0 km/h (0.5~12.0 mph) | each FAST or SLOW press changes it by 0.1 km/h (mph) |
| INCLINE | 0 | 0 to 15 | position shown 0 to 15, preset value 0 to 15, each press changes by 1 |
| TIME | 0:00:00 to 9:99:99 | 00:00 to 9:99:59 | COUNT UP by default; setting a time makes it COUNT DOWN, setup range 10:00 to 99:00 |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 | kilometres or miles |
| CALORIES | 0 to 999 | 0 to 999 | cumulative |
| PULSE | 0 to 999 | 50 to 200 BPM | hand pulse, or a receiver with a chest belt worn |

In RUN Mode, if the treadmill has **no pulse signal for 8 seconds** the displayed value becomes 0.

In RUN Mode, pressing STOP saves the time value; re-entering RUN Mode continues counting from it.

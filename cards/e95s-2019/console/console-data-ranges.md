---
id: e95s-2019-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the display ranges for speed, stride, level and pulse on a Sole
  e95s-2019 elliptical?
asked_as:
- how many stride positions does the sole e95s have
- how many resistance levels does the elliptical have
- what heart rate range does the console read
keywords:
- display range
- work range
- stride 20
- level 20
- speed
- calories
- pulse
- bpm
facets:
  brand:
  - sole
  product_line: elliptical
  model: e95s-2019
  applies_to:
  - e95s-2019
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e95s-2019-console-buttons
- e95s-2019-console-modes
source:
  ref: sole-elliptical-e95s-2019-service-manual
  locator: Function, pages 18-19
  extracted_at: '2026-09-04'
---

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | miles per hour |
| STRIDE | 0 to 99 | 1 to 20 | position shown 1 to 20, preset value 1 to 20, each press changes by 1 |
| LEVEL | 0 to 99 | 1 to 20 | position shown 1 to 20, preset value 1 to 20, each press changes by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count down setup range 10:00 to 99:00 |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | 40 to 220 BPM | hand pulse or chest belt receiver |

This machine adjusts **stride**, not incline. The LEVEL entry in the source is printed as "Display the stride position from 1 to 20" and its UP/DOWN line says "adjust stride"; those two lines are copied from the STRIDE entry above them. Level is the resistance level.

In RUN mode, if the elliptical has no pulse signal for **8 seconds** the displayed value becomes 0.

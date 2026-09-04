---
id: e25-2023-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the display ranges for rpm, incline, level and pulse on a Sole
  e25-2023 elliptical?
asked_as:
- what is the max incline on a sole e25
- how many resistance levels does the elliptical have
- what heart rate range does the console read
keywords:
- display range
- work range
- incline 15
- level 20
- rpm
- calories
- pulse
- bpm
facets:
  brand:
  - sole
  product_line: elliptical
  model: e25-2023
  applies_to:
  - e25-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- e25-2023-console-buttons
source:
  ref: sole-elliptical-e25-2023-service-manual
  locator: Function, pages 7-8
  extracted_at: '2026-09-04'
---

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| RPM | 0 to 888 | 0~120 | see the note below on the units |
| LEVEL | 0 to 99 | 1 to 20 | each press of LEVEL UP or DOWN changes it by 1 |
| INCLINE | 0 to 99 | **1 to 15** | each press of INCLINE UP or DOWN changes it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default; count down setup range 10:00 to 99:00 |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 | kilometres or miles |
| CALORIES | 0 to 999 | 0 to 999 | cumulative |
| PULSE | 0 to 999 | 40 to 220 BPM | hand pulse or chest belt receiver |

If there is no pulse signal for **8 seconds** the displayed value becomes 0.

**Two printing errors in this table, left as printed.** The row is headed RPM but its text reads "Display the current speed in mile per hour". And the pulse row says "if the **treadmill** doesn't have a signal for 8 seconds" in an elliptical manual.

The incline work range here is **1 to 15**. The 2019 E25 manual prints 0 to 20 for the same reading. They are different machines; do not carry the figure across.

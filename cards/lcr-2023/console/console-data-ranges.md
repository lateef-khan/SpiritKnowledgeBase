---
id: lcr-2023-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the display ranges for speed, level, time and pulse on a Sole LCR-2023
  bike?
asked_as:
- how many resistance levels does the 2023 lcr have
- what heart rate range does the lcr console read
- what is the max time on the light commercial recumbent console
keywords:
- display range
- work range
- speed
- level 40
- time
- distance
- calories
- pulse
- bpm
facets:
  brand:
  - sole
  product_line: bike
  model: lcr-2023
  applies_to:
  - lcr-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- lcr-2023-console-buttons
- sole-bike-tft-console-data-ranges
source:
  ref: sole-bike-lcr-2023-service-manual
  locator: Section 4 Product Operation, Function, pages 9-10
  extracted_at: '2026-09-04'
---

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0 to 99.9 | In miles per hour. |
| LEVEL | 0 to 999 | 1 to 40 | Position 1 to 40, preset 1 to 40. Each UP or DOWN press changes it by 1. |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | Counts up unless the user sets a time, then it counts down. Count-down setup range 10:00 to 99:00. |
| LAPS | 0 to 99 | 0 to 99 | Total working laps. |
| DISTANCE | 0.0 to 99.9 | 0.0 to 99.9 | In kilometres or miles. |
| CALORIES | 0 to 999 | 0 to 999 | Cumulative. |
| PULSE | 0 to 999 | 40 to 220 BPM | Hand pulse or receiver. A chest belt must be worn to use the receiver. |

In exercise mode, with no pulse signal for **8 seconds** the displayed value becomes 0.

**The pulse row is mislabelled.** It reads "if the treadmill doesn't have a signal", in a bike manual.

This machine has **40 resistance levels**. The B94 and R92 bikes have 20.

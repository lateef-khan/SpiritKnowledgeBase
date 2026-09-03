---
id: sole-bike-tft-console-data-ranges
title: "Display value ranges on the ten-inch touchscreen bikes"
kind: spec
question: "What are the display value ranges on a Sole LCB-2016, LCB-2019 or LCR-2016?"
asked_as:
- "how many resistance levels does the lcb have"
- "what is the max time on the light commercial bike console"
- "what pulse range does the bike show"
keywords:
- "resistance levels"
- "speed range"
- "time range"
- "distance"
- "calories"
- "pulse"
- "laps"
- "tft display"
- "bike"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - lcb-2016
  - lcb-2019
  - lcr-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-tft-console-modes
source:
  ref: sole-bike-lcb-2016-service-manual
  locator: "Section 4, Function (same section in the LCB 2016, LCB 2019 and LCR 2016 manuals)"
  extracted_at: '2026-09-03'
---

These bikes use a **10.1" TFT display**.

| Value | Display range | Working range | Note |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0 to 99.9 | In miles per hour. |
| LEVEL | 0 to 999 | 1 to 40 | Preset 1 to 40. Each UP or DOWN press changes it by 1. |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | Count up unless the user sets a time, then it counts down. Count-down setup range is 10:00 to 99:00. |
| LAPS | 0 to 99 | 0 to 99 | |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | In miles. |
| CALORIES | 00.0 to 999 | 00.0 to 999 | Cumulative. |
| PULSE | 0 to 999 | 40 to 220 BPM | Hand pulse or receiver. With no signal for 8 seconds in run mode the value goes to 0. |

These bikes have **40 resistance levels**. The nine-inch display bikes have 20.

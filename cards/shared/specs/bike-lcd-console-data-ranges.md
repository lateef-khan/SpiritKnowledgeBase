---
id: sole-bike-lcd-console-data-ranges
title: "Display value ranges on the nine-inch display bikes"
kind: spec
question: "What are the display value ranges on a Sole B94-2016, B94-2019 or R92-2016?"
asked_as:
- "how many resistance levels does my sole bike have"
- "what is the max time on the bike console"
- "what pulse range does the bike show"
keywords:
- "resistance levels"
- "rpm range"
- "time range"
- "distance"
- "calories"
- "pulse"
- "laps"
- "9 inch lcd"
- "bike"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - b94-2016
  - b94-2019
  - r92-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-lcd-console-modes
source:
  ref: sole-bike-b94-2016-service-manual
  locator: "Section 4, Function (same section in the B94 2016, B94 2019 and R92 2016 manuals)"
  extracted_at: '2026-09-03'
---

These bikes use a **9" LCD display**.

| Value | Display range | Working range | Note |
|---|---|---|---|
| RPM | 0 to 888 | 0 to 120 | |
| LEVEL | 0 to 99 | 1 to 20 | Preset 1 to 20. Each UP or DOWN press changes it by 1. |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | Count up unless the user sets a time, then it counts down. Count-down setup range is 10:00 to 99:00. |
| LAPS | 0 to 99 | 0 to 99 | |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | In miles. |
| CALORIES | 00.0 to 999 | 00.0 to 999 | Cumulative. |
| PULSE | 0 to 999 | 40 to 220 BPM | Hand pulse or receiver. With no signal for 8 seconds in run mode the value goes to 0. |

The manuals label the RPM entry "Display the current speed in mile per hour", which contradicts the RPM name and the 0 to 120 working range. Read the field as cadence in RPM.

---
id: b94-2023-console-data-ranges
title: Display and work ranges for each console reading
kind: spec
question: What are the display ranges for RPM, level, time and pulse on a Sole B94-2023
  bike?
asked_as:
- how many resistance levels does the 2023 b94 have
- what heart rate range does the bike console read
- what is the max time on the b94 console
keywords:
- display range
- work range
- rpm
- level 20
- time
- distance
- calories
- pulse
- bpm
facets:
  brand:
  - sole
  product_line: bike
  model: b94-2023
  applies_to:
  - b94-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- b94-2023-console-buttons
- sole-bike-lcd-console-data-ranges
source:
  ref: sole-bike-b94-2023-service-manual
  locator: Section 4 Product Operation, Function, pages 7-8
  extracted_at: '2026-09-04'
---

| Reading | Display range | Work range | Notes |
|---|---|---|---|
| RPM | 0 to 888 | 0 to 120 | |
| LEVEL | 0 to 99 | 1 to 20 | Each UP or DOWN press changes it by 1. |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | Counts up unless the user sets a time, then it counts down. Count-down setup range 10:00 to 99:00. |
| LAPS | 0 to 99 | 0 to 99 | Total working laps. |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 | In kilometres or miles. |
| CALORIES | 0 to 999 | 0 to 999 | Cumulative. |
| PULSE | 0 to 999 | 40 to 220 BPM | Hand pulse or receiver. A chest belt must be worn to use the receiver. |

In exercise mode, with no pulse signal for **8 seconds** the displayed value becomes 0.

**Two labels in this table are wrong.** The RPM row reads "Display the current speed in mile per hour", which contradicts both the RPM name and the 0 to 120 working range; read the field as cadence in RPM. The pulse row says "if the treadmill doesn't have a signal", in a bike manual.

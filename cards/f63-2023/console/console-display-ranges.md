---
id: f63-2023-console-display-ranges
title: Display and working ranges for each readout
kind: spec
question: What are the display ranges on a Sole F63-2023 console?
asked_as:
- what is the top speed of my treadmill
- max incline on my sole treadmill
- what heart rate range does the console read
keywords:
- speed range
- incline range
- time range
- distance
- calories
- pulse
- laps
- display range
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2023
  applies_to:
  - f63-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2023-console-buttons-run-mode
- f63-2023-incline-position-sensor-test
source:
  ref: sole-tm-f63-2023-service-manual
  locator: page 8, Function, with page 10 and page 27
  extracted_at: '2026-09-04'
---

| Readout | Display range | Working range |
|---|---|---|
| SPEED | 0.0 to 99.9 | **1.0~18.0KM or 0.5~12Mile**. Each press of FAST or SLOW changes it by 0.1 km/h (mph) |
| INCLINE | 0 to 99 | **0 to 10. Preset value 0 to 10** (see the note below) |
| TIME | 0:00:00 to 9:99:99 | 00:00 to 9:99:59. Count down setup range 10:00 to 99:00 |
| LAPS | 0 to 99 | 0 to 99 |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 |
| CALORIES | 0 to 999 | 0 to 999 |
| PULSE | 0 to 999 | **40 to 220 BPM** |

**The manual disagrees with itself about maximum incline.** The Function table on page 8 says the incline range is **0 to 10**. The Run Mode button table on page 10 says "the maximum incline position is 15", the incline quick keys are listed as **1/3/5/7/9/12/15**, and the E3 test procedure says the incline window shows **15 for max incline**. Check the machine and its calibration before quoting a figure.

Pulse comes from the hand grips or from a receiver, and the receiver needs a chest belt. **If the treadmill has no pulse signal for 8 seconds the displayed value becomes 0.**

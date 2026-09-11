---
id: ct850-2016-console-data-ranges
title: Display and work range for each console reading
kind: spec
question: What are the display ranges on a Spirit CT850-2016 treadmill console?
asked_as:
- what is the top speed on the ct850 console
- what heart rate range does the treadmill read
- how many incline levels are there
keywords:
- display range
- work range
- speed
- incline
- time
- laps
- distance
- calories
- pulse
- bpm
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - ct850-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-run-mode-buttons
- ct850-2016-calibration-procedure-metric-or-english
- ct850-2016-console-layout
- ct800-2016-console-calibration-in-kph-with-potentiometer-readings-235-to-22
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Section 4 Operation, Function, pp. 15-16 (printed 14-15). CT800-2016 service
    manual section 4 Operation, Function, PDF pp. 15-16 (printed 14-15), text.md lines
    207-244
  extracted_at: '2026-09-08'
---

| Reading | Display range | Work range | Step / note |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.5 to 12 mph | FAST / SLOW change it by 0.1 mph |
| INCLINE | 0 to 99 | 0 to 15 | UP / DOWN change it by 1. Preset value 0 to 15 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | Counts up by default; counts down if the user sets a time. Count-down setup range 10:00 to 99:00 |
| LAPS | 0 to 99 | 0 to 99 | Total working laps |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.9 | Kilometres or miles |
| CALORIES | 0.0 to 999 | 0.0 to 999 | Cumulative |
| PULSE | 0 to 999 | 50 to 200 BPM | Hand pulse or receiver; a chest belt must be worn to use the receiver |

In RUN Mode, with **no pulse signal for 8 seconds** the displayed value becomes 0.

In RUN Mode, pressing STOP saves the time value; re-entering RUN Mode continues counting up from it.

**This manual contradicts itself on the incline maximum.** The table above says the work range and
the preset range are 0 to 15. The RUN MODE key description on the next page but one says the UP key
raises the position by 1 and "the maximum incline position is 12". Treat 15 as the machine limit -
it is the value the calibration procedure sets - and treat the 12 as unreliable.

The speed row is printed as "Display the current speed in Kilometer mile per hour", which is
damaged text; the working range it quotes is in mph.

**The CT800-2016 service manual prints this same table**, so this card covers that machine, with one
row written in both units: its SPEED work range is **0.8~20.0 kph (0.5~12 mph)** and its FAST/SLOW
step **0.1 kph (mph)**, where the CT850-2016 book prints the mile figures only. Every other row -
incline 0 to 15 in steps of 1, LAPS 0 to 99, DISTANCE 0.00 to 99.9, CALORIES 0.0 to 999, PULSE 50 to
200 - is identical, and the CT800-2016 RUN MODE table carries the same "maximum incline position is
12" contradiction. Its own calibration routine sets 0.8 and 20.0 kph
(`ct800-2016-console-calibration-in-kph-with-potentiometer-readings-235-to-22`).


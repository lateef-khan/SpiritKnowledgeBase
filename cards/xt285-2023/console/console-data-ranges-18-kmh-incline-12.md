---
id: xt285-2023-console-data-ranges-18-kmh-incline-12
title: 'Display and work ranges: 1.0 to 18.0 km/h or 0.5 to 12 mph, incline 0 to 12,
  and the page that says 15'
kind: spec
question: What are the speed, incline and pulse ranges on a Spirit xt285-2023 treadmill
  console?
asked_as:
- what is the top speed of my treadmill
- what is the max incline on my treadmill
- what heart rate range does the console read
- does the incline go to 12 or 15
keywords:
- display range
- work range
- speed
- incline 12
- pace
- laps
- calories
- pulse
- bpm
- contradiction
facets:
  brand:
  - spirit
  product_line: treadmill
  model: xt285-2023
  applies_to:
  - xt285-2023
  section: console
  code: '*'
  model_number:
  - '285823'
authority: 3
not_to_be_confused_with:
- xt185-2023-console-data-ranges-16-kmh-10-mph
- spirit-xt-2023-console-data-ranges-20-kmh-incline-15
- spirit-xt-2015-console-data-ranges-16-kmh-incline-steps-of-1
see_also:
- spirit-xt-2023-console-keys-in-ready-and-run-mode
- xt285-2023-console-direct-speed-incline-buttons
- ct850-2016-window-display-modes
source:
  ref: spirit-treadmill-xt285-2023-service-manual
  locator: Section 4 Product Operation, Function, PDF p. 8 (printed 8); text.md lines
    135-175; the RUN MODE key table on PDF p. 10, text.md lines 206-234
  extracted_at: '2026-09-11'
---

**The incline work range printed for this console is 0 to 12, the lowest ceiling in the 2023 family
apart from the XT185.** The XT385-2023 and XT485-2023 go to 15
(`spirit-xt-2023-console-data-ranges-20-kmh-incline-15`); the XT185-2023 goes to 15 on its incline
but only 10 mph on speed (`xt185-2023-console-data-ranges-16-kmh-10-mph`).

| Reading | Display range | Work range | Step / note |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | **1.0 to 18.0 km, or 0.5 to 12 miles** | FAST / SLOW change it by 0.1 km/h (mph) |
| INCLINE | 0 to 99 | **0 to 12**; preset value 0 to 12 | UP / DOWN change it by 0.5 |
| TIME | 00:00 to 99:99 | 00:00 to 99:59 | Counts up by default; counts down if the user sets a time. Count-down setup range 10:00 to 99:00 |
| PACE | 99.99 | 0.00 to 99.59 | Time to walk one km or mile; shows 0.00 with no speed |
| LAPS | 0 to 999 | 0 to 999 | Total working laps |
| DISTANCE | 0.00 to 99.9 | 0.00 to 99.99 | Kilometres or miles |
| CALORIES | 0 to 9999 | 0 to 999 | Cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | Hand pulse or receiver; a chest belt must be worn to use the receiver |

In RUN Mode, with **no pulse signal for 8 seconds** the displayed pulse becomes "0".

In RUN Mode, pressing STOP saves the time value; re-entering RUN Mode continues counting from it.

The service manual's own words for these figures are "DISPLAY range" (what the window can show) and
"WORK range" (what the machine will actually do). Quote the work range as the machine's limit.

**The same book contradicts itself two pages later.** Its RUN MODE key table says of the Incline Up
key "each increase is 0.5. The maximum incline position is 15", and the E3 test procedure repeats "15
for max incline". Those two passages are the family boilerplate carried over unchanged. The Function
table above, the ten incline quick keys (0, 1, 2, 3, 4, 5, 6, 8, 10, 12) and the owner's manual
(`xt285-2023-console-direct-speed-incline-buttons`) all stop at 12. Treat 12 as this machine's limit.


---
id: xt685-2023-console-data-ranges-12-mph-20-kph-spec
title: 'Display and work ranges: 0.5 to 12.0 mph (1.0 to 20.0 km/h), incline 0 to
  15, and the "20.0 kph spec" note'
kind: spec
question: What are the speed, incline and pulse ranges on a Spirit xt685-2023 treadmill
  console?
asked_as:
- what is the top speed of my treadmill
- how many incline levels does the treadmill have
- what heart rate range does the console read
- what does 20 kph spec mean
keywords:
- display range
- work range
- speed
- 20 kph spec
- incline
- decline
- laps
- calories
- pulse
- bpm
facets:
  brand:
  - spirit
  product_line: treadmill
  model: xt685-2023
  applies_to:
  - xt685-2023
  section: console
  code: '*'
  model_number:
  - '685823'
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-console-data-ranges-20-kmh-incline-15
- xt285-2023-console-data-ranges-18-kmh-incline-12
see_also:
- spirit-xt-2023-console-keys-in-ready-and-run-mode
- xt685-2023-calibration-procedure
- ct850-2016-window-display-modes
source:
  ref: spirit-treadmill-xt685-2023-service-manual
  locator: Section 4 Product Operation, Function, PDF pp. 7-8 (printed 7-8); text.md
    lines 112-162
  extracted_at: '2026-09-11'
---

**This book prints the speed range with a note no other 2023 XT book has: "Some spec has 20.0 kph of
maximum speed."** The XT385-2023 and XT485-2023 tables give 1.0 to 20.0 km without any such note
(`spirit-xt-2023-console-data-ranges-20-kmh-incline-15`).

| Reading | Work range | Step / note |
|---|---|---|
| SPEED | **0.5 to 12.0 mph (1.0 to 20.0 kmph)** | FAST / SLOW change it by 0.1 km/h (mph). "Note: Some spec has 20.0kph of maximum speed." |
| INCLINE | **0 to 15**; preset value 0 to 15 | UP / DOWN adjust **incline/decline** by 0.5 |
| TIME | 0:00 to 99:59 | Counts up by default; counts down if the user sets a time. Count-down setup range 10:00 to 99:00 |
| LAPS | 0 to 999 | Total working laps |
| DISTANCE | 0.00 to 99.9 | Total distance for the workout, in kilometres or miles |
| CALORIES | 0.0 to 999 | "Only a rough guide used for comparison of different exercise sessions and is not to be used for medical purposes" |
| PULSE | **50 to 200 BPM** | Hand pulse or receiver; a chest belt must be worn to use the receiver |

**This table prints work ranges only.** The other 2023 XT books print a DISPLAY range column as
well; this one does not, so no display range is claimed here.

In RUN Mode, with **no pulse signal for 8 seconds** the displayed pulse becomes "0". In RUN Mode,
pressing STOP saves the time value; re-entering RUN Mode continues counting from it.

**The "20.0 kph spec" note is repeated at the quick keys.** The ten speed presets are 1, 2, 3, 4, 5,
6, 7, 8, 10, 12, and the book adds "On 20.0kph spec is 2, 4, 6, 8, 10, 12, 14, 16, 18, 20" - the
metric console's presets. See `spirit-xt-2023-console-keys-in-ready-and-run-mode`.

**This machine has a decline motor.** The electrical configuration table lists a separate Decline
Motor "within decline control board", and the incline key is described as adjusting incline/decline.
The table gives no decline figure; the 0 to 15 above is the incline range as printed.


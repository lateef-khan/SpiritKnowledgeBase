---
id: spirit-xtent-console-data-ranges-12-mph-time-to-999
title: 'Display and work ranges on the XT touchscreens: 0.5 to 12.0 mph, incline 0.0
  to 15.0, time to 999:99, pace in min/km'
kind: spec
question: What are the speed, incline and pulse ranges on a Spirit XT485ENT-2023 or
  XT685ENT-2023 treadmill console?
asked_as:
- what is the top speed of the touchscreen treadmill
- how many incline levels does the ent treadmill have
- what heart rate range does the console read
- what unit is the pace shown in
keywords:
- display range
- work range
- speed
- incline
- pace
- min/km
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
  - xt485ent-2023
  - xt685ent-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-console-data-ranges-20-kmh-incline-15
see_also:
- xt485ent-2023-console-keys-in-ready-and-run-mode
- xt685ent-2023-console-keys-in-ready-and-run-mode
- xt485ent-2023-console-direct-access-keys-two-or-three-digits
- ct850-2016-window-display-modes
source:
  ref: spirit-treadmill-xt485ent-2023-service-manual
  locator: XT485ENT section 4 Product Operation, Function, PDF pp. 14-15 (printed
    14-15); text.md lines 213-258. The XT685ENT service manual prints the same table
    on its PDF p. 7 (printed 7), text.md lines 122-159
  extracted_at: '2026-09-11'
---

**The touchscreen consoles print a PACE row in minutes per km or mile and a TIME display range up to
999:99**; the LED consoles print pace as a time unit and a time range to 99:99.

| Reading | Display range | Work range | Step / note |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | **0.5 to 12.0 mph** (kilometre figure below) | FAST / SLOW change it by 0.1 km/h (mph) |
| INCLINE | 0 to 999 | **0.0 to 15.0**; preset value 0.0 | UP / DOWN change it by 0.5 |
| TIME | 0:00 to 999:99 | not printed | Counts up by default; counts down if the user sets a time. Count-down setup range 10:00 to 99:00 |
| DISTANCE | 0.00 to 99.99 | 0.00 to 99.99 | Kilometres or miles |
| CALORIES | 0 to 999 | 0 to 999 | Cumulative |
| PULSE | 0 to 999 | **50 to 200 BPM** | Hand pulse or receiver; a chest belt must be worn to use the receiver |
| PACE | 00:00 to 99:99 | 00:00 to 99:99 | "How long will takes to walk (or run) per each Km or Mile at current speed?" Unit is **min/Km or min/Mi** |

In RUN Mode, with **no pulse signal for 8 seconds** the displayed pulse becomes "0". In RUN Mode,
pressing STOP saves the time value; re-entering RUN Mode continues counting from it.

**The two books disagree on the metric speed figure, and one of them is a misprint.** The XT485ENT
book prints the work range as **0.5~12.0 mph (1.0 ~ 18.0 kmph)**. The XT685ENT book prints
**0.5 ~ 12.0 mph (1.0 ~ 2.0 kmph)** - the page was rendered and read, and "2.0" is what is printed;
it is not an extraction error. 12.0 mph is about 19.3 km/h, so neither metric figure is the
conversion of the mile figure. Quote the mile figure; the XT485ENT owner's manual's own direct-access
maximum is 12.0 mph or 18.0 kmph (`xt485ent-2023-console-direct-access-keys-two-or-three-digits`).

**The touchscreen calibration screens print the same 0.5 and 12.0 mph as MIN SPEED and MAX SPEED**:
`xt485ent-2023-console-calibration-behind-the-software-version-and-password-20160620` and
`xt685ent-2023-console-calibration-behind-five-taps-on-settings`.


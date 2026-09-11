---
id: cu800-2012-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan
title: What each key does in Ready and Run mode, and the DATA SCAN the Display key
  starts through speed, RPM, level, watts and segment time
kind: fact
question: What do the console keys do before and during a workout on a Spirit cu800-2012
  bike, and what does the Display key show?
asked_as:
- what does the display key do on the cu800
- why does level up do nothing before i start on the cu800
- what is data scan on the spirit bike console
- what are the buttons on the cu800 console
keywords:
- ready mode
- run mode
- display key
- data scan
- four seconds
- seg time
- watt
- fan key
- program buttons
- enter key
facets:
  brand:
  - spirit
  product_line: bike
  model: cu800-2012
  applies_to:
  - cu800-2012
  section: console
  code: '*'
  model_number:
  - '800343'
authority: 3
not_to_be_confused_with:
- spirit-xbr-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
see_also:
- cu800-2012-console-software-modes-idle-child-lock-pause-end-and-reset
- cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- spirit-ce-console-display-button-four-window-sets
- spirit-ce-console-fan-key-on-the-front-right
source:
  ref: spirit-bike-cu800-2012-service-manual
  locator: Section 4 XU878 Product Operation, Function Button Locations and Function
    Button In Main Mode, PDF pp. 18-20 (printed 18-20); text.md lines 299-368, the
    button drawing read from the OCR supplement for PDF page 18
  extracted_at: '2026-09-11'
---

**The button page names ten program buttons** - Manual, Hill, Fat Burn, Cardio, Strength, Interval,
Custom, Fit-Test, HR, Constant power - a **Fan Key** ("Cooling fan switch on or off"), the
**DISPLAY** and the **CONTROL KEYS**; the drawing itself is labelled RESISTANCE LEVEL over the level
keys.

**READY MODE** (before Start):

| Key | What it does |
|---|---|
| STOP | Non-function |
| START | Starts the workout. The spec says "there will be 3 second final count down on window display, then machine starts running. In MANUAL, [it] starts at MIN LEVEL" |
| LEVEL UP / DOWN | Non-functional until a setting has been entered |
| FAN | Fan on or off |
| DISPLAY | Selects the speed profile when a program is selected (P0~P5, CUSTOM, FIT-TEST) |
| ENTER | Enters parameter setting, and confirms each setting |

**RUN MODE** (during a workout):

| Key | What it does |
|---|---|
| STOP | Stops the workout |
| START, ENTER | Non-functional |
| LEVEL UP / DOWN | Raises or lowers the level by 1 |
| FAN | Fan on or off |
| DISPLAY | Switches the exercise data. If the display already shows the latest data, pressing it shows **"DATA SCAN"** for two seconds, then the message window cycles automatically **every four seconds** through: `SPEED XX.XMPH`, `SPEED ** RPM`, `LEVEL XX MAX XX` (only in a program), `WATT XXX`, `SEG TIME X:XX` (not in HRC mode), `DATA SCAN` |

**"Treadmill", "start running" and the three-second count-down are the spec's words.** This chapter
is a treadmill software specification reused for the bike
(`cu800-2012-console-software-modes-idle-child-lock-pause-end-and-reset`); a generator bike has no
count-down to a moving belt. The message strings and the four-second scan are the console's.

**The owner's manual describes the Display button differently** - as cycling four sets of readings
in the data windows and switching the profile for the quarter-mile track
(`spirit-ce-console-display-button-four-window-sets`). The two do not contradict each other: this
spec lists the message-window strings, the owner's manual the data windows.

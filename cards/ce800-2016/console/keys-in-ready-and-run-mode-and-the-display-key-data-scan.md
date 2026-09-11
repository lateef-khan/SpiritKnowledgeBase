---
id: ce800-2016-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan
title: What each elliptical key does in Ready and Run mode, and the DATA SCAN the
  Display key starts through speed, RPM, level, watts and segment time
kind: fact
question: What do the console keys do before and during a workout on a Spirit ce800-2016
  elliptical, and what does the Display key show?
asked_as:
- what does the display key do on the ce800
- why does level up do nothing before i start on the ce800
- what is data scan on the spirit elliptical console
- what are the buttons on the 2016 ce800 console
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
- led display
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2016
  applies_to:
  - ce800-2016
  section: console
  code: '*'
  model_number:
  - '800045'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan
see_also:
- ce800-2016-console-software-modes-idle-child-lock-pause-end-and-reset
- ce800-2016-console-data-ranges-level-0-to-20-pulse-40-to-220-and-a-pace-window
- cu800-2012-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan
- spirit-ce-console-display-button-four-window-sets
- spirit-ce-console-blue-led-console-face
source:
  ref: spirit-elliptical-ce800-2016-service-manual
  locator: Section 4 XE890B Electrical Operation, Display Windows, Function Button
    Locations and Function Button In Main Mode, PDF pp. 12 and 17-19 (printed 12,
    17-19); text.md lines 201-207 and 317-383, the key legends read from a 100 dpi
    render of pages 12 and 17
  extracted_at: '2026-09-11'
---

**The Display Windows page carries one call-out, "LED Display".** Its drawing shows a numbered
program-key column either side of the blue dot matrix - **1 Manual, 2 Hill, 3 Fat Burn, 4 Cardio, 5
Strength** on the left, **6 Interval, 7 Custom, 8 Fitness Test, 9 HR, 0 Constant Power** on the
right - a HEART RATE % PROFILE bar (50 to 90 %), a message window (sample reads `TIME 31:59 DIST
10.7`), and below it DISPLAY (Cycle Scan), the RESISTANCE LEVEL up / ENTER / down keys, FAN
(on/off), START and STOP (hold to reset).

**The Function Button Locations legend names the program buttons as "Manual, Hill, Fat Burn,
Cardio, Strength, Interval, Custom, Fit-Test, 2HR"** - nine names for ten keys, and "2HR" where the
drawing prints one HR key and a Constant Power key. It also names the **DISPLAY**, the **CONTROL
KEYS** and a **Fan Key** ("Cooling fan switch on or off").

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
is a treadmill software specification reused for the elliptical
(`ce800-2016-console-software-modes-idle-child-lock-pause-end-and-reset`); a generator elliptical
has no count-down to a moving belt. The message strings and the four-second scan are the console's.

**The CE800-2013 owner's manual describes the Display button differently** - as cycling four sets of
readings in the data windows and switching the profile for the quarter-mile track
(`spirit-ce-console-display-button-four-window-sets`); that manual's console drawing is
`spirit-ce-console-blue-led-console-face`. The two do not contradict each other: this spec lists
the message-window strings, the owner's manual the data windows.

**The CU800-2012 bike's XU878 book prints this chapter word for word**, drawing included
(`cu800-2012-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan`).

---
id: tr75h-2025-programs-hrc-three-levels-and-three-control-modes
title: HRC levels target 60, 75 or 85 percent of 220 minus age, with speed-only, incline-only
  and combined control modes stepping 0.2 kph or one level per check
kind: procedure
question: How does heart rate control work on an Xterra tr75h-2025 treadmill, and
  what do H1, H2 and H3 adjust?
asked_as:
- tr75h heart rate control setup
- what is the difference between h1 h2 and h3 on the tr75h
- why did my tr75h pause and show hi
- tr75h hrc target percent
keywords:
- hrc
- heart rate control
- h1 h2 h3
- 60 percent
- 75 percent
- 85 percent
- 220 minus age
- speed control
- incline control
- pulse hi
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr75h-2025
  applies_to:
  - tr75h-2025
  section: programs
  code: '*'
  model_number:
  - '175825'
authority: 3
not_to_be_confused_with: []
see_also:
- tr75h-2025-programs-running-and-hiking-program-set-and-defaults
- xterra-treadmill-programs-target-zone-of-108-to-144-beats
source:
  ref: xterra-treadmill-tr75h-2025-owners-manual
  locator: TR75H OM "Programs - Heart Rate Control", PDF p. 29 (printed 28), text.md
    lines 889-917 (sections A and B native; tables C, D and E are pictures, in the
    OCR supplement for p. 29 and read from the render)
  extracted_at: '2026-09-11'
---

**A. Target heart rate** (default age 30):

- Level 1: (220 - age) x 60%
- Level 2: (220 - age) x 75%
- Level 3: (220 - age) x 85%

**B. Setup**

1. In standby, press **RUN/HIKE** to choose Running or Hiking mode.
2. Press **+ / -** to select HRC; the selected **H1 to H3** flashes in the PROGRAM window.
3. Press **ENTER**; the dot matrix scrolls "AGE".
4. Use + / - to select the age (default 30, range 13 to 99).
5. Press ENTER; the pulse window shows the highest heart rate and the dot matrix scrolls
   "CHOOSE LEVEL OR START".
6. Use + / - to select the level (default L1, range L1 to L3).
7. Press ENTER; the dot matrix scrolls "SET TIME OR START".
8. Use + / - to set the time (default 32:00, range 1:00 to 99:00).
9. Press ENTER; the dot matrix shows "PRESS START".
10. Press **START/STOP** to begin. Defaults are used for any value not entered.

**C, D, E. What each program code controls** (these three tables are printed as pictures;
read from the render):

| | H01 - Speed Control Only | H02 - Incline Control Only | H03 - Speed and Incline Control |
|---|---|---|---|
| Within 30 s after start, checks every 10 s for 3 consecutive times; heart rate detected | enters the corresponding heart rate control setting | same | same |
| ... heart rate not detected | PULSE blinks 3 times for 30 s; if still no reading, pauses | same | same |
| 30 s after start, heart rate within +/-10 bpm of target | keeps checking every 10 s; **speed adjusts by +/-0.2 KPH** per 10 s check | keeps checking every 10 s; **incline adjusts by 1 level** per 10 s check | keeps checking every 10 s; speed adjusts by +/-0.2 KPH, then incline by 1 level after the speed hits max/min, per 10 s check |
| ... heart rate outside +/-10 bpm of target | checks every 5 s; speed adjusts by +/-0.2 KPH per 5 s check | checks every 5 s; incline adjusts by 1 level per 5 s check | checks every 5 s; speed by +/-0.2 KPH, then incline by 1 level after the speed hits max/min, per 5 s check |
| ... heart rate exceeding 20 bpm over the highest HR in two consecutive checks | **pauses immediately; PULSE displays "HI"** | same | same |

The setup section names the levels L1 to L3 by target percentage and the tables name the
programs H01 to H03 by what they control; the book does not say in words that H1 = L1, and
the level chosen in step 6 is the target percentage.


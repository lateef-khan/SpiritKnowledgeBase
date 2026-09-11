---
id: cs800-2016-console-software-modes-idle-30-minute-sleep-child-lock-quick-start-pause-end-reset
title: 'The stepper console software modes as the 2016 book specifies them: idle,
  a 30-minute sleep, a CONSOLE LOCKED child lock, a five-minute pause, a WORKOUT SUMMARY
  of level, distance and pace, and a three-second reset'
kind: fact
question: What do CONSOLE LOCKED and WORKOUT SUMMARY mean on a Spirit cs800-2016 stepper,
  and how do I wake or reset the console?
asked_as:
- my cs800 says console locked
- how long until the cs800 stepper goes to sleep
- how do i reset the console on the older cs800
- what does workout summary show on the stepper
keywords:
- idle mode
- sleep mode
- 30 minutes
- child lock
- console locked
- quick start
- pause mode
- workout summary
- reset mode
- avg pace
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: console
  code: '*'
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset
- spirit-ce-console-stop-button-press-once-twice-hold
see_also:
- cs800-2016-console-engineering-mode-with-a-30-minute-sleep-a-da-test-and-a-safety-item
- cs800-2016-console-keys-in-ready-and-run-mode-and-the-display-key-scan-of-seg-time-dist-and-pace
- cs800-2016-console-data-ranges-rpm-0-to-120-level-1-to-20-and-pulse-40-to-220
- spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: CS800-2016 (XS200-SS003) service manual section 4 Product Operation, Operation
    / Window Display Mode, PDF pp. 15-16 (printed 15-16); text.md lines 212-265
  extracted_at: '2026-09-11'
---

**This chapter is a software specification**, and it is the Dyaco elliptical spec with a stepper's
summary line. Its messages and timings are the console's; its stray "Incline = 1" and "bike" are
leftovers of the machines it was written for.

**IDLE MODE** - each program profile is shown on the MESSAGE WINDOW for 5 seconds in turn, with the
PROGRAM PROFILE shown at the same time; the heart-rate bar LED is lit steady.

**SLEEP MODE** - pre-set **SLEEP ON**; set ON or OFF in Engineering Mode. With no RPM input in idle
the console enters **SLEEP MODE after 30 minutes** without a key press: the LCD shows nothing and the
LED is off. **Press any key to wake it** back to idle. "Resistance in SLEEP MODE: Incline = 1, fan
off." The spec also says the console "will not get into SLEEP MODE when the set up is ON, unless
turn off the power" - the elliptical spec's DISPLAY ON sentence with the word changed, contradicting
the pre-set two lines above it; read the 30 minutes and the ON/OFF switch, not the sentence.

**CHILD LOCK MODE** - pre-set **CHILD LOCK OFF**; set in Engineering Mode. With it ON the message
window shows **"CONSOLE LOCKED"** twice, then **"CHILD LOCK-ON PRESS START AND ENTER TO ENABLE
OPERATION"**. Hold **Start and Enter for more than two seconds** to switch it off and enter idle. No
key works while the lock is active.

**EXERCISE MODE (QUICK START)** - in idle, Start enters MANUAL MODE with age and weight preset; time
counts up from 00:00, every countable value from 0, resistance from 1. Or choose a program with the
**MANUAL, PROGRAM or HRC** keys and press Start; all parameters take their preset values.

**PAUSE MODE** - Stop records the exercise parameters; the message window shows **"PAUSE"** and the
upper window the recorded values. After 5 seconds it shows **"PRESS START TO RESUME OR STOP TO END"**.
With no key press for **five minutes** it drops to idle. On Start the resistance level "should back
to 1" and the tension motor returns to the level it held before the pause.

**END MODE** - the message window shows **"WORKOUT SUMMARY"** and the workout data for 3 minutes,
each item for three seconds: **`AVG LEVEL XX`, `Dist XXX`, `AVG PACE XX.X`**; LEVEL and STRIDE show
their averages, CALORIES and TIME their totals. With no key press for 3 minutes the console returns
to idle.

**RESET MODE** - in idle, hold **Stop for more than three seconds** to reset the system. If the
console is in CONSOLE LOCK MODE, leave lock mode first.

**A stepper's summary, not the elliptical's.** The XE and CE850 2016 books list TOTAL TIME, AVG SPD,
AVG WATT, AVG HR and LAPS here
(`spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset`,
`spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset`); this
one prints average level, distance and average pace, and "STRIDE" as the second averaged window.
Thirty minutes of sleep agrees with this book's own menu
(`cs800-2016-console-engineering-mode-with-a-30-minute-sleep-a-da-test-and-a-safety-item`).

**The 2020 CS800 owner's and service manuals print none of this** - no mode names, no CONSOLE LOCKED
and no summary list; their Stop key is the five-minute pause, the second press to the start-up
screen and the three-second reset (`spirit-ce-console-stop-button-press-once-twice-hold`).


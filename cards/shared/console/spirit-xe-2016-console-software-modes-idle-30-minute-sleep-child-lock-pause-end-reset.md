---
id: spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
title: 'The elliptical console software modes as the 2016 books specify them: idle,
  a 30-minute sleep, a CONSOLE LOCKED child lock, a five-minute pause, a WORKOUT SUMMARY
  and a three-second reset'
kind: fact
question: What do CONSOLE LOCKED and WORKOUT SUMMARY mean on a Spirit XE195, XE295,
  XE395, XE795 or XG400 2016 elliptical, and how do I wake or reset the console?
asked_as:
- my 2016 spirit elliptical console says console locked
- how long before the xe295 console goes to sleep
- how do i reset the xg400 console
- what does the xe795 show when it is idle
keywords:
- idle mode
- display mode
- sleep mode
- 30 minutes
- child lock
- console locked
- pause mode
- workout summary
- reset mode
- software spec
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe795-2016
  - xg400-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset
- ce800-2016-console-software-modes-idle-child-lock-pause-end-and-reset
see_also:
- spirit-xe-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
- spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item
- xe795-2021-console-engineering-mode-with-a-da-test
- spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset
- spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-xe-console-what-the-workout-summary-lists
source:
  ref: spirit-elliptical-xe195-2016-service-manual
  locator: XE195-2016 section 4 Elliptical Operation, Operation, Window Display Mode,
    PDF pp. 16-17 (printed 16-17); text.md lines 226-279. XE295-2016 PDF pp. 16-17,
    lines 225-284; XE395-2016 PDF pp. 16-17, lines 263-327; XE795-2016 PDF pp. 16-17,
    lines 222-283; XG400-2016 PDF pp. 14-15, lines 161-225. Differences between the
    five are named in the body
  extracted_at: '2026-09-11'
---

**This chapter is a software specification**, printed in all five books. Its messages and timings
are the console's; its stray "ramp incline" is a leftover from the elliptical the spec was written
for.

**IDLE MODE** - each program profile is shown on the message window in turn while it cycles
**"PRESS START FOR QUICK START OR PROGRAM BUTTON FOR SETUP"**. The heart-rate bar LED and the track
LED are lit steady; the data windows show RPM 000, CALORIES 000 (the XE395, XE795 and XG400 print
012), TIME 00:00, DISTANCE 0.00 and PULSE - - -.

**DISPLAY MODE** (the sleep setting) - pre-set **DISPLAY ON (DISABLE)**; set ON or OFF in Engineering
Mode. With it ON the console never sleeps unless the power is switched off. With no RPM input in idle
it enters **SLEEP MODE after 30 minutes** without a key press: the LCD shows nothing and the
backlight is off. **Press any key to wake it** back to idle. "Resistance in SLEEP MODE: Incline = 1".

**CHILD LOCK MODE** - pre-set OFF; set in Engineering Mode. With it ON the message window shows
**"CONSOLE LOCKED"** twice, then **"CHILD LOCK-ON PRESS START AND ENTER TO ENABLE OPERATION"**. Hold
**Start and Enter for more than two seconds** to switch it off and enter idle. No key works while the
lock is active.

**EXERCISE MODE (QUICK START)** - in idle, Start enters MANUAL MODE with age and weight preset; time
counts up from 00:00, every countable value from 0, resistance from 1. Or press a program key, then
Start; all parameters take their preset values. The XE195 lists the keys as **MANUAL, PROGRAM,
HRC**; the other four as **MANUAL, PROGRAM, USER1~2, HRC1~2**.

**PAUSE MODE** - Stop records the exercise parameters; the message window shows **"PAUSE"** and the
upper window the recorded values. After 5 seconds it shows **"PRESS START TO RESUME OR STOP TO END
WORKOUT"**. With no key press for **five minutes** it drops to idle. On Start the tension motor
returns to the level it held before the pause - the XE195, XE295 and XE395 books add "the ramp
incline level should back to 1 when the resistance level is 1"; the XE795 and XG400 books print
the tension motor only.

**END MODE** - the message window shows **"WORKOUT SUMMARY"** and the workout data for 3 minutes:
**TOTAL TIME XX:XX, AVG SPD XX.X, AVG WATT XXX, AVG HR XXX, LAPS XX**, three seconds each - the
XE395 adds **AVG INCLINE XX** and **TOTAL ALT XXX**; LEVEL shows its average, CALORIES, TIME and
DISTANCE their totals. With no key press for **3 minutes** the console returns to idle.

**RESET MODE** - in idle, hold **Stop for more than three seconds** to reset the system. If the
console is in lock mode, leave lock mode first.

**Thirty minutes here, twenty in the maintenance menu.** The menu page of every one of these books
says the same setting powers the console down after **20 minutes**
(`spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item`, and for the XE795
`xe795-2021-console-engineering-mode-with-a-da-test`). Nothing resolves it. **The CE850-2016 and
XE895-2016 print 20 in both places**
(`spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset`).

**The 2018, 2019 and 2021 owner's manuals print none of this** - no mode names, no CONSOLE LOCKED
message and no summary list - so a later machine is not covered by this card. The 2016 residential
bikes print the same chapter (`spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset`).

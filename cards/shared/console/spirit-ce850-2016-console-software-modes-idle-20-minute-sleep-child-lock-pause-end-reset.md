---
id: spirit-ce850-2016-console-software-modes-idle-20-minute-sleep-child-lock-pause-end-reset
title: 'The console software modes as the 2016 books specify them: idle, a 20-minute
  sleep, a CONSOLE LOCKED child lock, a pause that returns the stride to 18, a WORKOUT
  SUMMARY with AVG INCLINE and TOTAL ALT, and a three-second reset'
kind: fact
question: What do CONSOLE LOCKED and WORKOUT SUMMARY mean on a Spirit CE850-2016 or
  XE895-2016 elliptical, and how long before the console sleeps?
asked_as:
- my 2016 spirit elliptical console says console locked
- how long before the ce850 console goes to sleep
- how do i reset the xe895 console
- what does the ce850 show when it is idle
keywords:
- idle mode
- display mode
- sleep mode
- 20 minutes
- child lock
- console locked
- pause mode
- stride 18
- workout summary
- reset mode
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe895-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- ce800-2016-console-software-modes-idle-child-lock-pause-end-and-reset
see_also:
- spirit-ce850-2016-console-data-ranges-stride-18-to-24-and-level-1-to-20
- spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan
- spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item
- ce850-2016-console-engineering-mode-security-lock
- spirit-ce850-console-stride-calibration-stride-up-and-start-held-five-seconds
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: CE850-2016 (XE898-SE011) section 4 Product Operation, Operation, Window
    Display Mode, PDF pp. 16-17 (printed 16-17); text.md lines 275-337. XE895-2016
    (XE895-SE022) PDF pp. 16-17, lines 276-333, word for word except the program-key
    names named in the body
  extracted_at: '2026-09-11'
---

**This chapter is a software specification**, printed in both books; its messages and timings are
the console's.

**IDLE MODE** - each program profile is shown on the message window in turn while it cycles
**"PRESS START FOR QUICK START OR PROGRAM BUTTON FOR SETUP"**. The heart-rate bar LED and the track
LED are lit steady; the data windows show RPM 000, CALORIES 12, TIME 00:00, DISTANCE 0.00 and
PULSE - - -.

**DISPLAY MODE** (the sleep setting) - pre-set **DISPLAY ON (DISABLE)**; set ON or OFF in Engineering
Mode. With it ON the console never sleeps unless the power is switched off. With no RPM input in idle
it enters **SLEEP MODE after 20 minutes** without a key press: the LCD shows nothing and the
backlight is off. **Press any key to wake it** back to idle. "Resistance in SLEEP MODE: Incline = 1".

**CHILD LOCK MODE** - pre-set OFF; set in Engineering Mode. With it ON the message window shows
**"CONSOLE LOCKED"** twice, then **"CHILD LOCK-ON PRESS START AND ENTER TO ENABLE OPERATION"**. Hold
**Start and Enter for more than two seconds** to switch it off and enter idle. No key works while the
lock is active.

**EXERCISE MODE (QUICK START)** - in idle, Start enters MANUAL MODE with age and weight preset; time
counts up from 00:00, every countable value from 0, resistance from 1. Or press a program key, then
Start; all parameters take their preset values. **The key list is the one line that differs**: the
CE850-2016 prints **MANUAL, PROGRAM, CUSTOM1, CUSTOM 2, HRC1, HRC2**; the XE895-2016 prints **MANUAL,
PROGRAM, USER1, USER2, HRC1, HRC2**.

**PAUSE MODE** - Stop records the exercise parameters; the message window shows **"PAUSE"** and the
upper window the recorded values. After 5 seconds it shows **"PRESS START TO RESUME OR STOP TO END
WORKOUT"**. With no key press for **five minutes** it drops to idle. **"The STRIDE should back to
18 when the resistance level is 1"**; on Start the tension motor and the stride return to the
levels they held before the pause.

**END MODE** - the message window shows **"WORKOUT SUMMARY"** and the workout data for 3 minutes:
**TOTAL TIME XX:XX, AVG SPD XX.X, AVG WATT XXX, AVG HR XXX, LAPS XX, AVG INCLINE XX, TOTAL ALT
XXX**, three seconds each; LEVEL and STRIDE show their averages, CALORIES, TIME and DISTANCE their
totals. With no key press for **3 minutes** the console returns to idle.

**RESET MODE** - in idle, hold **Stop for more than three seconds** to reset the system. If the
console is in lock mode, leave lock mode first.

**Twenty minutes, in both places.** These two books print 20 minutes here and 20 minutes in their
maintenance menu (`spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item`), where
the XE195, XE295, XE395, XE795 and XG400 books of the same year print **30** here and 20 there
(`spirit-xe-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset`). **The
CE850-2016 owner's manual says 30** (`ce850-2016-console-engineering-mode-security-lock`); nothing
resolves it.

**AVG INCLINE and TOTAL ALT are printed for the powered stride.** The books call the same thing
stride in the function table and incline in the key table
(`spirit-ce850-2016-console-data-ranges-stride-18-to-24-and-level-1-to-20`,
`spirit-ce850-2016-console-keys-in-ready-and-run-mode-incline-half-steps-and-alt-in-the-scan`).

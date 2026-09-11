---
id: cu800-2012-console-software-modes-idle-child-lock-pause-end-and-reset
title: 'The console software modes as the XU878 book specifies them: idle, a CONSOLE
  LOCKED child lock, a five-minute pause, an END OF WORKOUT SUMMARY and a three-second
  reset'
kind: fact
question: What do CONSOLE LOCKED and END OF WORKOUT SUMMARY mean on a Spirit cu800-2012
  bike, and how do I reset the console?
asked_as:
- my cu800 console says console locked
- what does end of workout summary mean on the spirit bike
- how do i reset the cu800 console
- what does the cu800 show when it is idle
keywords:
- idle mode
- child lock
- console locked
- pause mode
- end mode
- workout summary
- reset mode
- user key to save
- avg level
- software spec
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
- spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
see_also:
- cu800-2012-console-maintenance-menu-30-minute-sleep-and-start-enter-three-second-unlock
- cu800-2012-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan
- cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- spirit-ce-console-stop-button-resume-by-pedalling
source:
  ref: spirit-bike-cu800-2012-service-manual
  locator: Section 4 XU878 Product Operation, Operation, Window Display Mode, PDF
    pp. 14-15 (printed 14-15); text.md lines 198-246
  extracted_at: '2026-09-11'
---

**This chapter is a software specification pasted from a treadmill book.** It says "treadmill" and
"incline" where it means this bike, and its numbering jumps from 4 to 6. The messages and timings
below are what it prints; treat the wording as the console's, and the vehicle names as noise.

**IDLE MODE** - the dot matrix scrolls every 2 seconds through each Program Profile, followed by the
program, with that program's indicator LED on. The message window displays
**"SELECT A PROGRAM OR PRESS START TO BEGIN"**.

**CHILD LOCK MODE** - set ON or OFF in Engineer Mode. With child lock ON, power-on shows
**"CONSOLE LOCKED"** for 3 seconds, then **"CHILD LOCK - ON, PRESS START AND ENTER TO ENABLE
OPERATION"** until you **press and hold Start and Enter for 2 seconds**, which enters Idle Mode.
Otherwise no key is recognised. The maintenance menu times the same unlock at 3 seconds
(`cu800-2012-console-maintenance-menu-30-minute-sleep-and-start-enter-three-second-unlock`).

**EXERCISE MODE (QUICK START)** - in idle, Start enters MANUAL MODE with age and weight at their
preset values; time counts up from 00:00, every countable value from 0, resistance from 1. Or choose
a program key - **MANUAL, PROGRAM, CUSTOM, FIT-TEST, HRC1, Constant power** - then Start.

**PAUSE MODE** - Stop records the exercise parameters; "Level returns to the first paragraph", the
message window shows **"PAUSE PRESS START TO RESUME OR STOP TO END"**, the profile and the flashing
position freeze and counting stops. With no Start key and no speed pulse for **5 minutes** it drops
to Idle Mode.

**END MODE** - the message window shows **"END OF WORKOUT SUMMARY"** and displays the workout
information for **three minutes**: **"AVG LEVEL XX", "AVG SPD XX.X", "AVG RPM XX", "AVG RAMP XX"**
each for three seconds, then **"PROGRAM END PRESS START TO REPEAT OR STOP TO END OR USER KEY TO
SAVE"**. Start repeats the program, Stop ends it, the **USER key saves the parameters to CUSTOM
USER**. The DATA window shows the average LEVEL and PULSE; CAL, TIME and DIST show totals; PACE
shows the pace value. **There is no ramp on this bike**; the AVG RAMP line is the treadmill's.

**RESET MODE** - in idle, hold **Stop for more than three seconds**. If the console is in lock mode,
leave lock mode first. The message window shows **"RESET"** for two seconds, and the console returns
to Idle Mode.

**The owner's manual describes the same keys in customer words** - Stop once pauses, twice ends,
held for three seconds resets (`spirit-ce-console-stop-button-resume-by-pedalling`). This card
holds the messages and the mode names the owner's manual never prints.

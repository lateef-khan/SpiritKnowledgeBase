---
id: spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
title: 'The console software modes as the 2016 books specify them: idle, a 30-minute
  sleep, a CONSOLE LOCKED child lock, a five-minute pause, a WORKOUT SUMMARY and a
  three-second reset'
kind: fact
question: What do CONSOLE LOCKED and WORKOUT SUMMARY mean on a Spirit XBR25, XBR55,
  XBR95 or XBU55 2016 bike, and how do I wake or reset the console?
asked_as:
- my 2016 spirit bike console says console locked
- how long before the xbr55 console goes to sleep
- how do i reset the xbu55 console
- what does the xbr95 show when it is idle
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
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbr55-2016
  - xbr95-2016
  - xbu55-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu800-2012-console-software-modes-idle-child-lock-pause-end-and-reset
see_also:
- spirit-xbr-2016-console-maintenance-menu-20-minute-sleep-described-motor-test-and-safety
- spirit-xbr-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
- spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
- xe795-2021-console-engineering-mode-with-a-da-test
source:
  ref: spirit-bike-xbr25-2016-service-manual
  locator: XBR25-2016 section 4 Product Operation, Operation, Window Display Mode,
    PDF pp. 15-16 (printed 15-16); text.md lines 188-251. XBR55-2016 PDF pp. 16-18,
    lines 195-268; XBU55-2016 PDF pp. 15-16, lines 181-243; XBR95-2016 PDF pp. 16-17,
    lines 203-267. All four print the block word for word
  extracted_at: '2026-09-11'
---

**This chapter is a software specification**, printed word for word in all four books. Its
messages and timings are the console's; its stray "ramp incline" is a leftover from the elliptical
the spec was written for.

**IDLE MODE** - each program profile is shown on the message window in turn while it cycles
**"PRESS START FOR QUICK START OR PROGRAM BUTTON FOR SETUP"**. The heart-rate bar LED and the track
LED are lit steady; the data windows show RPM 000, CALORIES 000, TIME 00:00, DISTANCE 0.00 and
PULSE - - -.

**DISPLAY MODE** (the sleep setting) - pre-set **DISPLAY ON (DISABLE)**; set ON or OFF in Engineering
Mode. With it ON the console never sleeps unless the power is switched off. With no RPM input in idle
it enters **SLEEP MODE after 30 minutes** without a key press: the LCD shows nothing and the
backlight is off. **Press any key to wake it** back to idle. "Resistance in SLEEP MODE: Incline = 1".

**CHILD LOCK MODE** - pre-set OFF; set in Engineering Mode. With it ON the message window shows
**"CONSOLE LOCKED"** twice, then **"CHILD LOCK-ON PRESS START AND ENTER TO ENABLE OPERATION"**. Hold
**Start and Enter for more than two seconds** to switch it off and enter idle. No key works while the
lock is active.

**EXERCISE MODE (QUICK START)** - in idle, Start enters MANUAL MODE with age and weight preset; time
counts up from 00:00, every countable value from 0, resistance from 1. Or press **MANUAL, PROGRAM or
HRC**, then Start; all parameters take their preset values.

**PAUSE MODE** - Stop records the exercise parameters; the message window shows **"PAUSE"** and the
upper window the recorded values. After 5 seconds it shows **"PRESS START TO RESUME OR STOP TO END
WORKOUT"**. With no key press for **five minutes** it drops to idle. On Start the tension motor
returns to the level it held before the pause.

**END MODE** - the message window shows **"WORKOUT SUMMARY"** and the workout data for **1 minute**:
**TOTAL TIME XX:XX, AVG SPD XX.X, AVG WATT XXX, AVG HR XXX, LAPS XX**, three seconds each; LEVEL shows
its average, CALORIES, TIME and DISTANCE their totals. With no key press for **3 minutes** the console
returns to idle.

**RESET MODE** - in idle, hold **Stop for more than three seconds** to reset the system. If the
console is in lock mode, leave lock mode first.

**Thirty minutes here, twenty in the maintenance menu.** The menu pages of the XBR25-2016 and
XBU55-2016 books say the same setting powers the console down after **20 minutes**
(`spirit-xbr-2016-console-maintenance-menu-20-minute-sleep-described-motor-test-and-safety`); the
XBR95-2016 menu also says 20 (`xe795-2021-console-engineering-mode-with-a-da-test`). Nothing
resolves it.

**The 2019 and 2021 owner's manuals print none of this** - no mode names, no CONSOLE LOCKED message
and no summary list - so a 2019 machine is not covered by this card; the 2016 books predate it.

---
id: cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
title: 'Display and work ranges for each console reading: speed to 99.9, level 0 to
  20, pulse 40 to 220 BPM, and a pace window'
kind: spec
question: What are the display ranges for speed, level, time and pulse on a Spirit
  cu800-2012 bike?
asked_as:
- how many resistance levels does the cu800 have
- what is the highest pulse the cu800 console shows
- what is pace on the spirit cu800 console
- how long can i set the countdown timer on the cu800
keywords:
- display range
- work range
- level 0 to 20
- pulse 40 to 220
- pace
- laps
- countdown
- calories
- speed
- spec
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
- spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
see_also:
- cu800-2012-console-software-modes-idle-child-lock-pause-end-and-reset
- cu800-2012-console-keys-in-ready-and-run-mode-and-the-display-key-data-scan
- spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
source:
  ref: spirit-bike-cu800-2012-service-manual
  locator: Section 4 XU878 Product Operation, Function, PDF pp. 16-17 (printed 16-17);
    text.md lines 246-299
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in Kilometer mile per hour" |
| LEVEL | 0 to 999 | 0 to 20 | "the incline position from 0 to 20"; preset 0 to 20; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| PACE | 00:00 to 99:99 | 00:00 to 99:99 | "Time to finish 1KM/MILE workout" |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in kilometres or miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**"Incline" and "treadmill" are the spec's words, not the bike's.** The LEVEL row calls the
resistance level an incline position and the PULSE row says "if the treadmill doesn't have a
signal"; this chapter was pasted from a treadmill specification
(`cu800-2012-console-software-modes-idle-child-lock-pause-end-and-reset`). On this bike LEVEL is the
brake resistance.

**Level 0 to 20 here; 1 to 20 on the 2016 XBR25 and XBU55.** The 2016 books of the residential
bikes print the same table with the LEVEL row differing between machines:
`spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20` and
`spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20`.

**A PACE window is unusual on a Spirit bike.** It is in this spec and in the END MODE summary of the
same chapter, and nowhere in the owner's manual.

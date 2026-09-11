---
id: spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20
title: Display and work ranges for each console reading, with a level range of 1 to
  20
kind: spec
question: What are the display ranges for speed, level, time and pulse on a Spirit
  XBR25-2016 or XBU55-2016 bike?
asked_as:
- how many resistance levels does the xbr25 have
- what is the highest pulse the xbu55 console shows
- how long can i set the countdown on the 2016 spirit bike
- what is the lowest level on the xbr25
keywords:
- display range
- work range
- level 1 to 20
- pulse 40 to 220
- laps
- countdown
- calories
- speed
- spec
- eight seconds
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbu55-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
- cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
see_also:
- spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
- spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-xbr-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
source:
  ref: spirit-bike-xbr25-2016-service-manual
  locator: XBR25-2016 section 4 Product Operation, Function, PDF pp. 17-18 (printed
    17-18); text.md lines 251-298. XBU55-2016 PDF pp. 17-18, lines 243-290, identical
    apart from the LEVEL wording quoted
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in mile per hour" |
| LEVEL | 0 to 999 | **1 to 20** | preset 1 to 20; UP or DOWN moves it by 1. The XBR25 book calls it "the level position", the XBU55 book "the incline position" |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**One to twenty, not zero.** The XBR55-2016 and XBR95-2016 books print the same table with a LEVEL
work range of **0 to 20** (`spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20`), and so
does the CU800-2012 (`cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220`). The
software-spec chapter of all four 2016 books says resistance counts up "from 1" in Quick Start
(`spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset`).

**The XBU55 book says "incline" where it means resistance.** It has no incline; the word is the
elliptical spec's. The XBR25 book corrected it to "level" in the first line and left "adjust
incline" in the last.

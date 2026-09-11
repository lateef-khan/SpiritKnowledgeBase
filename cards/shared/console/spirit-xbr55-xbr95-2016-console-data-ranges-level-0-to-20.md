---
id: spirit-xbr55-xbr95-2016-console-data-ranges-level-0-to-20
title: Display and work ranges for each console reading, with a level range of 0 to
  20
kind: spec
question: What are the display ranges for speed, level, time and pulse on a Spirit
  XBR55-2016 or XBR95-2016 bike?
asked_as:
- how many resistance levels does the xbr95 have
- what is the highest pulse the xbr55 console shows
- how long can i set the countdown on the xbr95
- is there a level zero on the xbr55
keywords:
- display range
- work range
- level 0 to 20
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
  - xbr55-2016
  - xbr95-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20
- cu800-2012-console-data-ranges-level-0-to-20-and-pulse-40-to-220
see_also:
- spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20
- spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- spirit-xbr-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: XBR55-2016 section 4 Product Operation, Function, PDF pp. 19-20 (printed
    19-20); text.md lines 268-315. XBR95-2016 PDF pp. 18-19, lines 267-315, word for
    word
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| SPEED | 0.0 to 99.9 | 0.0~99.9 | "the current speed in mile per hour" |
| LEVEL | 0 to 999 | **0 to 20** | "the level position from 0 to 20"; preset 0 to 20; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| LAPS | 0 to 99 | 0 to 99 | total working laps |
| DISTANCE | 00.0 to 99.9 | 00.0 to 99.9 | in miles |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**Zero to twenty here; one to twenty on the XBR25-2016 and XBU55-2016**
(`spirit-xbr25-xbu55-2016-console-data-ranges-level-1-to-20`). The software-spec chapter of all
four books says Quick Start starts resistance "from 1", and the XBR95's own menu tests a brake rather
than a motor, so whether a level 0 exists on the machine is not settled by either book.

**Twenty levels agrees with the owner's manuals**, which describe twenty resistance levels in Quick
Start (`spirit-xe-console-quick-start-with-twenty-resistance-levels`); the ranges, the 8-second
pulse drop-out and the count-down limits are printed only here.

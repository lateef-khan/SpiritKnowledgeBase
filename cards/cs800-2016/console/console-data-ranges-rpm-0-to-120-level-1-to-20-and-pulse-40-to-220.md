---
id: cs800-2016-console-data-ranges-rpm-0-to-120-level-1-to-20-and-pulse-40-to-220
title: 'Display and work ranges for each console reading: RPM works 0 to 120, level
  1 to 20, time to 99:59, calories to 999 and pulse 40 to 220 with an 8-second drop-out'
kind: spec
question: What are the display ranges for RPM, level, time, calories and pulse on
  a Spirit cs800-2016 stepper?
asked_as:
- what is the maximum time i can set on the cs800
- how many resistance levels does the older cs800 have
- why does the pulse on my stepper drop to zero
- rpm range on the spirit stepper console
keywords:
- display range
- work range
- rpm
- level 1 to 20
- time 99:59
- count down 10:00
- calories 999
- pulse 40 to 220
- 8 seconds
- preset
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
- spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- xe195-2016-console-data-ranges-level-1-to-20-and-pulse-40-to-220
see_also:
- spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220
- xe195-2016-console-data-ranges-level-1-to-20-and-pulse-40-to-220
- cs800-2016-console-software-modes-idle-30-minute-sleep-child-lock-quick-start-pause-end-reset
- cs800-2016-console-keys-in-ready-and-run-mode-and-the-display-key-scan-of-seg-time-dist-and-pace
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: CS800-2016 (XS200-SS003) service manual section 4 Product Operation, Function,
    PDF p. 17 (printed 17); text.md lines 270-296
  extracted_at: '2026-09-11'
---

| Reading | Display range | Work range | Notes as printed |
|---|---|---|---|
| RPM | 0 to 888 | **0~120** | "Display the current speed in mile per hour" |
| LEVEL | 0 to 99 | **1 to 20** | preset 1 to 20; UP or DOWN moves it by 1 |
| TIME | 0:00 to 99:99 | 0:00 to 99:59 | count up by default, count down once a time is set; count-down setup range **10:00 to 99:00**; Stop in Run Mode saves the value and the count continues on re-entry |
| CALORIES | 00.0 to 999 | 00.0 to 999 | cumulative |
| PULSE | 0 to 999 | **40 to 220 BPM** | from the hand pulse or the receiver, which needs a chest belt; with no signal for **8 seconds** the value becomes 0 |

**Five readings, not seven.** The elliptical version of this table has SPEED, LAPS and DISTANCE rows
(`spirit-xe-2016-console-data-ranges-level-0-to-20-and-pulse-40-to-220`); this one has RPM in place
of SPEED and no LAPS or DISTANCE row at all, though the console's message window scans a `Dist`
reading and the Function Button page shows one
(`cs800-2016-console-keys-in-ready-and-run-mode-and-the-display-key-scan-of-seg-time-dist-and-pace`).

**"Speed in mile per hour" under RPM is the elliptical spec's sentence left in place.** The display
range of 888 is the three-digit window's every segment; the work range, 0 to 120, is the figure.

**One to twenty, like the XE195-2016 and unlike the XE295, XE795 and XG400 books**, which print a
work range of 0 to 20 (`xe195-2016-console-data-ranges-level-1-to-20-and-pulse-40-to-220`). Twenty
levels agrees with every later CS800 owner's manual.

**"If the bike doesn't have a signal for 8 seconds"** - the pulse row calls the machine a bike; the
8-second drop to 0 is the figure, and it is printed only here for this machine.


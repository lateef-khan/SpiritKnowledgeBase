---
id: spirit-ct800-programs-preset-speed-incline-chart
title: Preset speed and incline values for the Hill, Fatburn, Cardio and Interval
  profiles
kind: fact
question: What speed and incline values does each preset program use on a Spirit treadmill?
asked_as:
- what is the speed profile of the hill program
- how does the fat burn program change incline
- segment by segment program chart
- what incline does the interval program use
keywords:
- preset program chart
- speed incline table
- hill
- fatburn
- cardio
- interval
- p1
- p2
- p3
- segment values
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2012
  - ct800-2016
  - ct800-2020
  - ct850-2016
  - ct850-2018
  - ct850-2020
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900-preset-programs-hill-fatburn-cardio-interval
- ctsbs900-preset-programs-speed-incline-table
see_also:
- spirit-ct800-programs-speed-is-percent-of-top-speed
- spirit-ct800-programs-preset-setup-steps
- ct900ent-hill-program
- ct900-preset-programs-hill-fatburn-cardio-interval
source:
  ref: spirit-treadmill-ct800-2020-owners-manual
  locator: 'printed page 21, Preset Programs Speed/Incline Settings (2012: page 13;
    2016: page 20)'
  extracted_at: '2026-09-09'
---

Speed numbers are a percentage of the top speed you set, not mph - see
`spirit-ct800-programs-speed-is-percent-of-top-speed`. Incline numbers are percent of grade.

**The programme letters differ between generations.** The 2012 and 2016 manuals label the Interval
row **P5** and print no P4 row at all; the 2020 manual labels the same row **P4**. Every number
below is identical in all three manuals.

**What is ambiguous:** the printed header names 26 columns - Warm up, segments 1 to 24, Cool down -
but every Speed and Incline row carries **30 values**. The manuals never say how the four surplus
values map onto the Warm up and Cool down columns, so no segment-by-segment mapping is invented
here. The values below are preserved in the exact left-to-right order printed. To tie one value to
one numbered segment, read the original chart.

```
P1 = HILL
  Speed:   20 30 40 50 60 60 70 70 70 80 80 70 80 80 100 100 70 80 80 70 70 80 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 4 3 3 4 4 5 3 3 4 3 3 4 4 5 4 3 1 1 0 0 0 0

P2 = FATBURN
  Speed:   20 30 40 50 60 60 70 80 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 80 70 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 3 4 5 3 3 4 4 3 3 2 2 3 4 5 6 4 2 1 0 0 0 0

P3 = CARDIO
  Speed:   20 30 40 50 60 60 70 70 70 80 70 70 80 80 60 70 80 80 70 70 70 100 70 80 60 60 50 40 30 20
  Incline: 0 0 0 0 1 1 1 2 2 3 2 2 3 3 1 2 3 3 2 2 4 4 2 3 1 1 0 0 0 0

P5 (2012 and 2016) / P4 (2020) = INTERVAL
  Speed:   20 30 40 50 60 60 70 80 100 60 60 70 80 100 60 70 100 60 70 100 60 70 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 5 6 2 3 5 6 7 2 3 7 2 3 8 2 3 5 4 3 1 0 0 0 0
```

**The CT800ENT manual prints the same explanatory paragraph and the legend P1 = HILL, P2 = FAT BURN,
P3 = CARDIO, P4 = INTERVAL, but its chart of numbers is a graphic that did not survive text
extraction.** No values are recorded for that machine and none may be carried across from this card.

Two other Spirit consoles print charts that look like this one but are **not** the same as recorded:
the CT900 chart (`ct900-preset-programs-hill-fatburn-cardio-interval`) and the CTSBS900 chart
(`ctsbs900-preset-programs-speed-incline-table`) both hold rows of 28 to 29 values where these hold
30, and both cards say their own column alignment is unverified. Do not read a value for one machine
off another machine's card.

**The 2016, 2018 and 2020 CT850 owner's manuals print these same four profiles, value for value**
(all three on printed page 21), and all three label the Interval row **P4**, as the 2020 CT800 manual
does. Their rows carry the same 30 values under the same 26-column header, so the same ambiguity
applies.

**The 2018 CT850 manual prints two further rows this card does not hold** - P5 = Calorie and
P6 = Strength - see `ct850-2018-programs-calorie-strength-speed-incline-chart`. **The CT850ENT manual
prints the same legend P1 = HILL, P2 = FAT BURN, P3 = CARDIO, P4 = INTERVAL but its chart is a
graphic**, so no values are recorded for that machine and none may be carried across.

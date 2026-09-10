---
id: ct850-2018-programs-calorie-strength-speed-incline-chart
title: Preset speed and incline values for the Calorie and Strength profiles
kind: fact
question: What speed and incline values do the Calorie and Strength programs use on
  a ct850-2018 treadmill?
asked_as:
- what is the profile of the strength program
- what does the calorie program do to the incline
- segment by segment chart for calorie and strength
- why does the strength program stay at one incline
keywords:
- preset program chart
- calorie
- strength
- p5
- p6
- speed incline table
- segment values
- percent of top speed
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2018
  applies_to:
  - ct850-2018
  section: programs
  code: '*'
  model_number: '850845'
authority: 3
not_to_be_confused_with:
- spirit-ct800-programs-preset-speed-incline-chart
- ct900ent-preset-speed-incline-chart
see_also:
- spirit-ct800-programs-preset-speed-incline-chart
- spirit-ct800-programs-speed-is-percent-of-top-speed
- ct850-2018-programs-twelve-program-lineup
- ct850-2018-programs-calorie-program-setup
source:
  ref: spirit-treadmill-ct850-2018-owners-manual
  locator: printed page 21, Preset Programs Speed/Incline Settings, rows P5 and P6
  extracted_at: '2026-09-09'
---

**These are the two extra profiles this console prints and the 2016 and 2020 CT850 manuals do not.**
Its Hill (P1), Fatburn (P2), Cardio (P3) and Interval (P4) rows hold exactly the values already
recorded in `spirit-ct800-programs-preset-speed-incline-chart`; only P5 and P6 are new, so only they
are recorded here.

Speed numbers are a percentage of the top speed you set, not mph - see
`spirit-ct800-programs-speed-is-percent-of-top-speed`. Incline numbers are percent of grade.

**What is ambiguous:** the printed header names 26 columns - Warm up, segments 1 to 24, Cool down -
but every Speed and Incline row carries **30 values**. The manual never says how the four surplus
values map onto the Warm up and Cool down columns, so no segment-by-segment mapping is invented
here. The values below are preserved in the exact left-to-right order printed. To tie one value to
one numbered segment, read the original chart.

```
P5 = CALORIE
  Speed:   20 30 40 50 50 60 80 90 100 70 100 70 100 70 100 70 100 70 100 70 100 90 80 70 60 50 50 40 30 20
  Incline: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

P6 = STRENGTH
  Speed:   20 30 40 50 60 60 70 70 80 80 90 90 90 100 100 100 100 100 100 100 100 100 100 90 80 60 50 40 30 20
  Incline: 0 0 0 1 1 1 4 4 4 4 4 4 5 5 5 5 5 5 5 5 3 3 3 3 3 1 1 0 0 0
```

**The Calorie profile runs at zero incline for its whole length.** Every one of its thirty incline
values is 0, so this program changes speed only.

**This manual prints no prose description of either program** - no paragraph saying what Calorie or
Strength is for, the way the 2016 and 2020 manuals describe Hill, Fat Burn, Cardio and Interval.
Other Spirit consoles print such descriptions under the same two names
(`ct900ent-calorie-program`, `ct900ent-strength-program`) but those are different machines with
different segment values; do not carry their profiles across.

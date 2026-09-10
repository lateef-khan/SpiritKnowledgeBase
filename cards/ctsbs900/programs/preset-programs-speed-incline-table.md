---
id: ctsbs900-preset-programs-speed-incline-table
title: Preset programs — speed and incline profile table (Hill, Fatburn, Cardio, Interval)
kind: fact
question: What speed and incline does each CTSBS900 preset program use?
asked_as:
- what does the hill program do at each stage
- how is program speed calculated from my top speed setting
- what incline does the fatburn program use
keywords:
- preset program table
- hill program
- fatburn program
- cardio program
- interval program
- speed percentage
- incline profile
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ctsbs900
  applies_to:
  - ctsbs900
  section: programs
  code: '*'
  model_number:
  - '900885'
authority: 3
not_to_be_confused_with:
- ctsbs900-preset-program-selection-and-setup
see_also:
- ctsbs900-preset-program-selection-and-setup
- ct900-preset-programs-hill-fatburn-cardio-interval
source:
  ref: ctsbs900-om
  locator: p. 26 (PRESET PROGRAMS SPEED / INCLINE SETTINGS)
  extracted_at: '2026-08-24'
---

The preset program Speed and Incline levels are shown in the chart below. The Speed numbers in the chart indicate a **percentage of the top speed of the program** (the user sets the top speed during setup — see [programs/preset-program-selection-and-setup.md](preset-program-selection-and-setup.md)). For instance, the first Speed setting for P1 (Program 1, HILL) shows the number 20 — meaning this segment will run at 20% of the top speed set for the program.

Example: if the user sets the top speed to 15.6 mph, the first segment will be 3 mph (20% of 15.6). Segment 12 shows 100, meaning the speed will be set to 100% of 15.6 mph, i.e. 15.6 mph.

**Legend:** P1 = Hill; P2 = Fatburn; P3 = Cardio; P4 = Interval

The chart's header names 26 columns: Warmup, segments 1 through 24, then Cooldown. Every Speed and
every Incline row prints **30** values, so the Warmup and Cooldown cells each hold more than one
value and the split between them is not recoverable from the print. The rows below are the printed
left-to-right sequences, complete and in order; treat the mapping of a value to a specific numbered
segment as unresolved and read the chart on printed page 26 before programming an exact segment.

```
P1 - Hill
  Speed:   20 30 40 50 60 60 70 70 70 80 80 70 80 80 100 100 70 80 80 70 70 80 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 4 3 3 4 4 5 3 3 4 3 3 4 4 5 4 3 1 1 0 0 0 0

P2 - Fatburn
  Speed:   20 30 40 50 60 60 70 80 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 80 70 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 3 4 5 3 3 4 4 3 3 2 2 3 4 5 6 4 2 1 0 0 0 0

P3 - Cardio
  Speed:   20 30 40 50 60 60 70 70 70 80 70 70 80 80 60 70 80 80 70 70 70 100 70 80 60 60 50 40 30 20
  Incline: 0 0 0 0 1 1 1 2 2 3 2 2 3 3 1 2 3 3 2 2 4 4 2 3 1 1 0 0 0 0

P4 - Interval
  Speed:   20 30 40 50 60 60 70 80 100 60 60 70 80 100 60 70 100 60 70 100 60 70 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 5 6 2 3 5 6 7 2 3 7 2 3 8 2 3 5 4 3 1 0 0 0 0
```

The CTSBS900 owner's manual PDF (source `spirit-treadmill-ctsbs900-owners-manual`, printed page 26)
prints all eight rows as machine-readable text, and every one of them holds exactly 30 values. A row
of any other length is a transcription short of the print.

**The CT900 owner's manual prints these same eight rows, value for value.** What differs between the
two machines is the worked example, not the profile: the CT900 manual works it at a 10 mph top speed
giving 2 mph for the first setting, against 15.6 mph and 3 mph here. See
[`ct900-preset-programs-hill-fatburn-cardio-interval`](../../ct900/programs/preset-programs-hill-fatburn-cardio-interval.md).

The **preset top speed** entered per program limits the highest speed the program will attain during the workout — see step 5 of [programs/preset-program-selection-and-setup.md](preset-program-selection-and-setup.md).

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
authority: 3
not_to_be_confused_with:
- ctsbs900-preset-program-selection-and-setup
see_also:
- ctsbs900-preset-program-selection-and-setup
source:
  ref: ctsbs900-om
  locator: p. 26
  extracted_at: '2026-08-24'
---

The preset program Speed and Incline levels are shown in the chart below. The Speed numbers in the chart indicate a **percentage of the top speed of the program** (the user sets the top speed during setup — see [programs/preset-program-selection-and-setup.md](preset-program-selection-and-setup.md)). For instance, the first Speed setting for P1 (Program 1, HILL) shows the number 20 — meaning this segment will run at 20% of the top speed set for the program.

Example: if the user sets the top speed to 15.6 mph, the first segment will be 3 mph (20% of 15.6). Segment 12 shows 100, meaning the speed will be set to 100% of 15.6 mph, i.e. 15.6 mph.

**Legend:** P1 = Hill; P2 = Fatburn; P3 = Cardio; P4 = Interval

Each program row is structured as: Warmup, segments 1–24, Cooldown (26 values per Speed/Incline row).

**Note on transcription:** The source table is a dense 26-column grid (Warmup + 24 numbered segments + Cooldown) rendered as a small image in the PDF. The digit sequences below are preserved in the exact printed order for each row; however, due to the density of the source table, exact column-by-column alignment against the Warmup/1–24/Cooldown headers could not be independently verified for every cell. If you need to confirm the exact value for one specific segment number, cross-check against the original PDF page 26 table image.

```
P1 - Hill
  Speed:   20 30 40 50 60 60 70 70 70 80 80 70 80 80 100 100 70 80 80 70 70 80 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 4 3 3 4 4 5 3 3 4 3 3 4 4 5 4 3 1 1 0 0 0 0

P2 - Fatburn
  Speed:   20 30 40 50 60 60 70 80 100 100 100 100 100 100 100 100 100 100 100 100 100 100 80 70 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 4 5 3 3 4 4 3 3 2 2 3 4 5 6 4 2 1 0 0 0

P3 - Cardio
  Speed:   20 30 40 50 60 60 70 70 70 80 70 70 80 80 60 70 80 80 70 70 70 100 70 80 60 60 50 40 30 20
  Incline: 0 0 0 0 1 1 1 2 2 3 2 2 3 3 1 2 3 3 2 2 4 4 2 3 1 1 0 0 0

P4 - Interval
  Speed:   20 30 40 50 60 60 70 80 100 60 60 70 80 100 60 70 100 60 70 100 60 70 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 5 6 2 3 5 6 7 2 3 7 2 3 8 2 3 5 4 3 1 0 0 0
```

The **preset top speed** entered per program limits the highest speed the program will attain during the workout — see step 5 of [programs/preset-program-selection-and-setup.md](preset-program-selection-and-setup.md).

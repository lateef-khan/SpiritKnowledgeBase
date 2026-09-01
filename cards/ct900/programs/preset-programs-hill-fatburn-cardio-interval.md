---
id: ct900-preset-programs-hill-fatburn-cardio-interval
title: Preset programs speed and incline chart - Hill, Fat Burn, Cardio, Interval
kind: fact
question: What speed and incline does each CT900 preset program use?
asked_as:
- what is the hill program
- what is the fat burn program
- what is the cardio program
- what is the interval program p4
keywords:
- hill program
- fat burn program
- cardio program
- interval program
- p1
- p2
- p3
- p4
- preset program chart
- speed incline table
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct900-program-options-overview
source:
  ref: ct900-om
  locator: p. 21
  extracted_at: '2026-08-24'
---

**P1 = Hill; P2 = Fat Burn; P3 = Cardio; P4 = Interval**

The preset program Speed and Incline levels are shown in the chart below. The Speed numbers shown in the chart indicate a **percentage of the top speed of the program** (the top speed the user sets during setup - see [program options overview](program-options-overview.md)). For instance, the first Speed setting for P1 (Program 1, HILL) shows the number 20. This means that this segment of the program will have a speed that is 20% of the top speed for the program. If the user sets the top speed to 10 mph, then the first segment will be 2 mph. Segment 12 shows 100, which means the speed will be set to 100% of 10 mph, or simply 10 mph.

Each program has 26 timeline columns: Warmup, segments 1 through 24, then Cooldown.

**A note on the table below**: the source table packs 26 numeric columns per row into a narrow chart. The exact column-by-column alignment of every value to its specific segment number could not be confirmed with full confidence from the source scan (particularly around runs of repeated "100" or "70"/"80" values, where the digit count did not cleanly resolve to exactly 26 per row on recount). The values below are preserved in printed left-to-right order exactly as shown in the source; treat the segment-by-segment mapping as approximate and consult the original PDF (page 21) directly before programming an exact custom segment value.

```
Header: Prog | SEG | Warmup | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | Cooldown

P1 (HILL)
  Speed:   20 30 40 50 60 70 70 70 80 80 70 80 80 100 100 70 80 80 70 70 80 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 4 3 3 4 4 5 3 3 4 3 3 4 4 5 4 3 1 1 0 0 0 0

P2 (FAT BURN)
  Speed:   20 30 40 50 60 70 80 100 100 100 100 100 100 100 100 100 100 100 100 100 100 80 70 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 3 4 5 3 3 4 4 3 3 2 2 3 4 5 6 4 2 1 0 0 0 0

P3 (CARDIO)
  Speed:   20 30 40 50 60 70 70 70 80 70 70 80 80 60 70 80 80 70 70 70 100 70 80 60 60 50 40 30 20
  Incline: 0 0 0 0 1 1 1 2 2 3 2 2 3 3 1 2 3 3 2 2 4 4 2 3 1 1 0 0 0 0

P4 (INTERVAL)
  Speed:   20 30 40 50 60 60 70 80 100 60 60 70 80 100 60 70 100 60 70 100 60 70 80 70 60 60 50 40 30 20
  Incline: 0 0 0 0 1 2 3 5 6 2 3 5 6 7 2 3 7 2 3 8 2 3 5 4 3 1 0 0 0 0
```

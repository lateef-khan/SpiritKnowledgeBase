---
id: f80-2026-program-segment-chart
title: The speed and incline values of every preset segment
kind: spec
question: What speed and incline does each segment use in the preset programs on a
  Sole F80-2026 treadmill?
asked_as:
- what are the incline levels in the hill program
- treadmill program chart speed values
- how steep does the strength program go
keywords:
- segment chart
- speed percentage
- incline level
- warm up
- cool down
- hill
- strength
- intervals
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2026
  applies_to:
  - f80-2026
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2026-preset-pattern-programs
- f80-2026-program-list
- f80-2026-manual-version-and-model
source:
  ref: sole-tm-f80-2026-owners-manual
  locator: page 17, Programs chart
  extracted_at: '2026-09-04'
---

Each cell is **speed \| incline**. **Speed is a percentage of the Max Speed you set before the start;
incline is an absolute level.**

| Position | Hill spd \| inc | Fat Burn spd \| inc | Cardio spd \| inc | Strength spd \| inc | Intervals spd \| inc |
|---|---|---|---|---|---|
| Warm up (1) | 20 \| 0 | 20 \| 0 | 20 \| 0 | 20 \| 0 | 20 \| 0 |
| Warm up (2) | 30 \| 0 | 30 \| 0 | 30 \| 0 | 30 \| 0 | 30 \| 0 |
| Warm up (3) | 40 \| 0 | 40 \| 0 | 40 \| 0 | 40 \| 0 | 40 \| 0 |
| Segment 1 | 50 \| 0 | 50 \| 0 | 50 \| 0 | 63 \| 0 | 50 \| 0 |
| Segment 2 | 50 \| 0 | 50 \| 0 | 50 \| 0 | 63 \| 0 | 50 \| 0 |
| Segment 3 | 63 \| 1 | 63 \| 1 | 63 \| 1 | 63 \| 1 | 63 \| 1 |
| Segment 4 | 75 \| 2 | 63 \| 2 | 75 \| 2 | 75 \| 2 | 75 \| 2 |
| Segment 5 | 75 \| 3 | 100 \| 4 | 75 \| 3 | 75 \| 4 | 88 \| 3 |
| Segment 6 | 75 \| 4 | 100 \| 5 | 88 \| 2 | 75 \| 6 | 63 \| 5 |
| Segment 7 | 88 \| 3 | 100 \| 3 | 75 \| 2 | 75 \| 8 | 63 \| 2 |
| Segment 8 | 75 \| 4 | 100 \| 4 | 75 \| 3 | 88 \| 7 | 88 \| 3 |
| Segment 9 | 88 \| 4 | 100 \| 4 | 88 \| 1 | 88 \| 6 | 63 \| 6 |
| Segment 10 | 88 \| 5 | 100 \| 3 | 63 \| 2 | 88 \| 5 | 75 \| 2 |
| Segment 11 | 100 \| 3 | 100 \| 2 | 75 \| 3 | 100 \| 4 | 100 \| 3 |
| Segment 12 | 75 \| 4 | 100 \| 3 | 88 \| 2 | 88 \| 3 | 63 \| 7 |
| Segment 13 | 88 \| 3 | 100 \| 4 | 75 \| 2 | 88 \| 4 | 75 \| 2 |
| Segment 14 | 75 \| 4 | 100 \| 5 | 75 \| 4 | 88 \| 5 | 100 \| 3 |
| Segment 15 | 88 \| 5 | 100 \| 6 | 100 \| 2 | 75 \| 7 | 63 \| 8 |
| Segment 16 | 88 \| 3 | 88 \| 4 | 75 \| 3 | 75 \| 5 | 75 \| 2 |
| Segment 17 | 75 \| 1 | 75 \| 2 | 88 \| 1 | 75 \| 3 | 88 \| 3 |
| Segment 18 | 63 \| 1 | 63 \| 1 | 63 \| 1 | 63 \| 1 | 63 \| 3 |
| Segment 19 | 50 \| 0 | 50 \| 0 | 50 \| 0 | 63 \| 0 | 50 \| 0 |
| Segment 20 | 50 \| 0 | 50 \| 0 | 50 \| 0 | 63 \| 0 | 50 \| 0 |
| Cool down (1) | 40 \| 0 | 40 \| 0 | 40 \| 0 | 40 \| 0 | 40 \| 0 |
| Cool down (2) | 30 \| 0 | 30 \| 0 | 30 \| 0 | 30 \| 0 | 30 \| 0 |
| Cool down (3) | 20 \| 0 | 20 \| 0 | 20 \| 0 | 20 \| 0 | 20 \| 0 |

**How this table was rebuilt, and what is uncertain.** The printed header row lists 22 labels - "Warm up",
segments 1 to 20, and "Cool down" - but every printed row carries **26 values**. Reading the column
positions of the incline rows against the header shows three values sitting under "Warm up" and three under
"Cool down", which accounts for all 26. The warm-up and cool-down values are printed in the same order here
as on the page, but the manual never numbers them, so the "(1) (2) (3)" labels above are positions in the
printed row, not names the manual uses.

The extraction split every "100" across two lines, as "10" above "0". Those were put back by column position,
which is why Fat Burn carries eleven consecutive 100s and Intervals carries two.

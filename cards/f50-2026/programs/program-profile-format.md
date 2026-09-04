---
id: f50-2026-program-profile-format
title: How to read the speed and incline profile table
kind: definition
question: How do I read the program profile table for a Sole F50-2026 treadmill?
asked_as:
- what does speed percent mean on my treadmill program
- how are treadmill program profiles laid out
- what are the segments in a treadmill program
keywords:
- profile table
- speed percent
- incline
- segments
- warm up
- cool down
- program chart
- columns
- reading the table
facets:
  brand:
  - sole
  product_line: treadmill
  model: f50-2026
  applies_to:
  - f50-2026
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f50-2026-calibration-values
- f50-2026-program-count
- f50-2026-selecting-a-preset-program
source:
  ref: sole-tm-f50-2026-owners-manual
  locator: pages 19 to 20, program profile table
  extracted_at: '2026-09-04'
---

Each of the twelve preset programs is **one pair of rows** in a table whose header reads:

```
program Seg | Warm up | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | Cool down
```

- The upper row of each pair is **Speed%**, the lower row is **Incline**.
- **Every row carries exactly 24 values.** Eighteen of the columns are numbered 1 to 18, which leaves **six** for "Warm up" and "Cool down".
- **The split used on the per-program cards is 3 warm-up columns, 18 numbered segments, 3 cool-down columns.** That is an inference from the arithmetic and from the shape of the data - **every** program starts 20, 30, 40 with incline 0, 0, 0 and ends 40, 30, 20 with incline 0, 0, 0. **The manual does not print column boundaries**, so treat the 3/18/3 split as this repo's reading, not as a printed fact.
- **The manual never states what Speed% is a percentage of, and never gives a unit or a duration for a segment.** The nearest statement is on the selection page: the Speed window "displays the preset max speed of the selected program" and adjusting it "allows you to limit the highest speed the program will reach at its peak". **No conversion from Speed% to mph has been invented here.**
- **Incline values are printed as bare whole numbers with no unit.** They range from 0 to 8 across the twelve programs.

Each program has its own card with its full 24-value profile.

---
id: f65-2026-interval-program-profile
title: 'Interval program: printed speed and incline profile'
kind: spec
question: What is the speed and incline profile of the Interval program on a Sole
  F65-2026 treadmill?
asked_as:
- what is the interval program on a treadmill
- p6 profile on my sole treadmill
- what does the interval program do on my treadmill
keywords:
- interval
- p6 program
- program profile
- speed percent
- incline profile
- segments
- preset program
- workout profile
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2026
  applies_to:
  - f65-2026
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2026-cardio-program-profile
- f65-2026-fat-burn-program-profile
- f65-2026-hill-program-profile
- f65-2026-program-list
- f65-2026-selecting-a-preset-program
- f65-2026-strength-program-profile
source:
  ref: sole-tm-f65-2026-owners-manual
  locator: page 19, program profile table
  extracted_at: '2026-09-04'
---

The console shows this program as **P6**.

**Speed, as a percentage, in printed order:**

```
20 30 40 50 63 75 88 63 63 88 63 75 100 63 75 100 63 75 88 63 50 40 30 20
```

**Incline, in printed order:**

```
0 0 0 0 1 2 3 5 2 3 6 2 3 7 2 3 8 2 3 3 0 0 0 0
```


**The printed table cannot be mapped to its own column headings.** The header row reads **Warm up, 1 to 18, Cool down** - **20 columns** - but **every printed row carries 24 values**. The manual gives no key that resolves the extra four. The values above are reproduced **in their printed order, unchanged**. Do not assume the first four are the warm-up or the last four the cool-down; that mapping is not stated anywhere in the manual.

**Speed is a percentage, not a speed.** It applies to the **preset max speed of the program**, which you set before starting; see `f65-2026-selecting-a-preset-program`.

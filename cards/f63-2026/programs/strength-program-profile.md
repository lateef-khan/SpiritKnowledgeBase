---
id: f63-2026-strength-program-profile
title: 'Strength program: printed speed and incline profile'
kind: spec
question: What is the speed and incline profile of the Strength program on a Sole
  F63-2026?
asked_as:
- what does the strength program do on my treadmill
- p5 profile on my sole treadmill
- how steep does the strength program get
keywords:
- strength
- p5 program
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
  model: f63-2026
  applies_to:
  - f63-2026
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2026-selecting-a-preset-program
- f63-2026-programs
source:
  ref: sole-tm-f63-2026-owners-manual
  locator: page 19, program profile table
  extracted_at: '2026-09-04'
---

The console shows this program as **P5**.

**Speed, as a percentage, in printed order:**

```
20 30 40 63 63 75 75 75 75 88 88 88 100 88 88 88 75 75 75 63 63 40 30 20
```

**Incline, in printed order:**

```
0 0 0 0 1 2 4 6 8 7 6 5 4 3 4 5 7 7 5 1 0 0 0 0
```


**One value in the printed speed row breaks the pattern.** Every other program opens `20 30 40 50`; this one opens `20 30 40 63`. That is what the manual prints.

**The printed table cannot be mapped to its own column headings.** The header row reads `Warm up, 1 to 18, Cool down` - **20 columns** - but every printed row carries **24 values**. The manual gives no key that resolves the extra four. The values above are reproduced **in their printed order, unchanged**. Do not assume the first four are the warm-up or the last four the cool-down; that mapping is not stated anywhere in the manual.

Speed is a **percentage**, not a speed. The preset max speed of the program, which you set before starting, is what the percentage applies to; see `f63-2026-selecting-a-preset-program`.

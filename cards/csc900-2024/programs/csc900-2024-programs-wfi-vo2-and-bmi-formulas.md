---
id: csc900-2024-programs-wfi-vo2-and-bmi-formulas
title: How the stairclimber turns your time and body mass index into an estimated VO2 max
kind: fact
question: How is the VO2 max score calculated on the Spirit csc900-2024 stairclimber?
asked_as:
- how does the stairclimber work out my vo2 max
- what is the vo2 formula
- how is bmi calculated on the stair climber
- what does the fitness test score mean
keywords:
- vo2 max
- vo2 estimation
- formula
- bmi
- body mass index
- stair climber time
- ml/kg/min
- decimal minutes
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: programs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900-vo2max-score-interpretation
- spirit-bike-programs-vo2max-score-charts
see_also:
- csc900-2024-programs-wfi-stairclimber-protocol
- csc900-2024-programs-cpat-stairclimber-protocol
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: printed page 23 (PDF page 25)
  extracted_at: '2026-09-10'
---

**Submax StairClimber Test VO2 estimation:**

```
VO2 Max (ml/kg/min) = 57.774 + (1.757 * TT) - (0.904 * BMI)
```

- **TT** is the Stair Climber Time - the time in minutes and seconds **converted to decimal**
  (the manual's example is **5.87**).
- **BMI** is Body Mass Index.

**Body Mass Index:**

```
BMI = Weight (kg) / Height (m)^2
  or
BMI = 703 x Weight (lbs) / Height (inches)^2
```

This is why the WFI test asks for **height** as well as age and weight - see
`csc900-2024-programs-wfi-stairclimber-protocol`. The console displays the estimated VO2 max during
the cool down.

**The manual prints no score bands.** It never says what VO2 max figure counts as excellent, good or
poor, and the excellent-to-very-poor charts other Spirit manuals print are absent from this book. Do
not carry `ct900-vo2max-score-interpretation` across: that chart belongs to the Gerkin and YMCA
tests, which use a different protocol and a different estimator.

**The CPAT test on the same machine produces no VO2 figure at all** - it is pass/fail.

*The formula lines are printed as a flat image and were read from a 400 dpi render. The BMI line
carries a stray "z" after "Height (m)2" in the print; it is not part of the formula.*

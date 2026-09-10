---
id: spirit-climber-specs-constant-and-isokinetic-fifty-levels
title: Constant and isokinetic resistance with fifty levels of effort
kind: spec
question: What kind of resistance does a Spirit 8.5S or 8.5S-FIT recumbent stepper
  have, and how many levels?
asked_as:
- how many resistance levels on the 8.5s
- what is constant mode on the 8.5s stepper
- is the 8.5s isokinetic
- what is the top level on the 8.5s
keywords:
- isokinetic
- constant
- resistance
- levels
- level range
- effort
- workload
- fifty levels
- rehabilitation
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 85s-2025
  - 85s-fit-2026
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-isokinetic-twenty-levels
- spirit-ce-specs-forty-resistance-levels
- spirit-ce850-specs-twenty-resistance-levels
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
see_also:
- spirit-climber-specs-electromagnet-eddy-current-brake
- spirit-climber-specs-workload-5-to-1000-watts
- spirit-climber-specs-rehabilitation-stepper-specification-page
source:
  ref: spirit-climber-85s-2025-owners-manual
  locator: SPECIFICATIONS, printed p. 59 (PDF p. 61), the Resistance row; the same
    row is 8.5S-FIT-2026 printed p. 50 (PDF p. 52). Both read from a 300 dpi render
    as well as the text layer
  extracted_at: '2026-09-10'
---

**`Constant and Isokinetic with 50 levels of effort`**, word for word on both
specification pages.

**Fifty, not twenty.** This is the only Spirit stepper in the repository with a
fifty-level scale, and the only one that offers **two resistance modes**. Constant
mode holds a set resistance whatever the patient does; isokinetic mode holds the
speed and lets the resistance follow the effort. The MS300, 7.0S and 7.5S of the
same family are isokinetic only, with twenty levels - see
`spirit-climber-specs-isokinetic-twenty-levels`.

## Never quote a level number across the family

| Machine | Levels | Modes |
|---|---|---|
| **8.5S and 8.5S-FIT** | **50** | constant **and** isokinetic |
| MS300, 7.0S, 7.5S | 20 | isokinetic only |
| CS800, CRS800S, XS895 steppers | 20 | ordinary resistance, four bands of five |
| CSC900 stair climber | 20, running backwards | braking falls as the level rises |

Level 40 exists on this machine and on none of the others. A customer who says
their stepper goes to 50 has an 8.5S.

## The brake is not the same either

The fifty-level scale sits behind an **energised electromagnet coil making eddy
currents in the flywheel** - not the gear motor and permanent magnets of the
twenty-level machines. See `spirit-climber-specs-electromagnet-eddy-current-brake`.
That is why the count and the modes could change: it is a different brake, not a
recalibrated one.

## No level-to-watts table is printed

Both books give a **work load of 5 watts up to 1000 watts** as a range and never
say which level produces which wattage. There is no way to answer "how many watts
is level 30" from the manual. See `spirit-climber-specs-workload-5-to-1000-watts`.

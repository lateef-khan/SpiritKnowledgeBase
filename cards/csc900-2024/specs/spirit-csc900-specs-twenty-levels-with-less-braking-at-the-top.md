---
id: spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
title: Twenty levels on which a higher level brakes the stairs less, so they turn faster
kind: spec
question: How many resistance levels does a Spirit csc900-2024 commercial stair climber
  have, and does a higher level make it harder?
asked_as:
- how many levels on the spirit stair climber
- why do the stairs speed up when i raise the level
- what is the top level on the stairclimber
- is level 20 the hardest on the stair climber
keywords:
- resistance levels
- level range
- braking
- steps per minute
- spm
- workload
- intensity
- maximum level
- rotation speed
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-specs-twenty-resistance-levels
- spirit-ce-specs-forty-resistance-levels
- crw800-2024-specs-level-range-1-to-16
see_also:
- spirit-climber-2024-specs-resistance-system
- spirit-climber-specs-no-specification-table
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: Features, printed p. 15 (PDF p. 17), the paragraph beginning "There are
    20 levels of resistance available for plenty of variety"
  extracted_at: '2026-09-10'
---

**20 levels - but they do not mean what twenty levels mean on any other Spirit
machine.** The manual is explicit:

> There are 20 levels of resistance available for plenty of variety. The first
> levels are very easy workloads, and the changes between levels are set to a
> good progression for de-conditioned users. **As the levels increase, the
> braking of the rotating stairs decreases, causing the user to step a faster
> rate, steps per minute (spm).** The highest levels, levels 15-20 are extremely
> challenging. These levels should not be used by deconditioned users as there is
> greater risk of falling off machine when the user cannot keep up with the rate
> of rotation of the stairs. These levels are extremely hard and are good for
> short interval peaks and elite athletic training.

**A higher level releases the brake, it does not apply it.** The staircase turns
faster and the work comes from having to step faster, not from pushing harder.
Every other Spirit machine that prints a level count means the opposite: on an
elliptical, a bike or a stepper the machine "will get harder to pedal as the rows
increase".

**That is a safety warning as much as a specification.** The manual singles out
levels 15 to 20 as a falling risk for a de-conditioned user - the only Spirit
level paragraph in the repository that does. Say so when a customer asks for the
top of the scale.

## Do not answer this from a stepper or elliptical card

The CS800 and CRS800S steppers of the same 2024 range also have 20 levels and
print the familiar four bands - "The first 5 levels are very easy ... Levels 6-10
are more challenging ... Levels 11-15 start getting tough ... Levels 16-20 are
extremely difficult". **This book prints no band edges below 15 at all** - it says
only "the first levels" - and its scale runs the other way. Serving
`spirit-ce850-specs-twenty-resistance-levels` for a stair climber gives a
customer a description that is backwards.

**No resistance figure is printed.** The manual states nothing in watts, newtons
or kilograms and prints no level-to-spm table, so there is no way to say how fast
the stairs turn at a given level. See `spirit-climber-specs-no-specification-table`.

## What is doing the braking

The CSC900 owner's manual prints no parts list, so it never names the brake in a
parts table. Its warranty table warrants a **Generator Brake** as a component in
its own right, and its troubleshooting page describes a **24 V power-failure
brake** and a **magneto wheel** - see `spirit-climber-2024-specs-resistance-system`,
which also records that the troubleshooting page is a flat image read by OCR.

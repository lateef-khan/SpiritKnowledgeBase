---
id: spirit-climber-specs-isokinetic-twenty-levels
title: Isokinetic resistance with twenty levels of effort
kind: spec
question: What kind of resistance does a Spirit MS300, 7.0S or 7.5S rehabilitation
  recumbent stepper have, and how many levels?
asked_as:
- how many resistance levels on the rehab stepper
- what is isokinetic resistance
- is the 7.0s stepper magnetic
- what is the top level on the ms300
keywords:
- isokinetic
- resistance
- levels
- level range
- effort
- workload
- constant speed
- twenty levels
- rehabilitation
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-constant-and-isokinetic-fifty-levels
- spirit-ce850-specs-twenty-resistance-levels
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
- spirit-climber-specs-no-level-count-printed
see_also:
- spirit-climber-specs-rehabilitation-stepper-brake-magnets-on-a-disc
- spirit-climber-specs-workload-5-to-1000-watts
- ms300-2021-specs-workload-5-to-650-watts
- spirit-climber-specs-rehabilitation-stepper-specification-page
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: SPECIFICATIONS, printed p. 41 (PDF p. 43), the Resistance row; the same
    row is 7.5S-2025 printed p. 43 (PDF p. 45) and MS300-2021 printed p. 61 (PDF p.
    61), the last of which is readable only from a 300 dpi render
  extracted_at: '2026-09-10'
---

**`Isokinetic with 20 levels of effort`**, word for word on all five
specification pages.

**Isokinetic is not the same claim as "20 resistance levels" on an elliptical or
a bike.** An isokinetic brake holds the pedal speed rather than the pedal force,
so the level sets the speed the machine will let the patient work at and the
resistance rises to meet whatever they push with. That is why these machines
report **Watts left and right** and a **Symmetry Index** and the fitness machines
do not.

## Three different twenties, and they are not interchangeable

| Machine | What twenty means |
|---|---|
| **MS300, 7.0S, 7.5S** (this card) | **isokinetic** levels of effort, on a rehabilitation machine that reports watts |
| CS800, CRS800S, XS895, CE850, XE and XG | ordinary resistance levels in four bands of five; harder as the number rises - see `spirit-ce850-specs-twenty-resistance-levels` |
| CSC900 stair climber | twenty levels on which a **higher level brakes less**, so the stairs turn faster - see `spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top` |

**Never answer one from another.** The words "20 levels" appear on all five and
describe three different things.

## The 8.5S has fifty, and they are constant as well as isokinetic

The 8.5S and 8.5S-FIT print `Constant and Isokinetic with 50 levels of effort` -
a different brake, a different count and a second resistance mode. See
`spirit-climber-specs-constant-and-isokinetic-fifty-levels`. **Do not tell an
8.5S owner they have twenty levels.**

## The MS300's line is invisible to the text extraction

`pdftotext` returns the word `Resistance` on the MS300's specification page and
then jumps straight to `Work load`, so the extraction reads as though the machine
never states a resistance type. A 300 dpi render of the same page read with
`tesseract --psm 4` returns the full line. **The value above was read from the
picture.** The 7.0S and 7.5S pages have complete text layers and were checked
against renders as well; all five agree.

## The level count is not a workload

The same pages give the work load separately, in watts, and the two machines that
share this resistance row do not share a workload range - the MS300 stops at 650
watts and the 7.0S and 7.5S go to 1000. See
`ms300-2021-specs-workload-5-to-650-watts` and
`spirit-climber-specs-workload-5-to-1000-watts`.

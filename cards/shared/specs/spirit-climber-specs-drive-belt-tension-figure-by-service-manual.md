---
id: spirit-climber-specs-drive-belt-tension-figure-by-service-manual
title: 'Which belt-tension figure each climber service manual prints: 380 N, 320 and
  240 N, 80 N, 190 Hz, a sonic meter with no figure, or none'
kind: spec
question: What belt tension figure does the service manual print for each Spirit stepper,
  climber or stair climber, and in what unit?
asked_as:
- belt tension for the crs800s in newtons
- what hz should the xs895 belt read
- does the cs800 2020 manual give a belt tension
- 7.5s stepper belt tension
keywords:
- belt tension
- drive belt
- poly-v
- 380 n
- 320 n
- 240 n
- 80 n
- 190 hz
- sonic belt tension meter
- j-bolt
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-5s-med
  - 85s-2025
  - crs800s-2021
  - cs800-2016
  - cs800-2021
  - csc880-2025
  - csc900-2019
  - csc900-2024
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-elliptical-specs-drive-belt-tension-figure-by-service-manual
see_also:
- crs800s-2021-maintenance-belt-slippery-front-idle-pulley-allen-wrench-380-n-then-cable-drive-pulley-one-way-bearing
- 7-5s-med-maintenance-belt-slip-584-mm-belt-320-n-and-1032-mm-belt-240-n-then-cable-guide-wheel-one-way-bearing
- 85s-2025-maintenance-belt-slip-idler-screw-clockwise-to-80-n-then-slide-wheel-one-way-bearing
- cs800-2021-maintenance-drive-belt-skidding-j-bolt-nut-13-mm-wrench-no-tension-figure
- cvc800-drive-belt-tension
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 'CRS800S: 9-5 Belt Slippery, PDF p. 41, text.md lines 607-621. 7.5S: 6.9.4,
    PDF p. 35, lines 421-433. 8.5S: 6-9 step 3, PDF p. 36, lines 510-525. XS895: 10-9
    step 6, PDF p. 59, lines 994-1019. CS800-2016 (XS200-SS003): 9-9 step 3, PDF p.
    60, lines 874-880. CS800(2020): 10-9 step 4, PDF p. 54, lines 849-866. CSC880,
    CSC900-2019, CSC900-2022: whole books, loose-word greps for tension, belt, Hz,
    N and newton'
  extracted_at: '2026-09-11'
---

Six of the ten books print a figure; they do not agree on the unit, and the stair climbers print
none. Each figure sits inside a replacement or slipping procedure, never in a table.

| Machine | Figure printed | Unit and gauge | Adjuster |
|---|---|---|---|
| **CRS800S-2021** | **380N** | force, newtons | front idle pulley, Allen wrench |
| **7.5S** | **320N** on the 584L belt, **240N** on the 1032L belt | force, newtons | the socket-head bolt and J bolt of the idler |
| **8.5S** | **80 N** | force, newtons | idler screw, 8 mm hex, clockwise to tighten |
| **XS895** | **190Hz +/- 10Hz** | frequency, "a sonic belt tension meter" | idle wheel assembly |
| **CS800-2016** | **190Hz +/- 10Hz** | frequency, "the sound wave tester ... when the belt vibrates with finger" | M8x9T nut on the idler |
| **CS800-2021** | **none** - "use Sonic belt tension meter to measuring belt tension" | frequency implied, no value | J-bolt nut, 13 mm |
| **CSC880-2025, CSC900-2019, CSC900-2024** | **none** | - | the CSC880 says only "remove the tensioning bolts at the bottom of the belt pressure roller" |

**A newton figure and a hertz figure are not interchangeable**, and the two 190 Hz machines are
different belts on different frames - the figure matches because both books were written from
the same Dyaco template that also gives the CVC800 190 Hz (`cvc800-drive-belt-tension`). **Do not
carry the CS800-2016's 190 Hz to the CS800-2021**; its book deliberately prints no number.

The 7.5S is the only book with two belts and two figures; get the belt length off the belt before
choosing. The 8.5S's 80 N is the lowest figure in the family and is not a misprint for 380 N -
the 8.5S is a different, single-belt drive.

The procedures themselves are on the maintenance cards linked from this card; the elliptical
family's table is `spirit-elliptical-specs-drive-belt-tension-figure-by-service-manual`.


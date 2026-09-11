---
id: cvc800-drive-belt-slipping
title: Drive belt slipping
kind: troubleshooting
question: What do I do when the drive belt slips on a Spirit CVC800 climber, an XS895 stepper
  or the 2016 CS800 stepper, and what tension should it have?
asked_as:
- the climber drive belt is slipping
- how do i tension the climber drive belt
- what tension should the climber drive belt be
keywords:
- drive belt slipping
- J bolt nut
- 13mm wrench
- crank arm bolt
- belt tension
- 190 Hz
- sonic belt tension meter
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - cs800-2016
  - cvc800
  - xs895-2018
  - xs895-2021
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2021-maintenance-drive-belt-skidding-j-bolt-nut-13-mm-wrench-no-tension-figure
- 7-5s-med-maintenance-belt-slip-584-mm-belt-320-n-and-1032-mm-belt-240-n-then-cable-guide-wheel-one-way-bearing
- 85s-2025-maintenance-belt-slip-idler-screw-clockwise-to-80-n-then-slide-wheel-one-way-bearing
- crs800s-2021-maintenance-belt-slippery-front-idle-pulley-allen-wrench-380-n-then-cable-drive-pulley-one-way-bearing
- spirit-cr900-maintenance-belt-slip-jam-nut-220-to-240-newtons
see_also:
- cvc800-drive-belt-drops-off
- cvc800-noise-troubleshooting
- cc81-2020-drive-belt-slipping
- sc200-2016-poly-v-belt-slipping
- spirit-xe-2016-maintenance-belt-slipping-hook-screw-cap-13-mm-190-hz
source:
  ref: spirit-climber-cvc800-service-manual
  locator: Section 10-3 and section 10-5 Troubleshooting for Drive Belt Slipping,
    pp. 49-50 (printed 49-50); tension value from section 9-7, p. 44 (printed 44). Word for word in
    spirit-stepper-xs895-2021-service-manual 9-5, PDF p. 45 (printed 44), text.md lines 699-700, and 9-7,
    PDF p. 47 (printed 46), lines 733-741, with the 190Hz+/-10Hz figure in 10-9 step 6, PDF p. 59 (printed 58),
    lines 1003-1006. The same figures in other words in spirit-stepper-cs800-2016-service-manual 10-3 item 3,
    PDF p. 67 (printed 67), lines 959-960; 11-2 Slip Problem, PDF p. 71 (printed 71), lines 1001-1010; and 9-9
    step 3, PDF p. 60 (printed 60), lines 874-875. All added 2026-09-11.
  extracted_at: '2026-09-08'
---

**The section numbers in the first part of this card are the CVC800 book's; the XS895 and CS800 2016 books,
which print the same adjustment and the same 190 Hz, are numbered below.**

This manual answers drive belt slipping in **two places**, and the two answers are different
adjustments. Do both.

## Section 10-3

"Drive belt slipping problem, please adjust **nut on J bolt with 13 mm wrench**." The J bolt is
the idler wheel assembly's tensioner (section 9-7).

## Section 10-5

"When the unit has Drive belt slipping problem — **Tighten bolt and nut on crank arm.**" and then
"**Adjust drive belt tension with 13 mm wrench.**"

## The tension figure

Section 9-7 gives the target: use a **sonic belt tension meter**; the right value is
**190 Hz +/- 10 Hz**. Rotate the crank afterwards to check that the flywheel, drive belt and drive
pulley operate smoothly. The illustration in section 10-5 shows a tension meter reading 190 Hz
against the belt, which confirms the figure.

Do not carry that number to another machine: the CU900ENT bike gives its drive belt as 180-210 N
and the CE800ENT elliptical as about 185-210 kHz.

A belt that comes off entirely is the neighbouring section — see `cvc800-drive-belt-drops-off`.

## The XS895 book is this book

The XS895 service manual (the XS300B-YS006 book; one machine with two owner's-manual printings, 2018 and
2021) prints sections 9-5 and 9-7 word for word — "Drive belt slipping problem, please adjust nut on J bolt with
13mm wrench" and "Tighten bolt and nut on crank arm. Adjust drive belt tension with 13mm wrench" — and its 10-9
step 6 the same target: "Use a sonic belt tension meter to measure, the right value is **190Hz+/-10Hz**."

## The CS800 2016 book says the same in other words

The CS800 2016 (the XS200-SS003 book) prints it in three places with the same figures:

- **10-3 item 3:** "If the Poly-V Belt is slipping, simply adjust the cap on the hook-type screw with the #13
  wrench" — the hook-type screw is the J-bolt. Item 4: a worn or damaged belt is replaced.
- **11-2 Slip Problem:** "First check the Socket Head Cap Bolt (M8x35mm) and the Nut M8x6.3T on the crank arm
  assembly to see if they are loose", then "The Belt: This is where problem occurs most often because belt gets
  loose after a certain time of operation. **Time duration and body weight are factors** of the cause of the
  problem", with a pointer to the belt disassembly procedure for the adjustment itself.
- **9-9 step 3:** after the idler wheel assembly is installed, "make sure M8x9T nut is so tight that the sound
  wave tester reads **190Hz +/- 10Hz** when the belt vibrates with finger."

**The CS800 (2020) book does not print the figure.** Its 9-3 gives the 13 mm J-bolt nut and sends you to a sonic
meter with no number — `cs800-2021-maintenance-drive-belt-skidding-j-bolt-nut-13-mm-wrench-no-tension-figure`. Do not read 190 Hz onto a machine you are reading from that book. The medical
steppers and the CRS800S set their belts to forces in newtons instead (`7-5s-med-maintenance-belt-slip-584-mm-belt-320-n-and-1032-mm-belt-240-n-then-cable-guide-wheel-one-way-bearing`, `85s-2025-maintenance-belt-slip-idler-screw-clockwise-to-80-n-then-slide-wheel-one-way-bearing`, `crs800s-2021-maintenance-belt-slippery-front-idle-pulley-allen-wrench-380-n-then-cable-drive-pulley-one-way-bearing`).

Sole's CC81 climber and SC200 stepper books are the same Dyaco texts under the other brand
(`cc81-2020-drive-belt-slipping`, `sc200-2016-poly-v-belt-slipping`), as is the Spirit XE 2016 elliptical page
(`spirit-xe-2016-maintenance-belt-slipping-hook-screw-cap-13-mm-190-hz`).

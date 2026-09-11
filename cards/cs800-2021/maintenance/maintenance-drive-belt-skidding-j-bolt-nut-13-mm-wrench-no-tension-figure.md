---
id: cs800-2021-maintenance-drive-belt-skidding-j-bolt-nut-13-mm-wrench-no-tension-figure
title: 'Drive belt skidding: the J-bolt nut with a 13 mm open-end wrench, and no tension
  figure anywhere in the book'
kind: troubleshooting
question: What do I do when the drive belt skids or slips on a Spirit cs800-2021 stepper,
  and what tension should it be?
asked_as:
- cs800 belt is slipping
- how tight should the stepper drive belt be
- drive belt skids under load on the cs800
- what wrench adjusts the belt on the spirit stepper
keywords:
- drive belt
- skidding
- slipping
- j-bolt
- j bolt nut
- 13mm open-end wrench
- idle wheel assembly
- sonic belt tension meter
- no tension figure
- worn belt
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2021
  applies_to:
  - cs800-2021
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- cvc800-drive-belt-slipping
- spirit-ce900-maintenance-belt-slips-or-falls-off-pressure-roller-280-to-310-n
see_also:
- cvc800-drive-belt-drops-off
- cvc800-resistance-not-changing-or-flywheel-noise
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: '9-3 Troubleshooting for Drive Belt, "Drive Belt is Skidding", PDF p. 39
    (printed 38), text.md lines 615-623; 10-9 Idle Wheel Assembly Replacement step
    4, PDF p. 54 (printed 53), line 861; 10-10 steps 4-5, PDF p. 56 (printed 55),
    lines 885-891. The absence of a figure was checked twice: the text.md including
    its 25 OCR supplements searched for Hz, newton, "N " after a number and 190 (the
    only hits are part sizes), and every page of the 56-page PDF was rendered by the
    ingest sweep, which appended a supplement wherever the render knew words the text
    layer did not.'
  extracted_at: '2026-09-11'
---

**This book prints the adjustment and no number.** Its 2016 predecessor for the same machine (the XS200-SS003
book) sets the same J-bolt to **190 Hz ± 10 Hz** on a sound-wave tester (`cvc800-drive-belt-slipping`); the CS800
(2020) book does not repeat that figure or print any other. Do not quote 190 Hz for a machine you are reading from
this book.

9-3 Troubleshooting for Drive Belt, "Drive Belt is Skidding" - as printed:

> To use a **13 mm open-end wrench to adjust the nut of J-Bolt** can fix it.
> If Drive Belt is worn please do the replacement.

The J-bolt is the idle wheel assembly's tensioner. The replacement procedures say the rest:

- **10-9 Idle Wheel Assembly Replacement, step 4:** "Use the nut of J-bolt to adjust drive belt tension then use
  **Sonic belt tension meter** to measuring belt tension" - a meter is named, a reading is not. Step 5: operate the
  crank to make sure the belt is aligned with the drive pulley, flywheel pulley and idle wheel before the covers go
  back.
- **10-10 Flywheel and Drive Belt Replacement, steps 4-5:** if the belt does not run centred on the drive pulley, a
  **17 mm open-end wrench on the flywheel nuts** moves the flywheel until it does; then "adjust the drive belt tension
  with the idle wheel assembly".

**The tension figure is not printed anywhere in the book.**

A belt that has come off the pulley is the first half of the same 9-3 and is carded with the other Dyaco steppers
and climbers that print it (`cvc800-drive-belt-drops-off`). Resistance that will not change, or a noisy flywheel, is
9-2 (`cvc800-resistance-not-changing-or-flywheel-noise`).


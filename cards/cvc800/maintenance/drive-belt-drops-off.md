---
id: cvc800-drive-belt-drops-off
title: Drive belt drops off the pulley
kind: troubleshooting
question: What do I do when the drive belt drops off the pulley on a Spirit CVC800 climber or a CS800
  or XS895 stepper?
asked_as:
- drive belt came off the climber
- belt keeps falling off the pulley
- how do i refit the climber drive belt
keywords:
- drive belt dropping
- belt falls off
- chain cover R
- idler wheel assembly
- drive pulley swings
- flywheel alignment
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - cs800-2016
  - cs800-2021
  - cvc800
  - xs895-2018
  - xs895-2021
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce900-maintenance-belt-slips-or-falls-off-pressure-roller-280-to-310-n
see_also:
- cvc800-drive-belt-slipping
- cvc800-noise-troubleshooting
- cvc800-resistance-not-changing-or-flywheel-noise
- cs800-2021-maintenance-drive-belt-skidding-j-bolt-nut-13-mm-wrench-no-tension-figure
- cc81-2020-drive-belt-dropping
- sc200-2016-poly-v-belt-falls-off
source:
  ref: spirit-climber-cvc800-service-manual
  locator: 'Section 10-3 Troubleshooting for Flywheel and Drive belt, p. 49 (printed
    49). Word for word in spirit-stepper-xs895-2021-service-manual 9-5, PDF p. 45 (printed 44), text.md lines
    708-716. In more words with the 100-120 RPM test: spirit-stepper-cs800-2016-service-manual 10-3 items 1-2, PDF p. 66
    (printed 66), lines 942-953, and spirit-stepper-cs800-2021-service-manual 9-3 "Drive Belt drops from drive pulley",
    PDF p. 39 (printed 38), lines 603-610, with the 17 mm flywheel-nut alignment in its 10-10 step 4, PDF p. 56
    (printed 55), lines 885-886. All added 2026-09-11.'
  extracted_at: '2026-09-08'
---

As printed: "Drive belt dropping problem, please take off chain cover (R) and loosen idler wheel
assembly, and then reassemble the drive belt."

Then check the following, both **with the machine operating at low speed**:

- **a.** Replace the **drive pulley** if it swings too much.
- **b.** If the **drive belt, drive pulley and flywheel are not aligned**, adjust the flywheel to
  make the alignment.

The flywheel is what carries the alignment on this machine: section 9-7 sets flywheel location
with 17 mm box wrenches so the drive belt runs centred on the drive pulley.

A belt that stays on but slips is the neighbouring section — see `cvc800-drive-belt-slipping`.
A belt that has dropped will also usually be reported as a noise — see
`cvc800-noise-troubleshooting`.

## The XS895 and the two CS800 books print it too

The XS895 book's 9-5 is this text word for word, including the two low-speed checks. The CS800 2016 book (10-3
items 1-2) and the CS800 (2020) book (9-3, "Drive Belt drops from drive pulley") say the same thing in more
words and add a test: remount the belt with the idler loosened, rotate slowly to see whether the drive pulley or
the belt runs offset or the belt, drive pulley and flywheel are out of line, **then run at 100-120 RPM** (the 2016
book adds abrupt stops) and check again; if the three are not in a straight line, move the flywheel until they
are — a **17 mm open-end wrench on the flywheel nuts** in the CS800 (2020) book's 10-10. The 2016 book adds that
"adjustments are always made to product ensuring alignment before shipment from factory". A belt that stays on but
skids on the CS800 (2020) is `cs800-2021-maintenance-drive-belt-skidding-j-bolt-nut-13-mm-wrench-no-tension-figure`.

Sole's CC81 and SC200 books are the same texts under the other brand (`cc81-2020-drive-belt-dropping`,
`sc200-2016-poly-v-belt-falls-off`).

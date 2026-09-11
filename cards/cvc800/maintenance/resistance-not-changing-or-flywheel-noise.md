---
id: cvc800-resistance-not-changing-or-flywheel-noise
title: Resistance will not change, or the flywheel makes a noise
kind: troubleshooting
question: Why will the resistance not change, or the flywheel make a noise, on a Spirit
  CVC800 climber or a CS800 or XS895 stepper?
asked_as:
- resistance level does not do anything on the climber
- noise coming from the flywheel
- steel cable came off the flywheel
keywords:
- resistance not functional
- steel cable
- flywheel
- drive pulley
- idle wheel assembly
- friction
- gear motor
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
- cvc800-e-2-tension-motor-error
- cvc800-tension-motor-voltage-test
see_also:
- cvc800-noise-troubleshooting
- cvc800-drive-belt-drops-off
- cs800-2016-maintenance-noise-bearings-flywheel-rear-slide-wheel-corrugated-washer
- sc200-2016-no-resistance-or-flywheel-noise
- cc81-2020-no-resistance-or-flywheel-noise
source:
  ref: spirit-climber-cvc800-service-manual
  locator: 'Section 10-3 Troubleshooting for Flywheel and Drive belt, p. 49 (printed
    49). Word for word in spirit-stepper-xs895-2021-service-manual 9-5, PDF p. 45 (printed 44), text.md lines
    689-704. The same two answers in other words: spirit-stepper-cs800-2021-service-manual 9-2 Troubleshooting for
    the Flywheel, PDF p. 38 (printed 37), lines 584-597; spirit-stepper-cs800-2016-service-manual 10-2 Flywheel Problem,
    PDF p. 65 (printed 65), lines 926-936. All added 2026-09-11.'
  extracted_at: '2026-09-08'
---

The manual gives these two symptoms one heading: "Adjust the resistance level but it is not
functional or some noise comes from Flywheel."

1. **If the gear motor is operating normally**, check that the **steel cable is mounted on the
   flywheel in the right way.**
2. **If there is noise when the flywheel is spinning**, check whether the **flywheel, drive pulley
   and idle wheel assembly are rubbing against each other** and causing the noise, or whether the
   **flywheel makes the noise itself.**

## Rule out the tension motor first

Step 1 begins "If Gear motor is operating normally" — that is a precondition, not a check. If the
resistance is dead rather than merely wrong, the fault may be electronic: this machine reports a
tension motor fault as **E-2** (`cvc800-e-2-tension-motor-error`), and there is a voltage test for
the motor (`cvc800-tension-motor-voltage-test`). This card is the mechanical half, for when the
motor is proven good.

For other noises see `cvc800-noise-troubleshooting`.

## The XS895 and both CS800 books print the same two answers

The XS895's 9-5 opens with this text word for word. The CS800 (2020) book's 9-2 says it as two situations: "The
console can adjust the resistance level and gear motor operates normally, but the resistance doesn't change" —
check the steel cable is mounted on the flywheel; "There is a noise when the flywheel is spinning" — check whether
it comes from the flywheel friction drive pulley or the idle wheel and reinstall those parts by their replacement
steps, and if it is the flywheel itself, replace it. The CS800 2016 book's 10-2 is the same pair in prose: an
unresponsive resistance with a working gear motor is the cable — "check the cable to see if the flywheel is in
place properly or if the cable is loose"; a noisy flywheel is checked with the drive pulley and idler wheel
assembly "for any foreign objects or friction first", taken off and refitted, and replaced if the noise persists.
Sole's SC200 and CC81 books are the same texts under the other brand (`sc200-2016-no-resistance-or-flywheel-noise`,
`cc81-2020-no-resistance-or-flywheel-noise`).

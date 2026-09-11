---
id: cvc800-noise-troubleshooting
title: Tracking down a noise on the climber
kind: troubleshooting
question: What causes a noise on a Spirit CVC800 climber or XS895 stepper, and how do I find it?
asked_as:
- the climber is making a noise
- noise coming from the pedal arm
- what do i check when the climber is noisy
keywords:
- noise
- pedal arm noise
- slide wheel bearing
- bearings on joint areas
- flywheel
- pedals
- defective bearing
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - cvc800
  - xs895-2018
  - xs895-2021
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2016-maintenance-noise-bearings-flywheel-rear-slide-wheel-corrugated-washer
- ct800-2016-maintenance-squeak-thump-or-clicking
see_also:
- cvc800-resistance-not-changing-or-flywheel-noise
- cvc800-drive-belt-drops-off
- cvc800-drive-belt-slipping
- cvc800-screen-does-not-light
- cc81-2020-noises
source:
  ref: spirit-climber-cvc800-service-manual
  locator: Section 10-2 Troubleshooting for Pedal arm, p. 48 (printed 48); section
    10-4 Troubleshooting for Noise, p. 50 (printed 50). spirit-stepper-xs895-2021-service-manual 9-6
    Troubleshooting For Noise, PDF p. 46 (printed 45), text.md lines 719-727, word for word; 9-2 Troubleshooting
    For Pedal arm, PDF p. 42 (printed 41), lines 636-643, with a second bearing; 9-3 Troubleshooting For Connect
    arm, PDF p. 43 (printed 42), lines 649-661, which the CVC800 book lacks. Added 2026-09-11.
  extracted_at: '2026-09-08'
---

## The general checklist (section 10-4)

When the unit has a noise problem, check the following and refer to the matching replacement
steps:

1. **Bearings on joint areas.**
2. **Flywheel.**
3. **Slide wheels.**
4. **Pedals.**

## Noise from the pedal arm (section 10-2)

Printed as its own section: "Noise from Pedal arm. (It usually cause by the bearing is
defective.): **Replace the Slide wheels' bearing.**"

That is the same answer as item 3 of the checklist, stated once more with the cause named. A pedal
arm noise on this machine is a slide wheel bearing until proven otherwise.

## Noise from the flywheel

Item 2 of the checklist has a section of its own, because on this machine flywheel noise shares a
heading with the resistance not changing. See `cvc800-resistance-not-changing-or-flywheel-noise`.

## Noise from the drive belt

A belt that has dropped off or is slipping is a separate pair of sections — see
`cvc800-drive-belt-drops-off` and `cvc800-drive-belt-slipping`.

## The XS895 prints the same list and two more lines

The XS895 book's 9-6 is the four-item checklist word for word. Its 9-2 answers the pedal-arm noise with **two**
bearings, not one: "Replace Pedal arm's bearing. Replace the Slide wheels' bearing." And it has a section this
book lacks, 9-3 Troubleshooting For Connect arm: a noise from the connecting arm is the **rod end bearing** —
"if this bearing has clearance and cause noise please does the replacement" — and "if the noise comes from Pedal
assembly, check **Pedal locking screws are secured, and the top of the assembly is taped foam tapes**." Those are
the only two lines in either book that answer a pedal noise short of replacing the pedal. The CS800 2016 book
answers the same question with a shorter list and a washer to check
(`cs800-2016-maintenance-noise-bearings-flywheel-rear-slide-wheel-corrugated-washer`); Sole's CC81 book is this
text under the other brand (`cc81-2020-noises`).

## The rest of chapter 10 (CVC800 numbering)

Chapter 10 opens with section **10-1 Troubleshooting For Console**, which is not a mechanical
section at all: it covers a dead screen and its answer is console wiring, the power adapter
connector in the DC socket, and the adapter's output voltage. See
`cvc800-screen-does-not-light`. Sections 10-2 to 10-5 are the mechanical ones and are covered by
this card and the three it links to.

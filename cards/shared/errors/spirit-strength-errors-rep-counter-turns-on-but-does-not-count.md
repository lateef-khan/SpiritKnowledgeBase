---
id: spirit-strength-errors-rep-counter-turns-on-but-does-not-count
title: The rep counter lights up with the head plate but counts no reps, and a full
  repetition is the first check
kind: troubleshooting
question: What does a Spirit strength owner's manual say to do when the rep counter
  switches on but does not count repetitions?
asked_as:
- my rep counter turns on but doesnt count
- counter lights up but reps stay at zero
- weight machine counter not counting my reps
- rep counter misses reps on my spirit strength machine
keywords:
- rep counter
- counting reps
- head plate
- reed switch
- magnet
- full repetition
- broken wires
- console
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csd-acbe
  - csd-bcte
  - csd-cpsp
  - csd-itot
  - csd-lelc
  - csd-lpce
  - csd-lpsr
  - csd-pfrd
  - csd-puda
  - css-abdo
  - css-bcur
  - css-bext
  - css-delt
  - css-glut
  - css-latp
  - css-latr
  - css-lext
  - css-lrow
  - css-prlc
  - css-scex
  - css-scpr
  - css-shpr
  - css-slgc
  - css-slgp
  - css-sqsc
  - css-srow
  - css-text
  - css-trot
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- srvo-error-code-table
see_also:
- spirit-strength-errors-rep-counter-and-timer-does-not-turn-on
- spirit-strength-errors-no-mechanical-fault-remedy
- spirit-strength-errors-no-troubleshooting-page-printed
- spirit-strength-csd-warranty-periods-with-counter-timer
source:
  ref: spirit-strength-css-abdo-owners-manual
  locator: TROUBLESHOOTING page, row 2 of 2, printed page 26-33 depending on the book
    (PDF page 26-32); verbatim on all 28 CSS and CSD manuals. Read from the PDF text
    layer on 27 of them and from a 300 dpi tesseract --psm 4 render on CSS-SROW, whose
    PDF carries no text layer on any page; CSS-DELT 2026 revision (spirit-strength-css-delt-owners-manual-2026)
    prints the same two rows, TROUBLESHOOTING, PDF p. 30 (printed 29), text.md lines
    876-897; CSD-CPSP May 2025 update (spirit-strength-csd-cpsp-owners-manual-2025-update)
    the same at PDF p. 32 (printed 31), read from the OCR supplement for page 32 because
    that page has no text layer (both checked 2026-09-11)
  extracted_at: '2026-09-10'
---

**This is the *second* of the two rows the CSS and CSD troubleshooting page prints.** It is the
counter that *works* - it wakes up - but never increments. The counter that stays dark is the other
row, `spirit-strength-errors-rep-counter-and-timer-does-not-turn-on`.

## Problem

**Rep counter turns ON when you pick up the head plate but does not count reps.**

## Solution / Cause, as printed

- **Make sure you are doing a full repetition. Magnet must go up past the counter reed switch and
  back down past it to count ONE repetition.**
- Check for broken or cut wires. If broken or cut wires found, replace the console.

**NOTE: Console includes all wiring.** A replacement console arrives with its loom, so cut or broken
wiring is not a separately ordered part.

## Why the first check is first

The manual puts user technique ahead of hardware here, and the reason is in the sentence itself: the
magnet has to travel **past** the reed switch and **back past it** for the console to score one
repetition. A short, partial rep that never clears the switch is mechanically indistinguishable from
no rep at all, and the console is behaving correctly when it ignores it. That is why this row exists
separately from the dead-counter row - the counter powering up at all proves the magnet, the reed
switch and the batteries are alive.

## What the page does not tell you

The manual prints **no** travel distance for how far past the switch the magnet must go, **no**
position or height for the reed switch, and **no** wiring diagram to trace a cut wire against. There
is no adjustment step: the printed remedy for damaged wiring is to replace the console, not to repair
the loom.

## Scope

All nineteen CSS selectorized single stations and all nine CSD dual stations print this row, word for
word. The other eleven Spirit strength machines print no troubleshooting page at all - see
`spirit-strength-errors-no-troubleshooting-page-printed`.

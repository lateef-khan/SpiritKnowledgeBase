---
id: spirit-strength-errors-rep-counter-and-timer-does-not-turn-on
title: The rep counter and timer does not turn on when weight is lifted, and the four
  checks that follow
kind: troubleshooting
question: What does a Spirit strength owner's manual say to do when the rep counter
  and timer will not turn on as the weight is lifted?
asked_as:
- my rep counter wont turn on when i lift the weight
- the counter on my weight machine is dead
- rep counter and timer not working on my spirit strength machine
- counter doesnt come on when i pull the stack
keywords:
- rep counter
- timer
- reed switch
- magnet
- batteries
- console
- dead display
- not turning on
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
- srvo-display-not-lighting-up
- srvo-error-code-table
see_also:
- spirit-strength-errors-rep-counter-turns-on-but-does-not-count
- spirit-strength-errors-no-mechanical-fault-remedy
- spirit-strength-errors-no-troubleshooting-page-printed
- spirit-strength-csd-warranty-periods-with-counter-timer
source:
  ref: spirit-strength-css-abdo-owners-manual
  locator: TROUBLESHOOTING page, row 1 of 2, printed page 26-33 depending on the book
    (PDF page 26-32); verbatim on all 28 CSS and CSD manuals. Read from the PDF text
    layer on 27 of them and from a 300 dpi tesseract --psm 4 render on CSS-SROW, whose
    PDF carries no text layer on any page; CSS-DELT 2026 revision (spirit-strength-css-delt-owners-manual-2026)
    prints the same two rows, TROUBLESHOOTING, PDF p. 30 (printed 29), text.md lines
    876-897; CSD-CPSP May 2025 update (spirit-strength-csd-cpsp-owners-manual-2025-update)
    the same at PDF p. 32 (printed 31), read from the OCR supplement for page 32 because
    that page has no text layer (both checked 2026-09-11)
  extracted_at: '2026-09-10'
---

**This is the *first* of the two rows the CSS and CSD troubleshooting page prints, and the whole page
is about the rep counter console.** The second row - the counter lights up but never increments - is
`spirit-strength-errors-rep-counter-turns-on-but-does-not-count`.

## Problem

**Rep Counter & Timer does not turn on when weight is lifted.**

## Solution / Cause, as printed

- Replace batteries.
- Check the magnet is still in position and the reed switch is still positioned next to the magnet.
- Check connections at back of console for battery and switch assembly.
- Replace the console.

**NOTE: A console comes with the magnet and reed switch assembly.** So a console ordered as a
replacement part brings a new magnet and a new reed switch with it; they are not ordered separately.

## What the page does not tell you

The manual prints **no** battery type or count on this page, **no** gap figure for how close the reed
switch must sit to the magnet, **no** part number for the console, and **no** meter or continuity
test. The four bullets above are the entire printed remedy - there is no deeper diagnostic step to
escalate to, and the page carries no error code, because these consoles display none.

The order is a replace-then-inspect-then-replace ladder: batteries first because they are the
cheapest thing that fails, then the magnet-and-reed-switch geometry, then the wiring at the back of
the console, and the console itself last.

## Scope

All nineteen CSS selectorized single stations and all nine CSD dual stations print this row, word for
word, on their one troubleshooting page. **The other eleven Spirit strength machines print no
troubleshooting page at all** - the six CSF functional and bench units, the two CSI machines and the
three ST800 units - see `spirit-strength-errors-no-troubleshooting-page-printed`.

Do not answer a Sole SRVO question from this card. The Sole strength range is a servo platform with
hexadecimal fault codes and a different console entirely (`srvo-error-code-table`,
`srvo-display-not-lighting-up`); it is a different brand and nothing filters it out at retrieval.

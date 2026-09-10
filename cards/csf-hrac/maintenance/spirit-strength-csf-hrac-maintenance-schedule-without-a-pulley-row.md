---
id: spirit-strength-csf-hrac-maintenance-schedule-without-a-pulley-row
title: The maintenance schedule with an add-on track to lubricate and no pulley row
  to inspect
kind: procedure
question: What is the preventative maintenance schedule for the Spirit CSF-HRAC, and
  why does it have no pulley inspection row?
asked_as:
- pm schedule for the half rack
- how often do i inspect the pulleys on the csf hrac
- maintenance table for the spirit rack
- what is the add on track on the half rack
keywords:
- preventative maintenance
- half rack
- add on track
- guide rod
- no pulley row
- fasteners
- labels
- bi-monthly
facets:
  brand:
  - spirit
  product_line: strength
  model: csf-hrac
  applies_to:
  - csf-hrac
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-maintenance-schedule-thirteen-actions-daily-to-bi-monthly
- spirit-strength-maintenance-schedule-with-internal-tower-and-add-on-track
- spirit-strength-csf-funt-maintenance-schedule-without-an-upholstery-row
- spirit-strength-csf-uprb-maintenance-schedule-of-six-actions
see_also:
- spirit-strength-maintenance-cables-inspected-weekly-and-before-every-use
- spirit-strength-maintenance-guide-rods-lubricated-monthly-and-no-lubricant-named
- spirit-strength-maintenance-replace-a-frayed-cable-at-first-sign-of-wear
- spirit-strength-maintenance-owner-responsibility-and-repair-log
source:
  ref: spirit-strength-csf-hrac-owners-manual
  locator: 'MAINTENANCE, printed p. 17 (PDF p. 18). Read from the PDF text layer with the tick
    column resolved by character position against the header row, and every row confirmed against
    a 300 dpi render of the same page read with tesseract --psm 4. The absence of the Pulleys row
    was checked on the render specifically, because a missing row in a text layer can be a missing
    glyph rather than a missing line: the render shows Upholstery, Labels, Main Frame, then the
    grey Lubricate band, with no Pulleys line between Labels and Main Frame'
  extracted_at: '2026-09-10'
---

**The CSF-HRAC prints fourteen action rows. Pulleys is not one of them.**

| Action | Daily | Weekly | Monthly | Bi-Monthly |
|---|:---:|:---:|:---:|:---:|
| **Cleaning** | | | | |
| Upholstery | ✔ | | | |
| Handgrips | ✔ | | | |
| Main Frame | | ✔ | | |
| Guide Rod | | | ✔ | |
| **Inspect** | | | | |
| Belt / Cables | | ✔ | | |
| Fasteners | | | ✔ | |
| Handgrips | | | ✔ | |
| Upholstery | | | ✔ | |
| Labels | | | ✔ | |
| Main Frame | | | | ✔ |
| **Lubricate** | | | | |
| Guide Rods | | | ✔ | |
| Add on Track | | | ✔ | |

## Against the range table

- **No `Inspect: Pulleys` row.** Thirty-seven of the thirty-nine strength manuals carry one; this
  one does not.
- **Plus `Lubricate: Add on Track`, monthly** — the row the nine CSD dual-station machines carry.
  This is the only CSF book with it.

So it is the range table with one row removed and one row added, and the removal was checked on the
rendered page rather than inferred from the extraction.

## Do not read a pulley interval onto this machine, and do not stop inspecting the pulleys

Both halves matter. The table gives no interval for pulleys, so there is nothing to quote — but the
same manual's facility precautions still say to *pay close attention to all areas most susceptible
to wear, including (but not limited to) cables, pulleys, belts and grips*, and its SAFEGUARDS page
still says to *check all belts, pulleys and bungee cords regularly for signs of wear, and replace
if needed*. **The obligation is printed; only the interval is missing.** See
`spirit-strength-maintenance-owner-responsibility-and-repair-log` and
`spirit-strength-maintenance-replace-a-frayed-cable-at-first-sign-of-wear`.

## The Add on Track row is undefined here too

As on the CSD machines, the phrase *Add on Track* appears only in this table and nowhere else in
the book — not in the assembly chapter and not in the parts list. Quote the row and the monthly
interval; do not name the part.

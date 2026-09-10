---
id: spirit-xe-maintenance-no-sanitizing-section
title: The maintenance page ends at the leveling pads and prints no sanitizing section
kind: fact
question: Does the Spirit XE195, XE295, XE395, XE395ENT, XE795, XE895 or XG400 owner's
  manual say how to sanitize the machine?
asked_as:
- my manual has no sanitizing page
- how do i disinfect my spirit elliptical
- what cleaner is safe on the xe895
- is there a page about cleaning solution
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2019
  - xe295-2019
  - xe395-2018
  - xe395ent-2021
  - xe795-2018
  - xe895-2018
  - xg400-2019
  section: maintenance
  code: '*'
keywords:
- sanitizing
- disinfect
- isopropyl alcohol
- cleaning solution
- missing section
- printing
- revision
- manual version
- leveling pads
authority: 3
not_to_be_confused_with:
- xe795-2021-maintenance-november-printing-adds-sanitizing
- spirit-xe-maintenance-manual-prints-no-maintenance-section
see_also:
- ct900-sanitizing-equipment
- spirit-xe-maintenance-squeak-thump-or-clicking
- ct800-2016-maintenance-squeak-thump-or-clicking
- spirit-ce-maintenance-no-repair-beyond-this-manual
source:
  ref: spirit-elliptical-xe395-2018-owners-manual
  locator: 'GENERAL MAINTENANCE, printed p. 36, which ends at the Engineering Mode Menu on p. 37 and is followed by the warranty on p. 38. The same shape in spirit-elliptical-xe795-2018-owners-manual printed p. 37 (warranty p. 38), spirit-elliptical-xe895-2018-owners-manual printed p. 35 (warranty p. 37), spirit-elliptical-xe195-2019-owners-manual printed p. 31 (warranty p. 33), spirit-elliptical-xe295-2019-owners-manual printed p. 35 (warranty p. 37) and spirit-elliptical-xg400-2019-owners-manual printed p. 34 (warranty p. 36). Proved three ways for each of the six: the words sanitiz, isopropyl and 75% return zero hits in the whole text.md including its OCR supplements; each table of contents runs GENERAL MAINTENANCE straight into MANUFACTURER''S LIMITED WARRANTY with nothing between; and every page of all six PDFs was extracted individually with pdftotext -layout and none contains the word. For xe395ent-2021 the evidence is the same zero hit across spirit-elliptical-xe395ent-2021-owners-manual and its table of contents, which runs GENERAL MAINTENANCE p. 47 into the warranty p. 48'
  extracted_at: '2026-09-10'
---

**These seven manuals print no sanitizing or disinfecting section.** Their GENERAL MAINTENANCE page
ends at the leveling pads, the Engineering Mode Menu follows, and then the warranty. There is no
alcohol strength, no conditioner note and no support-article link anywhere in the book.

This is an absence in the document, not a statement that the machines must not be sanitized. The
procedure Spirit publishes - a **75% isopropyl alcohol** solution on hard plastics, a conditioner
after sanitizing on upholstered or soft-plastic surfaces - is `ct900-sanitizing-equipment`, which
applies to every Spirit machine. Quote it as Spirit's procedure, not as something this book says.

## The section was added at the 2021 reprint, not at a change of machine

The XE195, XE295 and XG400 are the clearest case, because the same machine has a book on each side
of the change:

| printing | GENERAL MAINTENANCE list | SANITIZING section |
|---|---|---|
| XE395 2018, XE795 2018, XE895 2018 | unchanged | **none** |
| XE195 2019, XE295 2019, XG400 2019 | unchanged | **none** |
| XE195 2021, XE295 2021, XG400 2021 | unchanged | yes |
| XE395ENT 2021 | unchanged | **none** |
| XE795 2021 February | unchanged | **none** |
| XE795 2021 November | unchanged | yes |

**The maintenance list itself did not change.** Checked with difflib at word level, the 2018 and
2019 blocks match their 2021 reprints at 0.983 to 1.000, and every word difflib flags is a place
where `pdftotext` hyphenates across a line rather than a change of wording. 90% of noise calls, 2
leveling pads and a 14mm wrench are the figures in every printing. So a customer whose book has no
sanitizing page has an earlier printing, **not** a different machine and **not** an incomplete
book.

The XE795 of 2021 is the one model id that sits on both sides of the line, because its two 2021
printings differ - `xe795-2021-maintenance-november-printing-adds-sanitizing`. That is why
`xe795-2021` is not listed above.

## Not the same as a manual with no maintenance chapter

The **XE150/XE350/XE550** manual has no maintenance chapter at all - no wipe-down, no noise section
and no leveler count (`spirit-xe-maintenance-manual-prints-no-maintenance-section`). The seven
machines here do have one; it is only the sanitizing page that is missing. The **XE100/XE200/XE300**
and **XE395 2010** manuals also predate the section, and the **2023 XE395 and XE795** print it
inside a two-column Maintenance & Care page rather than under its own heading.

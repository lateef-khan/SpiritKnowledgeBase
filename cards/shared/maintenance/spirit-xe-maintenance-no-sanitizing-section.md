---
id: spirit-xe-maintenance-no-sanitizing-section
title: The maintenance page ends at the leveling pads and prints no sanitizing section
kind: fact
question: Does the Spirit XE195, XE295, XE395, XE395ENT, XE795, XE895, XG400, XBR25,
  XBR55, XBR95 or XBU55 owner's manual say how to sanitize the machine?
asked_as:
- my manual has no sanitizing page
- how do i disinfect my spirit elliptical
- what cleaner is safe on the xe895
- is there a page about cleaning solution
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - xbr25-2019
  - xbr55-2019
  - xbr55-2021
  - xbr95-2016
  - xbr95-2018
  - xbr95-2021
  - xbu55-2019
  - xbu55-2021
  - xe195-2019
  - xe295-2019
  - xe395-2018
  - xe395ent-2021
  - xe795-2018
  - xe895-2018
  - xg400-2019
  - xrw600-2019
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
- cu900ent-general-maintenance
- spirit-2026t-maintenance-post-workout-machine-care
source:
  ref: spirit-elliptical-xe395-2018-owners-manual
  locator: 'GENERAL MAINTENANCE, printed p. 36, which ends at the Engineering Mode Menu on p. 37 and is followed by the warranty on p. 38. The same shape in spirit-elliptical-xe795-2018-owners-manual printed p. 37 (warranty p. 38), spirit-elliptical-xe895-2018-owners-manual printed p. 35 (warranty p. 37), spirit-elliptical-xe195-2019-owners-manual printed p. 31 (warranty p. 33), spirit-elliptical-xe295-2019-owners-manual printed p. 35 (warranty p. 37) and spirit-elliptical-xg400-2019-owners-manual printed p. 34 (warranty p. 36). Proved three ways for each of the six: the words sanitiz, isopropyl and 75% return zero hits in the whole text.md including its OCR supplements; each table of contents runs GENERAL MAINTENANCE straight into MANUFACTURER''S LIMITED WARRANTY with nothing between; and every page of all six PDFs was extracted individually with pdftotext -layout and none contains the word. For xe395ent-2021 the evidence is the same zero hit across spirit-elliptical-xe395ent-2021-owners-manual and its table of contents, which runs GENERAL MAINTENANCE p. 47 into the warranty p. 48. Eight Spirit residential
    XBR/XBU bike owner''s manuals were added in wave 14 on the same three-way proof:
    spirit-bike-xbr95-2016-owners-manual printed p. 35, spirit-bike-xbr95-2018-owners-manual
    p. 35, spirit-bike-xbr95-2021-owners-manual p. 35, spirit-bike-xbr55-2019-owners-manual
    p. 33, spirit-bike-xbr55-2021-owners-manual p. 33, spirit-bike-xbu55-2019-owners-manual
    p. 33, spirit-bike-xbu55-2021-owners-manual p. 33 and spirit-bike-xbr25-2019-owners-manual
    p. 28. For each: saniti, isoprop, alcohol, disinfect, conditioner and 75% return zero
    hits across the whole text.md including its OCR supplements; each table of contents runs
    GENERAL MAINTENANCE straight into MANUFACTURER''S LIMITED WARRANTY with nothing between;
    and every page of all eight PDFs (40, 40, 40, 40, 40, 40, 40 and 36 pages) was extracted
    individually with pdftotext -layout and none contains any of those words. spirit-rower-xrw600-2019-owners-manual
    was added in wave 17 on the same three-way proof: GENERAL MAINTENANCE printed p. 37 (PDF p. 37,
    no offset), saniti, isoprop, alcohol, disinfect, conditioner and 75% return zero hits across the whole
    text.md including its OCR supplements; its table of contents runs GENERAL MAINTENANCE p. 37 straight
    into MANUFACTURER''S LIMITED WARRANTY p. 38 with nothing between; and all 40 pages of the PDF were
    extracted individually with pdftotext -layout and none contains any of those words. The page was also
    read from a 300 dpi render with tesseract --psm 4 (native 151 words, rendered 149), so the section is
    not hiding as a flattened image'
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

## Eight Spirit residential bikes are in exactly the same position

The **XBR95** of 2016, 2018 and 2021, the **XBR55** of 2019 and 2021, the **XBU55** of 2019 and
2021 and the **XBR25 2019** print no sanitizing or disinfecting section either. Their GENERAL
MAINTENANCE page ends at the same two levelling pads (`cu900ent-general-maintenance`), the
Engineering Mode Menu follows, and then the warranty. No alcohol strength, no conditioner note,
no support-article link.

## On the bikes the section arrived in November 2021, not in February

The residential bikes repeat the XE795 pattern, and here it separates two printings of the same
year:

| printing | warranty effective | GENERAL MAINTENANCE list | SANITIZING section |
|---|---|---|---|
| XBR95 2016, XBR95 2018 | Jan 25 2016, Aug 22 2018 | unchanged | **none** |
| XBR25 2019, XBR55 2019, XBU55 2019 | Feb 4 2019 | unchanged | **none** |
| XBR55 2021, XBU55 2021 | **Feb 4 2021** | unchanged | **none** |
| XBR95 2021 | **Mar 16 2021** | unchanged | **none** |
| XBR55ENT, XBU55ENT | **Nov 30 2021** | unchanged | **yes** |
| XBR25 2023, XBR55 2023, XBR95 2023, XBU55 2023 | 2023 | replaced | yes |

**The three February and March 2021 books do not have it and the two November 2021 books do**, so
on the residential bike line the cut-off falls inside 2021, exactly as it does between the
February and November printings of the XE795. **The maintenance list itself did not change across
any of it**: difflib at word level puts all ten blocks between 0.973 and 1.000, and the only
wording difference anywhere is the XBR25 2019 writing "This point cannot be stressed enough" for
"I cannot stress this point enough". 90% of noise calls, 2 levelling pads and a 14 mm wrench in
every printing. A customer whose bike book has no sanitizing page has an earlier printing, not a
different machine and not an incomplete book.

The two ENT books print the four bullets under GENERAL MAINTENANCE on the same page as the
levelling pads; the four 2023 books print them in a two-column Maintenance & Care page beside the
post-workout routine (`spirit-2026t-maintenance-post-workout-machine-care`). **None of the fourteen
prints the wear-parts WARNING** that the treadmill and commercial-bike versions carry - checked for
"susceptible" and "damage and wear" in all fourteen, zero hits; the only "PU wheel" hits are
parts-list rows.

## Not the same as a manual with no maintenance chapter

The **XE150/XE350/XE550** manual has no maintenance chapter at all - no wipe-down, no noise section
and no leveler count (`spirit-xe-maintenance-manual-prints-no-maintenance-section`). The seven
machines here do have one; it is only the sanitizing page that is missing. The **XE100/XE200/XE300**
and **XE395 2010** manuals also predate the section, and the **2023 XE395 and XE795** print it
inside a two-column Maintenance & Care page rather than under its own heading.

## The XRW600 rower repeats the pattern, and its two printings straddle the same cut-off

The **XRW600 2019** owner's manual, warranty effective **February 4 2019**, prints no sanitizing
section: its GENERAL MAINTENANCE page ends at the two levelling pads and the warranty follows.
The **XRW600 2021** printing, warranty effective **November 30 2021**, prints the four sanitizing
bullets on the same page, directly under the levelling pads.

**The maintenance list itself did not change** — difflib puts the two blocks at word level 0.987,
and every flagged word is a place where `pdftotext` breaks a line. So the rower falls exactly where
the XE795 and the residential bikes fall: the section arrived at a **November 2021** reprint, not
at a change of machine. `xrw600-2021` is therefore not listed above.

The CRW800 2021 rower, warranty effective **October 8 2021**, already has the section, so on the
commercial rowers it is in place a month earlier than on the XRW600.


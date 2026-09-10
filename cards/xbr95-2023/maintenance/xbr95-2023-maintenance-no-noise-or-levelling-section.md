---
id: xbr95-2023-maintenance-no-noise-or-levelling-section
title: No noise check, no crank arm nut and no leveller count anywhere in the book
kind: fact
question: What does the Spirit xbr95-2023 recumbent bike owner's manual say to do about
  a squeak, a thump or a bike that rocks?
asked_as:
- my xbr95 squeaks and the manual says nothing
- there is a clicking noise from the bike
- how many levelling feet does the xbr95 have
- the bike rocks on the floor
keywords:
- squeak
- thump
- clicking
- rough feeling
- loose hardware
- crank arm nut
- leveling pads
- levelers
- no troubleshooting section
- missing section
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2023
  applies_to:
  - xbr95-2023
  section: maintenance
  code: '*'
  model_number:
  - '951123'
authority: 3
not_to_be_confused_with:
- cu900ent-general-maintenance
- ct800-2016-assembly-levelling-pads
see_also:
- spirit-residential-bike-errors-2023-troubleshooting-chapter-three-rows
- spirit-2026t-maintenance-post-workout-machine-care
- ct900-sanitizing-equipment
- spirit-bike-maintenance-no-lubricant-belt-or-battery-service
- cu900ent-general-maintenance
source:
  ref: spirit-bike-xbr95-2023-owners-manual
  locator: 'Absence, proved four ways. Its table of contents (printed p. 1, PDF p. 3)
    runs Maintenance & Care 34, Engineering Mode 35, Exploded View Diagram 36, Parts
    List 37, Warranty 41 - and stops. Unlike the XBR25 2023, XBR55 2023 and XBU55 2023
    tables of contents it lists no Troubleshooting entry, and the book ends at the
    warranty. A loose search of text.md, including its OCR supplements, for "crank
    arm nut", "loose hardware" and "troubleshoot" returns zero hits, and the only 90%
    in the book is the heart-rate zone sentence. Its Maintenance & Care page (printed
    34, PDF 36) carries the four-step post-workout routine and the sanitizing bullets
    and nothing else; that page and the Engineering Mode page after it were rendered
    at 300 dpi and read with tesseract --psm 4 - native 185 and 179 words against 183
    and 179 rendered - so neither hides imaged text. Every one of the 48 PDF pages was
    also extracted individually with pdftotext -layout.'
  extracted_at: '2026-09-10'
---

**This manual prints no noise or levelling guidance of any kind.** It never mentions a squeak, a
thump, a click or a rough feeling; it never names the crank arm nut; it gives no leveller count
and no 90% figure; and it has **no Troubleshooting section at all**. The book runs Maintenance &
Care, Engineering Mode, Exploded View, Parts List, Warranty, and ends.

What its maintenance chapter does hold is the four-step post-workout routine
(`spirit-2026t-maintenance-post-workout-machine-care`) and the sanitizing bullets
(`ct900-sanitizing-equipment`), printed side by side on one page.

## The one levelling sentence it does print

Its setting-up chapter (printed p. 13) says only: **"Use a M14 Wrench to adjust the height of the
Leveling Feet."** No count, no direction of turn, no lock nut. That single line is every word this
book contains about levelling.

## The three sibling 2023 bikes do carry the noise checks

The **XBR25 2023**, **XBR55 2023** and **XBU55 2023** manuals were printed in the same style and
in the same year, and each ends with a **Troubleshooting** table that repeats all three remedies -
loose hardware and the 90% figure, the crank arm nut, and 2 levelling pads on the bottom of the
rear stabilizer turned with a 14 mm wrench - under two separate symptom rows, *Squeak, thump,
clicking sound heard* and *Rough feeling when using bike*. See `cu900ent-general-maintenance`
for the remedies and `spirit-residential-bike-errors-2023-troubleshooting-chapter-three-rows` for
the shape of that chapter.
Their Maintenance & Care pages are otherwise the same page as this one, matching at difflib 0.995
to 1.000 once the printed page number is discounted.

**The XBR95's own earlier printings carried the checks too.** The XBR95 of 2016, 2018 and 2021 all
print the full GENERAL MAINTENANCE list - sweat-path wipe, loose hardware, crank arm nut, 2
levelling pads, 14 mm wrench. The 2023 book dropped it and put nothing in its place. So a customer
comparing an older XBR95 manual with this one is not looking at two different machines.

**This is an absence in the document, not a statement that the machine needs no such check.** A
squeaking XBR95 2023 should still be checked for loose assembly hardware and a loose crank arm
nut, and it still has levelling feet. Quote `cu900ent-general-maintenance` as Spirit's procedure
for the line, and say plainly that this machine's own book does not print it.

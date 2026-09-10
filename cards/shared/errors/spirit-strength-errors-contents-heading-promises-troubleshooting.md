---
id: spirit-strength-errors-contents-heading-promises-troubleshooting
title: Three contents pages head a block "Warranty & Troubleshooting" and then list the warranty alone
kind: fact
question: Why does the contents page of a Spirit strength manual say Warranty & Troubleshooting when there is no troubleshooting page in the book?
asked_as:
- contents says troubleshooting but i cant find it
- the index lists warranty and troubleshooting where is the troubleshooting
- missing troubleshooting page in my spirit strength manual
- is a page missing from my spirit manual
keywords:
- contents page
- table of contents
- warranty and troubleshooting
- heading
- missing section
- page numbering
- not printed
- strength
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csf-legp
  - csi-cpsp
  - csi-lrow
  section: errors
  code: no-code
authority: 3
see_also:
- spirit-strength-errors-no-troubleshooting-page-printed
- spirit-strength-errors-resistance-box-cable-jam-over-8-kg
- spirit-strength-warranty-effective-dates
source:
  ref: spirit-strength-csi-cpsp-owners-manual
  locator: 'Contents page, PDF page 3 of the CSF-LEGP, CSI-CPSP and CSI-LROW owner''s manuals; confirmed against a 300 dpi render of the same page and against the page the contents points at.'
  extracted_at: '2026-09-10'
---

**The book is not missing a page. There is no troubleshooting page to find.**

On these three manuals the contents page prints a section heading

> **Warranty & Troubleshooting**

and then lists exactly one entry beneath it:

| Machine | The block, as printed |
|---|---|
| CSF-LEGP | Warranty & Troubleshooting → Warranty 17 |
| CSI-CPSP | Warranty & Troubleshooting → Warranty 48 |
| CSI-LROW | Warranty & Troubleshooting → Warranty 44 |

No troubleshooting entry, no page number for one, and no troubleshooting page anywhere in the book.
The word *troubleshooting* occurs twice in each of the three manuals and **both occurrences are this
heading and its repeat in the running header** - it appears nowhere in the body.

## Why the heading is there

It is boilerplate carried over from the CSS and CSD books, which use the same heading and *do* list a
`Troubleshooting` entry under it. Those twenty-eight print a real one-page Diagnosis Guide. When the
CSF and CSI books were laid out the heading came with the template and the page did not.

The tell is the other five CSF manuals: **CSF-AABB, CSF-BEXT, CSF-FUNT, CSF-HRAC and CSF-UPRB head
the same block simply "Warranty"**, with no mention of troubleshooting. Only CSF-LEGP, of the six
functional and bench machines, carries the longer heading - so within one family, printed within days
of each other, the heading is inconsistent and the content is not.

## What to do instead

Do not send a technician looking for a page-numbering offset, and do not tell them a page is missing
from their copy. For these three machines:

- **CSI-CPSP and CSI-LROW** have exactly one printed fault and remedy, on the assembly page:
  `spirit-strength-errors-resistance-box-cable-jam-over-8-kg`.
- **CSF-LEGP** has none at all.
- All three fall under `spirit-strength-errors-no-troubleshooting-page-printed`, which lists what the
  eleven manuals without a troubleshooting page print in its place.

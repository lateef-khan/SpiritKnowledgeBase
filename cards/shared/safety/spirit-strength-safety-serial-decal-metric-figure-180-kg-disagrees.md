---
id: spirit-strength-safety-serial-decal-metric-figure-180-kg-disagrees
title: The decal that says 180 kg where the manual says 163 kg, on eight machines
kind: fact
question: Why does the label on my Spirit strength machine say 180 kg when the manual
  says 163 kg?
asked_as:
- the sticker and the manual give different weight limits
- label says 180 kg manual says 163 kg
- which weight limit is right the decal or the book
- my machine label says 360 lbs and 180 kg
keywords:
- decal
- serial number label
- 180 kg
- 163 kg
- 360 lb
- contradiction
- which is right
- max user weight
- sticker
- conversion error
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
  - csd-puda
  - css-scpr
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-strength-safety-user-weight-limit-360-lb
- spirit-strength-safety-user-weight-limit-396-lb-label-only
- spirit-strength-safety-product-labels-three-decals
source:
  ref: spirit-strength-csd-acbe-owners-manual
  locator: 'Serial Number Decal on PRODUCT LABELS, printed page 4 (PDF page 5), read
    from 400-500 dpi renders, against SAFETY INSTRUCTIONS item 20 on printed page
    5. CSD-CPSP May 2025 update: Serial Number Decal on PRODUCT LABELS, PDF p. 5 (printed
    4), text.md lines 61-146 and OCR supplement at line 581, read from a 250 dpi render,
    in spirit-strength-csd-cpsp-owners-manual-2025-update. 2025 revision printings, all
    read from 600 dpi renders of PDF p. 5: spirit-strength-csd-acbe-owners-manual-2025-revision
    (text.md lines 112-153); spirit-strength-csd-itot-owners-manual-2025-revision (lines
    112-158); spirit-strength-csd-lelc-owners-manual-2025-february-printing (lines 153-188);
    spirit-strength-csd-lpce-owners-manual-2025-revision (lines 117-168); spirit-strength-csd-puda-owners-manual-2025-revision
    (lines 125-192). CSD-LELC March 2025 printing (already ingested, later than the
    February printing above): spirit-strength-csd-lelc-owners-manual, PDF p. 5, text.md
    line 268, read from a 600 dpi render.'
  extracted_at: '2026-09-17'
---

**Quote 360 lb / 163 kg from the manual. Where a decal says 180 kg, that figure is wrong.**

163 kg is **359 lb**, which is self-consistent with 360 lb. 180 kg is **397 lb**, not 360 lb: the
two halves of a `180 KG / 360 LBS` decal do not convert into each other, and the pound figure is
always the one that agrees with the rest of the book. This is a decal defect that Spirit has been
fixing book by book, not evenly, and not always in the fixed direction — see the CSD-LELC row
below. **Quote 163 kg regardless of which printing the decal figure comes from.**

| Machine | Printing | Decal reads | Verdict |
|---|---|---|---|
| CSD-ACBE | 2024 book (622233_OM_20240325) | `180 KG / 360 LBS` | wrong |
| CSD-ACBE | 2025 revision, v5.0, 04/11/2025 | `163kg / 360lb` | **fixed** |
| CSD-ITOT | 2024 book (648683_OM_20240221) | `180 KG / 360 LBS` | wrong |
| CSD-ITOT | 2025 revision, v4.0, 02/22/2025 | `163kg / 360lb` | **fixed** |
| CSD-LPCE | 2024 book (657233_OM_20240221) | `180 KG / 360 LBS` | wrong |
| CSD-LPCE | 2025 revision, v4.0, 03/03/2025 | `163kg / 360lb` | **fixed** |
| CSD-PUDA | 2024 book (678323_OM_20240619) | `180 KG / 360 LBS` | wrong |
| CSD-PUDA | 2025 revision, v4.0, 15/05/2025 | `163kg / 360lb` | **fixed** |
| CSD-LELC | February 2025 printing, v5.0, 02/20/2025 | `163kg / 360lb` | **fixed** |
| CSD-LELC | March 2025 printing, v5.0, 03/10/2025 (already ingested, the later book) | `180 KG / 360 LBS` | **reverted to wrong** |
| CSD-CPSP | February 2024 book | `180 KG / 360 LBS` | wrong |
| CSD-CPSP | May 2025 update, v5.0, 01/23/2025 | `163kg / 360lb` | fixed |
| CSD-BCTE | (not read in this wave) | `180 KG / 360 LBS` | wrong |
| CSS-SCPR | (not read in this wave) | `180 KG / 360 LBS` | wrong |

**CSD-LELC is the exception to "the later printing is right."** Its February 2025 printing —
version 5.0, revision 02/20/2025 — already carries the fix, but the March 2025 printing —
also version 5.0, revision 03/10/2025, printed three weeks later and the copy already ingested
into this repository — reverts to `180 KG / 360 LBS`. A customer holding the March book has the
older-looking fix undone. Do not use print date as the tie-breaker for this one figure; use the
arithmetic instead, which is unambiguous: 163 kg is correct, 180 kg is not, on every printing of
every one of these machines.

All decal readings above were taken from renders (400-600 dpi), never from the extraction — OCR on
these pages is unreliable for digits.

The two newest CSD manuals, **CSD-LPSR and CSD-PFRD**, print `MAX USER WEIGHT: 163kg / 360lb` on the
decal and have no such disagreement. Neither do the other eighteen CSS machines.

The same 180 kg appears legitimately elsewhere in the range and does not indicate an error there:
the four CSF benches pair it with **396 lb**, which is the correct conversion, and CSF-FUNT pairs it
with 400 lb.

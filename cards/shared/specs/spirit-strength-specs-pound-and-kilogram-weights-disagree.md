---
id: spirit-strength-specs-pound-and-kilogram-weights-disagree
title: On four machines the printed pound and kilogram weights are not the same weight, one of them out by 56 lb
kind: fact
question: Why do the pound and kilogram machine weights in a Spirit strength manual not match, and which figure is right?
asked_as:
- the lb and kg weight on my spirit machine dont match
- spirit strength manual weight conversion wrong
- which weight is correct on the spirit spec table
- 470 lb or 238 kg for the triceps machine
keywords:
- weight
- conversion
- lb
- kg
- mismatch
- contradiction
- specification table
- typo
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - css-abdo
  - css-bcur
  - css-bext
  - css-text
  section: specs
  code: '*'
authority: 3
see_also:
- spirit-strength-specs-machine-weight-and-overall-dimensions
- spirit-strength-specs-product-specifications-table-on-page-eleven
source:
  ref: spirit-strength-css-text-owners-manual
  locator: '"Product Specifications" box, printed page 11 of each of the four manuals, read from each PDF''s own text layer and confirmed against a 300 dpi render.'
  extracted_at: '2026-09-10'
---

**The manual is internally inconsistent on these four machines. Neither figure can be derived from
the other, so quote the unit the customer asked for and say the book disagrees with itself.**

| Machine | Printed | lb converted to kg | kg converted to lb | Gap |
|---|---|---|---|---|
| CSS-TEXT | `470lb / 238.6kg` | 213.2 kg | 526.0 lb | **56 lb** |
| CSS-BCUR | `468.3lb / 236.9kg` | 212.4 kg | 522.3 lb | **54 lb** |
| CSS-BEXT | `530lb / 248kg` | 240.4 kg | 546.7 lb | 17 lb |
| CSS-ABDO | `531 lb / 237kg` | 240.9 kg | 522.5 lb | 9 lb |

Every other machine in the range converts to within a pound or two, so this is four typesetting
errors and not a house rounding convention.

**Which one to trust is not settled by the manual.** For CSS-TEXT and CSS-BCUR the neighbouring
machines are the only cross-check there is: CSS-TROT, built on the same frame and the same 59"
height, is `468.5lb / 212.5kg`, and its two figures agree. That makes the **pound** figure the
plausible one on both, but the manual does not say so - do not present the conversion as the
manufacturer's number.

This is a specification-table defect, not a weight-stack question. The stacks on these four are at
`spirit-strength-specs-stack-of-190-lb`, `spirit-strength-specs-stack-of-270-lb` and
`spirit-strength-specs-stack-of-280-lb`.

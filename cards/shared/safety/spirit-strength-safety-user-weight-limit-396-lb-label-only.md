---
id: spirit-strength-safety-user-weight-limit-396-lb-label-only
title: The bench and leg press limit of 180 kg / 396 lb, which is on the decal and nowhere in the text
kind: spec
question: What is the user weight limit of a Spirit CSF-AABB, CSF-BEXT, CSF-LEGP or CSF-UPRB?
asked_as:
- what is the weight limit on the csf bench
- max user weight for the 45 degree leg press
- how heavy can someone be to use the back extension bench
- user weight limit for the multi purpose bench
keywords:
- user weight limit
- max user weight
- 396 lb
- 180 kg
- serial number decal
- bench
- leg press
- weight capacity
- maximum weight
- label
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csf-aabb
  - csf-bext
  - csf-legp
  - csf-uprb
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-safety-user-weight-limit-360-lb
- csf-hrac-safety-user-weight-limit-330-lb
- csf-funt-safety-user-weight-limit-400-lb
see_also:
- spirit-strength-safety-max-loading-capacity-600-lb
- csf-legp-safety-carriage-max-loading-770-lb
- spirit-strength-safety-serial-decal-fields-en-957-class-s-studio
source:
  ref: spirit-strength-csf-aabb-owners-manual
  locator: Serial Number Decal on PRODUCT LABELS, printed page 4 (PDF page 5), read from a 400 dpi render; SAFETY INSTRUCTIONS item 20, printed page 5
  extracted_at: '2026-09-10'
---

**180 kg / 396 lb** — but only on the serial number decal. On these four CSF machines the manual's
own text prints **no user weight limit at all**: item 20 of the safety instructions and the
safeguards line both give a *load* figure instead, which is a different fact.

| Machine | Serial decal | Item 20 of the safety instructions |
|---|---|---|
| CSF-AABB abdominal crunch board | `MAX USER WEIGHT: 180 KG / 396LBS` | `Max Loading Capacity: 600 lb` |
| CSF-BEXT back extension | `MAX USER WEIGHT 180 KG / 396 LBS` | `Max Loading Capacity: 600 lb` |
| CSF-LEGP 45 degree leg press | `MAX USER WEIGHT ... 180  396` | `Carriage Max Loading Capacity: 770 lb (385 lb per side)` |
| CSF-UPRB multi-purpose bench | `MAX USER WEIGHT 180 KG /396LBS` | `Max Loading Capacity: 600 lb` |

These decal readings come from 300–400 dpi renders of printed page 4; the decal is artwork, so
`pdftotext` returns only fragments of it and one of those fragments reads `MAX USER WEIGHT: 18`.
180 kg is 397 lb, so the decal is self-consistent to within a pound.

**The user limit and the load limit are not the same allowance and must not be swapped.** 600 lb is
what may be loaded onto an AABB, BEXT or UPRB; 396 lb is how heavy the person doing the loading may
be. Give both when someone asks "how much will it take".

CSF-BEXT is the *functional* back extension bench. CSS-BEXT is a different machine, a selectorized
back extension with a 360 lb limit.

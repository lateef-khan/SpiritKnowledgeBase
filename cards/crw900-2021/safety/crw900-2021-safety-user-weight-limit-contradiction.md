---
id: crw900-2021-safety-user-weight-limit-contradiction
title: The manual prints 450 lbs in its text and 330 lbs on the machine's own serial decal
kind: spec
question: What is the user weight limit of a Spirit CRW900 water rower (crw900-2021)?
asked_as:
- how much weight can the crw900 hold
- max user weight for the water rower
- am i too heavy for the crw900
- weight capacity of the crw900
keywords:
- weight limit
- maximum user weight
- 450 lbs
- 330 lbs
- 150 kg
- 204 kilograms
- capacity
- how heavy
- serial decal
- contradiction
facets:
  brand:
  - spirit
  product_line: rower
  model: crw900-2021
  applies_to:
  - crw900-2021
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-safety-user-weight-limit-450-lbs
- spirit-rower-safety-user-weight-limit-350-lb
- spirit-climber-safety-user-weight-limit-330-lb
- 85ue-2025-safety-user-weight-limit-440-lbs
see_also:
- crw900-2021-safety-warning-labels-and-serial-decal
- spirit-water-rower-safety-safeguards-list
source:
  ref: spirit-rower-crw900-2021-owners-manual
  locator: SAFEGUARDS, printed page 16, and the SERIAL NUMBER DECAL reproduced on WARNING LABELS
    AND COMMUNICATION STICKERS, printed page 15 (PDF page 15), read from a 300 dpi render
  extracted_at: '2026-09-10'
---

**The manual gives two different figures and never reconciles them.**

| Where | Figure |
|---|---|
| SAFEGUARDS list, printed page 16 | `The maximum weight for individuals riding the rower should not exceed 450 lbs (204 kilograms).` |
| SERIAL NUMBER DECAL, printed page 15 | `MAX USER WEIGHT : 150 kg / 330lbs` |

**They are not a rounding difference.** 450 lbs is 204 kg and 330 lbs is 150 kg; each pair converts
correctly on its own. The two statements are 120 lb / 54 kg apart.

**The decal is the label on the machine.** The page reproducing it is a flat image - `pdftotext`
returns the caption and nothing from inside the decal - so the figure was read from a **300 dpi
render** of PDF page 15. The same decal reads `MODEL NUMBER : CRW900`, `CLASS : SC`,
`SERIAL NUMBER: CRW90018120001` and `MADE IN TAIWAN`, and carries the CE, TÜV and GS marks
(`crw900-2021-safety-warning-labels-and-serial-decal`).

**Give the customer both figures and say which is which.** The lower one is what is printed on the
machine they own; the higher one is what the book's safety chapter says. Nothing in the manual
states which governs, and inventing a resolution would be inventing a fact.

**The CRW800H2O sits between them and settles nothing.** The other Spirit water rower's SAFEGUARDS
list prints `should not exceed 350 lbs.` in the same position on its page, with no metric figure and
no decal reproduction (`spirit-rower-safety-user-weight-limit-350-lb`). The two water rowers'
safety chapters are otherwise 93.3% identical at word level, and the weight figure is one of only
four substantive differences between them.

**Do not fill the gap from the CRW800 cards.** The CRW800-2021 and CRW800-2024 air rowers print a
clean `User Weight Limit: 450 lb` with no metric figure and no decal
(`spirit-ct800-safety-user-weight-limit-450-lbs`). That 450 agrees with this manual's text by
coincidence of number, not by evidence about this machine.

**Do not reach for the stair climber card either.** The Spirit CSC880-2025 prints
`330 lb / 150 kg` as its own single figure (`spirit-climber-safety-user-weight-limit-330-lb`); that
is a different machine whose two statements agree.

---
id: xt-2023-errors-trips-onboard-15-amp-breaker
title: The treadmill trips its own on-board 15 amp circuit
kind: troubleshooting
question: Why does a Spirit CT800, CT850 or XT treadmill trip its own on-board 15
  amp circuit?
asked_as:
- the breaker on the treadmill itself keeps popping
- treadmill trips its own 15 amp breaker
- machine cuts out and the breaker on the front pops
keywords:
- 15 amp
- on board breaker
- trips
- belt deck friction
- deck cleaning
- amp draw
- deck wear
- flip the deck
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2012
  - ct800-2016
  - ct800-2020
  - ct800-2024
  - ct850-2018
  - ct850-2024
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2013
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2010
  - xt685-2015
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900ent-trips-20-amp-circuit
- ct850-2020-trips-onboard-20-amp-circuit
- ct850-2016-trips-onboard-10-amp-circuit
- f65-2016-trips-onboard-15-amp-breaker
see_also:
- ct900ent-treadbelt-stops-suddenly-when-tether-pulled
- xt-2023-errors-house-breaker-trips
- xt-2023-maintenance-belt-and-deck-cleaning
- xt-2023-safety-afci-gfci-nuisance-tripping
- xt685-2023-flipping-a-worn-deck
source:
  ref: spirit-treadmill-xt185-2023-owners-manual
  locator: page 43, TROUBLESHOOTING - Service Checklist Diagnosis Guide, row "Treadmill
    trips on board 15 amp circuit"; the same row is page 51 in the XT285 manual, page
    56 in the XT385 and XT485 manuals and page 55 in the XT685 manual; the identical
    row is in the Service Checklist Diagnosis Guide on page 31 of the XT185 2015 manual,
    page 39 of the XT285, page 41 of the XT385, page 45 of the XT485 and page 46 of
    the XT685; both ENT manuals print the same table - Service Checklist Diagnosis
    Guide on printed page 54 of the XT485ENT owner's manual (its table of contents
    lists TROUBLESHOOTING as page 55), text.md lines 1040-1082, and on printed page
    56 of the XT685ENT owner's manual, text.md lines 1664-1695; the same row is Service
    Checklist - Diagnosis Guide on printed page 23 of the CT800 2012 owner's manual
    (text.md lines 1018-1022), printed page 39 of the CT800 2016 owner's manual (text.md
    lines 1013-1017) and TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 43 of the
    CT800 2020 owner's manual (text.md lines 1112-1116); the CT850 2018 owner's manual
    prints the same row in SERVICE CHECKLIST - DIAGNOSIS GUIDE on printed page 42
    (text.md lines 1072-1076); the same row is Service Checklist - Diagnosis Guide
    on printed page 31 of the XT685 2010 owner's manual (PDF page 35, text.md lines
    1420-1424); service manuals - XT285 2015 service manual 10-2 Service Troubleshooting
    Checklist, PDF p. 70-71 (printed 64-65), text.md lines 1433-1503; XT385 2015 service
    manual 10.2 Service Troubleshooting Checklist, PDF p. 69-70, text.md lines 1158-1222;
    XT485 2015 service manual 10.2 Service Troubleshooting Checklist, PDF p. 70-71,
    text.md lines 1166-1230; CT800 2016 service manual 9.1 Service Troubleshooting
    Checklist, PDF p. 61-62 (printed 60-61), text.md lines 1222-1273; the CT900ENT
    service manual prints the 15 amp row in the second copy of its checklist on PDF
    p. 58; XT485 2013 owner's manual (spirit-treadmill-xt485-2013-owners-manual, 485812)
    SERVICE CHECKLIST - DIAGNOSIS GUIDE, PDF p. 33 (printed 32), text.md lines 1286-1346,
    the "Treadmill trips on board 15 amp circuit" row
  extracted_at: '2026-09-09'
---

The printed cause is **high belt/deck friction**, and the manuals send the reader to the
Maintenance & Care section.

**Which manual prints the second step.** The longer answer reads: if cleaning does not
prevent this from reoccurring, check the amp draw of the motor; if this is high and there
are signs of significant wear of the deck, the deck may need to be flipped if it is on its
original side.

- **All five 2015 manuals** print it - XT185, XT285, XT385, XT485 and XT685 alike.
- **Of the 2023 manuals, only the XT685** prints it. The 2023 XT185, XT285, XT385 and XT485
  manuals stop at the friction line.

That is the 2023 document being briefer, not those machines behaving differently - the 2015
manual for the same model prints the full answer.

**This is the breaker on the treadmill, not the one in the house.** The house breaker
tripping while the treadmill's own breaker holds is a different row with a different answer:
check that the treadmill is the only appliance on the circuit (`xt-2023-errors-house-breaker-trips`).

Two look-alikes worth keeping apart: the Spirit CT900ENT trips a **20 amp** on-board circuit
(`ct900ent-trips-20-amp-circuit`), and the Sole cards for a 15 amp on-board breaker answer
with **lubrication** (`f65-2016-trips-onboard-15-amp-breaker`), which these Spirit manuals
never ask for - they ask for the deck to be cleaned.

**Three CT800 generations print the long answer, and the fourth changed the rating.** The
CT800 2012, 2016 and 2020 owner's manuals all print the amp-draw check and the "if it is on
its original side" qualifier against a 15 amp circuit. The **CT800ENT 2022** manual prints
the identical cause and remedy against a **20 amp** circuit, so it sits on
`ct900ent-trips-20-amp-circuit` instead. The rating is the only thing that changed across the
four generations.

**The 2010 XT685 owner's manual prints the long answer against a 15 amp circuit as well**, so
on that model the rating and both steps are unchanged across 2010, 2015 and 2023. That 2010
document is an OCR recovery in which the rating reads `|5 amp`, the scanner's rendering of the
digit 1; the XT685 2015 and 2023 manuals and the CT800 2012, 2016 and 2020 manuals all print
15 amp in the same row, which is what confirms the figure.

**One CT850 generation belongs here, and the other three do not.** The **CT850 2018** owner's
manual prints the long answer - the amp-draw check and the "if it is on its original side"
qualifier - against a **15 amp** circuit. The CT850 2016, CT850 2020 and CT850ENT 2022 owner's
manuals print the identical cause and remedy against a **20 amp** circuit
(`ct850-2020-trips-onboard-20-amp-circuit`), and the CT850 2016 *service* manual prints a
**10 amp** circuit with no remedy beyond the friction line
(`ct850-2016-trips-onboard-10-amp-circuit`). Only the rating moves.

**Both ENT manuals print the second step.** The XT485ENT and XT685ENT each carry the amp-draw
check and the "if it is on its original side" qualifier.

For the XT685ENT that agrees with its base XT685-2023 manual. **For the XT485ENT it does
not**: the base XT485-2023 manual stops at the friction line. The rule stated above - that of
the 2023 manuals only the XT685 prints it - does not hold once the ENT documents are counted.

**The CT800 2024 and CT850 2024 owner's manuals print this row with both steps** - the friction
line and the amp-draw and deck-wear check, the `if it is on its original side` qualifier included -
and send the reader to their **Machine Care** chapter rather than to *Maintenance & Care*.

**The two ENT treadmills of the same 2024 family print 20 amp in this row, not 15**, so do not
carry this card to a CT800ENT 2024 or CT850ENT 2024: `ct900ent-trips-20-amp-circuit`.

**The service manuals print the row shorter.** The 2015 XT285, XT385 and XT485 and the CT800 2016 service checklists say `High belt/deck friction. See General Maintenance section on Belt/Deck Lubrication.` against the same 15 amp circuit - lubrication rather than deck cleaning, and no amp-draw step. The XT485ENT service manual prints the row against a **10 amp** circuit (`ct850-2016-trips-onboard-10-amp-circuit`), and the 2023 XT service manuals have no checklist.

**The XT485 2013 owner's manual prints the shortest version of all** - *Treadmill trips on board 15 amp circuit: High belt/deck friction. See General Maintenance* - with no amp-draw check and no deck flip, against the same 15 amp rating (added 2026-09-11).


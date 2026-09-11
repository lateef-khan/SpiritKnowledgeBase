---
id: ct900ent-circuit-breaker-trips-not-treadmill-breaker
title: Circuit breaker trips, but not the treadmill circuit breaker
kind: troubleshooting
question: Why does the house breaker trip on a Spirit CT800, CT800ENT, CT850, CT900ENT,
  4.0T or XT treadmill when the machine's own breaker does not?
asked_as:
- my house breaker keeps tripping when i use the treadmill
- why does the wall breaker trip but not the treadmill breaker
- breaker trips on startup
keywords:
- circuit breaker trips
- facility breaker
- high inrush current
- breaker keeps tripping
- house breaker
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 40t-2026
  - ct800-2012
  - ct800-2016
  - ct800-2020
  - ct800-2024
  - ct800ent-2022
  - ct800ent-2024
  - ct850-2024
  - ct850ent-2024
  - ct900ent
  - xt285-2015
  - xt385-2015
  - xt485-2015
  - xt485ent-2023
  - xt685-2010
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xt-2023-errors-house-breaker-trips
see_also:
- ct900ent-electrical-requirements-gfci-breakers
source:
  ref: ct900ent-om
  locator: p. 48; the 4.0T 2026 owner's manual prints the same row in its TROUBLESHOOTING
    table on printed page 45; all four CT800 owner's manuals print the same row -
    Service Checklist - Diagnosis Guide on printed page 23 of the 2012 manual (text.md
    lines 1029-1030), printed page 38 of the 2016 manual (text.md lines 994-995),
    TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 42 of the 2020 manual (text.md
    lines 1093-1094) and TROUBLESHOOTING on printed page 52 of the CT800ENT 2022 manual
    (text.md lines 1182-1183). The XT685 2010 owner's manual prints the same row in
    Service Checklist - Diagnosis Guide on printed page 31 (PDF page 35, text.md lines
    1432-1434); service manuals - XT285 2015 service manual 10-2 Service Troubleshooting
    Checklist, PDF p. 70-71 (printed 64-65), text.md lines 1433-1503; XT385 2015 service
    manual 10.2 Service Troubleshooting Checklist, PDF p. 69-70, text.md lines 1158-1222;
    XT485 2015 service manual 10.2 Service Troubleshooting Checklist, PDF p. 70-71,
    text.md lines 1166-1230; XT485ENT 2023 service manual 10.2 Service Troubleshooting
    Checklist, PDF p. 64-65, text.md lines 981-1045; CT800 2016 service manual 9.1
    Service Troubleshooting Checklist, PDF p. 61-62 (printed 60-61), text.md lines
    1222-1273; CT800 2020 service manual 8-5 TROUBLESHOOTING, PDF p. 45 (printed 44),
    text.md lines 631-660; CT800ENT 2022 service manual 8-7 Troubleshooting, PDF p.
    39, text.md lines 791-819; CT900ENT service manual Service Troubleshooting Checklist
    (first printing), PDF p. 50-51, text.md lines 848-900; 4.0T 2026 service manual
    TROUBLESHOOTING, PDF p. 35 (printed 46), text.md lines 523-566
  extracted_at: '2026-08-24'
---

**Problem:** Circuit breaker trips, but not the treadmill circuit breaker.

**Cause / fix:** Need to replace the facility breaker with a "high in-rush current" type breaker. The 2026 4.0T prints the same row, worded "Need to replace the breaker with a 'High Inrush
current' type breaker." This is not a warranty defect — see the full explanation in [Electrical requirements - GFCI outlets and circuit breakers](../safety/electrical-requirements-gfci-breakers.md).

**All four CT800 generations print this row with the same answer**, worded "Need to replace
the breaker with a 'High In-rush current' type breaker", and each adds a pointer to its own
electrical instructions rather than repeating them: page 3 in the 2012, 2016 and 2020
manuals, page 4 in the CT800ENT 2022 manual. **The other half of this fact is on that
electrical page**, which is where the manuals put the reason (a treadmill's inrush current),
the statement that this is not a warranty defect, and the example part numbers. Neither half
is complete on its own.

**The XT685 changed its answer to this row after 2010, and only the 2010 machine belongs
here.** The XT685 **2010** owner's manual gives the high-inrush answer - *Need to replace the
breaker with a "High In-rush current" type breaker (see page 3 for details)* - word for word
as the CT800 manuals do. The XT685 **2015** and **2023** manuals print the same condition with
a completely different remedy: check that the treadmill is the only appliance on the circuit,
and neither of them names a breaker type at all
(`xt-2023-errors-house-breaker-trips`). Two different fixes for one symptom on one model, so
answer by the machine's generation and never carry either remedy across 2010.

The 2010 XT685 is the first XT machine on this card, and the statement on
`xt-2023-errors-house-breaker-trips` that no XT manual mentions a breaker type holds for the
2015 and 2023 revisions only.

**All four 2024 New Black treadmills print this row**, and the two halves of the family word it
differently. The CT800 2024 and CT850 2024 say `Need to replace the breaker with a "High In-rush
current" type breaker` and add `See "Electrical Safety" section for more details`. The CT800ENT
2024 and CT850ENT 2024 say `Need to replace the **house** breaker with a "High inrush current" type
breaker` and give no pointer. Same remedy; only the ENT books name whose breaker it is.

**The XT service manuals give the high-inrush answer, not the owner's-manual one.** The 2015 XT285, XT385 and XT485 and the XT485ENT service checklists print `Need to replace the house breaker with a "High inrush current" type breaker (see section 7.2 for Important Electrical Instructions)`, and their section 7.2 names the Grainger 1D237 and Square D QO120HM examples. The owner's manuals of the same four machines say only to check that the treadmill is the only appliance on the circuit (`xt-2023-errors-house-breaker-trips`). So for those machines the service document and the owner's document give different remedies for one symptom; the service document's is the one that names a part. The CT800 2016, CT800 2020, CT800ENT 2022, CT900ENT and 4.0T service manuals print the same high-inrush row as their owner's manuals.

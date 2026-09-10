---
id: ct900ent-trips-20-amp-circuit
title: Treadmill trips on board 20 amp circuit
kind: troubleshooting
question: Why does a Spirit treadmill trip its own onboard 20 amp circuit breaker?
asked_as:
- treadmill breaker keeps tripping on the machine itself
- the treadmills own circuit breaker trips
keywords:
- trips 20 amp circuit
- onboard breaker trips
- high friction
- amp draw
- motor
- deck wear
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 40t-2026
  - ct800ent-2022
  - ct800ent-2024
  - ct850ent-2024
  - ct900ent
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xt-2023-errors-trips-onboard-15-amp-breaker
see_also:
- ct900ent-belt-deck-cleaning
- ct900ent-circuit-breaker-trips-not-treadmill-breaker
source:
  ref: ct900ent-om
  locator: p. 48; the 4.0T 2026 owner's manual prints the same row in its TROUBLESHOOTING table on printed page 45; the CT800ENT 2022 owner's manual prints the same row in its TROUBLESHOOTING table on printed page 52 (text.md lines 1191-1192).
  extracted_at: '2026-08-24'
---

**Problem:** Treadmill trips on board 20 amp circuit (the treadmill's own onboard breaker, not the facility breaker — see [Circuit breaker trips, but not the treadmill circuit breaker](circuit-breaker-trips-not-treadmill-breaker.md) for that separate situation).

**Cause / fix:** High belt/deck friction. See [Belt and deck cleaning](../maintenance/belt-deck-cleaning.md). If cleaning doesn't prevent this from reoccurring, check the amp draw of the motor. If it is high and there are signs of significant wear of the deck, it may need to be flipped on its original side.

The 2026 4.0T prints this row word for word, including the "on its original side"
condition. So does the **CT800ENT 2022** owner's manual.

**The CT800ENT is the only CT800 generation with a 20 amp on-board breaker in this row.**
The 2012, 2016 and 2020 CT800 manuals print the identical cause and remedy against a **15
amp** circuit (`xt-2023-errors-trips-onboard-15-amp-breaker`). The rating is the only thing
that changed.

**The CT800ENT 2024 and CT850ENT 2024 owner's manuals print this row** with the friction cause, the
deck-cleaning remedy and the deck-wear check, the `if it is on its original side` qualifier
included, on printed page 59.

**Their non-ENT siblings in the same 2024 family print 15 amp in this row**, not 20:
`xt-2023-errors-trips-onboard-15-amp-breaker`.

---
id: ct850-2020-trips-onboard-20-amp-circuit
title: The treadmill trips its own onboard 20 amp circuit
kind: troubleshooting
question: Why does a Spirit CT850 or CT850ENT treadmill trip its onboard 20 amp circuit?
asked_as:
- treadmill keeps tripping its own breaker
- onboard breaker pops on my spirit treadmill
- machine breaker trips while running
keywords:
- onboard breaker
- 20 amp
- belt friction
- deck friction
- deck wear
- flip the deck
- tripping
- cleaning
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct850-2016
  - ct850-2020
  - ct850ent-2022
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ct850-2016-trips-onboard-10-amp-circuit
see_also:
- ct850-2016-trips-onboard-10-amp-circuit
- ct850-2016-house-breaker-trips-not-treadmill-breaker
- ct850-2016-running-deck-belt-and-cushion-replacement
- ct900ent-trips-20-amp-circuit
- xt-2023-errors-trips-onboard-15-amp-breaker
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-6 TROUBLESHOOTING, page 46 (printed 45) of the CT850 2020 service
    manual; three of the four CT850 owner's manuals print the same row against the same
    20 amp rating - TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 43 of the 2016
    manual (text.md lines 1109-1113) and of the 2020 manual (text.md lines 1108-1112),
    and TROUBLESHOOTING on printed page 52 of the CT850ENT 2022 manual (text.md lines
    1197-1198)
  extracted_at: '2026-09-08'
---

| Problem | Solution/cause |
|---|---|
| Treadmill trips on board 20 amp circuit | High belt/deck friction. See General Maintenance section on cleaning the deck. If cleaning doesn't prevent this from reoccurring, check to see if there is significant wear of the deck. If so, the deck may need to be flipped if it is on its original side. |

**Three of the four CT850 owner's manuals print this row against the same 20 amp rating** -
the 2016, the 2020 and the CT850ENT 2022 - and all three add one step this service-manual row
does not have:

> High belt/deck friction. See General Maintenance. If cleaning doesn't prevent this from
> reoccurring, **check the amp draw of the motor**. If this is high and there are signs of
> significant wear of the deck, it may need to be flipped if it is on its original side.

The fourth, the **CT850 2018** owner's manual, prints the identical cause and remedy against a
**15 amp** circuit, so it sits on `xt-2023-errors-trips-onboard-15-amp-breaker`. The rating is
the only thing that changed.

**The CT850 2016 *service* manual prints this row as a 10 amp circuit** and gives only the
words `High belt/deck friction`, with no cleaning or deck-flip advice - so for the 2016
machine the service and owner's documents disagree about the rating. See
`ct850-2016-trips-onboard-10-amp-circuit`.

The CT800ENT, CT900ENT and 4.0T manuals print the 20 amp row too, carded separately as
`ct900ent-trips-20-amp-circuit`.

If the *house* breaker trips and this one does not, that is a different row:
`ct850-2016-house-breaker-trips-not-treadmill-breaker`. The deck cleaning, deck wear check and deck
flip this row asks for are on `ct850-2016-running-deck-belt-and-cushion-replacement`.

---
id: sb600-2023-errors-er-on-the-recovery-screen-heart-rate-undetected
title: ER on the Recovery screen means the heart rate was undetected or only intermittent
kind: troubleshooting
question: Why does the console show ER when I press Recovery on an Xterra sb600-2023
  recumbent bike?
asked_as:
- sb600 shows er after recovery
- xterra recumbent er on screen
- recovery button gives er
- what does er mean on my xterra bike
keywords:
- er
- error
- recovery
- heart rate
- undetected
- intermittent
- handgrips
- chest strap
- recumbent
facets:
  brand:
  - xterra
  product_line: bike
  model: sb600-2023
  applies_to:
  - sb600-2023
  section: errors
  code: er
  model_number:
  - '160113'
authority: 3
not_to_be_confused_with:
- trx2500-2024-errors-er-incline-vr-out-of-range
- xterra-treadmill-errors-incline-er-no-vr-change-when-incline-runs
- spirit-xic600-errors-id-er-sync-timeout
see_also:
- sb600-2023-errors-no-heart-rate-reading-connectors-then-hand-grip-wiring-continuity
source:
  ref: xterra-bike-sb600-2023-owners-manual
  locator: SB600 OM RECOVERY POST WORKOUT, Note and Figure 48, PDF p. 38 (printed
    37); text.md lines 933-954
  extracted_at: '2026-09-11'
---

**This is `ER` on the SB600 console's Recovery screen, and it means no usable pulse - not the incline `ER`
of the Xterra treadmills and not the Spirit XIC600's pairing `ER`.**

The Recovery function needs a heart rate to score. You keep holding the handgrips and press RECOVERY; every
function stops except Time, which counts down from 00:60 to 00:00, and the screen then grades your recovery
from F1 (quickest, "best") to F6 (slowest). The book's note:

> If the heart rate is undetected or connected only intermittently, then the display will show "ER"
> (Error). (Figure 48)

So `ER` is the console saying it could not hold a pulse for the sixty seconds. Keep both hands on the grips
for the whole countdown, or wear the chest strap, and run it again; nothing is broken. What to check when
the grips never read a pulse at all is the service manual's page
(`sb600-2023-errors-no-heart-rate-reading-connectors-then-hand-grip-wiring-continuity`).


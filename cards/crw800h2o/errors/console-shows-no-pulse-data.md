---
id: crw800h2o-console-shows-no-pulse-data
title: The console shows no pulse data
kind: troubleshooting
question: Why does the console show no heart rate on a Spirit CRW800H2O rower?
asked_as:
- no heart rate on my spirit rower
- chest belt not reading on the rower
- what chest strap works with a spirit rower
keywords:
- no pulse
- heart rate
- chest belt
- 5.0khz
- analogue
- telemetry
- rower
- strap
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800h2o
  applies_to:
  - crw800h2o
  section: errors
  code: no-code
  model_number: '800998'
authority: 3
not_to_be_confused_with:
- crw900-2021-errors-heart-rate-signal-drops-during-the-stroke
see_also:
- crw900-2021-errors-heart-rate-signal-drops-during-the-stroke
- spirit-wireless-chest-belt-no-pulse
- ce800ent-bluetooth-chest-strap-no-heart-rate
- crw800h2o-console-shows-no-data
source:
  ref: spirit-rower-crw800h2o-service-manual
  locator: Section 2 Q&A, Console Error, page 21
  extracted_at: '2026-09-08'
---

The manual's answer, word for word:

> Check if use a 5.0KHZ chest belt, you must wear chest belt correctly.

Two things follow from that one line.

- The console reads a **5.0 kHz analogue** chest belt. A Bluetooth or ANT+ strap will not read on it.
- Wearing it correctly means skin contact and the right way up.

**This manual names no battery type and no working range.** The other five Spirit commercial manuals
answer the same question with a CR2032 cell and a 3-foot range - see
`spirit-wireless-chest-belt-no-pulse` - but that is a different console and those figures are not
printed here. The CE800ENT elliptical is the only one of the six that documents a **Bluetooth** strap:
`ce800ent-bluetooth-chest-strap-no-heart-rate`.

This rower has no hand pulse row at all.

**The CRW900, the other Spirit water rower, asks for 5.3 KHz, not 5.0** -
`crw900-2021-errors-heart-rate-signal-drops-during-the-stroke`. Two water rowers, two frequencies;
quote each machine's own figure.

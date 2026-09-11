---
id: erg550w-2023-errors-console-cannot-get-pulse-data-5-0-khz-chest-belt
title: 'The console cannot get pulse data: it needs a 5.0 kHz chest belt, worn correctly'
kind: troubleshooting
question: Why does the console show no heart rate on an Xterra erg550w-2023 water
  rower, and which chest belt works?
asked_as:
- xterra water rower no heart rate
- what chest strap works with an erg550w
- rower pulse stays blank
- bluetooth strap not reading on my xterra rower
keywords:
- no pulse
- no heart rate
- chest belt
- chest strap
- 5.0 khz
- analogue
- telemetry
- water rower
facets:
  brand:
  - xterra
  product_line: rower
  model: erg550w-2023
  applies_to:
  - erg550w-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- erg700-2022-errors-wireless-heartbeat-no-effect-strap-worn-within-3-feet-cr2032
- erg750w-2025-errors-no-heart-rate-exchange-the-wireless-transmitter-battery
see_also:
- erg550w-2023-errors-console-shows-no-data-full-stroke-of-1-m-then-batteries-wires-two-magnets
- erg700-2022-errors-wireless-heartbeat-no-effect-strap-worn-within-3-feet-cr2032
- crw800h2o-console-shows-no-pulse-data
source:
  ref: xterra-rower-erg550w-2023-service-manual
  locator: ERG550W SM 1.Q&A, Q "The console can not get pulse data", PDF p. 19, text.md
    lines 254-281; ERG550W OM PULSE paragraph ("Wireless chest strap sensor sold separately"),
    PDF p. 19 (printed 17), lines 671-708
  extracted_at: '2026-09-11'
---

The service manual's answer, word for word:

> Check if use a 5.0KHZ chest belt, you must wear chest belt correctly.

Two things follow. The console reads a **5.0 kHz analogue** chest belt - a Bluetooth or ANT+ strap will not read on it - and wearing it correctly means skin contact and the right way up. The owner's manual says only that the wireless chest strap sensor is sold separately.

**This book names no battery and no working range**, unlike the ERG700's strap row, which gives a CR2032 cell and 3 feet (`erg700-2022-errors-wireless-heartbeat-no-effect-strap-worn-within-3-feet-cr2032`), and the ERG750W's, which says to exchange the transmitter battery (`erg750w-2025-errors-no-heart-rate-exchange-the-wireless-transmitter-battery`). Those figures are those machines'.

**The ERG600W, this rower's sibling, asks for 5.3 kHz, not 5.0** - its owner's manual says the Recovery function "works with a 5.3 KHz chest strap heart rate monitor" (ERG600W OM PDF p. 22). Two water rowers, two frequencies, each printed in its own book; quote each machine's own. The Spirit CRW800H2O service manual gives 5.0 kHz in the same words for its own rower (`crw800h2o-console-shows-no-pulse-data`).

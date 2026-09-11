---
id: air650-2021-errors-no-speed-on-the-display-sensor-within-3-mm-of-its-magnet
title: 'No speed on the display: keep the speed sensor within 3 mm of its magnet,
  then test the sensor cable with another magnet'
kind: troubleshooting
question: Why does the console show no speed on an Xterra air650-2021 air bike, and
  what gap should the speed sensor have?
asked_as:
- air650 shows no speed
- xterra airbike rpm stays at zero
- air bike speed sensor gap
- how far should the sensor be from the magnet on the air650
keywords:
- no speed
- speed sensor
- magnet
- 3 mm
- gap
- cables
- reed switch
- another magnet
- air bike
facets:
  brand:
  - xterra
  product_line: bike
  model: air650-2021
  applies_to:
  - air650-2021
  section: errors
  code: '*'
  model_number:
  - '165718'
authority: 2
not_to_be_confused_with: []
see_also:
- ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm
- spirit-bike-errors-no-speed-readout-hall-sensor-or-magnet-test-with-another-magnet
- sb600-2023-errors-no-speed-reading-cables-behind-the-chain-covers-then-a-test-magnet
source:
  ref: xterra-bike-air650-2021-service-note
  locator: 'AIR650 service note (scan), PDF pp. 1-2, OCR; text.md lines 5-28: ''See
    Spirit AB900 Service Manual'', differences Blue Tooth No, iron-net wind cover,
    connecting-arm cover. The fact itself is in AB900 SM 9-1, the entry headed "Q
    No heart rate is displayed", which is the speed entry, PDF p. 48; text.md lines
    790-808'
  extracted_at: '2026-09-11'
---

**The AIR650 has no service manual of its own.** The manufacturer's service note for it reads *See Spirit AB900 Service Manual* and lists the only differences: the AIR650 has **no Bluetooth**, no iron-net wind cover and no connecting-arm covers. Everything below is the AB900 book's text, applied to the AIR650 by way of that note.


Section 9-1, printed under the heading *Q: No heart rate is displayed* - **the heading is wrong; the answer
is about speed**, and the book has no hand-grip heart-rate Q&A because the bike has no grip sensors (its
chest-strap rows are in the lookup table).

1. Console is displaying but without speed showing. **Check the speed sensor cable and magnet to keep the
   gap distance less than 3 mm.**
2. If installation is OK, normally there is a problem with **cables (23)**. **Use another magnet to determine
   if there is a problem with cables (23).** Either way, cables (23) require replacement.

**The figure is 3 mm.** Cables (23) is the speed sensor with its cable - the book's circuit diagram labels
it `RPM SENSOR (REED SWITCH)` and `SENSOR WIRE`. The SB600 recumbent's service book gives the same
test-magnet step without a gap
(`sb600-2023-errors-no-speed-reading-cables-behind-the-chain-covers-then-a-test-magnet`).

The Spirit AB900 card holding the same page is `ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm`.


---
id: xterra-trx-specs-driver-board-led-locations-power-led3-and-info-led-on-the-b017d
title: 'Two driver-board LEDs: a power LED called LED3 in the middle of the board,
  and an INFO LED to its right by the incline VR socket'
kind: spec
question: Where are the indicator LEDs on the driver board of an Xterra TRX treadmill
  in the TRX3500 and TRX4500 service manual, and which is which?
asked_as:
- trx3500 controller led locations
- where is the info led on the trx4500 board
- trx3500 driver board power light
keywords:
- driver board
- led
- indicator
- power led
- info led
- location
- lower controller
- b017d
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx3500-2024
  - trx4500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx2500-2024-specs-driver-board-led-locations-led1-communication-led2-power-led3-speed
- trx1400-2023-specs-driver-board-led-locations-power-led-and-info-led
- trx5500-2024-specs-driver-board-led-location-a-single-power-led
see_also:
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: TRX3500/TRX4500 SM '6.5 Driver Board LED Indicator Locations', PDF p. 33
    (printed 32), lines 492-508; read from the 110 dpi render
  extracted_at: '2026-09-11'
---

The LED-locations page is the **MODEL: B017D** photograph with two callouts:

| Callout as printed | Where on the board |
|---|---|
| **LED3**: Power directive LED. When treadmill power, LED will be blazed. | centre of the board, right of the transformer, on the row of small components below the black pin strip |
| It is a signal indicate LED, the INFO LED does not light represent the lower control board was not Received upper console board signal. | right side, just above the white INC VR socket |

So this board has a **power LED** (the page calls it LED3) and an **INFO LED**; the debugging table on the next page
names them POWER and INFO. There is no speed LED and no communication LED by those names - the INFO LED is the
console-link indicator. The TRX2500 book's board locates three LEDs (power, communication, speed feedback) and the
TRX5500's a single power LED; each has its own card. What the LEDs mean as fault indicators is the errors section's.

---
id: trx1400-2023-specs-driver-board-led-locations-power-led-and-info-led
title: The driver board has two indicators, a Power LED and an INFO LED, side by side
  at the lower right beside the main-control header
kind: spec
question: Where are the indicator LEDs on the driver board of an Xterra trx1400-2023
  treadmill?
asked_as:
- trx1400 controller led locations
- where is the info led on the trx1400 board
- trx1400 driver board power light
keywords:
- driver board
- led
- indicator
- power led
- info led
- location
- lower controller
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- tr260-2023-specs-driver-board-led-location-a-single-speed-led
- trx2500-2024-specs-driver-board-led-locations-led1-communication-led2-power-led3-speed
- xterra-trx-specs-driver-board-led-locations-power-led3-and-info-led-on-the-b017d
see_also:
- trx1400-2023-specs-driver-board-b307d-wire-connections
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM (T3-NT053-01) '6.5 Driver Board LED Indicator Locations', PDF
    p. 31 (printed 29), lines 451-464; read from the 110 dpi render
  extracted_at: '2026-09-11'
---

The LED-locations page is the B307D photograph with two callouts on the lower right of the board, between the
transformer and the 5-pin main-control header:

- **Power LED** - the left of the two, beside the small electrolytic capacitors;
- **INFO LED** - to its right, nearer the incline VR and speed-sensor sockets.

That is all this book locates: no speed LED, no incline up/down LEDs. What the two mean - the Power LED is on whenever
the DC supply is normal; the INFO LED lights only when the lower board is linked to the console - is the "Controller
Indicator LED debugging" table on the next page, which the errors section holds. The GT90 boards of the TRX2500,
TRX3500/4500 and TRX5500 books place and name their LEDs differently.

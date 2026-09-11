---
id: trx2500-2024-specs-driver-board-led-locations-led1-communication-led2-power-led3-speed
title: 'Three driver-board LEDs: the power LED at the top right by the motor terminals,
  the communication LED below it, and the speed-feedback LED at the bottom right by
  the speed-sensor socket'
kind: spec
question: Where are the three indicator LEDs on the driver board of an Xterra trx2500-2024
  treadmill, and which is which?
asked_as:
- trx2500 controller led locations
- which led is the power led on the trx2500 board
- trx2500 speed feedback led
- trx2500 communication led
keywords:
- driver board
- led
- indicator
- power led
- communication led
- speed led
- location
- lower controller
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx2500-2024
  applies_to:
  - trx2500-2024
  section: specs
  code: '*'
  model_number:
  - '125817'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-driver-board-led-locations-power-led3-and-info-led-on-the-b017d
- trx1400-2023-specs-driver-board-led-locations-power-led-and-info-led
- trx5500-2024-specs-driver-board-led-location-a-single-power-led
see_also:
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM (GT90B-NT022) '6.5 Driver Board LED Indicator Locations', PDF
    p. 28 (printed 27), lines 424-455; read from the 110 dpi render
  extracted_at: '2026-09-11'
---

The LED-locations page is the driver-board photograph with three callouts:

| Callout as printed | Where on the board |
|---|---|
| **LED2**: Power directive LED. When treadmill power, LED will be blazed. | top right, beside the M+ terminal |
| **LED1**: Communication directive LED. When during signal communication from consol to lower controller, the LED1 will be flashed. | right side, below LED2, by the blue torque trimmer |
| **LED3**: The Speed feedback, when speed signal output, the LED2 will be flashed. | bottom right, beside the white speed-sensor socket |

**The LED3 caption says "the LED2 will be flashed"** where it means LED3; the callout points at the LED by the
speed-sensor socket. The numbering LED1/LED2/LED3 follows the silkscreen, not the top-to-bottom order.

What each LED means as a fault indicator - the "Controller Indicator LED debugging" table on the next page - is the
errors section's card. The TRX3500/4500 book's board (B017D) names its LEDs differently and is on its own card.

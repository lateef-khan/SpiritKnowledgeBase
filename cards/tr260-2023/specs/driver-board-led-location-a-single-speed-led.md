---
id: tr260-2023-specs-driver-board-led-location-a-single-speed-led
title: The driver board has one indicator, the SPEED LED, beside the main-control
  and speed-sensor sockets
kind: spec
question: Where is the indicator LED on the driver board of an Xterra tr260-2023 treadmill?
asked_as:
- tr260 controller led location
- where is the speed led on the tr260 board
- tr260 driver board indicator light
keywords:
- driver board
- led
- indicator
- speed led
- location
- motor controller
- calibration
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx2500-2024-specs-driver-board-led-locations-led1-communication-led2-power-led3-speed
- trx1400-2023-specs-driver-board-led-locations-power-led-and-info-led
see_also:
- tr260-2023-specs-driver-board-b407d-sockets-acn-acl-to-m-plus
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM (GT75A-NT050) 'Driver Board LED Indicator Locations', PDF p. 23
    (printed 23), lines 325-336; read from the 110 dpi render
  extracted_at: '2026-09-11'
---

The LED-locations page is the B407DV12 photograph with a single callout, **SPEED LED**, pointing at a small LED on
the lower right of the board, between the row of electrolytic capacitors and the black 5-pin main-control header,
just left of the white speed-sensor socket.

That is the only indicator this book locates - no power LED, no communication LED, no incline up/down LEDs. What the
SPEED LED means (it blinks in calibration when the sensor reads speed) is the "Controller Indicator LED debugging"
table on the next page, which the errors section holds. The GT90 boards of the TRX books carry two or three named
LEDs on their own cards.

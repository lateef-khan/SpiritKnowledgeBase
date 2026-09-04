---
id: srvo-controller-cn7-encoder-pinout
title: Pinout of CN7, the SRVO encoder port
kind: spec
question: What is the pinout of the encoder port on a SOLE SRVO controller?
asked_as:
- srvo encoder connector pinout
- srvo encoder wiring
- how many pins on the srvo encoder plug
keywords:
- cn7
- encoder port
- pinout
- differential
- channel a
- channel b
- index
- 5v
- eight pin
- controller module
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: cn7
authority: 3
not_to_be_confused_with:
- srvo-display-board-speaker-port-pinout
- srvo-controller-cn6-rs485-pinout
see_also:
- srvo-controller-connector-map
- srvo-encoder-location
- srvo-error-0x400000-encoder-not-connected
source:
  ref: sole-srvo-service-manual
  locator: page 38, section 8-2-4
  extracted_at: '2026-09-04'
---

**This is CN7 on a controller module, the encoder port. It is not CN7 on the display main board, which is the right speaker port.**

| Pin | Name | Description |
|---|---|---|
| 1 | ENC_Z- | ENC_Z- |
| 2 | ENC_Z+ | ENC_Z+ |
| 3 | ENC_B- | ENC_B- |
| 4 | ENC_B+ | ENC_B+ |
| 5 | ENC_A- | ENC_A- |
| 6 | ENC_A+ | ENC_A+ |
| 7 | ENC_5V | ENC_5V |
| 8 | ENC_GND | ENC_GND |

Eight pins: three differential channel pairs (Z, B, A) plus a 5V supply and a ground. The manual prints no default value for any pin.

**This is the socket, not the sensor.** Three separate fault codes point here: `0x40000` encoder off set error, `0x80000` encoder value error and `0x400000` encoder not connected. All three list "defective encoder or loose contact" as the probable cause.

---
id: ct850-2016-display-board-small-connector-pinouts
title: Pin definitions for the display board's fan, handlebar, safety, wireless and
  keypad plugs
kind: spec
question: What are the pin definitions of the small display-board connectors on a
  Spirit CT850-2016 treadmill?
asked_as:
- what are the pins on the cooling fan plug of the ct850
- hand pulse connector pins 2016 ct850
- key board connector pinout treadmill
- wireless hr connector pins
keywords:
- pin definition
- connector
- cooling fan
- hand pulse
- safety
- wireless
- keypad
- display board
- pinout
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-display-board-connector-locations
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: p. 40 (printed 39) 'Pin definition'
  extracted_at: '2026-09-08'
---

From the pin-definition page that follows the display-board photo. JK10, the 12-pin system
cable, has its own card.

**JK13 - cooling fan (4 pins)**: P1 +12V, P4 GND. P2 and P3 are printed blank in the manual.

**JK21 - contact HR handlebar (4 pins)**: P1 NC, P2 PULSE, P3 GND, P4 VCC3.

**JK9 - safety (3 pins)**: P1 VCC5, P2 NC, P3 DC_5.

**JK5 - wireless HR (3 pins)**: P1 GND, P2 sensor input, P3 VCC3.

**JK6 - key board (10 pins)**: P1 NC, P2 KEY0, P3 KEY1, P4 KEY2, P5 KEY3, P6 KEY4, P7 KEY5,
P8 GND, P9 VCC3, P10 KEY_LED.

Two things in the source are worth knowing before you rely on this. The JK13 table leaves P2
and P3 with no description at all, and the board photo numbers JK6 **01 to 09** while the table
lists ten pins. Count the ways on the connector before you probe.

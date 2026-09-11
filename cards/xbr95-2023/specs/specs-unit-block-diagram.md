---
id: xbr95-2023-specs-unit-block-diagram
title: 'Block diagram of the generator recumbent: display board over a driver board,
  with the generator in and the generator brake out'
kind: spec
question: What does the unit block diagram of a Spirit xbr95-2023 recumbent bike show?
asked_as:
- block diagram of the xbr95 2023
- how are the boards connected on the xbr95
- what feeds the driver board on the xbr95
- xbr95 configuration diagram
keywords:
- block diagram
- display
- driver board
- generator
- generator brake
- rpm sensor
- hr handlebar
- key
- speaker
- usb charger
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2023
  applies_to:
  - xbr95-2023
  section: specs
  code: '*'
  model_number:
  - '951123'
authority: 3
not_to_be_confused_with:
- spirit-xbr55-xbu55-2023-specs-unit-block-diagram
see_also:
- xbr95-2023-specs-generator-controller-cs52005-33-connections
- xbr95-2023-specs-circuit-diagram-6-pin-computer-cable
source:
  ref: spirit-bike-xbr95-2023-service-manual
  locator: Section 5 Unit Block Diagrams, PDF p. 8 (printed 8 of 28), text.md lines
    138-143, flattened image read from a 300 dpi render (OCR supplement lines 781-810)
  extracted_at: '2026-09-11'
---

**Into the DISPLAY:** HR HANDLEBAR, KEY, WIRELESS HEART RATE RECEIVER. **Out of it:** SPEAKER,
USB CHARGER, FAN. **Display and DRIVER BOARD** exchange signals both ways.

**Into the driver board:** RPM SENSOR and GENERATOR. **Out of it:** GENERATOR BRAKE.

No adapter or mains block is drawn: the generator is the only power source, which is why this
bike "does not need to be plugged into an AC outlet" in its owner's manual. The RPM sensor is
read by the driver board, not the console - the controller page gives it a socket (J3).

The gear-motor XBR55/XBU55 diagram has no driver board at all:
`spirit-xbr55-xbu55-2023-specs-unit-block-diagram`.


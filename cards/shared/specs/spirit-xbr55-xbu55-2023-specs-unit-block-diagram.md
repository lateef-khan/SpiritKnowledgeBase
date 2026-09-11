---
id: spirit-xbr55-xbu55-2023-specs-unit-block-diagram
title: Block diagram with the AC power adapter, gear motor and RPM sensor all feeding
  the display directly, and no lower board
kind: spec
question: What does the unit block diagram of a Spirit XBR55 or XBU55 2023 bike show?
asked_as:
- block diagram of the xbr55 2023
- does the xbu55 2023 have a controller board
- how are the boards connected on the xbr55
- what feeds the display on the xbu55
keywords:
- block diagram
- display
- ac power adapter
- gear motor
- rpm sensor
- hr handlebar
- usb charger
- wireless heart rate receiver
- fan
- key
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55-2023
  - xbu55-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xbr95-2023-specs-unit-block-diagram
see_also:
- spirit-xbr55-xbu55-2023-specs-circuit-diagram-10-pin-computer-cable
- spirit-xbr55-xbu55-2023-specs-display-board-cs11037-and-interface-board-connections
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55-2023: section 5 Unit Block Diagrams, PDF p. 7 (printed 7 of 30),
    text.md lines 137-142, flattened image read from a 300 dpi render (OCR supplement
    lines 848-866). XBU55-2023: PDF p. 7, lines 134-139 (OCR 705-723). The same drawing'
  extracted_at: '2026-09-11'
---

One box, **DISPLAY**, with everything wired to it:

- **Into the display:** HR HANDLEBAR, WIRELESS HEART RATE RECEIVER, KEY, RPM SENSOR, and the
  **AC POWER ADAPTER**.
- **Out of the display:** USB CHARGER, FAN, SPEAKER.
- **Both ways:** GEAR MOTOR.

**There is no driver board and no controller.** The adapter's DC lead, the gear motor and the RPM
sensor all terminate at the console; the schematic shows them as three branches of one ten-pin
computer cable. When the E2 pages talk about "the drive board", on these two bikes that is the
console PCB.

The XBR95-2023 drawing is the one with a driver board between the display and the generator:
`xbr95-2023-specs-unit-block-diagram`.


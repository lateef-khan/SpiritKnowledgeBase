---
id: s77-2019-display-board-connections
title: What plugs into the display board
kind: spec
question: What connects to the display board on a Sole S77-2019 treadmill?
asked_as:
- what plugs into the console board on my treadmill
- s77 display board connections
- where does the bluetooth module sit on my treadmill
keywords:
- display board
- bluetooth module
- heart module
- usb
- amplifier
- key board
- 6 pin
- handrail pulse
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- s77-2019-e5-communication
- s77-2019-e0-safety-key
- s77-2019-console-replacement
source:
  ref: sole-tm-s77-2019-service-manual
  locator: Section 6.1 Display Board wire Connections, page 23
  extracted_at: '2026-09-04'
---

The display board carries the console's whole wiring loom:

- Multimedia processor IC and Main IC
- TFT-LCD display wire
- USB wire
- **Bluetooth module** and the Bluetooth speaker wire
- Amplifier wire
- **Wireless heart receiver** and the heart module
- Fan
- Safety key
- Key board, and the quick speed and incline key board
- Handrail pulse
- Quick speed handrail buttons and quick incline handrail buttons
- **6-pin main control wire** down to the lower controller

The 6-pin main control wire is the one E5 and E1 both point at: it carries the TX/RX speed signal and the +12V safety switch loop.

**This machine has Bluetooth on the display board**, which the block diagram also shows; the earlier ST725 manual's display board section names no Bluetooth module.

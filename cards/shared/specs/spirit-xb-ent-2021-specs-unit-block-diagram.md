---
id: spirit-xb-ent-2021-specs-unit-block-diagram
title: 'Bike Configuration block diagram of the touchscreen residential bikes: line
  in, thumb switch, fan and speakers on the display board, a power switch, a tension
  motor and an RPM sensor'
kind: spec
question: What does the unit block diagram of a Spirit XBR55ENT or XBU55ENT bike show?
asked_as:
- block diagram of the xbr55 ent
- how are the boards connected on the xbu55ent
- xbu55 ent configuration diagram
- does the xbr55ent have a lower board
keywords:
- block diagram
- bike configuration
- display board
- line in
- thumb switch
- fan
- speaker l/r
- power switch
- tension motor
- rpm sensor
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55ent-2021
  - xbu55ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800ent-cu800ent-specs-unit-block-diagram
see_also:
- spirit-xb-2016-specs-unit-block-diagram
- spirit-xb-ent-2021-specs-display-board-ata10001-and-interface-board-connections
- spirit-xb-2016-specs-circuit-diagram
source:
  ref: spirit-bike-xbr55ent-2021-service-manual
  locator: 'XBR55ENT: section 5 ''Bike Configuration'', PDF p. 15, text.md lines 178-184,
    flattened image read from a 300 dpi render (OCR supplement lines 1071-1096, upside
    down). XBU55ENT: PDF p. 15, lines 175-181 (OCR lines 529-554). The same drawing'
  extracted_at: '2026-09-11'
---

Read from the render.

**Into the display board:** HR HANDLEBAR, KEY, WIRELESS HR RECEIVER (top), **LINE IN** (left),
**THUMB SWITCH** (right), and the **RPM SENOR** (spelt so) from below.
**Out of the display board:** **FAN** and **SPEAKER L/R** (right).
**Power:** POWER through a POWER SWITCH into the display board.
**Resistance:** a TENSION MOTOR with a two-way arrow to the display board.

**There is no amplifier block, no Bluetooth block and no driver board.** The 2016 XBR55/XBU55
diagram routed the speakers through a separate amplifier fed from the display board
(`spirit-xb-2016-specs-unit-block-diagram`); on the ENT console the speakers hang directly off the
display board's AJ1/BJ1 sockets. The wireless HR receiver is drawn as before.

The XBU55ENT prints the same drawing under a XBU55 ENT title; the drawing does not show the
incline motor its electrical-configuration text mentions.


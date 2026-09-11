---
id: spirit-xb-2016-specs-unit-block-diagram
title: Bike Configuration block diagram with a power switch and tension motor, and
  on two of the three an amplifier, speakers, line in and Bluetooth
kind: spec
question: What does the unit block diagram of a Spirit XBR25, XBR55 or XBU55 2016
  bike show?
asked_as:
- block diagram of the xbr55 2016
- does the xbr25 have bluetooth
- how are the boards connected on the xbu55 2016
- bike configuration diagram xr329
keywords:
- block diagram
- bike configuration
- display board
- tension motor
- power switch
- rpm sensor
- amplifier
- speaker
- line in
- bluetooth
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbr55-2016
  - xbu55-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xbr95-2016-cu800-2012-specs-unit-block-diagram
see_also:
- spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections
- spirit-xb-2016-specs-circuit-diagram
- spirit-xb-ent-2021-specs-unit-block-diagram
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: 'XBR55-2016: section 5 ''Bike Configuration'', PDF p. 25, text.md lines
    382-388, flattened image read from a 300 dpi render (OCR supplement lines 1382-1402).
    XBR25-2016: PDF p. 23, lines 358-364 (OCR lines 1304-1320, upside down). XBU55-2016:
    PDF p. 23, lines 358-364 (OCR lines 1181-1201)'
  extracted_at: '2026-09-11'
---

Read from the renders.

**All three:** HR HANDLEBAR, KEY and WIRELESS HR RECEIVER into the **DISPLAY BOARD**; **POWER**
through a **POWER SWITCH**; a **TENSION MOTOR** with a two-way arrow to the display board; and an
**RPM SENOR** (spelt so) into the display board. There is no driver board block - the display
board drives the motor and reads the sensor itself.

**XBR55 and XBU55 add four blocks the XBR25 does not have:** the display board feeds an
**AMPLIFIER**, the amplifier feeds **SPEAKER L/R** and takes a **LINE IN**, and the display board
feeds a **BLUETOOTH** block. The XBR25 drawing is the bare bike: no fan, no speaker, no Bluetooth.

**One oddity of the drawing.** On all three the power switch's arrow lands on the *tension motor*
box rather than on the display board; the circuit diagram shows the adapter's DC lead joining
the console cable, so read the arrow as "power enters here", not as the motor being switched.

The display-board pages name the connectors these blocks use:
`spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections`.


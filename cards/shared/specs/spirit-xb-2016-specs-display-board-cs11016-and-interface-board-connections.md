---
id: spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections
title: 'The CS11016 display board: ten-pin system cable, key board, level thumb switch,
  contact HR, wireless HR and fan sockets, with Bluetooth and amplifier power on the
  -01 board only'
kind: spec
question: What plugs into the display board and the console interface board of a Spirit
  XBR25, XBR55 or XBU55 2016 bike, and what are the boards marked?
asked_as:
- what plugs into the xbr55 2016 console board
- cs11016 board
- xbr25 display board connections
- where does the thumb switch plug in on the xbu55
keywords:
- display board
- cs11016-01
- cs11016-47
- interface board
- w-cs11002-1
- system cable 10 pins
- j1 bluetooth
- j2
- j4 key board
- j5 thumb switch
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
- spirit-xbr55-xbu55-2023-specs-display-board-cs11037-and-interface-board-connections
- xbr95-2016-specs-display-amplifier-and-interface-board-connections
see_also:
- spirit-xb-2016-specs-unit-block-diagram
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
- spirit-xb-2016-specs-circuit-diagram
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: 'XBR55-2016: ''Display Board wire Connections'', PDF p. 27, text.md lines
    394-400 (OCR supplement lines 1411-1428); ''The console Interface Board wire Connections'',
    PDF p. 30, lines 413-418 (OCR 1476-1495); board photographs PDF pp. 28-29. XBR25-2016:
    PDF p. 25 (OCR 1329-1346) and p. 28 (OCR 1411-1427). XBU55-2016: PDF p. 25 (OCR
    1210-1227) and p. 28 (OCR 1275-1294). All read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

**Display board.** The XBR55 and XBU55 books draw a board marked **CS11016-01**; the XBR25 book
draws **CS11016-47**. The connector map is the same except for two sockets the XBR25 board does
not use:

| Connector | Lead | XBR55 / XBU55 (CS11016-01) | XBR25 (CS11016-47) |
|---|---|---|---|
| **J1** | BLUETOOTH | yes | **not drawn** |
| **J2** | SYSTEM CABLE (**10 PINS**) | yes | yes |
| **J4** | KEY BOARD | yes | yes |
| **J5** | LEVEL THUMB SWITCH | yes | yes |
| **J9** | CONTACT HR HANDLEBAR | yes | yes |
| **J10** | WIRELESS HR | yes | yes |
| **J11** | COOLING FAN | yes | yes |
| **J12** | AMPLIFIER POWER | yes | **not drawn** |

**Console interface board.** All three books draw the same board, **W-CS11002-1**: **J13** SYSTEM
WIRE, **J1** and **J2** HANDGRIP PULSE SENOR (one per grip), **J4** LEVEL THUMB SWITCH. The
"system wire" here is the short link between the interface board and the display board, not the
mast cable.

**Note the XBR25 draws a J5 thumb-switch socket on its display board** although the XBR25 has no
handgrip resistance buttons - the socket is on the board whether or not the bike uses it.

No pin definitions are printed for any of these connectors; the only pin table in the 2016 books
is the 14-way console-to-driver-board list, `spirit-xb-2016-specs-console-to-driver-board-14-pin-definition`.


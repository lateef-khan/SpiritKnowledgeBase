---
id: spirit-xb-ent-2021-specs-display-board-ata10001-and-interface-board-connections
title: Ten sockets on the ATA10001 touchscreen display board, with a 6-pin system
  cable and two speaker sockets, and the interface board below it
kind: spec
question: What plugs into the display board and the console interface board of a Spirit
  XBR55ENT or XBU55ENT bike, and what are the boards marked?
asked_as:
- what plugs into the xbr55 ent console board
- ata10001 board
- xbu55ent display board connections
- how many pins is the system cable on the xbr55ent
keywords:
- display board
- ata10001-02
- ata10001-03
- interface board
- w-cs11002-1-60
- w-cs31002-2-11
- system cable 6 pins
- aj1
- bj1
- j15 line in
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
- spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections
- spirit-xbr55-xbu55-2023-specs-display-board-cs11037-and-interface-board-connections
see_also:
- spirit-xb-ent-2021-specs-unit-block-diagram
- spirit-xb-specs-gear-motor-connector-5-pin-definition
source:
  ref: spirit-bike-xbr55ent-2021-service-manual
  locator: 'XBR55ENT: ''Display Board wire Connections'', PDF p. 17, text.md lines
    190-196 (OCR supplement lines 1105-1125); ''The console Interface Board wire Connections'',
    PDF p. 20, lines 210-216 (OCR 1147-1166); board photographs PDF pp. 18-19. XBU55ENT:
    PDF p. 17, lines 187-193 (OCR 563-584); PDF p. 20, lines 207-213 (OCR 606-624).
    All read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

**Display board.** The XBR55ENT draws **ATA10001-02** and the XBU55ENT **ATA10001-03**; the
connector map is the same on both:

| Connector | Lead |
|---|---|
| **J2** | COOLING FAN |
| **AJ1** | SPEAKER L |
| **BJ1** | SPEAKER R |
| **J15** | LINE IN |
| **J5** | WIRELESS HR |
| **J14** | CONTACT HR HANDLEBAR |
| **J6** | USB CHARGE |
| **J8** | SYSTEM CABLE (**6 PINS**) |
| **J11** | THUMB SWITCH |
| **J10** | KEY BOARD |

**A 6-pin system cable, where the 2016 LCD consoles used 10 pins** - the mast cable is not
interchangeable between generations.

**Interface board.** The two books draw different boards. XBR55ENT: **W-CS11002-1-60** with **J4**
LEVEL THUMB SWITCH, **J6** SYSTEM WIRE, **J3** HANDGRIP PULSE SENOR. XBU55ENT: **W-CS31002-2-11**
with **J6** SYSTEM WIRE and **J1**, **J2** HANDGRIP PULSE SENOR - no thumb-switch socket, the
upright's level buttons being on the console.

No pin definitions are printed for any of these, and unlike the 2016 books there is no
console-to-board pin list anywhere in the ENT books; the only pin table they keep is the
five-way motor plug, `spirit-xb-specs-gear-motor-connector-5-pin-definition`.


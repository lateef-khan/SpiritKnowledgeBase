---
id: xterra-tr-specs-display-board-jkm-337-eleven-sockets
title: 'The eleven numbered display-board sockets: 3-pin fast speed, 4-pin hand pulse,
  2-pin safety, two 6-pin controller sockets for AC and DC systems, 3-pin fast incline,
  12-pin button board, 4-pin USB, 4-pin Bluetooth, 5-pin program update and 3-pin
  wireless heart rate'
kind: spec
question: What plugs into each numbered socket on the display board of an Xterra TR
  hiking treadmill, and what board is it?
asked_as:
- tr95h console board sockets
- tr75h display board part number
- which socket is the usb on the tr95h console board
- tr75h program update socket
keywords:
- display board
- console board
- sockets
- numbered callouts
- usb
- bluetooth
- program update
- button board
- safety socket
- jkexer
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx5500-2024-specs-display-board-connections-with-usb-and-a-bluetooth-wifi-board
see_also:
- xterra-tr-specs-driver-board-td-65hs-seventeen-callouts
- xterra-tr-specs-wiring-diagram-with-a-brake-module-and-a-7-pin-computer-cable
- xt685ent-2023-specs-display-board-sockets
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: 'TR95H SM (JKEXER 337) ''10. Display board PCB sockets'', PDF p. 15, lines
    193-209, OCR supplement lines 319-350. TR75H SM ''10.'', PDF p. 13 (printed 13),
    lines 264-286, OCR supplement lines 489-528: the same photograph and list. Board
    markings read from the 120 dpi render'
  extracted_at: '2026-09-11'
---

Both books print the same photograph of a green board silkscreened **JKM-337-MB / JKM-655-MB / 2023-09-19_V1.3**
(an AS TEK logo beside it) with eleven red numbers and this list:

| No. | Socket |
|---|---|
| 1 | Fast speed buttons (handrail) socket (3 PIN) |
| 2 | Hand pulse signal socket (4 PIN) |
| 3 | Safety socket (2 PIN) |
| 4 | Upper and lower controller connection cable socket (6 PIN / for AC system) |
| 5 | Upper and lower controller connection cable socket (6 PIN / for DC system) |
| 6 | Fast incline buttons socket (3 PIN) |
| 7 | Button board socket (12 PIN) |
| 8 | USB socket (4 PIN) |
| 9 | Bluetooth socket (4 PIN) |
| 10 | Console program update socket (5 PIN) |
| 11 | Wireless heart rate receiver socket (3 PIN) |

Sockets 1 and 2 are at the bottom left (silkscreen reads SP KEY and HP as far as it is legible); 3, 4 and 5 along the
bottom centre (SAFETY KEY, AC DRV, DC DRV); 6 to 11 run up the right edge, 7 being the long 12-pin socket.

**Two controller sockets, one used.** The board serves both an AC-drive and a DC-drive system and has a 6-pin socket
for each; these treadmills are DC-drive, so socket 5 is the one the "upper and lower controller connection cable"
uses. The wiring diagram calls that cable 7-pin at the controller end; the books do not reconcile the two counts.
The board also carries a sticker (JKM-337 ... DPCB-337000010B / P001-224043 as far as it can be read) that the books
do not transcribe.

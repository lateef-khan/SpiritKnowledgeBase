---
id: ce800-2021-specs-display-board-cs24005-connections
title: 'Eight leads on the CS24005 display board of the elliptical: handlebar, CSAFE
  board, BLE board, wireless receiver, charger board, cooling fan, computer cable
  and key board'
kind: spec
question: What plugs into the display board inside the console of a Spirit ce800-2021
  elliptical, and what is the board marked?
asked_as:
- what plugs into the ce800 console board
- cs24005 board elliptical
- what is the ble board on the ce800
- where does the computer cable go on the ce800 display board
keywords:
- display board
- console pcb
- cs24005
- handlebar
- csafe board
- ble board
- wireless receiver
- charger board
- cooling fan
- computer cable
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2021
  applies_to:
  - ce800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800-2016-specs-display-board-alatech-21-11-001-connections
- ce850-2020-specs-display-board-cs24005-and-interface-board-connections
see_also:
- ce800-2021-specs-unit-block-diagram
- ce800-2021-specs-generator-controller-connections
- spirit-cr800-cu800-2021-specs-display-board-cs24005-connections
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: Section 6-1 Display Board PCB Component Locations, 6-1-1 PCB BOARD TOP,
    6-1-2 PCB BOARD BOTTOM and 6-1-3 DISPLAY BOARD WIRE CONNECTIONS, PDF pp. 19-21
    (printed 18-20), text.md lines 308-328; all three photographs read from a 300
    dpi render (OCR supplement lines 945-1004)
  extracted_at: '2026-09-11'
---

The board is photographed from the back with eight call-outs. Down the left edge, top to bottom:
**HANDLEBAR**, **CSAFE BOARD**, **BLE BOARD**, **WIRELESS RECEIVER**, **CHARGER BOARD**. Along the
bottom and right: **COOLING FAN**, **COMPUTER CABLE** (the widest header, bottom centre), **KEY
BOARD** (bottom right).

The sticker on the board reads **CS24005-12ED-V10** and the silkscreen **CS24005 Rev 1.0**
(CoreStar). The top-side photograph shows the fourteen-character message centre, the dot-matrix
window, two three-digit LED windows and the Scan, Display, Up, Enter, Down, Program and Fan push
buttons soldered to the same board.

**The Bluetooth radio, the CSAFE interface and the USB charger are separate small boards** that
plug into this one - a "BLE board" or "charger board" quoted for this machine is a daughter board,
not the console PCB.

**No pin numbers are printed** for any of the eight connectors. The 2020-version CR800/CU800 bikes
photograph the same board with the same call-outs
(`spirit-cr800-cu800-2021-specs-display-board-cs24005-connections`); the CE850-2020 draws a
CS24005 with different sockets in use, for its stride and level thumb switches
(`ce850-2020-specs-display-board-cs24005-and-interface-board-connections`).


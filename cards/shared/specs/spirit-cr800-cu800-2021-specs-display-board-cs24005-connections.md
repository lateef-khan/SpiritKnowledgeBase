---
id: spirit-cr800-cu800-2021-specs-display-board-cs24005-connections
title: 'Eight leads on the CS24005 display board: handlebar, CSAFE board, BLE board,
  wireless receiver, charger board, cooling fan, computer cable and key board'
kind: spec
question: What plugs into the display board of a Spirit CR800 or CU800 2020-version
  bike, and what is the board marked?
asked_as:
- what plugs into the cu800 console board
- cr800 display board connections
- cs24005 board
- where does the ble board connect on the cu800
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
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cu800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-cr800-cu800-2021-specs-generator-controller-connections
- spirit-cr800-cu800-2021-specs-unit-block-diagram
source:
  ref: spirit-bike-cu800-2021-service-manual
  locator: 'CU800(2020): 6-1-3 Display Board Wire Connections, PDF p. 20 (printed
    19), text.md lines 285-314, a photograph read from a 300 dpi render; 6-1-1 / 6-1-2
    board top and bottom, PDF pp. 18-19. CR800(2020): PDF p. 20 (printed 19), lines
    263-292; pp. 18-19. The same photographs'
  extracted_at: '2026-09-11'
---

The board is photographed from the back with eight call-outs. Down the left edge, top to
bottom: **HANDLEBAR**, **CSAFE BOARD**, **BLE BOARD**, **WIRELESS RECEIVER**, **CHARGER BOARD**.
Along the right and bottom: **COOLING FAN** (top right), **COMPUTER CABLE** (bottom centre, the
widest header), **KEY BOARD** (bottom right).

The sticker on the board reads **CS24005-12ED-V10 (RoHS)** and the silkscreen **CS24005 Rev 1.0**
(CoreStar). The Bluetooth radio, the CSAFE interface and the USB charger are **separate small
boards** that plug into this one - a "BLE board" or "charger board" quoted for these bikes is a
daughter board, not the console PCB.

**No pin numbers are printed** for any of the eight connectors; the 2018 CR900/CU900 book is the
one that tables them (`spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables`), and
its board is a different one.


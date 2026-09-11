---
id: ce850-2020-specs-display-board-cs24005-and-interface-board-connections
title: Ten labelled sockets on the CS24005 display board of the adjustable-stride
  LED elliptical, including CSAFE, BLE and USB charging daughter boards, and a five-socket
  interface board
kind: spec
question: What plugs into the display board and the swing-arm interface board on a
  Spirit ce850-2020 elliptical?
asked_as:
- ce850 2020 display board connections
- cs24005 board ce850
- where does the ble module plug in on the ce850
- ce850 interface board j14 j4
keywords:
- display board
- cs24005
- interface board
- csafe board
- ble module
- heart rate receiver
- usb charging board
- stride thumb switch
- level thumb switch
- system cable
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce850-2020
  applies_to:
  - ce850-2020
  section: specs
  code: '*'
  model_number:
  - '850040'
authority: 3
not_to_be_confused_with:
- ce850-2016-specs-display-board-cs22002-and-interface-board-connections
- ce800-2021-specs-display-board-cs24005-connections
see_also:
- ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
- ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v
- ce850-2020-specs-circuit-diagram-xe898d-se028
- ce850-2020-specs-unit-block-diagram
source:
  ref: spirit-elliptical-ce850-2020-service-manual
  locator: 'Section 6 Basic Connections and Wiring: Display Board PCB Component Locations
    and wire connections, PDF pp. 19-20 (printed 19-20), text.md lines 361-373; Interface
    Board, PDF pp. 22-23, lines 381-393; photographs and the drawn board read from
    300 dpi renders (OCR supplement lines 1149-1182)'
  extracted_at: '2026-09-11'
---

**Display board - CS 24005**, drawn rather than photographed, with eleven sockets, ten of them
labelled:

| Socket | Lead |
|---|---|
| **J1** | CSAFE BOARD |
| **J2** | BLE MODULE |
| **J3** | CONTACT HR HANDLEBAR |
| **J4** | HEART RATE RECEIVER |
| **J5** | COLLING FAN (spelt so) |
| **J6** | SYSTEM CABLE (the 14-pin loom) |
| **J8** | KEYPAD |
| **J10** | USB CHARGING BOARD |
| **J11** | LEVEL THUMB SWITCH |
| **J12** | STRIDE THUMB SWITCH |
| **J13** | drawn, not labelled |

**Interface board** in the swing arm (no part number printed): **J2 SYSTEM CABLE**, **J19** and
**J20 HANDGRIP PULSE SENSOR**, **J14 LEVEL** and **J4 STRIDE** thumb switches.

The CSAFE interface, the Bluetooth radio and the USB charger are **separate small boards** plugged
into J1, J2 and J10 - order them as daughter boards, not as the console PCB. The CE800-2021 uses
the same CS24005 with a different set of sockets in use
(`ce800-2021-specs-display-board-cs24005-connections`); the 2016 CE850 had a CS22002 with seven
sockets and no daughter boards (`ce850-2016-specs-display-board-cs22002-and-interface-board-connections`).
**No pin numbers are printed** for any socket on either board.


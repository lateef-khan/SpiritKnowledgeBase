---
id: ce850-2016-specs-display-board-cs22002-and-interface-board-connections
title: Seven leads on the CS22002 display board and five on the W-CS11002-1-10 interface
  board of the adjustable-stride elliptical with an LCD console
kind: spec
question: What plugs into the display board and the swing-arm interface board on a
  Spirit ce850-2016 elliptical?
asked_as:
- ce850 2016 display board connections
- cs22002 board
- where does the stride thumb switch plug in on the ce850
- ce850 interface board wiring
keywords:
- display board
- cs22002
- interface board
- w-cs11002-1-10
- stride thumb switch
- level thumb switch
- system cable
- wireless hr
- contact hr handlebar
- handgrip pulse sensor
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce850-2016
  applies_to:
  - ce850-2016
  section: specs
  code: '*'
  model_number:
  - '850045'
authority: 3
not_to_be_confused_with:
- ce850-2020-specs-display-board-cs24005-and-interface-board-connections
- spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections
see_also:
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
- spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
- spirit-ce850-specs-parts-electronic-parts-named
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'Section 6 Basic Connections and Wiring: Display Board PCB Component Locations
    and Display Board wire Connections, PDF pp. 25-26 (printed 25-26), text.md lines
    468-480; Interface Board Component Locations and wire Connections, PDF pp. 28-29,
    lines 488-500; photographs checked on 300 dpi renders'
  extracted_at: '2026-09-11'
---

**Display board - CS22002** (CoreStar; the top-side photograph shows the LCD window and the
key-pad contacts). Seven call-outs on the back:

| Socket | Lead |
|---|---|
| **J1** | SYSTEM CABLE (the 14-pin loom to the driver board) |
| **J2** | KEY BOARD |
| **J3** | CONTACT HR HANDLEBAR |
| **J4** | COOLING FAN |
| **J6** | WIRELESS HR |
| **J7** | LEVEL THUMB SWITCH |
| **J8** | STRIDE THUMB SWITCH |

**Interface board - W-CS11002-1-10**, in the swing arm, five call-outs: **J8 SYSTEM WIRE**,
**J4 LEVEL** and **J5 STRIDE** thumb switches, **J1** and **J2 HANDGRIP PULSE SENSOR**.

The CS22002 is unique to this book. The XE895, which is the same manual under another name,
prints a **CS11016-24** in the same chapter with a J1 Bluetooth header
(`spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections`) - the two exports
photograph different console boards. The 2020 CE850 moves to a CS24005 with CSAFE, BLE and USB
daughter boards (`ce850-2020-specs-display-board-cs24005-and-interface-board-connections`).
**No pin numbers are printed** for the display-board sockets; the 14-pin cable is defined on its
own page (`spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins`).


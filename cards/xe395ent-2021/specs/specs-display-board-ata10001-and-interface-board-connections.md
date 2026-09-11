---
id: xe395ent-2021-specs-display-board-ata10001-and-interface-board-connections
title: Ten sockets on the ATA10001-01 display board of the incline touchscreen elliptical,
  with a 6-pin system cable and left and right speakers, and a five-socket W-CS31002-1-00
  interface board
kind: spec
question: What plugs into the display board and the swing-arm interface board on a
  Spirit xe395ent-2021 elliptical?
asked_as:
- xe395ent display board connections
- ata10001 board
- where do the speakers plug in on the xe395 ent
- xe395ent interface board wiring
keywords:
- display board
- ata10001-01
- interface board
- w-cs31002-1-00
- speaker l
- speaker r
- line in
- usb charge
- system cable 6 pins
- thumb switch
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe395ent-2021
  applies_to:
  - xe395ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections
- spirit-xb-ent-2021-specs-display-board-ata10001-and-interface-board-connections
see_also:
- xe395ent-2021-specs-console-to-driver-board-6-pin-definition
- xe395ent-2021-specs-driver-board-cs51005-connections
- xe395ent-2021-specs-circuit-diagram-xe539s-se025
- spirit-xe395-xe895-specs-parts-electronic-parts-named
source:
  ref: spirit-elliptical-xe395ent-2021-service-manual
  locator: 'Section 6 Basic Connections and Wiring: Display Board PCB Component Locations
    and Display Board wire Connections, PDF pp. 16-17 (printed 16-17), text.md lines
    199-211; Interface Board Component Locations and wire Connections, PDF pp. 19-20,
    lines 219-231; photographs checked on 300 dpi renders'
  extracted_at: '2026-09-11'
---

**Display board - ATA10001-01** (the touchscreen console's board). Ten call-outs:

| Socket | Lead |
|---|---|
| **AJ1** | SPEAKER L |
| **BJ1** | SPEAKER R |
| **J2** | COOLING FAN |
| **J5** | WIRELESS HR |
| **J6** | USB CHARGE |
| **J8** | SYSTEM CABLE (6 PINS) |
| **J10** | KEY BOARD |
| **J11** | THUMB SWITCH |
| **J14** | CONTACT HR HANDLEBAR |
| **J15** | LINE IN |

**Interface board - W-CS31002-1-00**, in the swing arm: **J4 INCLINE** and **J5 LEVEL** thumb
switches, **J6 SYSTEM WIRE**, **J1** and **J2 HANDGRIP PULSE SENSOR**.

The speakers are driven from the display board itself - there is no separate CS63005 amplifier as
on the 2016 XE395. The block diagram of this book draws the audio side as *AMPLIFIER, SPEAKER L/R
and LINE OUT*, while the board's socket is labelled **LINE IN**; the socket label is the one to
follow. The 6-pin system cable's signals are on
`xe395ent-2021-specs-console-to-driver-board-6-pin-definition`. The 2021 XB ENT bikes use the same
ATA10001 board (`spirit-xb-ent-2021-specs-display-board-ata10001-and-interface-board-connections`).


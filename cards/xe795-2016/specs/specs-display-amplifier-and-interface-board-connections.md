---
id: xe795-2016-specs-display-amplifier-and-interface-board-connections
title: Eight leads on the CS11020-01 display board of the 2016 generator elliptical,
  including RPM IN and a 6-pin system cable, with a CS63005 amplifier and a W-CS22003-1
  interface board
kind: spec
question: What plugs into the display board, the amplifier and the swing-arm interface
  board on a Spirit xe795-2016 elliptical?
asked_as:
- xe795 2016 display board connections
- cs11020 board
- where does the rpm sensor plug in on the xe795 console
- xe795 interface board jk7
keywords:
- display board
- cs11020-01
- rpm in
- system cable 6 pins
- amplifier power
- cs63005
- interface board
- w-cs22003-1
- level thumb switch
- handgrip pulse sensor
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2016
  applies_to:
  - xe795-2016
  section: specs
  code: '*'
  model_number:
  - '795015'
authority: 3
not_to_be_confused_with:
- xe795-2023-specs-display-board-cs11039-and-interface-board-connections
- spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections
- xbr95-2016-specs-display-amplifier-and-interface-board-connections
see_also:
- xe795-2016-specs-console-to-driver-board-6-pin-definition
- xe795-2016-specs-unit-block-diagram
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- xe795-2016-specs-parts-electronic-parts-named
source:
  ref: spirit-elliptical-xe795-2016-service-manual
  locator: Display Board PCB Component Locations and wire Connections, PDF pp. 25-26
    (printed 25-26), text.md lines 406-418; Interface Board, PDF pp. 28-29, lines
    426-438; Amplifier Board, PDF p. 30, lines 438-444; photographs read from 300
    dpi renders
  extracted_at: '2026-09-11'
---

**Display board - CS11020-01** (sticker CS11020-01.V10.20160219, silkscreen CS11020 REV1.0). Eight
call-outs:

| Socket | Lead |
|---|---|
| **J2** | SYSTEM CABLE (**6 PINS**) |
| **J3** | **RPM IN** |
| **J4** | KEY BOARD |
| **J5** | LEVEL THUMB SWITCH |
| **J9** | CONTACT HR HANDLEBAR |
| **J10** | WIRELESS HR |
| **J11** | COOLING FAN |
| **J12** | AMPLIFIER POWER |

**Amplifier - CS63005**: two speaker sockets, audio in, power - the same board as the XE395's.

**Interface board - W-CS22003-1** in the swing arm: **JK7 SYSTEM WIRE**, **JK9** and **JK8 HANDGRIP
PULSE SENSOR**, **JK5 LEVEL**.

**The speed sensor plugs into the console board**, not the controller: J3 RPM IN, carried down the
6-pin cable as its RPM pin (`xe795-2016-specs-console-to-driver-board-6-pin-definition`). The
031101B controller below has only generator, brake and system-cable sockets
(`spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections`). The 2016 XBR95
bike photographs the same three boards
(`xbr95-2016-specs-display-amplifier-and-interface-board-connections`); the 2023 XE795 moves to a
CS11039 with the sensor on the driver board
(`xe795-2023-specs-display-board-cs11039-and-interface-board-connections`).


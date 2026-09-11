---
id: xbr95-2016-specs-display-amplifier-and-interface-board-connections
title: The CS11020 display board with a 6-pin system cable and an RPM IN socket, the
  CS63005 amplifier board, and the W-CS22003 interface board
kind: spec
question: What plugs into the display board, the amplifier board and the interface
  board of a Spirit xbr95-2016 recumbent bike, and what are the boards marked?
asked_as:
- what plugs into the xbr95 2016 console board
- cs11020 board
- xbr95 amplifier board connections
- xr829 interface board
keywords:
- display board
- cs11020-01
- amplifier board
- cs63005
- interface board
- w-cs22003-1
- system cable 6 pins
- rpm in
- j3
- j2
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2016
  applies_to:
  - xbr95-2016
  section: specs
  code: '*'
  model_number:
  - '951115'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections
- xbr95-2023-specs-display-board-cs11039-and-interface-board-connections
see_also:
- xbr95-2016-specs-console-to-driver-board-6-pin-definition
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: '''Display Board wire Connections'', PDF p. 26, text.md lines 391-397 (OCR
    supplement lines 1364-1386); ''The console Interface Board wire Connections'',
    PDF p. 29, lines 411-417 (OCR 1425-1443); ''Amplifier Board wire Connections'',
    PDF p. 30, lines 417-422 (OCR 1446-1457); board photographs PDF pp. 27-28. Read
    from 300 dpi renders'
  extracted_at: '2026-09-11'
---

**Display board CS11020-01:**

| Connector | Lead |
|---|---|
| **J3** | **RPM IN** |
| **J2** | SYSTEM CABLE (**6 PINS**) |
| **J4** | KEY BOARD |
| **J5** | LEVEL THUMB SWITCH |
| **J9** | CONTACT HR HANDLEBAR |
| **J11** | COOLING FAN |
| **J10** | WIRELESS HR |
| **J12** | AMPLIFIER POWER |

Two differences from the CS11016 board of the 2016 XBR55/XBU55: the system cable is **6 pins, not
10**, because the motor drive stays on the lower board, and the RPM sensor has its own **RPM IN**
socket on the console - the speed lead comes up the mast rather than stopping at the driver
board. There is no Bluetooth socket drawn.

**Amplifier board CS63005:** **J4** and **J5** SPEAKER (2PINS), **J2** AUDEO IN (spelt so), **J1**
POWER (from J12 above).

**Interface board W-CS22003-1:** **JK7** SYSTEM WIRE, **JK9** and **JK8** HANDGRIP PULSE SENOR,
**JK5** LEVEL THUMB SWITCH.

The board photographed on p. 28 carries a CoreStar label; no pin definitions are printed for any
of these sockets. The six pins of the system cable are defined on the error page:
`xbr95-2016-specs-console-to-driver-board-6-pin-definition`.


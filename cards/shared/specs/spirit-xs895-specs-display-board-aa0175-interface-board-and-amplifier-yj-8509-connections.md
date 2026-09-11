---
id: spirit-xs895-specs-display-board-aa0175-interface-board-and-amplifier-yj-8509-connections
title: Six sockets on the AA0175 display board, five on the interface board with level
  and incline thumb switches, and four on the YJ-8509 amplifier
kind: spec
question: What plugs into the display board, the console interface board and the amplifier
  board on a Spirit XS895 incline stepper?
asked_as:
- xs895 display board connections
- aa0175 board jk sockets
- where do the thumb switches plug in on the xs895
- yj-8509 amplifier board speaker plugs
keywords:
- display board
- aa0175
- interface board
- amplifier board
- yj-8509
- thumb switch
- system cable
- jk13
- speaker
- audio in
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections
- cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections
see_also:
- spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
- spirit-xs895-specs-unit-block-diagram-display-board-driver-board-amplifier-and-fuse
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 6-1-1 DISPLAY BOARD WIRE CONNECTIONS, PDF p. 19 (printed 18), text.md lines
    294-301 (OCR supplement 1230-1246); 6-1-2/6-1-3 PCB BOARD TOP and BOTTOM photographs,
    PDF pp. 20-21, lines 302-313 (supplement 1249-1272); 6-1-4 THE CONSOLE INTERFACE
    BOARD WIRE CONNECTIONS, PDF p. 22, lines 314-319 (supplement 1275-1295); 6-1-5
    AMPLIFIER BOARD WIRE CONNECTIONS, PDF p. 23, lines 320-325 (supplement 1298-1312);
    all three drawings are flattened images read from 110 dpi renders
  extracted_at: '2026-09-11'
---

**Display board - AA0175, six sockets**

| Socket | Lead |
|---|---|
| **JK7** | AMP POWER |
| **JK13** | FAN |
| **JK4** | HR HANDLEBAR |
| **JK5** | WIRELESS HR |
| **JK3** | KEY BOARD |
| **JK9** | SYSTEM CABLE |

The photographs show a green **AA0175-V1.0** board (sticker *AA01755-200428_V1.1*, batch
A512-210121006/200, an *XS895* label at the top left) with the buzzer, a programming header and
the eleven-way system socket along the bottom edge; its pins are on
`spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins`. The pin-definition
photograph names the same sockets by function - AMP POWER, FAN, HR HAND, KEYS, HR RECEIVE.

**Console interface board - five sockets**

| Socket | Lead |
|---|---|
| **JK2** | SYSTEM WIRE (the long socket) |
| **JK7** | LEVEL THUMB SWITCH |
| **JK6** | INCLINE THUMB SWITCH |
| **JK10** | HANDGRIP PLUSE SENSOR [sic] |
| **JK11** | HANDGRIP PLUSE SENSOR [sic] |

No board code is printed on the interface-board drawing.

**Amplifier board - YJ-8509, four sockets**

| Socket | Lead |
|---|---|
| **JK7** | AUDIO IN |
| **JK2** | POWER |
| **JK4** | SPEAKER (2 PINS) |
| **JK3** | SPEAKER (2 PINS) |

The XS895 is the only stepper in this family with an amplifier, speakers and thumb switches on
the handlebar; the CS800 and CRS800S boards are the CS24005 family
(`spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections`).


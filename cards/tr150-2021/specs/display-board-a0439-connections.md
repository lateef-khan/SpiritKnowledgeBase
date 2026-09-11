---
id: tr150-2021-specs-display-board-a0439-connections
title: 'What plugs into the display board: wireless receiver, key board, handrail
  pulse, safety key, MP3 power, a heart module, and a 5-pin main-control socket marked
  GND, RXD, TXD, VDD, SW'
kind: spec
question: What connects to each socket on the display board (upper control board)
  of an Xterra tr150-2021 treadmill?
asked_as:
- tr150 console board connections
- where does the safety key plug into the tr150 display board
- tr150 upper control board sockets
- tr150 heart module
keywords:
- display board
- upper control board
- console board
- sockets
- wire connections
- keyboard
- safety key
- hand pulse
- heart module
- main control
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: specs
  code: '*'
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with:
- tr260-2023-specs-display-board-a3404-connections
- trx1400-2023-specs-display-board-a0127-connections
see_also:
- tr150-2021-specs-driver-board-b426d-wire-connections
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- spirit-xt-2015-specs-display-board-connections
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM (GT65-NT014) '6.1 Display Board wire Connections', PDF p. 23 (printed
    24), lines 273-306; '6.2 Display Board PCB Component Locations' PDF p. 24-25 (printed
    25-26), lines 306-319, two uncaptioned photographs. Board markings read from the
    110 dpi render
  extracted_at: '2026-09-11'
---

The board photographed is silkscreened **A0439_V11**, dated **2014-4-22**, with an "EW" (Shanghai EWay) logo and UL
file **E334460**. Section 6.1 boxes eight things on it:

| Callout | Where on the board |
|---|---|
| CONNECTION WIRELESS | white 2-pin socket, top left |
| Connection with KEY BOARD | long white socket along the top edge |
| Connection with Handrail Pulse | two white 2-pin sockets, top right |
| Heart Module | daughter board at the right end with a round sensor can |
| Connection with Safety key | white 2-pin socket, left edge |
| **GND / RXD / TXD / VDD / SW** | the black 5-pin main-control header on the left edge, labelled top to bottom |
| Display IC | the square chip left of centre |
| MAIN IC | the chip right of centre |
| Connection with MP3 POWER WIRES | red 2-pin socket, bottom left |

The 5-pin header's labels read GND, RXD, TXD, VDD, SW from the top; that is the same five signals as the circuit
diagram's pin define (1 S/W, 2 VDD, 3 TXD, 4 RXD, 5 GND) read from the other end. A buzzer sits at the bottom
centre; a red 4-pin socket beside it is not labelled.

Section 6.2, "PCB Board Top" and "PCB Board Bottom", is two photographs with no captions at all - the top is the LCD
glass in its frame, the bottom is the same board as 6.1 without the callouts. Nothing is named there that 6.1 does
not name.

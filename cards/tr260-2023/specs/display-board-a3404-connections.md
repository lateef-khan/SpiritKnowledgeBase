---
id: tr260-2023-specs-display-board-a3404-connections
title: 'What plugs into the display board: handrail pulse, a Bluetooth board, the
  key board, speed and incline rapid keys, the 5-pin main control wires and the safety
  key, on a board stickered with its part number and program'
kind: spec
question: What connects to each socket on the display board of an Xterra tr260-2023
  treadmill, and what is written on the board?
asked_as:
- tr260 console board connections
- tr260 display board part number
- where do the rapid keys plug in on the tr260
- tr260 bluetooth board socket
keywords:
- display board
- console board
- sockets
- wire connections
- bluetooth board
- rapid key
- keyboard
- safety key
- main control
- part number
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-display-board-a0439-connections
- trx2500-2024-specs-display-board-a0463-connections
see_also:
- tr260-2023-specs-driver-board-b407d-sockets-acn-acl-to-m-plus
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- tr260-2023-specs-unit-block-diagram-with-incline-motor-vr-set-and-amplifier
- spirit-xt-2023-specs-display-board-connections
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM (GT75A-NT050) 'Display Board wire Connections', PDF p. 18 (printed
    18), lines 267-300, OCR supplement lines 1208-1249; 'Display Board PCB Component
    Locations' PDF p. 19-20, lines 300-313, OCR supplement lines 1261-1320. Board
    markings read from the 110 dpi render
  extracted_at: '2026-09-11'
---

The board photographed is silkscreened **A3404-V61**, dated **2020-04-15**, UL file **E349902**, with an "EW" logo.
Its sticker reads: **Customer Model: GT75A-NT050 / Part Number: A001010728 / Description: INC-A3404J5 /
ProgrammingNumber: A340401_C05A17V20 22071202.hex / Speed: 10km**, over serial 04220719A00009 - the part number and
the loaded program of the display board as shipped.

The wire-connections page boxes nine things:

| Callout | Where on the board |
|---|---|
| Connection with Handrail Pulse | white socket, top left |
| Bluetooth board wires socket | white socket, top right, beside the buzzer |
| Display IC | large chip, left of centre |
| MAIN IC | small chip, right of centre |
| Speed Rapid key | red socket, right edge, upper |
| Incline Rapid key | white socket, right edge, middle (a blue socket sits below it) |
| Connection with KEYBOARD | long white socket along the bottom edge |
| Connection with 5-pin Main control wires | black 5-pin header, bottom right |
| Connection with Safety key | white 2-pin socket, bottom right, left of the header |

The "PCB Board Top" and "PCB Board Bottom" pages that follow are the same board photographed without callouts; the
bottom view shows the sticker again. The block diagram for this machine draws a WIRELESS HR RECEIVER where the board
has a Bluetooth socket.

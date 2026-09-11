---
id: xterra-trx-specs-display-board-connections-with-an-mp3-audio-input-socket
title: 'What plugs into the display board, with an MP3 audio input socket: two boards,
  one per machine, each stickered with its own part number and a 12KM program'
kind: spec
question: What connects to each socket on the display board of an Xterra TRX treadmill
  in the TRX3500 and TRX4500 service manual, and how do the two boards differ?
asked_as:
- trx3500 console board connections
- trx4500 display board part number
- where does the mp3 audio plug into the trx3500
- trx4500 hand pulse sockets
keywords:
- display board
- console board
- sockets
- wire connections
- mp3 audio input
- handrail keys
- bluetooth board
- hand pulse
- part number
- program
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx3500-2024
  - trx4500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx2500-2024-specs-display-board-a0463-connections
- trx5500-2024-specs-display-board-connections-with-usb-and-a-bluetooth-wifi-board
see_also:
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
- xterra-trx-specs-driver-board-led-locations-power-led3-and-info-led-on-the-b017d
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- spirit-xt-2023-specs-display-board-connections
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: 'TRX3500/TRX4500 SM ''6.2 Display Board wire Connections'': ''For GT90C-NT023
    (TRX3500)'' PDF p. 29 (printed 28), lines 410-446, OCR supplement lines 1572-1610;
    ''For GT90D-NT024 (TRX4500)'' PDF p. 30 (printed 29), lines 446-480, OCR supplement
    lines 1611-1697. ''6.1 Display Board PCB Component Locations'' PDF p. 25-28 (top
    and bottom for each machine), lines 385-410, stickers in OCR supplement lines
    1512-1539 and OCR supplement lines 1540-1571'
  extracted_at: '2026-09-11'
---

The book prints one wire-connections page per machine with the same callouts on each:

| Callout | Notes |
|---|---|
| Speaker (two) | one at each upper corner |
| Wireless Pulse Socket | top right |
| Fan power wires socket | top right |
| AMP power wires socket | right, upper |
| Bluetooth board wires socket | right, middle |
| Safety key wires socket | right |
| Main Control wires Socket | right, lower - the 5-pin cable |
| **MP3 Audio input wires socket** | left, middle - the socket the TRX2500 board does not have |
| Display IC / MAIN IC | centre |
| Hand Pulse Module | left, lower |
| Hand Pulse Socket | bottom left (the TRX4500 page labels **two** Hand Pulse Sockets) |
| Incline Handrail keys socket | bottom, centre-left |
| Key board wires Socket | bottom, centre |
| Speed Handrail keys socket | bottom, centre-right |

The stickers, read from the "PCB Board Bottom" photographs:

| Machine | Part Number | Description | ProgrammingNumber | Speed |
|---|---|---|---|---|
| TRX3500 (GT90C-NT023) | A001010421 | INC-A0464A0 | NT023_A0464_S102_70623.mot | 12KM |
| TRX4500 (GT90D-NT024) | A001010422 | INC-A0465A0 | NT024_A0465_S102_70622.mot | 12KM |

So the two machines take different display boards with different programs, although the sockets are the same. The
6.1 pages ("PCB Board Top / Bottom for GT90C-NT023 (TX3500)" and "for GT90D-NT024 (TX4500)" - the headings drop the
R) are uncaptioned photographs. The "12KM" on both stickers sits oddly against the books' calibration figure of 12
for the maximum speed; the sticker is quoted as printed.

---
id: 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
title: Electrical wiring diagram with the CS31003-1 console board, the CS51009 lower
  control board, a power supply module, an AC entry module with switch and fuse, a
  data transfer board and every cable numbered
kind: spec
question: What does the electrical wiring diagram of the Spirit 85s-2025 recumbent
  stepper service manual show, and which cable number goes where?
asked_as:
- 8.5s wiring diagram
- what is cable 103 and 104 on the 8.5s
- where does the data transfer board connect on the 8.5s
- 8.5s console j3 j6 j9
keywords:
- wiring diagram
- cs31003
- cs51009
- lower control board
- lcb
- power supply module
- ac power entry module
- data transfer board
- cable numbers
- ir reflective sensor board
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: specs
  code: '*'
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- 7-5s-med-specs-wiring-diagram-j13-14-pin-with-wire-colours-and-sensor-cables
see_also:
- 85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
- 85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: '4-3 Electrical Wiring Diagram, PDF p. 12 (printed 12), text.md line 188,
    a flattened drawing read from 200 and 400 dpi renders (OCR supplement 739-783
    is partial); the part numbers are the book''s own # numbers; 5-2 UART Communication
    Error names cables #103 and #104, PDF p. 19, lines 266-278'
  extracted_at: '2026-09-11'
---

Every part and cable on the sheet carries a **# number** - the book's own item numbers, used again
in its troubleshooting flowcharts.

**Boards and parts**

| # | Part | Sockets drawn |
|---|---|---|
| #086 | **Console**, with its board **CS31003-1** | USB, J6, J5, J9, J4, **J3** |
| #105 | **Lower Control Board** (LCB), **CS51009** | J5, J6, J8, J4, J2, CN1, CN2; LEDs D14, D13, D12, D5 |
| #097 | **Power Supply Module** | CN100 (DC out), CN1 (AC in) |
| #092 | **AC Power Entry Module with Switch and Fuse** | #093 Neutral, #094 Line, #095 earth, #096 to the PSU |
| #106 | **IR Reflective Sensor Board - Step Position & Direction**, reading a **Reflective Encoder Disc** | into LCB **J6** |
| #085 | **Brake and Angle Sensor** (the magnetic brake with its angle-sensor board) | two **#102** cables from **CN1** and **CN2** |
| #087 | **Data Transfer Board** (a DB9 and a USB-B on a bracket under the machine) | cables #088 and #090 |

**Cables**

| # | From | To |
|---|---|---|
| **#103 / #104** | LCB **J4** | console **J3** - one lead with an inline join; the console's 12 V and UART |
| **#099** | LCB **J2** (DC 24V) | PSU **CN100** |
| **#181** | LCB **J8** | drawn to **CN2** |
| **#102** x2 | LCB CN1 and CN2 | brake and angle sensor |
| **#089 / #088** | console **J6** | data transfer board |
| **#091 / #090** | console **J9** | data transfer board |
| **#096** | AC entry module | PSU **CN1** |

**How the power flows** (section 4-4): the power supply module makes **24 VDC** for the whole
machine; the LCB "converts it to 12 VDC for the console and supplies power to the angle and magnet
sensors", and "sensor readings are used to control resistance on the brake"
(`85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds`,
`85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v`).

**Two numbering slips in the book.** Section 4.4.1 says "Power Supply #081 provides 24 VDC" and
"Brake #086", where the diagram numbers the power supply **#097**, the console **#086** and the
brake **#085**; and the no-power flowchart calls the console lead "the inline connector cable
(#089, 090)", which on the diagram are the data-transfer-board cables - the console lead is
#103/#104, as the UART page says. Follow the diagram's numbers.

The firmware files CS51009-01.bin and CS31003.bin are named for these two boards
(`85s-2025-console-firmware-lcb-and-console-app-update-from-a-usb-root-or-over-wifi`).


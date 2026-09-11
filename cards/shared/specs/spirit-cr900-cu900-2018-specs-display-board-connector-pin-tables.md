---
id: spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables
title: The nine display-board connectors with their pin tables, from the RPM header
  to the USB header, on the CS26004 board
kind: spec
question: What is the pin definition of each display board connector on a Spirit CR900
  or CU900 2018 bike?
asked_as:
- cu900 display board pinout
- which pins carry rpm on the cr900 console board
- j7 interface pins spirit bike
- what is j17 on the 2018 cu900 console
keywords:
- display board
- pin define
- pinout
- j16
- j7
- j12
- j1 csafe
- j3
- j8 main key
- j9 key pad
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900-2018
  - cu900-2018
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
- spirit-cr900-cu900-2018-specs-circuit-diagram
source:
  ref: spirit-bike-cr900-2018-service-manual
  locator: 'CR900-2018: ''Display Board wire Connections pin define'', PDF pp. 20-21,
    text.md lines 275-325; board photographs PDF pp. 22-23 read from a 300 dpi render
    (OCR supplement lines 1270-1338). CU900-2018: PDF pp. 21-22, lines 337-391; photographs
    PDF pp. 23-24 (OCR lines 1211-1288). Identical tables in both books'
  extracted_at: '2026-09-11'
---

Nine connectors are tabled. Pin 1 is on the left of each row; the manual spells the row
"Discription".

| Connector | Pin 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **J16 RPM** | GND | RPM | | | | | | | | | |
| **J7 INTERFACE** | +12V | GND | +6V | N/A | PWM | BREAK | | | | | |
| **J12 FAN** | FAN-VCC | N/A | N/A | FAN-GND | | | | | | | |
| **J1 CSAFE** | RX | TX | CSAFE-POWER | N/A | GND | | | | | | |
| **J3 INTERFACE** | GND | +5V | Pulse | HP/WP | | | | | | | |
| **J8 MAIN KEY** | GND | D6 | D5 | D4 | D3 | D2 | D1 | D0 | S1 | S0 | |
| **J9 KEY PAD** | GND | D6 | D5 | D4 | D3 | D2 | D1 | D0 | S4 | S3 | S2 |
| **J10 GND** | GND | GND | | | | | | | | | |
| **J17 USB** | GND | D+ | D- | +5V | GND | CAP_PWR | +6V | | | | |

Two things to read carefully:

- **J7 pin 6 is printed "BREAK"**, the brake line to the lower board; J7 is the six-way
  interface that carries +12 V, +6 V and the PWM resistance command.
- **J9 has eleven positions and the header row numbers the last two "10, 10"** - a misprint. The
  eleventh signal is S2.

The board photographed on the following pages is a **CoreStar CS26004, Rev 1**, with the sticker
**CS26004-01**; the top photo is too small to read individual connector labels, so the table above
is the reference, not the photo.


---
id: ce900-2021-specs-display-board-connector-pin-tables
title: The nine display-board connectors of the generator elliptical with their pin
  tables, from the RPM header to the seven-pin USB
kind: spec
question: What are the pin definitions of the display board connectors on a Spirit
  ce900-2021 elliptical?
asked_as:
- ce900 display board pinout
- what is the j7 interface connector on the ce900 elliptical
- pin 6 break on the ce900 console board
- ce900 elliptical usb header pins
keywords:
- display board
- pin define
- pinout
- rpm
- interface
- fan
- csafe
- main key
- key pad
- usb
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900-2021
  applies_to:
  - ce900-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ce900-2021-specs-unit-block-diagram
- ce900-2021-specs-driver-board-blcb002a-connections
- ce900-2021-specs-circuit-diagram-se8800-sb026
- spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables
source:
  ref: spirit-elliptical-ce900-2021-service-manual
  locator: Section 6 Basic Connections and Wiring, Display Board wire Connections
    pin define, PDF pp. 21-22 (printed 21-22), text.md lines 348-402; PCB Board Top
    and Bottom photographs, PDF pp. 23-24, lines 402-416 (OCR supplement lines 1272-1359)
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

- **J7 pin 6 is printed "BREAK"**, the brake line to the lower board; J7 is the six-way interface
  that carries +12 V, +6 V and the PWM resistance command.
- **J9 has eleven positions and the header row numbers the last two "10, 10"** - a misprint. The
  eleventh signal is S2.

The board photographed on the following pages is a **CoreStar CS26004**; the top photo is too
small to read individual connector labels, so the table above is the reference, not the photo.

**The 2018 CR900 and CU900 bikes print these nine tables line for line**, misprint included
(`spirit-cr900-cu900-2018-specs-display-board-connector-pin-tables`) - one console board on the
generator bikes and this elliptical. This is the only book in the elliptical wave that prints
display-board pin definitions.


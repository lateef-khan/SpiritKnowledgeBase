---
id: ce1000ent-2023-specs-driver-board-cs56012-connections
title: 'Five sockets on the CS56012 driver board of the elliptical: COMM PORT system
  wire, TFT PWR console power out, RPM IN, MAG-BRAKE out and DC 24V power in'
kind: spec
question: Which connector on the ce1000ent-2023 driver board takes which cable, and
  what is the board marked?
asked_as:
- what plugs into the ce1000 driver board
- cs56012 board elliptical
- where does the brake wire go on the ce1000ent lower board
- which plug is the 24v input on the ce1000
keywords:
- driver board
- lower controller
- cs56012
- comm port
- tft pwr
- rpm in
- mag-brake
- dc 24v pwr in
- system wire
- console power output
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce1000ent-2023
  applies_to:
  - ce1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210054'
authority: 3
not_to_be_confused_with:
- ce900ent-specs-driver-board-dya-w10a-connectors
see_also:
- ce1000ent-2023-specs-circuit-diagram-se8880-sb028-230v
- ce1000ent-2023-specs-power-adapter-100-w-24-v-5-a
- ce1000ent-2023-specs-io-board-bottom-connections
- cu1000ent-2023-specs-driver-board-cs56012-connections
source:
  ref: spirit-elliptical-ce1000ent-2023-service-manual
  locator: Section 6.2 Driver Board PCB Component Locations, PDF p. 10, and 6.3 Driver
    Board function, PDF p. 11 (printed 10-11), text.md lines 205-260; both photographs
    read from a 300 dpi render (OCR supplement lines 904-923)
  extracted_at: '2026-09-11'
---

The board silkscreen reads **CS56012 Rev 1.0** (CoreStar), date code 2204 on the sample
photographed. Its sockets are labelled on the silkscreen and again by call-outs on p. 11:

| Silkscreen | Designator | Call-out on p. 11 |
|---|---|---|
| **COMM PORT** | J1, six-way, left edge | SYSTEM WIRE |
| **TFT PWR** | J3, top left | CONSOLE POWER OUTPUT |
| **RPM IN** | J2, top | RPM SENSOR |
| **MAG-BRAKE** | J5, top | BRAKE FLIWHEEL OUTPUT (spelt so) |
| **DC 24V - PWR IN** | J4, top right | DC 24V INPUT |

A sixth header marked **ICP** at the bottom is a programming port with no call-out.

The board takes **24 V DC** from the adapter through the DC jack and sends **TFT power** up to the
screen on its own lead, separate from the 6-pin main control wires - see the circuit diagram. It is
not the CE900ENT's DYA-W10A-IMX6-R10 board (`ce900ent-specs-driver-board-dya-w10a-connectors`),
which has the same five functions on CN-numbered sockets. The CU1000ENT bike uses this same CS56012
board (`cu1000ent-2023-specs-driver-board-cs56012-connections`).


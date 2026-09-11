---
id: cu1000ent-2023-specs-driver-board-cs56012-connections
title: 'Five sockets on the CS56012 driver board: COMM PORT system wire, TFT PWR console
  power out, RPM IN, MAG-BRAKE out and DC 24V power in'
kind: spec
question: Which connector on the Spirit CU1000ENT or CR1000ENT 2023 driver board takes which
  cable, and what is the board marked?
asked_as:
- what plugs into the cu1000 driver board
- cs56012 board
- where does the brake wire go on the cu1000ent lower board
- which plug is the 24v input on the cu1000
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
  product_line: bike
  model: '*'
  applies_to:
  - cr1000ent-2023
  - cu1000ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-driver-board-connectors
see_also:
- cu1000ent-2023-specs-circuit-diagram
- cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a
- cu1000ent-2023-specs-io-board-bottom-connections
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: "Section 6.2 Driver Board PCB Component Locations, PDF p. 10, and 6.3 Driver Board
    function, PDF p. 11 (printed 10-11), text.md lines 203-228; both photographs read from a
    300 dpi render (OCR supplement lines 867-896). CR1000(2023) SR8880-SB028 service manual
    (spirit-rower-cr1000ent-2023-service-manual): sections 6.2-6.3, PDF pp. 10-11 (printed
    10-11), lines 181-238, the same two photographs (OCR supplement 1110-1169), board read
    from a 150 dpi render"
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

The board takes **24 V DC** from the adapter through the DC jack and sends **TFT power** up to
the screen on its own lead, separate from the 6-pin main control wires - see the circuit diagram.
It is not the CU900ENT's DYA-W10A-IMX6-R10 board (`cu900ent-driver-board-connectors`), which has
the same five functions on CN-numbered sockets.

**The CR1000ENT-2023 recumbent uses the same board.** Its service manual photographs a CS56012
Rev 1.0 with the same 2204 date code, the same five silkscreen labels and the same five call-outs
(BRAKE FLIWHEEL OUTPUT misspelling included), so this card covers that machine too. On the
recumbent the board sits in the rear shroud behind the seat rail (its replacement page calls it
the lower controller and takes the iron plate off first).


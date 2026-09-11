---
id: ce900ent-specs-driver-board-dya-w10a-connectors
title: Five call-outs on the DYA-W10A-IMX6-R10 driver board of the ENT elliptical,
  with the CN numbers the circuit diagram gives them
kind: spec
question: What connects to the driver board on a Spirit ce900ent elliptical, and what
  is the board marked?
asked_as:
- what plugs into the ce900ent driver board
- dya-w10a board elliptical
- where does the brake wire go on the ce900 ent lower board
- which plug is the 24v input on the ce900ent
keywords:
- driver board
- lower controller
- dya-w10a-imx6-r10
- rpm sensor input
- console power output
- brake flywheel output
- dc 24v input
- system wire
- cn8
- cn2
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: specs
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with:
- ce1000ent-2023-specs-driver-board-cs56012-connections
- ce900-2021-specs-driver-board-blcb002a-connections
see_also:
- ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board
- ce900ent-specs-io-board-connections
- cu900ent-driver-board-connectors
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Driver Board PCB Component Locations, PDF p. 19, and Driver Board function,
    PDF p. 20 (printed 19-20), text.md lines 270-295; the photographs are flattened
    images read from a 300 dpi render (OCR supplement lines 1504-1540); connector
    numbers from the circuit diagram on PDF p. 24
  extracted_at: '2026-09-11'
---

The board silkscreen reads **DYA-W10A-IMX6-R10-LCB BOARD Rev:1.0**; the circuit diagram on p. 24
prints the same board as **DYA-W10A-IMX6-R10-LCD BOARD**. The photo shows a "B", so LCB (lower
control board) is the likelier reading, but the manual is not consistent.

Call-outs on p. 20, and the connector numbers the circuit diagram gives the same cables:

| Call-out on p. 20 | Connector on p. 24 |
|---|---|
| RPM SENSOR (input) | CN4 (speed sensor) |
| CONSOLE POWER OUTPUT | CN3, the **3 PIN POWER CABLE** up the mast |
| BRAKE FLIWHEEL OUTPUT (spelt so in the manual) | CN8, marked BRAKE, 2-pin red wire |
| DC 24V INPUT | CN2, from the DC jack |
| SYSTEM WIRE | the 8-pin computer cable; the diagram lands it on the top-right socket |

**CN6** is on the board and is left unwired on the circuit diagram. Other silkscreen visible on the
photo: CN7, FAN1, and a USB socket.

**The CU900ENT and CR900ENT bike books print the same two pages** with the same five call-outs and
the same CN numbers (`cu900ent-driver-board-connectors`). The CE900-2021 generator elliptical uses
a different board, the BLCB002A (`ce900-2021-specs-driver-board-blcb002a-connections`), and the
CE1000ENT a CS56012 (`ce1000ent-2023-specs-driver-board-cs56012-connections`).


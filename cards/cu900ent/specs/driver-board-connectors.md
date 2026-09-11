---
id: cu900ent-driver-board-connectors
title: Driver board connectors and the board's markings
kind: spec
question: Which connector on the Spirit CU900ENT or CR900ENT driver board takes which cable,
  and what is the board marked?
asked_as:
- what plugs into the cu900 driver board
- where does the brake wire go on the bike board
- dc 24v input on the cu900ent
- what board number is the bike lower controller
keywords:
- driver board
- lower controller
- connector
- rpm sensor
- brake flywheel
- dc 24v
- console power
- system wire
- dya-w10a
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900ent-2021
  - cu900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-circuit-diagram
- cu900ent-ac-adapter-rating
- cu900ent-electronic-parts-locations
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: "p. 19 (printed 19) and p. 20 (printed 20), section 6 'Driver Board PCB Component Locations' / 'Driver Board function'; connector numbers from the circuit diagram on p. 24 (printed 24). CR900ENT-2021 (spirit-bike-cr900ent-2021-service-manual): 'Driver Board PCB Component Locations' PDF p. 18 and 'Driver Board function' PDF p. 19 (printed 18-19), text.md lines 191-215 (OCR supplement lines 1459-1470), the same photographs; connector numbers on its circuit diagram, PDF p. 23"
  extracted_at: '2026-09-08'
---

The board photo on p. 20 is a flattened image and was read from the 300 dpi render. The board
silkscreen reads **DYA-W10A-IMX6-R10-LCB BOARD Rev:1.0**; the circuit diagram on p. 24 prints the
same board as **DYA-W10A-IMX6-R10-LCD BOARD**. The photo shows a "B", so LCB (lower control board)
is the likelier reading, but the manual is not consistent.

Call-outs on p. 20, and the connector numbers the circuit diagram gives for the same cables:

| Call-out on p. 20 | Connector on p. 24 |
|---|---|
| RPM sensor input | CN4 (speed sensor) |
| Console power output | - |
| Brake fliwheel output (spelt so in the manual) | CN8, marked BRAKE, 2-pin red wire |
| DC 24V input | CN2, from the DC jack |
| System wire | CN3, the 8-pin computer cable |

**CN6** is on the board and is left unwired on the circuit diagram. Other silkscreen visible on
the photo: CN7, CN8, FAN1, and a USB socket.

**The CR900ENT book prints the same two pages** - the same board photograph with the same five
call-outs (RPM SENSOR INPUT, CONSOLE POWER OUTPUT, BRAKE FLIWHEEL OUTPUT, DC 24V INPUT, SYSTEM
WIRE) and the same CN numbers on its circuit diagram. The 2018 CR900/CU900 used a different
board, the BLCB002A (`spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections`).

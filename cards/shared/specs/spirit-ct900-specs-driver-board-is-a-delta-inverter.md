---
id: spirit-ct900-specs-driver-board-is-a-delta-inverter
title: The driver board is a Delta inverter captioned VFD015TM12A, photographed with
  no call-outs
kind: fact
question: What is the driver board on a Spirit CT900 or CT900ENT treadmill, and does
  the manual show its connectors?
asked_as:
- what inverter is in the ct900
- ct900 driver board part number
- where are the connectors on the ct900 inverter
- vfd015tm12a
keywords:
- driver board
- inverter
- lower controller
- delta
- vfd-tm
- component locations
- no callouts
- connector
- heatsink
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct900
  - ct900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-driver-board-connector-locations
see_also:
- ct900-specs-circuit-diagram
- ct900ent-specs-circuit-diagram
- ct1000ent-2023-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct900-service-manual
  locator: 'CT900: PDF p. 25 (printed 25) ''DRIVER BOARD PCB Component Locations'',
    text.md lines 312-319. CT900ENT: PDF p. 14 (printed 14), lines 182-190. Both captioned
    ''VFD015TM12A'' under the photograph'
  extracted_at: '2026-09-11'
---

Both books give the driver board one page: a photograph of a large inverter on a heat-sink plate -
electrolytic capacitors, a finned heatsink, two relays and a row of screw terminals along the bottom -
captioned **VFD015TM12A** and nothing else. **No connector, terminal or LED is called out**, so the manual
does not tell you where the console, motor or incline plugs are on this board.

VFD015TM12A is a Delta VFD-TM series drive; the CT900 book's error chapter is headed "AC MOTOR DRIVER
INVERTER VFD-TM Error and Warning Codes' Descriptions" and refers to a **KPC-CC01** keypad display for
reading them. The CT1000ENT book prints the same photograph without any caption and its circuit diagram
names the maker as DELTA.

The connector names this family does print are on the circuit diagrams: AC1 / AC2, U / V / W, DOWN / UP /
COM, the VR position wire and the signal wire from the ERP board.

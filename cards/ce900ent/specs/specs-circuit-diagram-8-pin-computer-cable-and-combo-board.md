---
id: ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board
title: Circuit diagram of the ENT elliptical with a combo board, an 8-pin computer
  cable, a 3-pin power cable and a 24 V adapter into a DC jack
kind: spec
question: What does the circuit diagram of a Spirit ce900ent elliptical show?
asked_as:
- ce900ent wiring diagram
- ce900 ent schematic
- what cables run up the mast on the ce900ent
- what is the combo board on the ce900ent
keywords:
- circuit diagram
- wiring diagram
- schematic
- combo board
- 8 pin computer cable
- 3 pin power cable
- dc jack
- 2 pin red wire brake
- speed sensor
- csafe hdmi bnc rj45
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
- ce1000ent-2023-specs-circuit-diagram-se8880-sb028-230v
- ce900-2021-specs-circuit-diagram-se8800-sb026
see_also:
- ce900ent-specs-ac-adapter-fsp100-rtaan2-24-v-4-17-a
- ce900ent-specs-driver-board-dya-w10a-connectors
- ce900ent-specs-io-board-connections
- cu900ent-circuit-diagram
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Circuit diagram headed (CE900-ENT) ELLIPTICAL CIRCUIT DIAGRAM, PDF p. 24
    (printed 24), text.md lines 341-345; the page is a flattened image read from a
    300 dpi render (OCR supplement lines 1564-1615)
  extracted_at: '2026-09-11'
---

Read from the 300 dpi render; the page is a flattened image and its extracted text is garbled.

**Console head** - four leads run to a **CSAFE / HDMI / BNC / RJ45 Combo Board**.

**Down the mast** - an **8 PIN COMPUTER CABLE** and a **3 PIN POWER CABLE**.

**Driver board** - **DYA-W10A-IMX6-R10-LCD BOARD**, with CN4, CN6 and CN3 along the top and CN8
(BRAKE) and CN2 along the bottom. The 8-pin computer cable lands on the top-right socket; the
**SPEED SENSOR** lands on CN4; a **2 PIN RED WIRE BRAKE** runs from CN8 to the flywheel brake; the
**DC JACK** feeds CN2; the 3-pin power cable leaves CN3. CN6 is drawn but nothing is wired to it.

**Power** - an **AC ADAPTER, FSP100-RTAAN2, INPUT AC 100-240V, OUTPUT DC 24V / 4.17A**, into the DC
jack.

**Flywheel** - drawn with its brake at the edge, wired back to the 2-pin red brake lead.

**The CU900ENT and CR900ENT bike books print the same drawing** under their own headings - same
combo board, cables, board number, connector numbers, adapter and flywheel, line for line; only
the title and the console picture change (`cu900ent-circuit-diagram`).


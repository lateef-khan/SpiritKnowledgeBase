---
id: cu900ent-circuit-diagram
title: Upright bike circuit diagram
kind: spec
question: What does the circuit diagram of a Spirit cu900ent upright bike show?
asked_as:
- wiring diagram for the cu900 bike
- cu900ent schematic
- how is the cu900 wired
- what cables run up the bike mast
keywords:
- circuit diagram
- wiring diagram
- schematic
- combo board
- computer cable
- power cable
- dc jack
- brake
- speed sensor
- flywheel
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-ac-adapter-rating
- cu900ent-driver-board-connectors
- cu900ent-io-board-connections
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: p. 24 (printed 24), full-page drawing titled '(CU900-ENT) UPRIGHT CIRCUIT
    DIAGRAM'
  extracted_at: '2026-09-08'
---

Read from the 300 dpi render; the page is a flattened image and its extracted text is garbled.

**Console head** - four leads run to a **CSAFE / HDMI / BNC / RJ45 Combo Board**.

**Down the mast** - an **8 PIN COMPUTER CABLE** and a **3 PIN POWER CABLE**.

**Driver board** - **DYA-W10A-IMX6-R10-LCD BOARD**, with CN4, CN6 and CN3 along the top and
CN8 (BRAKE) and CN2 along the bottom. The 8-pin computer cable lands on CN3; the **speed sensor**
lands on CN4; a **2 PIN RED WIRE BRAKE** runs from CN8 to the flywheel brake; the **DC JACK**
feeds CN2. CN6 is drawn but nothing is wired to it.

**Power** - an **AC ADAPTER, FSP100-RTAAN2, INPUT AC 100-240V, OUTPUT DC 24V / 4.17A**, into the
DC jack.

**Flywheel** - drawn with its brake at the edge, wired back to the 2-pin red brake lead.

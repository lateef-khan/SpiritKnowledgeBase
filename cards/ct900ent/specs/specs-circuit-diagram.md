---
id: ct900ent-specs-circuit-diagram
title: 'The 120 volt circuit diagram: an AC inverter, a combo board with SAFE, HDMI,
  BNC and RJ45, and an ERP board'
kind: spec
question: What does the circuit diagram of a Spirit ct900ent treadmill show, and which
  parts does it name?
asked_as:
- wiring diagram for the ct900 ent
- ct900ent schematic
- what is the combo board on the ct900 ent
- where does the hdmi go on the ct900 ent
keywords:
- circuit diagram
- wiring diagram
- schematic
- ac inverter
- erp board
- combo board
- hdmi
- rj45
- bnc
- incline motor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900-specs-circuit-diagram
- ct1000ent-2023-specs-circuit-diagram
see_also:
- ct900ent-specs-io-board-connectors
- spirit-ct900-specs-driver-board-is-a-delta-inverter
- ct900ent-specs-electrical-part-descriptions
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: PDF p. 24 (printed 24) 'Circuit diagram(120V)', drawing titled 'ST8800-WT002
    TREADMILL CIRCUIT DIAGRAM'; text.md lines 341-346, OCR supplement lines 1669-1722;
    read from the render
  extracted_at: '2026-09-11'
---

The sheet is headed **ST8800-WT002** and the page title says **120V**.

**Console.** Four lines drop from the console to a **Combo Board** labelled **SAFE, HDMI, BNC, RJ45**. A
separate **COMPUTER CABLE (MIDDLE)** runs from the console down to the **ERP BOARD**; the sheet does not
print its pin count (the CT900 sheet calls the equivalent cable 12-pin).

**Power path.** AC POWER INPUT plug with a green/yellow ground wire, **AC SWITCH** (white wire), a
**FILTER** (white wire in and out, black wire in and out), then **AC1 / AC2** on the **AC INVERTER**.
There is **no choke** on this sheet; the CT900's 220-volt sheet has one.

**Drive.** The AC INVERTER drives the **MOTOR** on **U / V / W**; the motor has a ground wire and returns an
**RPM SENSOR SIGNAL**. **DOWN / UP / COM** go to the **INCLINE MOTOR** on black / red / white wires, with an
**INCLINE MOTOR VR POSITION** wire and a ground wire. The ERP board's **TO INVERTER SIGNAL WIRE** goes to a
fifth inverter terminal beside U / V / W.

No breaker, inverter model, motor model, cable length or pin table is printed on the sheet.

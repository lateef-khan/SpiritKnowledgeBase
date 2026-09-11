---
id: ct1000ent-2023-specs-circuit-diagram
title: 'The 230 volt circuit diagram: a DELTA inverter with an inverter bridge board,
  optically coupled sensing and a front transfer board'
kind: spec
question: What does the circuit diagram of a Spirit ct1000ent-2023 treadmill show,
  and which parts does it name?
asked_as:
- wiring diagram for the ct1000 ent
- ct1000 schematic
- what is the inverter bridge board
- how many pins is the ct1000 upper main control wire
keywords:
- circuit diagram
- wiring diagram
- schematic
- inverter
- delta
- inverter bridge board
- front transfer board
- choke
- filter
- optically coupled
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct1000ent-2023
  applies_to:
  - ct1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210854'
authority: 3
not_to_be_confused_with:
- ct900-specs-circuit-diagram
- ct900ent-specs-circuit-diagram
see_also:
- ct1000ent-2023-specs-io-board-connectors
- ct1000ent-2023-specs-electrical-part-descriptions
- spirit-ct900-specs-driver-board-is-a-delta-inverter
source:
  ref: spirit-treadmill-ct1000ent-2023-service-manual
  locator: PDF p. 16 (printed 16) '6.2 Circuit Diagram(230V)', drawing titled 'ST8880-ST018
    230V TREADMILL CIRCUIT DIAGRAM'; text.md lines 354-359, OCR supplement lines 1043-1098;
    read from the render
  extracted_at: '2026-09-11'
---

The sheet is headed **ST8880-ST018 230V**.

**Console.** A **6-PIN Upper Main Control Wire** and a **TFT DC Power** lead leave the console, plus
**C-SAFE**, **HDMI**, **RJ45** and a **TV Cable RF Connector**, the last four into a **Front Transfer
Board**.

**Power path.** AC POWER INPUT plug, power cable and connector into a block holding the **AC SOCKET**,
**BREAKER** and **AC SWITCH** with a grounding lead; then a **FILTER** (Nin / Lin / Lout / Nout) and a
**Choke** (Nin / Nout) into the inverter's **AC IN (L, N)**.

**Inverter bridge board.** Sits between console and inverter with: an **Optically Coupled Sensing
Connector**, **To DELTA Cable**, **TFT DC IN**, **DELTA Control Wire**, **TFT DC OUT** and **To Console
Control Wire**. An **INVERTER Communication WIRE** and an **Optically Coupled Sensing** line run down to
the inverter, whose own labels read **To Inverter bridge board Cable**, **DC OUT**, **To Inverter bridge
Control Wire**.

**Drive.** The **Inverter** feeds the **AC MOTOR** on **U V W** plus **G** and a **TEMP** lead, and the
motor carries its own **Optically Coupled Sensing** line and a ground wire. **DOWN / UP / COM** go to the
**INCLINE MOTOR** on black / red / white wires with a **3-PIN INCLINE COMPUTER CABLE** and a ground wire.

The word DELTA names the inverter maker; the CT900 and CT900ENT books name the same family's board
VFD015TM12A, a Delta VFD-TM drive. No breaker rating, motor model or cable length is printed.

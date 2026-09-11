---
id: ct900-specs-circuit-diagram
title: 'The circuit diagram: an AC inverter, a choke and filter, an ERP board and
  a 12-pin console cable'
kind: spec
question: What does the circuit diagram of a Spirit ct900 treadmill show, and which
  parts does it name?
asked_as:
- wiring diagram for the ct900
- ct900 schematic
- what is the erp board on the ct900
- is there a chock on the ct900 power line
keywords:
- circuit diagram
- wiring diagram
- schematic
- ac inverter
- erp board
- chock
- filter
- incline motor
- rpm sensor
- computer cable
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: specs
  code: '*'
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900ent-specs-circuit-diagram
- ct1000ent-2023-specs-circuit-diagram
see_also:
- ct900-specs-transfer-board-pin-definitions
- ct900-specs-console-back-cover-transfer-board
- spirit-ct900-specs-driver-board-is-a-delta-inverter
- ct900-specs-electrical-part-descriptions
source:
  ref: spirit-treadmill-ct900-service-manual
  locator: PDF p. 39 (printed 39) 'Circuit diagram', drawing titled 'ST8800-ST006
    TREADMILL CIRCUIT DIAGRAM'; text.md lines 573-578, OCR supplement lines 2095-2157;
    read from the render
  extracted_at: '2026-09-11'
---

The sheet is headed **ST8800-ST006**. It is the only CT900 drawing that prints a document code.

**Power path.** AC POWER INPUT plug with a green/yellow ground wire, **AC SWITCH** (white wire), a
**FILTER** (white wire in and out, black wire in and out), then a **CHOCK** on the black line, then
**AC1 / AC2** on the **AC INVERTER**.

**Drive.** The AC INVERTER drives the **MOTOR** on **U / V / W**; the motor has a ground wire and returns an
**RPM SENSOR SIGNAL** to the inverter. The inverter's **DOWN / UP / COM** go to the **INCLINE MOTOR** on
black / red / white wires; an **INCLINE MOTOR VR POSITION** wire and a ground wire complete the motor.

**Console.** A **12 PIN COMPUTER CABLE (MIDDLE)** runs from the console to an **ERP BOARD**, which passes
a **TO INVERTER SIGNAL WIRE** down to the inverter. The console's four connector tables (J1·J9 main
connector, J6·J16 HR board, J4·J14 safety, J5·J15 keypad) are printed on the sheet and are on the
pin-definition card.

**What the sheet does not print.** No breaker, no inverter model, no motor model, no cable length and no
input voltage appear on the drawing itself; the book's safety page is the 220-volt page, and the 120-volt
sister sheet is the CT900ENT's ST8800-WT002.

---
id: jb950-2022-specs-circuit-diagram-9-pin-console-cable-and-6-pin-key-cable
title: 'Circuit diagram: an exercise meter on 6- and 9-terminal blocks, a 9-pin console
  cable to the CS52003 controller, and a brake cable down to the CS63027 limit board,
  the CS63029 encoder and the DC motor'
kind: spec
question: What does the circuit diagram of a Spirit jb950-2022 indoor cycle show?
asked_as:
- jb950 wiring diagram
- jb950 circuit diagram
- how is the jb950 console connected to the controller
- what is the 6 pin cable on the jb950
keywords:
- circuit diagram
- wiring diagram
- schematic
- exercise meter
- 9 pin cable
- 6 pin cable
- 6 terminal block
- 9 terminal block
- console connection
- up/down/play key
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: specs
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-cr900-cu900-2018-specs-circuit-diagram
see_also:
- jb950-2022-specs-lower-control-board-cs52003-connectors-and-pin-definitions
- jb950-2022-specs-mcu-board-connectors-j1-to-j5-pin-definitions
- jb950-2022-specs-brake-assembly-limit-sensor-board-cs63027-and-encoder-board-cs63029
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 5.2 Circuit Diagram, 'JB950 CIRCUIT DIAGRAM', PDF p. 38 (printed 38), text.md
    lines 593-605, a flattened drawing read from a 300 dpi render (OCR supplement
    lines 1129-1148)
  extracted_at: '2026-09-11'
---

A harness drawing with cable pin counts and board socket numbers, no wire colours.

- The console is drawn as the **EXERCISE METER**; under it a **6 TERMINAL BLOCK** and a **9
  TERMINAL BLOCK** - the MCU board's J5 and J1.
- The **UP/DOWN/PLAY KEY** in the handlebar (the forward control panel) runs a **6 PIN CABLE** to
  the 6-terminal block.
- A **9 PIN CABLE**, captioned *CONSOLE CONNECTION*, runs from the 9-terminal block to
  **CONTROLLER CS52003 J2**.
- On the controller: **J3** to the **SPEED SENSOR**, **J1** to the **GENERATOR**, **J4** down to
  the brake.
- **CS63027** (the limit sensor board): **J2** from the controller's J4; **J3** to **OUT** on
  **CS63029** (the encoder board); **J1** to the **DC MOTOR**'s **M+** and **M-**.

**Nothing else is drawn** - no adapter, no mains, no heart-rate receiver, no Bluetooth module. The
9 V external input on the controller's J5 exists on the board page but not on this drawing.
The 9-pin and 8-pin lists behind J2 and J4 are on
`jb950-2022-specs-lower-control-board-cs52003-connectors-and-pin-definitions`.


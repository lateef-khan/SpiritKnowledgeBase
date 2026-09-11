---
id: ce1000ent-2023-specs-circuit-diagram-se8880-sb028-230v
title: 'Circuit diagram titled 230V for the elliptical: adapter into a DC jack, 6-pin
  main control wires, a TFT power lead, a communication transfer board and 4-pin and
  3-pin XHP hand-pulse plugs'
kind: spec
question: What does the circuit diagram of a Spirit ce1000ent-2023 elliptical show?
asked_as:
- ce1000ent wiring diagram
- ce1000 schematic 230v
- what cables run up the mast on the ce1000 ent
- how is the ce1000 console powered
keywords:
- circuit diagram
- wiring diagram
- schematic
- se8880-sb028
- 230v
- dc jack
- 6-pin main control wires
- tft power
- communication transfer board
- xhp
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce1000ent-2023
  applies_to:
  - ce1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210054'
authority: 3
not_to_be_confused_with:
- ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board
see_also:
- ce1000ent-2023-specs-power-adapter-100-w-24-v-5-a
- ce1000ent-2023-specs-driver-board-cs56012-connections
- ce1000ent-2023-specs-unit-block-diagram
- cu1000ent-2023-specs-circuit-diagram
source:
  ref: spirit-elliptical-ce1000ent-2023-service-manual
  locator: Section 7.4 Circuit Diagram, PDF p. 13 (printed 13), text.md lines 290-296;
    the drawing is a flattened image read from a 300 dpi render (OCR supplement lines
    924-974)
  extracted_at: '2026-09-11'
---

The drawing is headed **SE8880-SB028 230V Elliptical CIRCUIT DIAGRAM**. The 230V in the title is part
of the drawing's own name; the adapter beside it is not given a mains rating.

**Power.** AC POWER INPUT (plug, power cable, connector) feeds a **100W Power Adapter, OUTPUT DC 24V /
5A**, whose lead ends in a **DC JACK** on the frame. From the jack, **INPUT DC 24V / 5A** goes into
the **CONTROLLER**. The controller has a separate **POWER OUT TO TFT POWER** lead up to the screen's
**TFT POWER INPUT**.

**Control.** **6-PIN MAIN CONTROL WIRES** run between the controller and the console. Two more
controller leads: **M+** to the brake on the flywheel, and **JK** to a **2-PIN SENSOR WIRE** (the
speed sensor).

**Console side.** A **Communication transfer board** carries **RJ45 INTERNET**, **TV RF CABLE**,
**C-SAFE** and **HDMI** from their sockets on the console. The keypad below the screen is drawn with
**NFC, START, STOP and LEVEL - / +**. Two hand-grip pulse plugs are labelled **4-PIN XHP** and
**3-PIN XHP**, captioned *Holding heartbeat*.

**Spelling to search for:** the console-side C-SAFE socket is printed **C-SAVE** on this drawing.
The CU1000ENT bike's drawing is the same layout under the code SU8880-SB028
(`cu1000ent-2023-specs-circuit-diagram`); the CE900ENT is a different loom with an 8-pin computer
cable (`ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board`).


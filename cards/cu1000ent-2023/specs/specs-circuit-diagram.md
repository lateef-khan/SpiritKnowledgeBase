---
id: cu1000ent-2023-specs-circuit-diagram
title: 'Circuit diagram titled 230V: adapter into a DC jack, 6-pin main control wires,
  a TFT power lead, a communication transfer board and 4-pin and 3-pin XHP hand-pulse
  plugs'
kind: spec
question: What does the circuit diagram of a Spirit cu1000ent-2023 upright bike show?
asked_as:
- cu1000ent wiring diagram
- cu1000 schematic 230v
- what cables run up the mast on the cu1000 ent
- how is the cu1000 console powered
keywords:
- circuit diagram
- wiring diagram
- schematic
- su8880-sb028
- 230v
- dc jack
- 6-pin main control wires
- tft power
- communication transfer board
- xhp
facets:
  brand:
  - spirit
  product_line: bike
  model: cu1000ent-2023
  applies_to:
  - cu1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210354'
authority: 3
not_to_be_confused_with:
- cu900ent-circuit-diagram
see_also:
- cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a
- cu1000ent-2023-specs-driver-board-cs56012-connections
- cu1000ent-2023-specs-unit-block-diagram
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: Section 7.4 Circuit Diagram, PDF p. 13 (printed 13), text.md lines 259-264;
    the drawing is a flattened image read from a 300 dpi render (OCR supplement lines
    898-946)
  extracted_at: '2026-09-11'
---

The drawing is headed **SU8880-SB028 230V Upright Bike CIRCUIT DIAGRAM**. The 230V in the title is
part of the drawing's own name; the adapter beside it is not given a mains rating.

**Power.** AC POWER INPUT (plug, power cable, connector) feeds a **100W Power Adapter, OUTPUT DC
24V / 5A**, whose lead ends in a **DC JACK** on the frame. From the jack, **INPUT DC 24V / 5A** goes
into the **CONTROLLER**. The controller has a separate **POWER OUT TO TFT POWER** lead up to the
screen's **TFT POWER INPUT**.

**Control.** **6-PIN MAIN CONTROL WIRES** run between the controller and the console. Two more
controller leads: **M+** to the brake on the flywheel, and **JK** to a **2-PIN SENSOR WIRE** (the
speed sensor).

**Console side.** A **Communication transfer board** carries **RJ45 INTERNET**, **TV RF CABLE**,
**C-SAFE** and **HDMI** from their sockets on the console. The keypad below the screen is drawn
with **NFC, START, STOP and LEVEL - / +**. Two hand-grip pulse plugs are labelled **4-PIN XHP** and
**3-PIN XHP**, captioned *Holding heartbeat*.

**Spelling to search for:** the console-side C-SAFE socket is printed **C-SAVE** on this drawing.


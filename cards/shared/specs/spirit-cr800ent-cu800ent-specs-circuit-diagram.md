---
id: spirit-cr800ent-cu800ent-specs-circuit-diagram
title: 'Schematics headed with the YB037 factory codes: a fused appliance inlet, black
  and white mains wires, a 6+4-pin computer cable, and a 5-pin controller cable on
  the upright against a 6-pin on the recumbent'
kind: spec
question: What does the circuit diagram of a Spirit CR800ENT or CU800ENT bike show,
  and how do the two differ?
asked_as:
- cu800ent wiring diagram
- cr800 ent schematic
- how many pins is the controller cable on the cu800ent
- what is xu480-yb037
keywords:
- circuit diagram
- schematic
- xu480-yb037
- xr480-yb037
- appliance inlet
- fuse
- power cord
- 6+4 pins computer cable
- 5 pins controller cable
- 6 pins controller cable
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800-cu800-2021-specs-circuit-diagram
- cu900ent-circuit-diagram
see_also:
- spirit-cr800ent-cu800ent-specs-driver-board-connections
- spirit-cr800ent-cu800ent-specs-power-bridge-board-and-converter
- spirit-cr800ent-cu800ent-specs-console-transfer-board-and-hdmi-csafe-board
- ct800ent-2022-specs-circuit-diagram
source:
  ref: spirit-bike-cu800ent-2022-service-manual
  locator: 'CU800ENT: 7-2 Circuit Diagram ''#XU480-YB037 SCHEMATIC'', PDF p. 26 (printed
    26), text.md lines 412-417, a rotated flattened drawing read from a 220 dpi render
    (OCR supplement lines 1013-1030). CR800ENT: ''#XR480-YB037 SCHEMATIC'', PDF p.
    26, lines 419-424 (OCR lines 1098-1148)'
  extracted_at: '2026-09-11'
---

Both drawings are printed sideways on the page. They are headed with the Dyaco factory codes
**XU480-YB037** (upright) and **XR480-YB037** (recumbent) - the same 480 codes the owner's-manual
exploded views carry.

**Shared by both.** POWER CORD into a fused **APPLIANCE INLET** with a rocker switch; from it
**GROUNDING**, a **BLACK WIRE** and a **WHITE WIRE**. The black and white wires feed the **POWER
CONVERTER** (L, N) and the **TFT POWER BRIDGE BOARD** (AC N, AC L, twice), and run on to the
**CONTROLLER**. The converter's **V+, V-** lead goes to the bridge board's **12V POWER INPUT**;
**JK 2** on the bridge board feeds the **6+4(6+2+2) PINS COMPUTER CABLE** up to the console's
CONTROL socket; **DATA INPUT** takes the controller cable from the controller's **STD** socket.
The **HDMI/ETHERNET/C-SAFE PCB** (sockets HDMI, JK 1, C-SAFE) sends an **HDMI CABLE**, an
**ETHERNET CABLE** and a **5 PINS C-SAFE CABLE** up to the console. The **INDUCTION BRAKE** hangs
on a **2 PIN wire**, joined through two 2 PIN plugs to a **Red wire** into the controller, and the
controller's **SPEED** socket takes the **RPM SENSOR WIRE**.

**Where the two differ:**

| | CU800ENT (XU480) | CR800ENT (XR480) |
|---|---|---|
| Controller cable | **5 PINS CONTROLLER CABLE** | **6 PINS CONTROLLER CABLE** |
| Mains sockets on the controller | **J5**, **J12** | **ACN**, **ACL** |
| Hand pulse | HP-RIGHT **3 PIN CABLE**, HP-LEFT **4 PIN CABLE** straight to the sensor pads | the same two, but through a **HANDPULSE CABLE** and two **LINK CABLE**s to the seat-side pads |

A controller cable ordered from the wrong book will have the wrong pin count. The treadmill ENT
schematic is the same layout with a motor drive in place of the brake: `ct800ent-2022-specs-circuit-diagram`.


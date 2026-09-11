---
id: xterra-tr-specs-wiring-diagram-with-a-brake-module-and-a-7-pin-computer-cable
title: 'The wiring diagram: motor through a brake module to the controller, a 7-pin
  computer cable, 3-pin incline and speed wires with 2-pin hand pulse wires on each
  grip, and a power switch, socket and breaker on blue and brown wires'
kind: spec
question: What does the treadmill wiring diagram in the Xterra TR hiking treadmill
  service manual show, and which book is it drawn for?
asked_as:
- tr95h wiring diagram
- tr75h wiring diagram
- what is the brake module on the tr95h
- tr75h 7 pin computer cable
keywords:
- wiring diagram
- brake module
- computer cable
- 7-pin
- incline wire
- speed wire
- hand pulse wire
- power switch
- breaker
- jkexer
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
see_also:
- xterra-tr-specs-driver-board-td-65hs-seventeen-callouts
- xterra-tr-specs-brake-board-four-callouts
- xterra-tr-specs-display-board-jkm-337-eleven-sockets
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: 'TR95H SM (JKEXER 337) ''7. Treadmill wiring diagram'', PDF p. 12, lines
    160-161, OCR supplement lines 281-318, read from a 160 dpi render. TR75H SM (V1.0,
    Jan 2026) ''7. Treadmill wiring diagram'', PDF p. 10 (printed 10), lines 213-220,
    OCR supplement lines 468-488: the same drawing, still titled TR95H'
  extracted_at: '2026-09-11'
---

**Both JKEXER books print the sheet headed "TR95H TREADMILL WIRING DIAGRAM" - the TR75H book reuses the TR95H
drawing under that title.** The two machines share the boards on the other JKEXER cards, so the drawing fits both,
but a reader of the TR75H book should know the title names the other machine.

**Console side.** The console connects to the controller's **J8** by the **COMPUTER CABLE (7 PIN)** - not the 5-pin
cable of the Dyaco-built Xterra treadmills. The **(L)** grip, "HAND PULSE & Quick handrail button (INCLINE)", carries
an **INCLINE WIRE (3 PIN)** and a **HAND PULSE WIRE (2 PIN)**; the **(R)** grip, "(SPEED)", carries a **SPEED WIRE
(3 PIN)** and a **HAND PULSE WIRE (2 PIN)**. The **SAFETY KEY** hangs below the console on its own lead.

**Drive.** MOTOR → **BRAKE MODULE** → CONTROLLER. The motor's **RED WIRE** goes to the brake module's **M+** and its
"BREAK" (black) wire to the module's **M-**; the motor has a GROUND WIRE. From the brake module a **WHITE WIRE**
carries M+ and a "BREAK WIRE" carries M- to the controller's **M+** and **M-**. A **BRAKE CONTROL WIRE (3 PIN)** runs
from the brake module to the controller's **J13**; the **SENSOR WIRE (2 PIN)** lands on **J9**.

**Incline.** The INCLINE MOTOR takes **DOWN (BLACK WIRE)**, **UP (RED WIRE)** and **COM (WHITE WIRE)** from the
controller and returns an **INCLINE VR CABLE (3 PIN)**; it has its own GROUND WIRE.

**Mains.** The AC SOCKET's **BLUE WIRE** goes to the POWER SWITCH (ON/OFF), its **BROWN WIRE** to the **BREAKER**, and
its ground wire to earth. From the switch a **WHITE WIRE** and from the breaker a "BREAK WIRE" (black) reach the
controller's two **AC** terminals.

The diagram prints no pin definition for the 7-pin cable and no wire gauges. The word "break" on the sheet stands for
"black" throughout.

---
id: mt200-2022-specs-wiring-diagram
title: 'The wiring diagram: console, lower control board, inverter, angle sensor,
  brake and step sensors, with the pin tables and test values'
kind: spec
question: What does the wiring diagram of a Spirit mt200-2022 treadmill show, and
  what should be measured at each connector?
asked_as:
- wiring diagram for the mt200
- pinout of the mt200 12 pin console cable
- what voltage should the mt200 step sensor get
- mt200 brake voltage
keywords:
- wiring diagram
- schematic
- pinout
- lower control board
- inverter
- angle sensor
- brake
- step sensor
- rs485
- test voltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2026
  - mt200-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct800-2016-specs-console-12-pin-cable-pinout
- ct900-specs-transfer-board-pin-definitions
see_also:
- mt200-2022-specs-component-description-callouts
- mt200-2022-assembly-drive-motor-and-belt-replacement
- mt200-2022-assembly-step-sensor-replacement
- mt200-2022-assembly-incline-motor-replacement
- mt200-2022-console-screen-layout
source:
  ref: spirit-treadmill-mt200-2022-service-manual
  locator: 'PDF p. 52 (printed 52), section 8 Wiring Diagram, text.md lines 1032-1037,
    OCR supplement lines 1248-1357 (partly misread); read from the 300 dpi render,
    a low-resolution raster on which the two smallest tables are only partly legible.
    Test values: troubleshooting steps 1.4-1.5 (PDF p. 18, lines 390-402), 2.2 (p.
    19, line 409), 3.1 (p. 20, lines 421-422), 4.1-4.2 (p. 21, lines 434-442), 5.1
    (p. 22, lines 456-458); brake 18vdc, maintenance mode p. 8, lines 144-145 The February 2026 export of the same book is titled 7.0T-770885 (MT8000-ST021-01), spirit-treadmill-70t-2026-service-manual, and prints this page unchanged.'
  extracted_at: '2026-09-11'
---

The whole sheet is one flattened picture. It is drawn as boxes for the **Console**, the **Lower control
board (LCB)**, the **Inverter**, the motor, the two incline motors, the brake, the angle sensor, the fan
and the step sensors, joined by numbered connectors. Where the render was too coarse to be sure, the
entry says so.

**Console J5 ↔ LCB J5 - the 12-pin console cable**

| Pin | Signal | Pin | Signal | Pin | Signal |
|---|---|---|---|---|---|
| P1 | S/W | P5 | TX | P9 | SPD2 |
| P2 | Front Incline Down | P6 | RX | P10 | +5V |
| P3 | Front Incline UP | P7 | PGND | P11 | Front IPOS(VR) |
| P4 | VIN | P8 | SPD1 | P12 | GND |

**Console J7 ↔ LCB J3 - rear incline control (5 pins)**: P1 GND, P2 IPOS(VR), P3 +5V, P4 Rear Incline
Enable, P5 Rear Incline UP/Down.

**Console J6 ↔ Inverter J9 - RS485 (8 pins)**: P1-P3 N.C., **P4 B**, **P5 A**, P6-P8 N.C.

**Inverter JP3 ↔ LCB J4 (12 pins)**: the same list as J5 with **P5 and P6 marked NC** - the console's TX
/ RX do not pass through the LCB to the inverter; the console talks to the inverter on RS485.

**Inverter**: motor **G020601** U / V / W on J3 / J4 / J5; **angle sensor** (encoder, 8 pins) on J4 -
P1 A+, P2 A-, P3 B+, P4 B-, P5 M+, P6 M-, P7 +5V, P8 GND; **brake** on JP5; front incline **J9 Incline
down, J2 Common, J8 Incline up**; front position sensor on **JP7**; line AC power / neutral on **J1 /
J6** from LCB **J9 / J11**; fan **F040012** on J13 / J14.

**Lower control board**: rear position sensor on **J6**; rear incline down / common / up on **J12 / J13
/ J14**; mains in on **J10 / J8** from the filter **F060009**; left and right step sensors on **J1 /
J2**. The 3-pin position-sensor table and the step-sensor table are too coarse to read reliably; as far
as they read, the position sensor is GND / POS(VR) / +5V and the step sensor +12 V / GND / signal.

**Power-entry parts named on the sheet**: power cord **E060107**, AC input module **F030062-01**, wires
**E010808** and **E010809** (300 mm white and black), **E010772** (150 mm white), **E010773** (300 mm
black).

**What to measure at these connectors** (the troubleshooting chapter's figures):

| Where | Expect |
|---|---|
| Console 12-pin, pin 4 (Vin) to pin 12 (Gnd), console unplugged; then the red 12-pin on the LCB, same pins | **12 V DC** |
| Motor, between each pair of the three wires | **about 2 Ohms** |
| Brake wires, brake turned OFF in maintenance mode (coil energised) | **18 vdc** on the maintenance page, **about 19 V DC** at the drive output in troubleshooting; **0 V** when the brake is ON |
| Step-sensor cable from the LCB, pin 1 to pin 2 (LEFT / RIGHT) | **10 to 12 V DC** |
| Incline-motor potentiometer, pin 1 to pin 3 | **5 V DC**; pin 1 to pin 2 **0.5 to 5 V DC** through the travel |

The brake figure is printed two ways in one book, 18 and 19 volts, both "when the brake is off". The
motor-casing-to-chassis 1.5 megohm check and the belt tension are in the drive-motor replacement card.

**This book is also the 7.0T 770885's service manual.** Spirit's February 2026 export of it is titled *7.0T-770885 (MT8000-ST021-01)* and is 99.7% the same text (the parts-list header reads MT8000 where the 2021 export reads MT7000), so the 2026 7.0T (`70t-2026`) is listed here alongside the MT200.

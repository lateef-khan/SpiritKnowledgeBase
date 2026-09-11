---
id: ct800ent-2022-specs-circuit-diagram
title: 'The ENT circuit diagram: a DC motor, a 10-pin upper cable and a communication
  transfer board'
kind: spec
question: What does the circuit diagram of a Spirit ct800ent-2022 treadmill show,
  and which parts does it name?
asked_as:
- wiring diagram for the ct800 ent
- ct800ent schematic
- how many pins is the ct800 ent console cable
- what is the communication transfer board
keywords:
- circuit diagram
- wiring diagram
- schematic
- dc motor
- power bridge board
- power adapter
- communication transfer board
- hdmi
- c-safe
- tft
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800ent-2022
  applies_to:
  - ct800ent-2022
  section: specs
  code: '*'
  model_number:
  - '800852'
authority: 3
not_to_be_confused_with:
- ct850ent-2022-specs-circuit-diagram
- ct800-2020-specs-circuit-diagram
see_also:
- ct800ent-2022-specs-console-transfer-and-power-bridge-boards
- spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter
- spirit-ct-ent-specs-unit-block-diagram
- spirit-ct800-specs-driver-board-connector-locations
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: PDF p. 35 (printed 35), section 8-5 Circuit Diagram, drawing titled 'CT800_YT059-01
    TREADMILL CIRCUIT DIAGRAM'; text.md lines 679-684, OCR supplement lines 1465-1516
    is garbled; read from the 300 dpi render
  extracted_at: '2026-09-11'
---

The page is drawn sideways as one flat image and was read from the render. The sheet is headed
**CT800_YT059-01**.

**Console end.** A TFT console with a FAN, two **3 PIN Holding heartbeat group** grips, and four cables
leaving it: **10-PIN UPPER MAIN CONTROL WIRES**, **RJ45 INTERNET**, **C-SAFE** and **HDMI**.

**Power path.** AC POWER INPUT plug, power cable, connector, then an **AC SOCKET**, **BREAKER** and **AC
SWITCH** in one block with a green/yellow earth wire, then a **FILTER**. From the filter a white and a
black wire go to the **Power bridge Board** (terminals AC N, AC L, AC N) and on to a **Power Adapter**,
and a white / black pair goes to the drive board's N and L.

**Drive.** The lower board is labelled **Inverter** even though the machine has a **DC MOTOR** on its M+ /
M- terminals. It also carries N / L, DOWN / UP / COM to the incline motor, a **JK** for the **2-PIN SENSOR
WIRE**, and **JK1** for the **6-PIN CONTROL WIRES** from the power bridge board's JK1. The incline motor
has a **3-PIN INCLINE COMPUTER CABLE** plus black / red / white wires and a ground wire. An **AC FAN**
hangs on the board's N / L.

**Communication.** A **Communication transfer board** takes HDMI, RJ45 INTERNET and C-SAFE; the **6+2+2
PIN LOWER MAIN CONTROL WIRES** run from it "TO JK2" on the power bridge board.

The CT850ENT sheet (CT850_YT060-01) is the same drawing with an AC motor on U / V / W; the CT800-2020
sheet has no power bridge board, no adapter and a 6-pin console cable.

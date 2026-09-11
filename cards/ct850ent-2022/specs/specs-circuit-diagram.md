---
id: ct850ent-2022-specs-circuit-diagram
title: 'The ENT circuit diagram: an AC motor on an inverter, a 10-pin upper cable
  and a communication transfer board'
kind: spec
question: What does the circuit diagram of a Spirit ct850ent-2022 treadmill show,
  and which parts does it name?
asked_as:
- wiring diagram for the ct850 ent
- ct850ent schematic
- how many pins is the ct850 ent console cable
- what is the communication transfer board on the ct850
keywords:
- circuit diagram
- wiring diagram
- schematic
- ac motor
- inverter
- power bridge board
- power adapter
- communication transfer board
- hdmi
- c-safe
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850ent-2022
  applies_to:
  - ct850ent-2022
  section: specs
  code: '*'
  model_number:
  - '850852'
authority: 3
not_to_be_confused_with:
- ct800ent-2022-specs-circuit-diagram
- ct850-2020-treadmill-circuit-diagram
see_also:
- ct850ent-2022-specs-console-transfer-and-power-bridge-boards
- spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter
- spirit-ct-ent-specs-unit-block-diagram
- ct850-2020-driver-board-connector-locations
source:
  ref: spirit-treadmill-ct850ent-2022-service-manual
  locator: PDF p. 36 (printed 36), section 8-5 Circuit Diagram, drawing titled 'CT850_YT060-01
    TREADMILL CIRCUIT DIAGRAM'; text.md lines 698-703, OCR supplement lines 1563-1604
    is garbled; read from the 300 dpi render
  extracted_at: '2026-09-11'
---

The page is drawn sideways as one flat image and was read from the render. The sheet is headed
**CT850_YT060-01**.

**Console end.** A TFT console with a FAN, two **3 PIN Holding heartbeat group** grips, and four cables
leaving it: **10-PIN UPPER MAIN CONTROL WIRES**, **RJ45 INTERNET**, **C-SAFE** and **HDMI**.

**Power path.** AC POWER INPUT plug, power cable, connector, then an **AC SOCKET**, **BREAKER** and **AC
SWITCH** in one block with a green/yellow earth wire, then a **FILTER**. From the filter a white and a
black wire go to the **Power bridge Board** and on to a **Power Adapter**, and a white / black pair goes
to the inverter's N and L.

**Drive.** The **Inverter** carries N / L, **U / V / W** to the **AC MOTOR**, DOWN / UP / COM to the
incline motor, a **JK** for the **2-PIN SENSOR WIRE**, and **JK1** for the **6-PIN CONTROL WIRES** from the
power bridge board's JK1. The incline motor has a **3-PIN INCLINE COMPUTER CABLE** plus black / red /
white wires and a ground wire. An **AC FAN** hangs on the inverter's L / N.

**Communication.** A **Communication transfer board** takes HDMI, RJ45 INTERNET and C-SAFE; the **6+2+2
PIN LOWER MAIN CONTROL WIRES** run from it "TO JK2" on the power bridge board.

The sheet prints no inverter model, motor model, breaker rating or harness length - unlike the CT850-2020
sheet, which names an RM6T6-1003 inverter, a KSP485 motor and an RFMB 20A breaker. The CT800ENT sheet
(CT800_YT059-01) is the same drawing with a DC motor.

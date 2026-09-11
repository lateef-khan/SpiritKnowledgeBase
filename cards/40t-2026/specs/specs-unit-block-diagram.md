---
id: 40t-2026-specs-unit-block-diagram
title: The unit block diagram, with a wireless Bluetooth heart-rate receiver and no
  RPM-sensor box
kind: spec
question: What does the unit block diagram of a Spirit 40t-2026 treadmill show?
asked_as:
- block diagram of the 4.0t
- how are the boards connected on the 4.0t
- treadmill configuration 4.0t
- signal flow between console and inverter 4.0t
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- inverter
- bluetooth
- hr receiver
- safety key
- signal flow
- current braker
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 40t-2026
  applies_to:
  - 40t-2026
  section: specs
  code: '*'
  model_number:
  - '740885'
authority: 3
not_to_be_confused_with:
- ct850-2020-unit-block-diagram
see_also:
- 40t-2026-specs-circuit-diagram
- 40t-2026-specs-display-board-and-transfer-board-connectors
- 40t-2026-specs-rear-incline-interface-board-and-inverter-connectors
source:
  ref: spirit-treadmill-40t-2026-service-manual
  locator: PDF p. 17 (printed 17) 'Treadmill Configuration', section 5, text.md lines
    248-253, OCR supplement lines 1082-1103; read from the render
  extracted_at: '2026-09-11'
---

The page is one flat drawing; the extracted text carries only the title.

**Upper half.** KEY, COOLING FAN, HR HANDLEBAR, a **wireless Bluetooth HR receiver** and SAFETY KEY feed
the **DISPLAY BOARD**, which feeds an **AMPLIFIER** with **LINE IN** and drives **SPEAKER L** and
**SPEAKER R**.

**Lower half.** POWER goes through the **POWER SWITCH** and a **CURRENT BRAKER** to the **DRIVER BOARD**,
which drives the **MOTOR** and the **INCLINE MOTOR**; a **VR SET** box hangs on the incline side.

Two things differ from the CT850-2020 drawing this one was copied from: the receiver box says
*Bluetooth*, and there is **no RPM SENSOR box** beside the motor. The drawing does not show the rear
incline motor, the rear incline interface board or the relay; those are on the driver-board pages and
the circuit diagram.

---
id: f63-2023-drive-motor-spec
title: Drive motor voltage and wiring
kind: spec
question: What are the drive motor specifications for a Sole F63-2023?
asked_as:
- what voltage is the treadmill motor
- which motor wire is positive
- drive motor wiring on my sole treadmill
keywords:
- drive motor
- dc motor
- 0-90 volt
- 0-180 volt
- m+
- m-
- motor wires
- grounding wire
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2023
  applies_to:
  - f63-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2023-e4-error-code
- f63-2023-drive-motor-replacement
source:
  ref: sole-tm-f63-2023-service-manual
  locator: page 6, GENERAL INFORMATION, and page 40
  extracted_at: '2026-09-04'
---

A variable speed DC motor. The main controller feeds it **0 to 180 DC volts**, or **0 to 90 DC volts on a 120Vac electronic power system**, to raise or lower the speed of the running belt. The higher the voltage, the faster the motor turns.

**Three wire connection: red, black and green.**

- The **red** wire goes into **M+**.
- The **green** wire is the grounding wire.

**The manual is inconsistent about M-.** The general information table on page 6 says "The White wire is inserted into M-", while the drive motor replacement steps on page 40 say the motor has **2 input wires, black and red**, and that they plug in as **Red to M+ and Black to M-**. The motor supplied has red, black and green leads.

The main controller carries the DC power supply for the console, the incline driver and the DC motor driver.

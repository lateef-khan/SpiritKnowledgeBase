---
id: f63-2016-drive-motor-spec
title: Drive motor voltage and wiring
kind: spec
question: What are the drive motor specifications for a Sole F63-2016?
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
  model: f63-2016
  applies_to:
  - f63-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f63-2016-e4-error-code
- f63-2016-drive-motor-replacement
- f63-2016-driver-board-sockets
source:
  ref: sole-tm-f63-2016-service-manual
  locator: page 11, GENERAL INFORMATION, and 12-3 Motor Replacement
  extracted_at: '2026-09-04'
---

A DC motor with variable speed. The main controller feeds it **0 to 90 volts (or 0 to 180 volts)** to raise or lower the speed of the running belt. The higher the voltage, the faster the motor turns.

**Three wire connection: red, black and green.**

- The **red** wire goes into **M+**.
- The **white** wire goes into **M-** in the general information section on page 11.
- The **green** wire is the grounding wire.

**The manual is inconsistent about M-.** Page 11 says the white wire goes to M-, while the motor replacement steps say to connect **red M+, black M-** and to remove "motor wire (+) red and motor wire (-) black". The motor itself has red, black and green leads.

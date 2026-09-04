---
id: srvo-power-board-dc-output-pinout
title: Pinout of the SRVO power board direct-current outputs
kind: spec
question: What is the pinout of the DC output ports on the SOLE SRVO power board?
asked_as:
- srvo power board dc output pinout
- srvo power supply output pins
- what feeds the srvo controllers
keywords:
- dc output
- pinout
- positive
- negative
- pe
- ground
- full range power board
- two outputs
- cn1
- cn2
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- srvo-display-board-cn1-debug-pinout
- srvo-controller-cn2-motor-power-pinout
see_also:
- srvo-power-board-connector-map
- srvo-controller-cn3-ac-pinout
source:
  ref: sole-srvo-service-manual
  locator: page 41, section 8-3-2
  extracted_at: '2026-09-04'
---

**These are the two direct-current output ports on the full range power board, CN1 and CN2. On the display main board CN1 is a debug header, and on a controller module CN2 is the motor power port - three different things sharing two numbers.**

| Pin | Name | Description |
|---|---|---|
| CN1-1 | L1 | DC output positive terminal |
| CN1-2 | N1 | DC output negative terminal |
| CN1-3 | PE1 | PE ground electrode terminal |
| CN2-1 | L2 | DC output positive terminal |
| CN2-2 | N2 | DC output negative terminal |
| CN2-3 | PE2 | PE ground electrode terminal |

**The pin names read like AC.** L and N normally mean live and neutral, yet the description column calls them the positive and negative DC terminals, and the port each one feeds - CN3 on a controller module - is labelled an "AC port" with pins named AC_L and AC_N. The manual never resolves this. The key component list says the power module puts out **0 V to 330 V**, which is consistent with a DC bus fed to the motor drives.

The manual prints no default value for any pin.

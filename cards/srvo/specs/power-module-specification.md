---
id: srvo-power-module-specification
title: Power module input and output voltage
kind: spec
question: What voltage does the power module in the SOLE SRVO take and put out?
asked_as:
- what voltage does the srvo run on
- srvo power supply spec
- can the srvo run on 230v
keywords:
- power module
- pfc
- voltage
- input
- output
- 90 to 130v
- 330v
- mains
- power supply
- firmware
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
not_to_be_confused_with: []
see_also:
- srvo-key-component-part-numbers
- srvo-power-board-connector-map
- srvo-disassembly-power-board
- srvo-servo-motor-specification
source:
  ref: sole-srvo-service-manual
  locator: page 28, key component list row 6
  extracted_at: '2026-09-04'
---

Part number **004.057.0054583**, described as: "Single power module, rbt.pfc.01, 90 to 130V, 0 v-330 v, without firmware".

| Item | Value |
|---|---|
| Model | rbt.pfc.01 |
| Input | 90 to 130 V |
| Output | 0 V to 330 V |
| Firmware | supplied without firmware |

The **90 to 130 V** input is a North American mains range. The manual nowhere states a 220 or 230 V variant of this board, so nothing here supports running the machine on a 230 V supply.

"Without firmware" is how the part is stocked. The manual does not say where firmware for it comes from or how it is loaded.

The three voltage fault codes - `0x40` power module low voltage, `0x400` high voltage and `0x800` low voltage - are all judged against this board's range.

---
id: ce800ent-power-bridge-and-power-converter
title: Console power bridge board and power converter connections
kind: spec
question: What connects to the console power bridge board and the power converter
  on a Spirit ce800ent elliptical?
asked_as:
- what is the power converter on the ce800 elliptical
- dc 13v output on the ce800ent
- power bridge board wiring
- ac output on the elliptical converter
keywords:
- power bridge
- power converter
- dc 13v
- ac_l
- ac_n
- computer cable
- controller cable
- connector
- console power
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800ent
  applies_to:
  - ce800ent
  section: specs
  code: '*'
  model_number: '800054'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-console-transfer-board-connections
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: p. 20 (printed 20) 'The console POWER BRIDGE PCB board and POWER CONVERTER';
    p. 22 (printed 22) 'Power Converter PCB board'
  extracted_at: '2026-09-08'
---

**Power bridge board (p. 20)** call-outs:

- **Computer cable (6+2+2 pins)**
- **DC_13V/4A (converter end)**
- **Controller cable**
- **AC_L (output)** and **AC_N (output)**
- **AC_L (input)** and **AC_N (input)**

**Power converter (p. 22, read from the 300 dpi render - the page is a flattened image)**:

- **POWER CONVERTER V+ (RED)** and **V- (BLACK)** on the left
- **AC_N (AC output)** and **AC_L (AC output)** on the right

The converter's DC output is the **13 V / 4 A** rail named on p. 20. No input voltage rating is
printed for the converter itself.

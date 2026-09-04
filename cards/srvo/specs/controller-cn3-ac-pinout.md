---
id: srvo-controller-cn3-ac-pinout
title: Pinout of CN3 on the SRVO controller module
kind: spec
question: What is the pinout of the AC port on a SOLE SRVO controller module?
asked_as:
- srvo controller ac port pinout
- srvo cn3 controller pins
- which pin is live on the srvo controller
keywords:
- cn3
- ac port
- pinout
- live
- neutral
- controller module
- mains
- two pin
- wiring
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: cn3
authority: 3
not_to_be_confused_with:
- srvo-power-board-cn3-ac-input-pinout
- srvo-controller-cn2-motor-power-pinout
see_also:
- srvo-controller-connector-map
source:
  ref: sole-srvo-service-manual
  locator: page 35, section 8-2-1
  extracted_at: '2026-09-04'
---

**This is CN3 on a controller module: two pins, no earth. It is not CN3 on the full range power board, which has three pins and adds PE.**

| Pin | Name | Description |
|---|---|---|
| 1 | L | AC_L |
| 2 | N | AC_N |

The manual prints no default value for either pin.

The manual labels this port "AC" even though the board upstream of it, the full range power board, describes its own CN1 and CN2 as **direct-current** output ports. The manual does not resolve that; measure before you assume.

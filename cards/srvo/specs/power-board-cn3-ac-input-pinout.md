---
id: srvo-power-board-cn3-ac-input-pinout
title: Pinout of CN3 on the SRVO full range power board
kind: spec
question: What is the pinout of the AC input on the SOLE SRVO power board?
asked_as:
- srvo power board ac input pinout
- where does mains connect on the srvo power supply
- srvo pfc board earth pin
keywords:
- cn3
- ac input
- pinout
- live
- neutral
- earth
- ground
- pe
- full range power board
- mains
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
- srvo-controller-cn3-ac-pinout
- srvo-power-board-dc-output-pinout
see_also:
- srvo-power-board-connector-map
source:
  ref: sole-srvo-service-manual
  locator: page 40, section 8-3-1
  extracted_at: '2026-09-04'
---

**This is CN3 on the full range power board: three pins, including the earth. It is not CN3 on a controller module, which has two pins and no earth.**

| Pin | Name | Description |
|---|---|---|
| 1 | L | AC firewire input terminal |
| 2 | N | AC null line input terminal |
| 3 | PE | AC Grounding Terminal |

"Firewire" and "null line" are the manual's translations of live and neutral. They are quoted here as printed; they have nothing to do with the IEEE 1394 Firewire bus.

The manual prints no default value for any pin.

---
id: cu900ent-ac-adapter-rating
title: AC adapter part number and rating
kind: spec
question: What power supply does a Spirit CU900ENT upright or CR900ENT recumbent bike use?
asked_as:
- what adapter does the cu900 bike use
- power supply rating for the cu900ent
- what voltage is the cu900 bike
- replacement power brick for the upright bike
keywords:
- ac adapter
- power supply
- fsp100-rtaan2
- 24v
- 4.17a
- dc jack
- input voltage
- power brick
- rating
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900ent-2021
  - cu900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-circuit-diagram
- cu900ent-driver-board-connectors
- cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: "p. 24 (printed 24), the AC adapter block on the '(CU900-ENT) UPRIGHT CIRCUIT DIAGRAM'. CR900ENT-2021 (spirit-bike-cr900ent-2021-service-manual): the same block on PDF p. 23 (printed 23), text.md line 262, read from the render (OCR supplement lines 1519-1560, upside down)"
  extracted_at: '2026-09-08'
---

The bike runs from an external desktop adapter, not from the mains directly.

| | |
|---|---|
| Part number | **FSP100-RTAAN2** |
| Input | **AC 100-240 V** |
| Output | **DC 24 V / 4.17 A** |

The output goes into a **DC jack** on the frame, and from there to **CN2** on the driver board.
The block diagram on p. 16 shows the same thing as a single "DC POWER" block into the driver
board.

Read from the 300 dpi render of a flattened-image page.

The CR900ENT recumbent's circuit diagram prints the same adapter block - FSP100-RTAAN2, AC
100-240 V in, DC 24 V / 4.17 A out - so the two ENT-900 bikes share the supply. The CU1000ENT
is fed by a different, 100 W 24 V / 5 A unit (`cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a`).

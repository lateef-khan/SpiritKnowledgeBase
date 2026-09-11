---
id: cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a
title: A 100 W desktop adapter delivering DC 24 V at 5 A into a DC jack
kind: spec
question: What power supply does a Spirit CU1000ENT upright or CR1000ENT recumbent 2023 bike use?
asked_as:
- what adapter does the cu1000 ent use
- power supply rating for the cu1000ent
- is the cu1000 24 volt
- replacement power brick for the cu1000
keywords:
- ac adapter
- power adapter
- power supply
- 100w
- 24v
- 5a
- dc jack
- power brick
- rating
- input
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr1000ent-2023
  - cu1000ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-ac-adapter-rating
see_also:
- cu1000ent-2023-specs-circuit-diagram
- cu1000ent-2023-specs-driver-board-cs56012-connections
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: "Section 7.4 Circuit Diagram, PDF p. 13 (printed 13), the adapter block and the
    controller input label, read from a 300 dpi render (OCR supplement lines 923-929);
    text.md lines 259-264 carry only the heading. CR1000(2023) SR8880-SB028 service manual
    (spirit-rower-cr1000ent-2023-service-manual): section 7.4, PDF p. 13 (printed 13), lines
    269-274, the same adapter block '100W Power Adapter, OUTPUT DC 24V / 5A' and controller
    'INPUT DC 24V / 5A' read from a 200 dpi render (OCR supplement 1172-1204)"
  extracted_at: '2026-09-11'
---

The bike runs from an external adapter, not from the mains directly.

| | |
|---|---|
| Power | **100 W** |
| Output | **DC 24 V / 5 A** |
| Lands on | a **DC jack** on the frame, then the controller's **DC 24V - PWR IN** socket |

**No part number, no input voltage range and no plug type are printed** for it - the drawing's
title says 230V, the section-3 text prints no figure, and the adapter box carries only the
wattage and output.

**Same voltage as the CU900ENT, different current.** The CU900ENT and CR900ENT books print an
**FSP100-RTAAN2, DC 24 V / 4.17 A** with an AC 100-240 V input (`cu900ent-ac-adapter-rating`).
Quote the adapter from the book for the machine in front of you.

**The CR1000ENT-2023 recumbent prints the same figures** - a 100W Power Adapter with OUTPUT DC
24V / 5A into a DC jack, INPUT DC 24V / 5A at the controller, and again no part number, input
range or plug type - so this card covers that machine too. Its outline drawing adds an *AC switch
cover* (item 27) between the front shrouds, the only hint on either machine of where the mains
lead enters.


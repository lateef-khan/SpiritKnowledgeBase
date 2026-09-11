---
id: ce1000ent-2023-specs-power-adapter-100-w-24-v-5-a
title: A 100 W desktop adapter delivering DC 24 V at 5 A into a DC jack, on the elliptical
kind: spec
question: What power supply does a Spirit ce1000ent-2023 elliptical use?
asked_as:
- what adapter does the ce1000 ent use
- power supply rating for the ce1000ent elliptical
- is the ce1000 24 volt
- replacement power brick for the ce1000
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
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce1000ent-2023
  applies_to:
  - ce1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210054'
authority: 3
not_to_be_confused_with:
- ce900ent-specs-ac-adapter-fsp100-rtaan2-24-v-4-17-a
see_also:
- ce1000ent-2023-specs-circuit-diagram-se8880-sb028-230v
- ce1000ent-2023-specs-driver-board-cs56012-connections
- cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a
source:
  ref: spirit-elliptical-ce1000ent-2023-service-manual
  locator: Section 7.4 Circuit Diagram, PDF p. 13 (printed 13), the adapter block
    and the controller input label, read from a 300 dpi render (OCR supplement lines
    924-974); text.md lines 290-296 carry only the heading
  extracted_at: '2026-09-11'
---

The elliptical runs from an external adapter, not from the mains directly.

| | |
|---|---|
| Power | **100 W** |
| Output | **DC 24 V / 5 A** |
| Lands on | a **DC jack** on the frame, then the controller's **DC 24V - PWR IN** socket |

**No part number, no input voltage range and no plug type are printed** for it - the drawing's
title says 230V, the section-3 text prints no figure, and the adapter box carries only the wattage
and output.

**Same voltage as the CE900ENT, different current.** The CE900ENT book prints an **FSP100-RTAAN2,
DC 24 V / 4.17 A** with an AC 100-240 V input (`ce900ent-specs-ac-adapter-fsp100-rtaan2-24-v-4-17-a`).
The CU1000ENT bike shares this 100 W unit (`cu1000ent-2023-specs-power-adapter-100-w-24-v-5-a`).
Quote the adapter from the book for the machine in front of you.


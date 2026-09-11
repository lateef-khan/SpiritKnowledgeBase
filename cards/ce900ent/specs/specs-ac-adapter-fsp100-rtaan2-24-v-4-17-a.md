---
id: ce900ent-specs-ac-adapter-fsp100-rtaan2-24-v-4-17-a
title: AC adapter FSP100-RTAAN2, 100 to 240 V in and DC 24 V at 4.17 A out, on the
  ENT elliptical
kind: spec
question: What power supply does a Spirit ce900ent elliptical use?
asked_as:
- what adapter does the ce900 ent use
- power supply rating for the ce900ent elliptical
- is the ce900ent 24 volt
- fsp100 adapter elliptical
keywords:
- ac adapter
- power adapter
- power supply
- fsp100-rtaan2
- 24v
- 4.17a
- dc jack
- 100-240v
- power brick
- rating
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: specs
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with:
- ce1000ent-2023-specs-power-adapter-100-w-24-v-5-a
see_also:
- ce900ent-specs-circuit-diagram-8-pin-computer-cable-and-combo-board
- ce900ent-specs-driver-board-dya-w10a-connectors
- cu900ent-ac-adapter-rating
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Circuit diagram, PDF p. 24 (printed 24), the AC ADAPTER block, read from
    a 300 dpi render (OCR supplement lines 1564-1615); text.md lines 341-345 carry
    only the page heading
  extracted_at: '2026-09-11'
---

The elliptical runs from an external desktop adapter, not from the mains directly.

| | |
|---|---|
| Part number | **FSP100-RTAAN2** |
| Input | **AC 100-240 V** |
| Output | **DC 24 V / 4.17 A** |

The output goes into a **DC jack** on the frame, and from there to **CN2** on the driver board. The
block diagram on p. 16 shows the same thing as a single "DC POWER" block into the driver board.

**The page is mis-headed.** The drawing sits on p. 24 under the running title *Setting and
Operation for Engineering Mode*; the circuit diagram has no heading of its own in this book.

The CU900ENT and CR900ENT bikes print the same adapter block (`cu900ent-ac-adapter-rating`). The
CE1000ENT is fed by a different, 100 W 24 V / 5 A unit
(`ce1000ent-2023-specs-power-adapter-100-w-24-v-5-a`).


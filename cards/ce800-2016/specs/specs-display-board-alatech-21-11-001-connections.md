---
id: ce800-2016-specs-display-board-alatech-21-11-001-connections
title: 'Two call-outs on the Alatech 21-11-001 display board: cooling fan and key
  board'
kind: spec
question: What plugs into the display board inside the console of a Spirit ce800-2016
  elliptical, and what is the board marked?
asked_as:
- what plugs into the 2016 ce800 console board
- alatech display board ce800
- xe890b display board connections
- which board is in the ce800 2016 console
keywords:
- display board
- console pcb
- alatech
- 21-11-001
- cooling fan
- key board
- led display
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800-2016
  applies_to:
  - ce800-2016
  section: specs
  code: '*'
  model_number:
  - '800045'
authority: 3
not_to_be_confused_with:
- ce800-2021-specs-display-board-cs24005-connections
see_also:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- ce800-2016-specs-circuit-diagram-xe890b-ae10m
source:
  ref: spirit-elliptical-ce800-2016-service-manual
  locator: Section 5 Basic Connections and Wiring, Display Board PCB Component Locations
    (top and bottom) and Display Board wire Connections, PDF pp. 21-23 (printed 21-23),
    text.md lines 391-417; the photographs were read from a 300 dpi render (OCR supplement
    lines 1081-1163)
  extracted_at: '2026-09-11'
---

Three photographs of one board, and only two call-outs on it: **COOLING FAN** (a small white header
at the top edge) and **KEY BOARD** (the wide header at the bottom edge).

The board is an **ALATECH 21-11-001 VER 1.0** (date code 110826A02 on the sample), with a
"21-11-001 V1.0" label on its main IC. It is not a CoreStar CS-series board: the 2020-version CE800
moved to a CS24005 with eight call-outs, separate BLE, CSAFE and charger daughter boards and a USB
charger (`ce800-2021-specs-display-board-cs24005-connections`).

**No pin numbers are printed** for either connector, and the computer cable, hand-pulse and
wireless-receiver headers visible on the photograph carry no call-out. The mast cable's other end
is on the generator controller, `spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections`.


---
id: csc900-2019-specs-controller-ev60-k2412-dc-dc-converter-and-ai3-console-board
title: The controller carries a potted DC-DC converter, 15 to 40 V in and 12 V 5 A
  out, and a 20 A relay, and the console board is photographed with no callouts
kind: fact
question: What is inside the controller of a Spirit csc900-2019 stair climber, and
  what console board does it use?
asked_as:
- csc900 controller board photo
- ev60-k2412 converter on the stair climber
- what relay is in the csc900 controller
- ai3 console board csc900
keywords:
- controller
- internal circuit
- ev60-k2412
- dc-dc converter
- 12v 5a
- relay
- bt90-s
- ai3 console
- console board
- eveps
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: specs
  code: '*'
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc880-2025-specs-controller-seven-cables-named
see_also:
- csc900-2019-specs-power-flow-diagrams-alternator-brake-and-power-resistor
- csc900-2019-specs-parts-proximity-switch-tl-n20me1
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: AI3 console internal circuit, PDF p. 20 (printed 20), text.md lines 645-650
    (OCR supplement 877-886); Controller internal circuit, PDF p. 21 (printed 21),
    lines 651-660 (supplement 889-898); both photographs read from 150 dpi renders;
    the controller replacement note, PDF p. 15, lines 537-566
  extracted_at: '2026-09-11'
---

The last two pages of the book are photographs with one caption each and no callouts.

**Controller internal circuit.** A green board whose largest part is a potted module marked
**EV60-K2412 EVEPS DC-DC CONVERTER, IN: 15V~40V, OUT: 12V 5A** - the alternator's variable
output is stepped down to 12 V for the console and logic. Beside it a black relay marked **AFE
BT90-S**, **NO: 20A 250VAC, NC: 10A 250VAC**, **12VDC** coil - the switch that puts the power
resistor across the alternator. Silkscreened sockets read **+24V** (top left), **JK1**, **JK2**,
two headers on the left edge, a **FIELD** terminal with a blue wire and three thick leads (blue,
red, brown) at the right, and terminals **E2** and **E3**.

**AI3 console internal circuit.** The console's own board: a large green board with an RJ45
socket, a **USB** header, an **RS232 (232)** header, a blue **JK2** socket, a row of headers along
the right edge and several LED driver ICs - "AI3" is the only name the book gives it.

**Two things the replacement chapter says about the controller:**

- "The internal circuit board of the controller has a programming program. When replacing, you
  need to replace the controller with the same batch."
- Reinstall with the original line sequence and fix the leads with cable ties; the pedal must be
  turned with the machine powered to reach the brake and generator from the front.

**No part number is printed for either board**, and the +24V label on the controller is the only
voltage the book states for the adapter. The 2022 magnetic-system controller is a different board
whose seven leads are named (`csc880-2025-specs-controller-seven-cables-named`).


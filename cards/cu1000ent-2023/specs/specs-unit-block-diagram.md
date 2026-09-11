---
id: cu1000ent-2023-specs-unit-block-diagram
title: Unit block diagram with a connecting board for HDMI, C-safe, TV and internet,
  and a key connecting board for the handlebar HR
kind: spec
question: What does the unit block diagram of a Spirit cu1000ent-2023 upright bike
  show?
asked_as:
- block diagram of the cu1000 ent
- how are the boards connected on the cu1000ent
- what is the connecting board on the cu1000
- cu1000ent signal flow
keywords:
- block diagram
- display console
- connecting board
- key connecting board
- driver board
- dc power
- brake flywheel
- rpm sensor
- hr handlebar
- system cable
facets:
  brand:
  - spirit
  product_line: bike
  model: cu1000ent-2023
  applies_to:
  - cu1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210354'
authority: 3
not_to_be_confused_with:
- cu900ent-unit-block-diagram
see_also:
- cu1000ent-2023-specs-io-board-bottom-connections
- cu1000ent-2023-specs-circuit-diagram
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: Section 5 Unit Block Diagrams, PDF p. 9 (printed 9), text.md lines 165-170;
    the diagram is a flattened image read from a 300 dpi render (OCR supplement lines
    848-865)
  extracted_at: '2026-09-11'
---

Everything points up into the **DISPLAY CONSOLE**.

**From the driver board**, two paths: **SYSTEM CABLE CONNECT** and **Console Power CONNECT**.
**Into the driver board**: DC POWER, Brake Flywheel, RPM SENSOR.

**Through a CONNECTING BOARD**: HDMI CONNECT, C-safe CONNECT, TV CONNECT, Internet CONNECT.

**Through a KEY CONNECTING BOARD**: the HR Handlebar.

So the console has two board-level feeds below it - the connecting board for the audio-visual and
network cables, and the key connecting board for the keypad and hand pulse - and one direct
system cable from the driver board. The circuit diagram names the connecting board the
*Communication transfer board* and draws the key connecting board as the keypad with its
4-pin and 3-pin XHP hand-pulse plugs.

Unlike the CU900ENT diagram (`cu900ent-unit-block-diagram`), this one is titled correctly and
has no cooling-fan block.


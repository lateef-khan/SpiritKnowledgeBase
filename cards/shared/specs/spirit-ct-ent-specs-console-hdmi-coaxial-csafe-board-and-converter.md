---
id: spirit-ct-ent-specs-console-hdmi-coaxial-csafe-board-and-converter
title: 'The console cable set: HDMI, coaxial and 5-pin C-SAFE on one board, a 13 volt
  4 amp converter, and the mast groove'
kind: spec
question: What cables run up the mast to the console of a Spirit CT800ENT or CT850ENT
  treadmill, and what is the converter board?
asked_as:
- what cables go up to the ent console
- hdmi coaxial c-safe board in the ct850 ent
- what voltage is the console converter on the ct800 ent
- where do the console wires go in the mast
keywords:
- hdmi
- coaxial cable
- c-safe
- converter
- dc 13v
- 4a
- console mast
- cable groove
- pcb
- connector
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct800ent-2022-specs-console-transfer-and-power-bridge-boards
- ct850ent-2022-specs-console-transfer-and-power-bridge-boards
- ct800ent-2022-specs-circuit-diagram
- ct850ent-2022-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: 'CT800ENT-2022: PDF p. 22 (printed 22) ''The console HDMI/Coaxial cable/C-SAFE
    PCB board'', text.md lines 413-424, OCR supplement lines 1327-1342 for the board
    marking; PDF p. 23 ''The console Converter PCB board'', lines 425-440; PDF p.
    24 ''The console mast Cable place'', lines 441-448. CT850ENT-2022: the same three
    pages at PDF pp. 22-24, lines 402-437'
  extracted_at: '2026-09-11'
---

Both ENT books print the same three pages.

**The console HDMI / coaxial cable / C-SAFE PCB board (p. 22)** carries three connectors: **Coaxial
Cable**, **HDMI Cable** and **C-SAFE (5 PINS)**. The board silkscreen reads **AC0044-K1-V1.0-200116**.

**The console converter PCB board (p. 23)** has three labelled ends: **DC_13V/4A (Converter End)**, **AC_N
(Converter End)** and **AC_L (Converter End)**. That is the only rating printed for the console supply:
**13 V DC at 4 A**, fed from mains through the power bridge board.

**The console mast (p. 24)**: "Putting the wire (HDMI/Coaxial cable/C-SAFE) in the groove during
installation" - the three signal cables run in a groove in the mast, separately from the main control
wires.

The circuit diagrams count the other cables: a **10-PIN upper main control** cable, **RJ45 internet**, and
a **6+2+2 pin lower main control** cable to the communication transfer board.

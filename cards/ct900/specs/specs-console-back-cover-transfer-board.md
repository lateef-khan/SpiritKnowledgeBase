---
id: ct900-specs-console-back-cover-transfer-board
title: Console back-cover transfer board, both faces, with the main connector, keypad,
  safety and hand-grip plugs
kind: spec
question: What are the connectors on the console back-cover transfer board of a Spirit
  ct900 treadmill?
asked_as:
- what plugs into the transfer board behind the ct900 console
- cs26002 board connectors
- where is the safety plug on the ct900 transfer board
- which plug is the keypad on the ct900
keywords:
- transfer board
- connector
- console back cover
- main connector
- keypad
- safety
- hand grip
- hr board
- earth gnd
- rpm
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: specs
  code: '*'
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct850-2020-console-back-cover-transfer-board
- 40t-2026-specs-display-board-and-transfer-board-connectors
see_also:
- ct900-specs-transfer-board-pin-definitions
- ct900-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct900-service-manual
  locator: PDF p. 22 (printed 22) 'The console back cover transfer PCB board', front
    of the board, text.md lines 290-298, OCR supplement lines 1861-1875; PDF p. 23
    (printed 23), behind the board, lines 299-305, OCR supplement lines 1880-1908;
    read from the render
  extracted_at: '2026-09-11'
---

The board is silkscreened **CS26002-1 V1.0** (sticker W-CS26002-1-00, C1051107003) and is mounted in the
console back cover. Both faces were read from the 300 dpi renders; the extracted text carries only the
page titles.

**Front of the board**: **J9 MAIN CONNECTOR** (12-way), **J10** and **J11** under the heading **HEART RATE
HAND GRIP**, **J16 HR BOARD**, **J17 EARTH GND**, **J14 SAFETY**, **J15 KEYPAD**, and two unlabelled
3-way plugs **J13** and **J12**.

**Behind the board** (the face silkscreened "INSIDE"): **J1 MAIN CONNECTOR** (12-way, with a rainbow
ribbon cable in the photo), **J2 RPM (GEN. Only)**, **J8** and **J7** under **HEART RATE HAND GRIP**, **J6
HR BOARD**, **J18 EARTH GND**, **J5 KEYPAD**, **J4 SAFETY**, and a 6-way **J3** with no name.

The pin definitions are printed as pairs - J1·J9, J5·J15, J4·J14, J6·J16 - one number for each face; they
are on the pin-definition card.

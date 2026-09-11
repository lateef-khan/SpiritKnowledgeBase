---
id: ct800-2016-specs-display-board-connectors-and-pinouts
title: Display board connectors and the pin definitions of the fan, safety, hand-pulse
  and keyboard plugs
kind: spec
question: Which connector on the display board of a Spirit ct800-2016 treadmill takes
  which cable, and what are the pin definitions?
asked_as:
- what plugs into jk13 on the ct800 display board
- where is the safety plug on the 2016 ct800 console board
- key board connector pinout
- cooling fan connector pins
keywords:
- display board
- pcb
- connector
- socket
- pin definition
- cooling fan
- safety
- keyboard
- hand pulse
- writer
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: specs
  code: '*'
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- ct850-2016-display-board-connector-locations
- ct850-2016-display-board-small-connector-pinouts
see_also:
- ct800-2016-specs-console-12-pin-cable-pinout
- ct800-2016-specs-driver-board-connectors-and-leds
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: PDF p. 24 (printed 23) '6.2 PCB Board Bottom', text.md lines 383-414, OCR
    supplement lines 1744-1780; the same photo with pin numbering on PDF p. 43 (printed
    42), lines 729-757; pin definitions PDF p. 44 (printed 43), lines 758-796. Board
    marking read from the render
  extracted_at: '2026-09-11'
---

The display board sits behind the console; its bottom face carries every cable connector. The board is
labelled **YJ-66240** on its DYACO sticker (the silkscreen beside it reads YJ-6620 with a suffix the photo
does not resolve). Section 6.1's "PCB Board Top" page (p. 23) is a bare photograph of the display side.

| Connector | Cable | Pin numbering as drawn on p. 43 |
|---|---|---|
| JK9 | COOLING FAN | P4-P1 |
| JK16 | WRITER (programming header) | not numbered |
| JK13 | SYSTEM CABLE (12 PINS) | P1-P12 |
| JK14 | SAFETY | P1-P2 |
| JK11 | CONTACT HR HANDLEBAR / WIRELESS HR | P1-P4 |
| JK3 | KEY BOARD | P1-P12 |

**Pin definitions (p. 44).** JK13 is the 12-pin console cable and has its own card.

- **JK14 - safety (2 pins)**: P1 Safety switch signal input, P2 VDD.
- **JK9 - cooling fan (4 pins)**: P1 FAN OUT, P2 FAN OUT, P3 GND, P4 GND.
- **JK11 - hand pulse / wireless HR (4 pins)**: P1 GND, P2 VCC, P3 HEART, P4 printed blank.
- **JK3 - key board (12 pins)**: P1 KEY_D0, P2 KEY_D1, P3 KEY_D2, P4 KEY_D3, P5 KEY_D4, P6 KEY_D5,
  P7 KEY_D6, P8 KEY_D7, P9 SCAN_0, P10 SCAN_1, P11 SCAN_2, P12 SCAN_3.

The JK11 table leaves P4 with no description. The CT850-2016 display board is a different board
(ST8100-U23-B) with a different connector set - JK10 / JK9 / JK5 / JK6 / JK21 - so do not read one
board's JK number against the other.

---
id: 85ue-2025-specs-power-supply-module-mean-well-rps-120s-24-v
title: An internal Mean Well RPS-120S module, numbered 075, 100 to 240 VAC in and
  24 V out, behind an inlet with switch and fuse
kind: spec
question: What power supply is inside a Spirit 8.5UE upper body ergometer (85ue-2025)
  according to its service manual?
asked_as:
- what power supply is in the 8.5ue
- is the upper body ergometer 24 volt inside
- mean well rps-120s ube
- 8.5ue cn100 24 vdc
keywords:
- power supply module
- mean well
- rps-120s
- 24 vdc
- cn100
- cn1
- open frame
- ac power entry module
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
see_also:
- spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v
- 85ue-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- 85ue-2025-specs-electrical-wiring-diagram-renumbered-parts
- 85ue-2025-specs-fuse-rating
- 85ue-2025-specs-specification-page
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 4.4.2 Power Supply Module (#075), PDF p. 18 (printed 18), text.md lines
    231-232 (sentence native; the photograph read from a 110 dpi render); 5.1 No power
    steps 2 and 4, PDF pp. 21-22, lines 260-273 (OCR supplement lines 759-767 reads
    the "110 VAC or 220 VAC" caption); the wiring diagram PDF p. 16
  extracted_at: '2026-09-11'
---

**"AC power is converted to 24VDC to provide DC voltage for the entire system."** The photograph is
the one the 8.0U, 8.5R and 8.5S books print: a **Mean Well RPS-120S** open-frame board with a
TF-5559 transformer, **CN1** for the AC in and **CN100** for the 24 V out, labelled 100-120VAC 2.3A /
200-240VAC 1.1A in and 24V 4.16A / 5.0A out. The full label reading is on the bike card
(`spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v`); this card exists because the
ergometer is its own product line and numbers the part **#075**.

Mains reaches it through the **AC Power Entry Module with Switch and Fuse** (#070 on this book's
sheet). The no-power procedure meters AC at CN1 - the figure caption reads "Measured 110 VAC or 220
VAC depending on the mains voltage" - checks the switch and the fuse, then meters **pins 1 and 4 of
CN100 for 24 VDC**; no 24 V is a new module, 24 V present is a new LCB.

The owner's manual's own figures for this machine - the mains draw, the 5 A fuse - are on
`85ue-2025-specs-specification-page` and `85ue-2025-specs-fuse-rating`.


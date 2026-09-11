---
id: spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v
title: An internal Mean Well RPS-120S module making the 24 V for the touchscreen bikes,
  100 to 240 VAC in, behind an inlet with switch and fuse
kind: spec
question: What power supply is inside a Spirit Medical 8.0U or 8.5R bike according
  to its service manual?
asked_as:
- what power supply is in the 8.0u
- is the 8.5r 24 volt inside
- mean well rps-120s bike
- 8.0u cn100 24 vdc
keywords:
- power supply module
- mean well
- rps-120s
- 24 vdc
- 4.16a
- 5.0a
- cn100
- cn1
- open frame
- ac power entry module
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-70-bike-specs-mains-power-through-an-ac-input-module-and-switching-power-supply
- 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
see_also:
- spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds
- spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
- spirit-med-8-bike-specs-mains-100-to-240-v-1-76-to-0-71-a
- spirit-med-bike-specs-fuse-rating-5-a-250-v-fast-acting-glass
- 85ue-2025-specs-power-supply-module-mean-well-rps-120s-24-v
- 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: '8.0U: 4.4.2 Power Supply Module (#081), PDF p. 19 (printed 19/51), text.md
    lines 334-338 (the sentence is native; the module label read from a 130 dpi render
    of the photograph); 5.1 No power steps 2 and 4, PDF pp. 21-22, lines 370-390;
    the wiring diagram PDF p. 17. 8.5R: 4.4.2, PDF p. 18, lines 255-256; 5.1, PDF
    p. 20, lines 285-297; the same photograph'
  extracted_at: '2026-09-11'
---

**"AC power is converted to 24VDC to provide DC voltage for the entire system."** That is the whole
printed text; the rest is on the photograph's label, which reads:

| | |
|---|---|
| Maker and model | **Mean Well RPS-120S-** (the suffix runs off the edge of the photo; the output is 24 V) |
| Input | **100-120VAC 2.3A / 200-240VAC 1.1A** |
| Output | **24V 4.16A (for 100-120 V input)** / **24V 5.0A (for 200-240 V input)** |
| Connectors | **CN1** - AC in from the entry module (cable #080); **CN100** - 24 V out to the LCB (cable #083) |

An open-frame board with a Mean Well **TF-5559** transformer, mounted inside the base - **no external
brick**. Mains reaches it through the **AC Power Entry Module with Switch and Fuse** (#076), so the
no-power procedure meters AC at CN1 first ("110 VAC or 220 VAC depending on the mains voltage"),
checks the switch and the fuse, then meters **pins 1 and 4 of CN100 for 24 VDC**.

**Three current figures for one machine, all correct for what they describe.** The owner's manuals
print *100 ~ 240 Vac, 1.76 ~ 0.71 Amps* on their specification pages
(`spirit-med-8-bike-specs-mains-100-to-240-v-1-76-to-0-71-a`) - the machine's draw; the module label
gives the module's rating; and the owner's manual's 5 A glass fuse
(`spirit-med-bike-specs-fuse-rating-5-a-250-v-fast-acting-glass`) is the one in the entry module the
service manual tells you to check without printing a rating.

The same module is photographed in the 8.5UE and 8.5S books
(`85ue-2025-specs-power-supply-module-mean-well-rps-120s-24-v`,
`85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v`). The 7.0R and 7.0U use a different
switching supply whose output the book gives as 24 V in one place and 36 V in another
(`spirit-med-70-bike-specs-mains-power-through-an-ac-input-module-and-switching-power-supply`).


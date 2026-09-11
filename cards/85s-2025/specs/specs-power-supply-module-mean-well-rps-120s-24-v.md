---
id: 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
title: An internal Mean Well RPS-120S open-frame module, 100 to 240 VAC in, 24 V out
  at 4.16 A or 5.0 A, behind an inlet with switch and fuse
kind: spec
question: What power supply is inside the Spirit 85s-2025 recumbent stepper according
  to its service manual?
asked_as:
- what power supply is in the 8.5s
- is the 8.5s 24 volt inside
- mean well rps-120s stepper
- 8.5s cn100 24 vdc
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
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: specs
  code: '*'
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- spirit-climber-85s-specs-mains-power-supply
- spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply
- 7-5s-med-specs-service-manual-switching-power-supply-12-vdc-1-6-a
see_also:
- 85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
- spirit-climber-specs-fuse-rating
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 4.4.2 Power Supply Module (097), PDF p. 14 (printed 14), text.md lines
    194-195 (the sentence is native; the module's label read from a 400 dpi render
    of the photograph); 5-1 No power steps 2 and 4, PDF pp. 16-17, lines 216-244;
    the wiring diagram, PDF p. 12
  extracted_at: '2026-09-11'
---

**"AC power is converted to 24VDC to provide DC voltage for the entire system."** That is the whole
printed text; the rest is on the photograph's label, which reads:

| | |
|---|---|
| Maker and model | **Mean Well RPS-120S-** (the suffix is hidden under the edge of the photo; the output is 24 V) |
| Input | **100-120VAC 2.3A / 200-240VAC 1.1A** |
| Output | **24V 4.16A (for 100-120 V input)** / **24V 5.0A (for 200-240 V input)** |
| Connectors | **CN1** - AC in from the entry module (cable #096); **CN100** - 24 V out to the LCB (cable #099) |

It is an open-frame board with a Mean Well TF-5559 transformer, mounted inside the base - the
8.5S has **no external brick**. Mains reaches it through the **AC Power Entry Module with Switch
and Fuse** (#092), so the no-power procedure meters AC at CN1 first ("110 VAC or 220 VAC depending
on the mains voltage"), checks the switch and the fuse, then meters **pins 1 and 4 of CN100 for
24 VDC**.

**Three books, three current figures for this family.** The 8.5S owner's manual prints
*100 ~ 240 Vac, 1.76 ~ 0.71 Amps* on its specification page
(`spirit-climber-85s-specs-mains-power-supply`) - the machine's draw, not the module's rating,
and neither figure is wrong for what it describes. The 7.5S runs from a 12 V external adapter
instead (`spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply`,
`7-5s-med-specs-service-manual-switching-power-supply-12-vdc-1-6-a`). The fuse in the entry
module is the 250 V 5 A glass fuse of `spirit-climber-specs-fuse-rating`; the service manual prints
no rating of its own.


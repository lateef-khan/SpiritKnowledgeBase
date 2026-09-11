---
id: csc900-2019-specs-parts-proximity-switch-tl-n20me1
title: The proximity switch is a CHIIB TL-N20ME1, an NPN normally-open 20 mm inductive
  sensor on 6 to 36 V DC
kind: spec
question: What proximity switch does the alternator-drive Spirit csc900-2019 stair
  climber use, and how is it wired?
asked_as:
- what proximity switch is in the csc900
- part number for the stair climber proximity sensor
- proximity switch wire colours csc900
- is the csc900 proximity switch npn or pnp
keywords:
- proximity switch
- proximity sensor
- inductive sensor
- tl-n20me1
- chiib
- npn
- normally open
- wire colour
- stair climber
- part number
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
not_to_be_confused_with: []
see_also:
- spirit-climber-specs-parts-service-manual-tool-list-six-tools
- spirit-climber-safety-generator-is-live-while-the-stairs-turn
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: The photograph at the head of PDF p. 17 (printed 17), text.md lines 592-611,
    which closes the "Proximity switch Replacement" steps that begin on PDF p. 16
    (lines 567-592); the label was read from a 400 dpi render of the photograph, as
    the text layer holds only the OCR fragment "TL-N20ME | PROXIMITY SWITCH" (line
    846 onward)
  extracted_at: '2026-09-11'
---

**The CSC900 V1.0 (alternator drive) service manual never names the proximity switch in its
text; it photographs it.** The picture that closes the Proximity switch Replacement steps
shows a yellow rectangular sensor whose label reads:

| On the label | Meaning |
|---|---|
| CHIIB 国际工牌 | the maker's brand - 沪工集团有限公司, Hugong Group Co., Ltd., printed at the foot of the label |
| TL-N20ME1 | the model |
| PROXIMITY SWITCH | |
| NPN | NPN output |
| 常开 NO | normally open |
| 20mm | 20 mm sensing distance |
| 棕 BN + / 黑 BK 300mA (load) / 蓝 BU - | three leads: brown to +, black is the 300 mA switched output, blue to - |
| 6 to 36V DC | supply |

The sensor's lead ends in a small three-way connector, and the replacement steps
(PDF p. 16) are to disconnect that cable, cut the tie, remove the fixing screws with a short-handle
screwdriver and lift the switch out; no adjustment, gap or torque is printed.

**What it does is stated on the wiring pages, not here**: the Power Flow-2 drawing puts the
proximity switch on the controller beside the magnetic switch, and troubleshooting row 5 -
speed and distance stay at 0 - blames "the magnetic safety switch", a different part. The book
prints no fault for the proximity switch itself.

**This is the alternator-drive book only.** The CSC900 2022 (magnetic system) book and the
CSC880 book name a "proximity switch cable" among the controller's leads (the CSC880 numbers it
③) and print no sensor label; the light sensor on those machines is a different part. Do not
carry this model number to them.

**Two other components are photographed with labels in the same book and are not this card**:
the controller board on PDF p. 21 carries an `EV60-K2412 EVEPS DC-DC CONVERTER, IN 15V~40V,
OUT 12V 5A` module and an `AFE BT90-S` 12 VDC relay rated NO 20 A / NC 10 A at 250 VAC. They
belong with the controller's wiring card.


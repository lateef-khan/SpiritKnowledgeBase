---
id: tr150-2021-specs-mcb-terminal-map-from-the-annotated-photograph
title: 'Where each lead lands on the motor control board, from an annotated photograph:
  5-pin lower cable, speed sensor, motor red to M+ and black to M-, switch white to
  AC N and black to AC L'
kind: spec
question: Which lead goes to which terminal on the motor control board (MCB) of an
  Xterra tr150-2021 treadmill, according to the annotated photograph?
asked_as:
- tr150 mcb wiring
- where does the speed sensor plug in on the tr150 board
- tr150 motor control board terminals
- which switch wire goes to ac l
keywords:
- mcb
- motor control board
- lower controller
- terminal map
- 5 pin lower cable
- speed sensor
- m plus
- m minus
- ac n
- ac l
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: specs
  code: '*'
  model_number:
  - '450887'
authority: 2
not_to_be_confused_with: []
see_also:
- tr150-2021-specs-driver-board-b426d-wire-connections
- tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
source:
  ref: xterra-treadmill-tr150-2021-mcb-wiring-photo
  locator: 'The whole source: a 4032x3024 phone photograph dated 21 November 2019
    with hand-written labels, transcribed verbatim in sources/xterra-treadmill-tr150-2021-mcb-wiring-photo/text.md
    lines 1-31. Title label ''TR150/T500 MCB'''
  extracted_at: '2026-09-11'
---

**Authority 2: a technician's annotated photograph, not a manual.** It agrees with the TR150 service manual's
driver-board page, which is the authority-3 card.

The photograph is titled **TR150/T500 MCB** - "T500" names a second machine that shares this board; nothing else in
the picture identifies it. Six hand-written labels point at the board:

| Label on the photo (verbatim) | Terminal it points at | Board silkscreen |
|---|---|---|
| 5 pin lower cable | black 5-pin header, top left | - |
| If you have speed sensor, then it plugs here. | small white 2-pin connector on the left edge, below the 5-pin header | SPD |
| M+ Red lead from drive motor | spade terminal, left edge, mid-height | M+, with RED beside it |
| M- Black lead from drive motor | spade terminal, left edge, lower | M-, with BLACK beside it |
| White lead from On/off switch | spade terminal, right edge, upper | AC N (partly hidden) |
| Black lead from on/ off switch | spade terminal, right edge, lower | AC L |

The board in the picture is the one the service manual photographs: a green board on a finned aluminium plate with
an oval **110V** label by the AC terminals, a radial capacitor marked **1000µF 200V** with a "Shanghai Electronics Way
Co.,Ltd" sticker, a transformer marked **EE22-1.2mH**, a RoHS sticker, a row of four opto-isolators under the 5-pin
header and two red LEDs near the AC terminals - the same features as the **B426D** on the manual's page.

**What the photo does not establish**: the 5-pin cable's pin-out (see the 5-pin card), the switch's other
connections, and any voltage or resistance value. "If you have speed sensor" implies some units of this board have no
sensor fitted; the manual's E1 chapter says the sensor is needed only for calibration.

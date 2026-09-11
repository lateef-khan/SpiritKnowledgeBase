---
id: csc900-2019-errors-magnetic-safety-switch-magnet-and-buzzer-test
title: 'Testing the magnetic safety switch: the buzzer sounds and the reading drops
  near zero ohms when a magnet comes close'
kind: procedure
question: How do I test the magnetic safety switch on a Spirit csc900-2019 stair climber?
asked_as:
- how to test the climbmill magnetic switch
- csc900 reed switch test with a magnet
- stair climber speed sensor check with multimeter
keywords:
- magnetic safety switch
- reed switch
- magnet
- buzzer
- multimeter
- continuity
- climbmill
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: '*'
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with: []
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 7. Determination of defective accessories, Measurement of magnetic safety
    switch, PDF p. 11; text.md lines 415-425
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** > Use the multi-meter buzzer file, and the two test leads respectively contact the two terminals of the magnetic safety switch. Use a magnet to approach the magnetic safety switch. If the beep sounds when approaching, the resistance value is close to 0 ohms, then the magnetic safety switch is normal. If there is no change, the magnetic safety switch is defective.

**It is a reed switch, tested as one.** Meter on the buzzer setting across the switch's two terminals, bring a magnet up to it: a beep and a reading near 0 ohms as the magnet arrives is a pass; no change is a fail. "Buzzer file" is the book's phrasing for the continuity setting.

**Test it before you move it.** The symptom this switch causes - the steps run but speed and distance sit at zero - has *position* as its first cause and the part as its second (`csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch`). A switch that passes with a magnet held to it and fails in the machine is out of position, not broken.

The extraction of this page runs the words *Resistor measurement* into the middle of this paragraph; on the printed page they are the heading of the next test (`csc900-2019-errors-brake-resistor-reads-about-half-an-ohm`).

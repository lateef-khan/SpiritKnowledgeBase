---
id: srvo-display-board-speaker-port-pinout
title: Pinout of the SRVO display board speaker ports
kind: spec
question: What is the pinout of the speaker ports on the SOLE SRVO display board?
asked_as:
- srvo speaker connector pinout
- which srvo speaker port is left
- srvo speaker wiring polarity
keywords:
- speaker port
- pinout
- left channel
- right channel
- polarity
- positive
- negative
- audio
- display main board
facets:
  brand:
  - sole
  product_line: strength
  model: srvo
  applies_to:
  - srvo
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- srvo-controller-cn6-rs485-pinout
- srvo-controller-cn7-encoder-pinout
see_also:
- srvo-display-board-connector-map
- srvo-speaker-specification
- srvo-disassembly-speaker
source:
  ref: sole-srvo-service-manual
  locator: page 33, section 8-1-3
  extracted_at: '2026-09-04'
---

**These are the two speaker ports on the display main board: CN6 is the left channel and CN7 is the right. On a controller module the same two numbers are the RS485 interface and the encoder port.**

| Pin | Name | Description |
|---|---|---|
| CN6-1 | L+ | Left channel positive pole |
| CN6-2 | L- | Left channel negative electrode |
| CN7-1 | R+ | Right channel positive pole |
| CN7-2 | R- | Right channel negative electrode |

Two pins each, so a swapped pair reverses the polarity of that channel rather than damaging anything.

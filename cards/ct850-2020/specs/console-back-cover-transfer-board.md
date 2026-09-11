---
id: ct850-2020-console-back-cover-transfer-board
title: Console back-cover transfer board, both sides
kind: spec
question: What are the connectors on the console back-cover transfer board of a Spirit
  CT850-2020 or CT800-2020 treadmill?
asked_as:
- ab0054 k2 board connectors
- what is the transfer board behind the ct850 console
- which side of the transfer board is the keyboard on
- console back cover pcb ct850
keywords:
- transfer board
- ab0054-k2
- connector
- console back cover
- keyboard
- safety
- hand
- esp
- fan
- std
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct850-2020
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct800ent-2022-specs-console-transfer-and-power-bridge-boards
- ct850ent-2022-specs-console-transfer-and-power-bridge-boards
see_also:
- ct850-2020-display-board-connector-locations
- ct850-2020-console-keypad-board
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: p. 23 (printed 22) and p. 24 (printed 23) for the rear face; p. 25 (printed
    24) and p. 26 (printed 25) for the front face, section 6-1-3. The CT800-2020 service
    manual prints the same four pages, same board and JK labels, at PDF pp. 23-26 (printed
    22-25), text.md lines 319-359
  extracted_at: '2026-09-08'
---

The board is silkscreened **AB0054-K2** and is mounted in the console back cover. The manual
shows each face twice: a photo, then a labelled block drawing. Both block drawings are flattened
images and were read from the 300 dpi renders.

**Behind the board** - top edge: HAND (4 pins) to **JK18**, KEYBOARD (7 pins) to **JK2**,
RF (3 pins) to **JK21**, SAFETY (3 pins) to **JK13**, plus a **GND** pad.
Bottom edge: STD (6 pins) to **JK5 (YT057)**, FAN (2 pins) to **JK35**, **JK8 N/C**,
RM6Y3 (6 pins) to **JK9 (YT058)**, ESP (2 pins) to **JK16 (YT058)**.

**Front of the board** - top edge: SAFETY (3 pins) to **JK1**, KEYBOARD+RF (10 pins) to **JK4**,
HAND-LEFT (4 pins) to **JK17**, HAND-RIGHT (3 pins) to **JK3**, plus a **GND** pad.
Bottom edge: ESP (2 pins) to **JK15 (YT058)**, RM6Y3 (6 pins) to **JK11 (YT058)**,
**JK10 N/C**, FAN (2 pins) to **JK30**, STD (6 pins) to **JK6 (YT057)**.

The CT800-2020 book prints the same board and the same four pages; on that machine the STD
sockets (YT057) are the ones in use and the RM6Y3 / ESP sockets (YT058) are for the CT850. The
ENT books replace this board with a different transfer board that also carries HDMI, coaxial
and audio plugs.

The two faces reuse the same JK numbers for different cables. JK9 is RM6Y3 on the rear face but
there is no JK9 on the front face; JK10 is N/C on the front face but is the ESP connector on the
display board. Always say which board and which face you mean.

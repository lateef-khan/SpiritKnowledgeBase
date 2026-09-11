---
id: spirit-crw800-2016-xrw600-specs-display-board-aa0127-with-and-without-the-rf-module
title: The AA0127-V1.0 display board, stickered AA01270 with a radio module on the
  air rower and AA01273 with the radio header empty on the other
kind: fact
question: What display board is in the console of a Spirit CRW800 (2016) or XRW600
  rower, and how do the two boards differ?
asked_as:
- what board is in the xrw600 console
- aa0127 display board
- is the xrw600 console board the same as the crw800
- amp rf pulse jk13 writer sockets on the rower board
keywords:
- display board
- pcb
- aa0127
- aa01270
- aa01273
- rf module
- jk13
- amp
- rf pulse
- writer
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - xrw600-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crw800-2021-specs-display-board-aa0210-photographed
see_also:
- xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13
- spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor
source:
  ref: spirit-rower-crw800-2016-service-manual
  locator: 'CW800-YR001: Display Board PCB Component Locations, PCB Board Top and
    PCB Board Bottom, PDF pp. 25-26 (printed 24-25), text.md lines 349-351 (photographs;
    OCR supplement 1234-1256). DW400-YR002 (XRW600): PDF pp. 25-26, lines 362-364
    (supplement 1180-1208). Both read from 110 dpi renders'
  extracted_at: '2026-09-11'
---

Both books photograph the same printed circuit board, front and back, and neither draws a
wire-connection diagram or a pin table for it.

**Top (component side):** the LCD in its metal frame and five red tactile switches along the
bottom edge - the console's five keys. The silkscreen reads **AA0127-V1.0**, dated **2015.11.13**.

**Bottom:** the microcontroller, the buzzer (top left), a DC jack (top right), and four labelled
sockets along the bottom - **AMP** (two pins), **RF PULSE** (three pins), **JK13** (the long white
multi-way socket - the system cable, and the J13 the XRW600 block diagram names) and **WRITER**.

**The two machines' boards differ in one thing:**

| Book | Sticker | Bottom right corner |
|---|---|---|
| CRW800-2016 | **AA01270** (AA01270-20151218 V1.0, batch A512-151126005/200) | a **2.4 GHz radio module** with a printed antenna is fitted |
| XRW600-2019 | **AA01273** (AA01273-160728 V1.0, batch A512-160902014/500) | the module's header **JK2** is empty |

The radio is the receiver for the CRW800's handlebar resistance buttons; the XRW600 has none, so
its board is built without it. Do not swap the boards on that assumption - order by the sticker.

The 2020-version CRW800 moves to a different board, AA0210
(`crw800-2021-specs-display-board-aa0210-photographed`).


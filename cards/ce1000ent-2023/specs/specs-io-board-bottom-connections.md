---
id: ce1000ent-2023-specs-io-board-bottom-connections
title: 'Nine sockets under the console: USB, ground, console power, internet, 4-pin
  C-safe, HDMI, TV, 20-pin keyboard and 8-pin system cable, on the elliptical'
kind: spec
question: What plugs into the I/O board on the bottom of the console of a Spirit ce1000ent-2023
  elliptical?
asked_as:
- what cables go into the back of the ce1000 console
- ce1000ent i/o board connections
- how many pins is the keyboard cable on the ce1000
- c-safe connector ce1000ent
keywords:
- i/o board
- console
- usb connect
- ground
- console power
- internet
- c-safe 4 pins
- hdmi
- key board 20 pins
- system cable 8 pins
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce1000ent-2023
  applies_to:
  - ce1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210054'
authority: 3
not_to_be_confused_with:
- ce900ent-specs-io-board-connections
see_also:
- ce1000ent-2023-specs-driver-board-cs56012-connections
- ce1000ent-2023-specs-circuit-diagram-se8880-sb028-230v
- cu1000ent-2023-specs-io-board-bottom-connections
source:
  ref: spirit-elliptical-ce1000ent-2023-service-manual
  locator: Section 6.1 I/O Board Bottom, PDF p. 10 (printed 10), text.md lines 205-245;
    the photograph was checked on a 300 dpi render
  extracted_at: '2026-09-11'
---

Nine call-outs on the underside of the console panel (the panel label reads **OP-7145W**,
15.6" LCD/touch, colour black):

- **USB CONNECT**
- **GROUND**
- **Console Power CONNECT**
- **Internet CONNECT** (the RJ45)
- **C-safe CONNECT (4 PINS)**
- **HDMI CONNECT**
- **TV CONNECT** (the coaxial socket)
- **Key Board CONNECT (20 PINS)**
- **SYSTEM CABLE CONNECT (8 PINS)**

**Two differences from the CE900ENT I/O board** (`ce900ent-specs-io-board-connections`): the C-safe
socket is called out as **4 pins**, and the two hand-pulse wires of the CE900ENT are replaced by a
single **20-pin keyboard** connector - on this machine the hand-pulse leads plug into the keypad,
not the console. The 8-pin system cable is the same count on both.

The CU1000ENT bike prints the same nine call-outs on the same panel
(`cu1000ent-2023-specs-io-board-bottom-connections`).


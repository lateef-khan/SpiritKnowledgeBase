---
id: spirit-xe-2016-specs-display-board-cs11016-and-interface-board-connections
title: The CS11016 display board in five variants, from -46 to -24, with a W-CS11002-1
  interface board and, on the actuator machines, a CS63005 amplifier
kind: spec
question: What plugs into the display board, the swing-arm interface board and the
  amplifier on a Spirit XE195, XE295, XE395, XG400 or XE895 elliptical?
asked_as:
- xe295 display board connections
- cs11016 board
- where does the incline thumb switch plug in on the xe395
- xe895 amplifier board cs63005
keywords:
- display board
- cs11016
- interface board
- w-cs11002-1
- amplifier
- cs63005
- bluetooth
- level thumb switch
- system cable
- handgrip pulse sensor
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe895-2016
  - xg400-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce850-2016-specs-display-board-cs22002-and-interface-board-connections
- xe795-2016-specs-display-amplifier-and-interface-board-connections
- spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections
see_also:
- spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
- spirit-xe-2016-specs-unit-block-diagram-no-driver-board
- spirit-xe195-xe295-xg400-2016-specs-parts-electronic-parts-named
- spirit-xe395-xe895-specs-parts-electronic-parts-named
source:
  ref: spirit-elliptical-xe295-2016-service-manual
  locator: 'XE295-2016: Display Board wire Connections PDF p. 26 (printed 26), text.md
    lines 416-422; Interface Board PDF pp. 28-29, lines 430-442. XE195-2016: PDF p.
    26, lines 408-414 and pp. 28-29, lines 422-434. XG400-2016: PDF p. 24, lines 354-360
    and pp. 26-27, lines 368-380. XE395-2016: PDF p. 26, lines 465-471, p. 29, lines
    485-491, amplifier p. 30, lines 491-497. XE895-2016: PDF p. 26, lines 469-475,
    p. 29, lines 489-495, amplifier p. 30, lines 495-501. Photographs and drawings
    read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

One CoreStar console board, drawn with a different suffix in each book:

| Book | Drawn as | J1 | J2 SYSTEM CABLE | J6 |
|---|---|---|---|---|
| XE195 | **CS11016-46** | - | **10 PINS** | - |
| XE295 | **CS11016-0L** | BLUETOOTH | 14 PINS | - |
| XG400 | **CS11016-0L** | BLUETOOTH | 14 PINS | - |
| XE395 | **CS11016-13** | BLUETOOTH | 14 PINS | **INCLINE THUMB SWITCH** |
| XE895 | **CS11016-24** | BLUETOOTH | 14 PINS | **STRIDE THUMB SWITCH** |

Common to all five: **J4 KEY BOARD**, **J5 LEVEL THUMB SWITCH**, **J9 CONTACT HR HANDLEBAR**, **J10
WIRELESS HR**, **J12 COOLING FAN**.

**The photographs do not always match the drawings.** The XE295 and XG400 pages draw a CS11016-0L
but the board photographed in the same chapter carries the sticker **CS11016-46.V10.20160215**
(silkscreen CS11016 REV1.0) - the XE195 variant. Read the sticker on the board in the machine.

**Interface board - W-CS11002-1** in the swing arm, all five books: two **HANDGRIP PULSE SENSOR**
sockets (J1, J2), a **LEVEL** thumb-switch socket (J4) and a **SYSTEM WIRE** socket (J6 on the
XE195/XE295/XG400, **J13** on the XE395/XE895). The XE395 and XE895 add a second thumb-switch socket
for **INCLINE** or **STRIDE**, and **label it J4 as well** - two J4s on one drawing.

**Amplifier - CS63005**, XE395 and XE895 only: **J4** and **J5 SPEAKER (2 PINS)**, **J2 AUDEO IN**
(spelt so), **J1 POWER**.

**No pin numbers are printed** for any socket on these boards; the system cable is defined on its
own page - ten pins used on the machines without a driver board
(`spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used`), all fourteen on
the XE395 and XE895 (`spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins`).
The 2016 XB bikes use the same CS11016 family
(`spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections`).


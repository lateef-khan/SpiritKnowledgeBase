---
id: xterra-tr-specs-driver-board-td-65hs-seventeen-callouts
title: 'The seventeen numbered driver-board callouts: bridge rectifier, IGBT, fast
  recovery diode, M+ and M- to the brake board, two indicator lights, the 3-pin VR,
  2-pin speed, 3-pin brake and 7-pin console sockets, the three incline power terminals,
  an incline start light and two AC inputs'
kind: spec
question: What are the numbered parts, indicator lights and sockets on the driver
  board of an Xterra TR hiking treadmill?
asked_as:
- tr95h driver board sockets
- tr75h lower board numbered parts
- where does the brake board cable plug into the tr95h controller
- tr95h 7 pin socket
keywords:
- driver board
- lower controller
- sockets
- numbered callouts
- brake board
- indicator light
- incline power
- 7-pin
- speed sensor
- jkexer
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
see_also:
- xterra-tr-specs-brake-board-four-callouts
- xterra-tr-specs-display-board-jkm-337-eleven-sockets
- xterra-tr-specs-wiring-diagram-with-a-brake-module-and-a-7-pin-computer-cable
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: 'TR95H SM (JKEXER 337) ''8. Driver board PCB main parts & indicator lights
    & sockets'', PDF p. 13, lines 161-182. TR75H SM ''8.'', PDF p. 11 (printed 11),
    lines 220-246: the same photograph and table. Board sticker read from the 120
    dpi render'
  extracted_at: '2026-09-11'
---

Both JKEXER books print the same photograph of the lower board - a blue PCB on a black plate, stickered
**TD-65HS 110V** - with seventeen red numbers and this table:

| No. | Description |
|---|---|
| 1 | Bridge Rectifier |
| 2 | IGBT (Insulated Gate Bipoler) |
| 3 | Fast Recovery Diode (FRD) |
| 4 | M+ (connected to brake board PCB M+) |
| 5 | M- (connected to brake board PCB M-) |
| 6 | Current limit indicator light |
| 7 | Motor start indicator light |
| 8 | Incline motor VR signal cable socket (3 PIN) |
| 9 | Speed sensor cable socket (2 PIN) |
| 10 | Brake board signal and power cable socket (3 PIN) |
| 11 | Upper and lower controller connection cable (7 PIN) |
| 12 | Incline motor power cable (DOWN-connect to black wire) |
| 13 | Incline motor power cable (UP-connect to red wire) |
| 14 | Incline motor power cable (COM-connected to white wire) |
| 15 | Incline motor start indicator light |
| 16 | AC power input |
| 17 | AC power input |

Where they sit: 1, 2 and 3 are the three modules along the bottom edge on the plate; 4 and 5 the two spade
terminals at the lower right; 6 (red) and 7 (green) the pair of LEDs above them; 8 and 9 the white sockets on the
right edge; 10 the socket by the centre right; 11 the long white socket at the top; 12, 13 and 14 the three spade
terminals down the top left; 15 the green LED beside them; 16 and 17 the two AC spade terminals at the left, below a
capacitor marked 110V / 120V.

**The motor does not connect to this board directly**: M+ and M- go to the brake board, which in turn feeds the
motor. The 7-pin console cable has no pin definition anywhere in either book. What the three indicator lights mean
beyond their names is not printed; the books' error pages are the errors section's.

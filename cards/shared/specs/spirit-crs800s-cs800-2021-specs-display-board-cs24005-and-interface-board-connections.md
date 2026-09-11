---
id: spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections
title: Ten sockets on the CS24005 display board of the 2020-version steppers, a 14-pin
  system cable on the -23ED and a 10-pin on the -12ED, and a two-socket interface
  board
kind: spec
question: What plugs into the display board and the console interface board on a Spirit
  CRS800S or CS800 (2020 version) stepper?
asked_as:
- crs800s display board connections
- cs24005-23ed board
- where does the bluetooth plug in on the cs800 console
- w-cs24005 interface board j21 j20
keywords:
- display board
- cs24005
- cs24005-23ed
- cs24005-12ed
- system cable
- interface board
- w-cs24005-1-00
- w-cs24005-1-10
- bluetooth
- c-safe
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - cs800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections
- spirit-cr800-cu800-2021-specs-display-board-cs24005-connections
- ce800-2021-specs-display-board-cs24005-connections
see_also:
- crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
- cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
- spirit-crs800s-cs800-2021-specs-unit-block-diagram
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 'CRS800S: Display Board wire Connections, PDF p. 19 (printed 19), text.md
    lines 266-271 (flattened, read from a 110 dpi render; OCR supplement 765-785);
    PCB Board Top/Bottom photographs, PDF pp. 20-21, lines 272-283; The console Interface
    Board wire Connections, PDF p. 22, lines 284-289 (supplement 844-856). CS800(2020):
    6-1-1 DISPLAY BOARD WIRE CONNECTIONS, PDF p. 20 (printed 19), lines 315-322 (supplement
    1118-1186); 6-1-2/6-1-3 photographs, PDF pp. 21-22; 6-1-4 interface board, PDF
    p. 23, lines 335-340 (supplement 1220-1235)'
  extracted_at: '2026-09-11'
---

**One board family, two variants; the system-cable socket is the difference.**

| Socket | Lead | CRS800S (CS24005-23ED) | CS800 2020 (CS24005-12ED) |
|---|---|---|---|
| **J7** and **J6** | SYSTEM CABLE (14 PINS) | both sockets | - |
| **J6** | SYSTEM CABLE (10 PINS) | - | J6 only |
| **J5** | COOLING FAN | yes | yes |
| **J9** | USB CHARGE | yes | yes |
| **J13** and **J1** | C-SAFE & POWER | yes | yes |
| **J3** (beside J4) | CONTACT HR HANDLEBAR | yes | yes |
| **J8** | KEY BOARD | yes | yes |
| **J2** | BLUETOOTH | yes | yes |
| **J4** | WIRELESS HR | yes | yes |

The photographs show a red **CS24005 Rev 1.0** board (sticker *CS24005-23ED-V1.0* on the CRS800S,
*CS24005-12ED-V10* on the CS800) with a row of alphanumeric characters along the top, a dot
matrix, two three-digit windows and the key switches on the top side. **No pin numbers are printed on the
socket drawing**; the system cable's pins are defined on a separate page in each book, and they
differ - 11 pins on the CRS800S, 14 on the CS800
(`crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines`,
`cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used`).

**The CS800 book contradicts itself on the count**: its display-board page says *SYSTEM CABLE (10
PINS)*, its pin-definition page numbers 1 to 14 with four spares.

## The console interface board

| Book | Board | System wire | Handgrip pulse wire |
|---|---|---|---|
| CRS800S | **W-CS24005-1-00** | **J2** | **J6** |
| CS800 2020 | **W-CS24005-1-10** | **J21** | **J20** |

Two sockets each, nothing else. The 2016 CS800 uses a CS22002 display board with a CS11002-1
interface board instead
(`cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections`). The CS24005
also serves the 2021 CE800 elliptical and CR800/CU800 bikes with their own socket maps
(`ce800-2021-specs-display-board-cs24005-connections`,
`spirit-cr800-cu800-2021-specs-display-board-cs24005-connections`).


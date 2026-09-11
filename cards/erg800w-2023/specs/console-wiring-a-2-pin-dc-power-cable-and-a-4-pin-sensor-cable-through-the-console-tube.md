---
id: erg800w-2023-specs-console-wiring-a-2-pin-dc-power-cable-and-a-4-pin-sensor-cable-through-the-console-tube
title: 'Console wiring: a 2-pin DC power cable and a 4-pin signal sensor cable run
  up the console tube to a ribbon connector at the console, from an adapter with no
  rating printed'
kind: spec
question: How is the console wired on an Xterra erg800w-2023 water rower, and what
  connectors and wires does the service manual name?
asked_as:
- erg800w wiring diagram
- erg800w console cable connectors
- where does the power plug in on the erg800w
- erg800w sensor wire
keywords:
- wiring
- 2-pin
- 4-pin
- dc power cable
- sensor cable
- ribbon cable
- console tube
- adaptor
- dc line 620mm
- no wiring diagram
facets:
  brand:
  - xterra
  product_line: rower
  model: erg800w-2023
  applies_to:
  - erg800w-2023
  section: specs
  code: '*'
  model_number:
  - '180913'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-specs-external-power-adapter-with-no-rating-printed
- sb600-2023-specs-console-wiring-8-pin-ribbon-cable-2-pin-hand-grip-connectors-and-sensor-wires
- air650-2021-specs-console-wiring-four-aa-batteries-and-a-two-pin-reed-switch-rpm-sensor-with-no-bluetooth
- crw900-2021-specs-service-manual-prints-no-wiring-diagram-outline-or-block-diagram
- erg800w-2023-specs-main-parts-indication-thirteen-callouts-and-the-console-appearance-drawing
source:
  ref: xterra-rower-erg800w-2023-service-manual
  locator: '''Replacing the DC Power Wire'', PDF pp. 10-11 (numbered ''Page 10 of
    39'', ''Page 11 of 39''), text.md lines 228-277 (OCR supplement agrees); ''Replacing
    the Console'' step 4, PDF p. 9, lines 198-228; ''Replacing the Sensor Cable'',
    PDF p. 12, lines 277-302; parts list items A20 DC POWER SUPPLY COVER (p. 6, lines
    60-122), A50 MAGNET Φ6x5T (6), K ADAPTOR, N1 WIRE 400mm, N2 DC LINE 620mm, N3
    WIRE620mm, N4 WIRE300mm, N5 SENSOR WIRE 6x25x150mm (p. 8, lines 176-198). Owner''s
    manual (xterra-rower-erg800w-2023-owners-manual): ''How to Use the Adaptor'',
    PDF p. 26 (printed 25), lines 767-793; Bluetooth name ERG800, PDF p. 34 (printed
    33), lines 1095-1112'
  extracted_at: '2026-09-11'
---

**Two cables up the console tube, no wiring diagram printed.** The DC power wire procedure describes what is
inside: "Slightly press the Console Tube (H2) downward toward the handlebar. Two cable connectors will be visible
inside the tube: a **2-Pin Connector (DC Power Cable)** and a **4-Pin Connector (Signal Sensor Cable)**." At the
top, the console end is a **Ribbon Cable Connector** on the console (H) joined to the lower tube cable (H1); the
caution is not to let that cable drop into the steel tube when the console comes off.

| Item | What the book says |
|---|---|
| Adaptor (K) | "Plug the adaptor (K) like the below graphic" - no voltage, current or polarity is printed in either book (`xterra-specs-external-power-adapter-with-no-rating-printed`) |
| DC power plug (N2, "DC LINE 620mm") | held to the DC power cable cover (A20) by a hex nut; its 2-pin male plug meets a 2-pin female socket at the lower end of the console tube |
| Other wires | N1 WIRE 400 mm, N3 WIRE 620 mm, N4 WIRE 300 mm, N5 SENSOR WIRE 6 x 25 x 150 mm |
| Sensor | a magnet-and-sensor pickup at the flywheel pulley: six Ø6 x 5 mm magnets (A50); the new sensor is set 1.5 mm from the pulley and fixed with hot-melt glue (the maintenance section holds the adjustment) |
| Radio | the console's Bluetooth name is **ERG800**, printed on its back; FTMS is the protocol to choose in Kinomap |

The console is not battery powered - the owner's manual lists an "Adaptor" and an "Adapter" in the carton and
never names a cell. To change the power cable the old and new cables are tied end to end and the new one pulled
up through the tube from the top opening. There is no block diagram, circuit diagram or PCB drawing anywhere in
the 39 pages, unlike the Xterra treadmill and SB600 service manuals
(`sb600-2023-specs-console-wiring-8-pin-ribbon-cable-2-pin-hand-grip-connectors-and-sensor-wires`); the Spirit
CRW900 water rower's service manual has the same gap
(`crw900-2021-specs-service-manual-prints-no-wiring-diagram-outline-or-block-diagram`).


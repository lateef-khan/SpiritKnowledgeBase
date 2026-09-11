---
id: spirit-xbr-2007-specs-no-outline-or-wiring-chapters
title: 'The 2007 recumbent book has no outline, electrical configuration, block diagram
  or wiring chapter: three voltage-test procedures are its only electrical content'
kind: fact
question: Does the Spirit XBR25 or XBR55 2007 service manual print an outline drawing,
  a wiring diagram or connector definitions?
asked_as:
- xbr25 2007 wiring diagram
- does the old xbr55 manual have a circuit diagram
- xbr55 2007 pinout
- what does the 2007 xbr service manual cover
keywords:
- absence
- no outline
- no wiring diagram
- no block diagram
- no pin definition
- voltage test
- 24 volts
- 6 volts
- pin 2
- pin 3
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2007
  - xbr55-2007
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- xbr25-2007-specs-parts-list
- xbr55-2007-specs-parts-list
- spirit-xbr-2016-specs-outline-and-skeleton-part-names
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
source:
  ref: spirit-bike-xbr25-xbr55-2007-service-manual
  locator: Table of Contents, PDF p. 2 (printed 2), text.md lines 5-30, listing only
    a troubleshooting guide, five repair procedures, warranty pages and parts; every
    page from PDF p. 3 to p. 20 opened - Bike Troubleshooting pp. 3-6 (lines 31-110),
    warranty and forms pp. 7-11, exploded views and parts lists pp. 12-20; OCR supplements
    for pp. 1, 2, 10, 11, 12, 15, 16 (lines 750-1068) add nothing of the kind
  extracted_at: '2026-09-11'
---

**Neither an outline nor a wiring page exists in this book.** The contents list is a two-column
troubleshooting guide (Electronic System, Mechanical System), five repair procedures, the
warranty pages and forms, and an exploded view with a parts list for each model. Every page was
opened: the four troubleshooting pages carry photographs of a meter on a plug, and the two
exploded views are the only drawings. No page names the parts of the machine, describes the
console, controller or brake, draws a block diagram, or defines a connector.

**What the electrical procedures do give**, without a diagram:

- Procedure 1 - test the **adapter** on the meter's **AC** setting: "There should be at least
  **24 volts**"; if not, replace the adapter.
- Procedure 2 - at the console end of the harness, **pin #2 to pin #3** should read "around
  **6 volts**" DC; if it does but the display stays dark, replace the console.
- Procedure 3 - with the harness on the controller, meter the **2nd and 5th wires**; the reading
  should rise as the resistance level is raised. Then the **2-pin connector** to the **brake coil**:
  zero at level 1, a reading at level 2 and above, or the controller is at fault.

So the 2007 bikes run from an AC-output adapter into a controller that drives an electromagnetic
brake coil - a different system from the 2016 books' DC-adapter, gear-motor design, whose
fourteen-pin list (`spirit-xb-2016-specs-console-to-driver-board-14-pin-definition`) must not be
read back onto these. The steps themselves are in the errors section; the parts lists are on
`xbr25-2007-specs-parts-list` and `xbr55-2007-specs-parts-list`.


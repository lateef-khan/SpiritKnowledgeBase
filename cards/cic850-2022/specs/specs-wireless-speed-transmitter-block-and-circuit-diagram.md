---
id: cic850-2022-specs-wireless-speed-transmitter-block-and-circuit-diagram
title: 'No wire between the pedals and the console: a speed sensor into an AAA-powered
  speed transmitter, radioed to a DT-3268F console on an LR03 cell'
kind: spec
question: What does the block diagram and circuit diagram of a Spirit cic850-2022
  indoor cycle show, and how is the console powered?
asked_as:
- cic850 wiring diagram
- how does the cic850 console get speed
- what battery does the cic850 console take
- cic850 block diagram
keywords:
- block diagram
- circuit diagram
- speed sensor
- speed transmitter
- wireless
- console
- dt-3268f
- lr03 battery
- aaa battery
- lcd display
facets:
  brand:
  - spirit
  product_line: bike
  model: cic850-2022
  applies_to:
  - cic850-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ab900-2018-specs-console-wiring-four-aa-batteries-and-2-pin-reed-switch-rpm-sensor
- sole-spinner-console-spec
see_also:
- spirit-cic850-specs-dt3268f-console-part-number
- cic850-2022-specs-parts-electronic-parts-named
- cic850-2022-specs-outline-and-skeleton-part-names
source:
  ref: spirit-bike-cic850-2022-service-manual
  locator: Section 3 Electrical Configurations, PDF p. 9 (printed 8), text.md lines
    148-161; section 5 Unit Block Diagrams, PDF p. 18 (printed 17), line 274, a flattened
    drawing read from a 300 dpi render (OCR supplement lines 722-737); section 7 Circuit
    diagram, PDF p. 22 (printed 21), lines 313-321, read from the render (OCR lines
    740-744)
  extracted_at: '2026-09-11'
---

**Electrical configuration:** "CONSOLE: Display relevant workout information of the bike" and, under
General Information, "Contains Key controls and **LCD Display**." No other part is described.

**Block diagram (printed p. 17):** five boxes. **SPEED SENSOR** with a two-way arrow to the **SPEED
TRANSMITTER**; **AAA BATTERY** into the transmitter; the transmitter with a two-way arrow to the
**CONSOLE**; **LR03 BATTERY** into the console. **The transmitter-to-console link is the radio
link** - there is no cable up the frame, which is why the troubleshooting pages talk about
pairing, cross-talk between bikes and a 36-inch separation. LR03 is the IEC name for an AAA
cell, so both ends run on the same size of battery named two ways.

**Circuit diagram (printed p. 21):** two photographs, no lines between them - the **DT-3268F
CONSOLE** and the **SEPPD TRANSMITTER** (sic, for *speed*). That is the whole schematic: nothing
is wired to anything.

The DT-3268F part code is on `spirit-cic850-specs-dt3268f-console-part-number`; the same
Dyaco console family is on Sole spinners as the DT-3268 (`sole-spinner-console-spec`) - a
different brand. The pairing procedure is in the console section.


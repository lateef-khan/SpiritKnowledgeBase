---
id: cic850-2022-specs-parts-electronic-parts-named
title: 'The named electronic parts: display, speed sensor and speed transmitter'
kind: fact
question: Which electronic parts does the Spirit cic850-2022 service manual name,
  and where are they?
asked_as:
- what electronic parts are in the cic850
- where is the speed transmitter on the cic850
- what talks to the cic850 console
- indoor cycle speed sensor location
keywords:
- electronic parts
- upper controller
- lower controller
- part names
- service manual
- speed transmitter
- transmitter
- indoor cycle
- battery
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
- jb950-2022-specs-parts-electronic-parts-named
- ab900-2018-specs-parts-electronic-parts-named
see_also:
- spirit-cic850-specs-dt3268f-console-part-number
- spirit-cycle-specs-resistance-systems
- spirit-bike-specs-parts-service-manual-tool-list-is-one-multimeter
source:
  ref: spirit-bike-cic850-2022-service-manual
  locator: 2-1 Upper Controllers PDF p. 7 (printed 6), text.md lines 115-125; 2-2
    Lower Controller and Driver PDF p. 8 (printed 7), lines 126-141; the block diagram
    that names the battery is PDF p. 18, lines 276 and 722-737
  extracted_at: '2026-09-11'
---

**2-1 Upper Controllers (p. 7)** - **DISPLAY** alone: a photograph of the battery LCD console.

**2-2 Lower Controller and Driver (p. 8)** - **SPEED SENSOR** and **SPEED TRANSMITTER**. The sensor is the
reed switch at the flywheel; the transmitter is the separate battery box it plugs into, which sends the
cadence to the console by radio. The block diagram on PDF p. 18 (printed 17) draws it as *SPEED SENSOR - SPEED TRANSMITTER
<-> CONSOLE* with an **LR03** battery, and the circuit diagram on PDF p. 22 (printed 21) labels the console **DT-3268F** and
the transmitter **SEPPD**.

**There is no controller and no motor to name.** Resistance on this cycle is a hand-set brake block on
the flywheel, so the chapter names nothing under "driver"; the pairing between transmitter and console is
what the troubleshooting pages are about ("Each transmitter and console are matched one to one"). How the
indoor cycles' resistance systems differ is on `spirit-cycle-specs-resistance-systems`.

**The DT-3268F console is the one part number this book prints**, on its circuit diagram; the owner's manual
prints the same number in its parts list (`spirit-cic850-specs-dt3268f-console-part-number`).

**This book prints no tool list.** The tools lettered A to E in its crank and bottom-bracket procedure are
photographed inside that procedure and stay with it.

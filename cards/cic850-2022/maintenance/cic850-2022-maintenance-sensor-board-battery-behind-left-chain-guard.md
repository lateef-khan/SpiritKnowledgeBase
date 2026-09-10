---
id: cic850-2022-maintenance-sensor-board-battery-behind-left-chain-guard
title: The speed sensor board battery behind left chain guard B, whose type the manual
  never prints
kind: procedure
question: How do I change the speed sensor battery on a cic850-2022, and what type
  of cell does it take?
asked_as:
- how do i change the speed sensor battery on my cic850
- my cic850 stopped showing speed
- what battery is in the sensor board on the cic850
- how do i take the chain guard off my indoor cycle
keywords:
- sensor board
- speed sensor
- battery
- left chain guard
- screw 119
- guard 118
- pairing
- transmitter
- mode key
- set key
facets:
  brand:
  - spirit
  product_line: bike
  model: cic850-2022
  applies_to:
  - cic850-2022
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-indoor-cycle-speed-transmitter-two-aaa-batteries
- spirit-indoor-cycle-maintenance-console-two-aaa-batteries
- sole-spinner-transmitter-battery-behind-left-cover
see_also:
- cic850-2022-maintenance-belt-tension-behind-the-top-and-right-guards
source:
  ref: spirit-bike-cic850-2022-owners-manual
  locator: 'CIC850 STEP EIGHT, printed p. 17 (PDF p. 17). The absence of a cell type
    was proved twice: the native extraction of that page names none, and a 300 dpi
    render read with tesseract --psm 4 returned only the same sentence. A spacing-tolerant
    search of the whole text.md for battery, cell, AAA, AA, CR and lithium finds no
    type for this component anywhere in the manual.'
  extracted_at: '2026-09-09'
---

1. Loosen the **SCREW (119)** using **Wrench (C)**. Remove **LEFT CHAIN GUARD B (118)**.
2. **Insert the new battery on the sensor board.**
3. Replace **LEFT CHAIN GUARD B (118)** and secure it with the screw.

**The manual never says what battery this is.** No chemistry, no size, no voltage — the whole
instruction is "insert the new battery on the sensor board". Checked in the native text and again
in a 300 dpi render of the page, in case the type were printed inside the diagram. It is not.
**Do not guess a CR2032 or a AAA for this machine**; tell the customer the manual does not name it
and that they should read the cell they remove.

## Re-pairing after the change

All transmitters are paired with the console before shipping, and these steps should only be needed
if the devices have been unpaired:

1. Hold **both MODE and SET** keys on the console for **3 seconds**.
2. On the speed transmitter, press the small **"SPEED CONTROL PAIR KEY"**.
3. The console should read **0** once pairing has been established.
4. If the console reads **Err**, pairing has failed. Press **SET** to repeat. If no action is taken
   within **10 seconds** the console exits pairing mode automatically.

## This is not the XIC600 transmitter

The XIC600's transmitter is an external module held on by Velcro under the left crank, takes **2
AAA** cells, and is paired by holding two console keys and then a **blue button** on the transmitter
until the display reads **ID 0** — `spirit-indoor-cycle-speed-transmitter-two-aaa-batteries`. The
CIC850's sensor is a **board inside the machine**, behind a guard, paired with MODE and SET, and
reports **Err** rather than **ID ER**. Nothing carries across.

The CIC850's console battery is a separate item and *is* named: **2 AAA** —
`spirit-indoor-cycle-maintenance-console-two-aaa-batteries`.

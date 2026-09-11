---
id: spirit-ct800-specs-electrical-part-descriptions
title: What each electrical part does on the DC-motor machines, with a 110 volt incline
  motor
kind: fact
question: What does each electrical part do on a Spirit CT800 2020 or CT800ENT treadmill,
  and what voltage is the incline motor?
asked_as:
- what voltage is the incline motor on the ct800
- is the ct800 ent a dc motor treadmill
- incline motor wire colours on the new ct800
- what does the main controller do
keywords:
- electrical configuration
- main controller
- dc motor
- incline motor
- safety key
- console
- voltage
- wire colour
- dc control board
- tft
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct800-2016-specs-electrical-part-descriptions
- ct850-2020-electrical-part-descriptions
see_also:
- spirit-ct800-specs-driver-board-connector-locations
- ct800-2020-specs-circuit-diagram
- ct800ent-2022-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct800-2020-service-manual
  locator: 'CT800-2020: PDF p. 9 (printed 9), section 3 Electrical Configurations,
    text.md lines 117-144. CT800ENT-2022: PDF p. 10 (printed 10), section 3, lines
    141-171'
  extracted_at: '2026-09-11'
---

Both books print the same table, with one difference in the console line.

- **Safety key** - fits on the console and activates all functions. With no safety key the console cannot
  be controlled.
- **Console** - the interface that controls all functions of the treadmill; key controls and an **LED**
  display on the CT800-2020, key controls and a **TFT** display on the CT800ENT.
- **Main controller** - the circuit board that carries the AC power supply for the console, the incline
  driver and the motor driver, and links the console to output the voltages for the **DC control Board**.
- **DC motor** - increases and decreases speed. **Neither book prints a work voltage for it.**
- **Incline motor** - a **110 volt AC** motor with four wires (red, black, white, green) plus one 3-pin
  position-sensor cable. AC on **red = UP**, AC on **black = DOWN**, **white = COM (neutral)**, **green =
  ground**.

**The CT800-2020 book contradicts itself on the motor type.** Its first table says "DC motor" and "DC
motor driver", but its general-information lines then say "AC motor driver", "AC motor" and "AC INVERTER
Board control circuit" - text copied from the CT850-2020. The machine is a DC-motor treadmill: its driver
board is the PA-AE00301L-002 with M+ / M- terminals and its circuit diagram names a Ya Cheng YC782 DC
motor. The CT800ENT book says DC throughout.

The CT800-2016 prints a **120 volt** incline motor and a **DC 90V~** drive motor; the CT850 books describe
an AC-inverter machine. Use the book for the machine in hand.

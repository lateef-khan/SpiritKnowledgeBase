---
id: spirit-med-70-bike-specs-wiring-diagram-6-pin-console-9-pin-angle-sensor-and-13-pin-power-cables
title: Wiring diagram with a 6-pin computer cable, a 9-pin angle sensor cable and
  a 13-pin DC power cable marked 36 V, on a bike whose text meters 24 V
kind: spec
question: What does the wiring diagram of a Spirit Medical 7.0R or 7.0U bike show,
  and what is on each pin of the console, angle sensor and power cables?
asked_as:
- 7.0r wiring diagram
- 7.0u pinout of the console cable
- which pin is 12v on the spirit medical 7.0 bike
- angle sensor cable pins 7.0r
keywords:
- wiring diagram
- mr7000
- mu7000
- pinout
- computer cable
- angle sensor cable
- crank sensor cable
- brake controller
- switching power supply
- 36v dc power cable
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2025
  - 70u-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-40-bike-specs-circuit-diagram-6-pin-computer-cable-to-a-cs52005-controller
- spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
- mt200-2022-specs-wiring-diagram
see_also:
- spirit-med-70-bike-specs-mains-power-through-an-ac-input-module-and-switching-power-supply
- 70r-2025-specs-component-description-thirteen-numbered-parts
- 70u-2025-specs-component-description-fourteen-numbered-parts
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
source:
  ref: spirit-bike-70r-2025-service-manual
  locator: '7.0R: "MR7000 Wiring Diagram", PDF p. 45 (the last page), text.md line
    663, one embedded picture whose four pin tables were read from crops of a 300
    dpi render (OCR supplement lines 1132-1168 cannot read them). 7.0U: "MU7000 Wiring
    Diagram", PDF p. 42 (last page), line 684 (OCR 717-760). The voltages the text
    expects: 5.2.4 Troubleshooting "No Power" steps iii-vi, 7.0R PDF pp. 8-11, lines
    117-140; 7.0U PDF pp. 8-11, lines 168-191'
  extracted_at: '2026-09-11'
---

The recumbent's sheet is titled **MR7000 Wiring Diagram** and the upright's **MU7000 Wiring Diagram**;
the drawing, the boards and the pin tables are the same, only the cable lengths differ.

**What is drawn.** A **Console assembly** with two **hand pulse sensor** leads; a green **Brake
controller** board (captioned **F090355** on the 7.0U sheet); a boxed **Switching power supply**;
the **Induction Brake** with its two coil harnesses; a **Power cord** into an **AC input module** with
a **200 mm ground wire** to earth.

**Cable lengths, per book**

| Cable | 7.0R (MR7000) | 7.0U (MU7000) |
|---|---|---|
| Angle sensor cable, brake to console | 1500 mm | 1500 mm |
| Crank (reed) sensor cable, to the controller | 1550 mm | 660 mm |
| Computer cable, controller to console | 1950 mm | 1850 mm |
| DC power cable, power supply to controller | 350 mm, "36v DC" | 500 mm, "36v DC" |
| Wire brake coil harnesses | 800 mm and 950 mm | 200 mm and 250 mm |
| AC connecting wire, input module to power supply | 1200 mm | 1400 mm |
| Hand pulse sensor assembly | 2100 mm | not dimensioned |

**Computer cable, 6 pins (controller to console)**

| Pin | Colour | Signal | Level |
|---|---|---|---|
| P1 | Black | VCC | 12V |
| P2 | Brown | GND | 0 |
| P3 | Red | VIN | 12V |
| P4 | Orange | NC | - |
| P5 | Yellow | PWM | square wave |
| P6 | Green | RPM | pulse |

**Angle sensor cable, 9 pins (brake to console)**

| Pin | Colour | Signal | Pin | Colour | Signal |
|---|---|---|---|---|---|
| P1 | Black | N.C. | P6 | Green | CS-P |
| P2 | Brown | GND, 0 | P7 | Blue | DIO-N |
| P3 | Red | CLK-N | P8 | Purple | DIO-P |
| P4 | Orange | CLK-P | P9 | Grey | 5V |
| P5 | Yellow | CS-N | | | |

The three signal pairs carry the square-wave glyph in the Level column; they are a differential
clock, chip-select and data line to the angle sensor on the brake. The 5 V on P9 against GND on P2
is the "pin 2 and pin 9 ... 5V DC" the troubleshooting chapter meters.

**DC power cable, 13 pins (power supply to controller)**: only four positions are wired - **P4 and P5
Black GND 0**, **P10 and P11 Red Vdc 36V**; P1-P3, P6-P9, P12 and P13 are NC.

**Hand pulse sensor, 4 pins (7.0R sheet only)**: P1 Black L, P2 Brown C, P3 Red C, P4 Orange R.

**Two voltages in one book.** The sheet labels the power cable *36v DC* and its table *36V*, but the
No Power procedure in the same book meters "the 4 pin connector for **24V DC**" at the control board
and "**24V DC** at the output" of the switching power supply, and says the 6-pin console cable
carries 12 V on "pin 1/pin 6 and pin 3/pin 6" - where the table puts GND on pin 2, not pin 6. The
text also calls the supply's output an 8-pin connector where the sheet draws thirteen. Meter what the
procedure says and expect either figure; the book does not reconcile them
(`spirit-med-70-bike-specs-mains-power-through-an-ac-input-module-and-switching-power-supply`).

The 8.0U and 8.5R are a different platform, on a 24 V Mean Well module and a CS51009 board
(`spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards`).


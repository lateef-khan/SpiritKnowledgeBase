---
id: spirit-med-70-bike-specs-mains-power-through-an-ac-input-module-and-switching-power-supply
title: Mains power enters through an AC input module with a fuse and a switching power
  supply, which the text meters at 24 V DC and the diagram labels 36 V
kind: spec
question: How is a Spirit Medical 7.0R or 7.0U bike powered, and what voltages should
  be measured at the power supply, control board and console?
asked_as:
- does the 7.0r plug in
- what voltage comes out of the 7.0u power supply
- is the spirit medical 7.0 bike self powered
- where is the fuse on the 7.0r
keywords:
- power supply
- switching power supply
- ac input module
- fuse
- 90-240vac
- 24v dc
- 36v dc
- 12v dc
- plug in
- hospital grade power cord
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
- spirit-med-40-bike-specs-electrical-configuration-generator-brake
see_also:
- spirit-med-70-bike-specs-wiring-diagram-6-pin-console-9-pin-angle-sensor-and-13-pin-power-cables
- spirit-med-bike-specs-fuse-rating-5-a-250-v-fast-acting-glass
- spirit-med-70-bike-specs-mains-90-to-240-v-1-76-to-0-71-a
- spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v
- 7-5s-med-specs-service-manual-switching-power-supply-12-vdc-1-6-a
source:
  ref: spirit-bike-70r-2025-service-manual
  locator: '7.0R: 5.2.4 Troubleshooting "1. No Power" steps i-vii, PDF pp. 8-11 (printed
    8-11), text.md lines 117-140; parts list items 236 Power Adaptor, 237 Generator/Brake
    Controller, 238 AC Electronic Module (OCR supplement reads them Switching Power
    Supply, Brake Controller, AC Input Module), PDF p. 42, lines 606-608; the wiring
    diagram PDF p. 45. 7.0U: the same steps, PDF pp. 8-11, lines 168-191; parts list
    27 AC Power Input Module, 123 Controller Brake, 124 Switching Power Supply, 161
    Power Cord Hospital Grade, lines 570 and 629-665; the wiring diagram PDF p. 42'
  extracted_at: '2026-09-11'
---

**These bikes plug in; they do not generate their own power.** The chain the book describes, in the
order the No Power procedure meters it:

1. **The A.C. outlet** - "90~240VAC", the line cord "plugged in securely and the power switch on".
2. **The input module** - between the power switch and the line cord socket, and it holds **the fuse**:
   "Use the meter to check the fuse, the fuse should be short ... replace the fuse if the fuse was
   open." The service manual prints no fuse rating; the owner's manuals do (5 A, 250 V glass -
   `spirit-med-bike-specs-fuse-rating-5-a-250-v-fast-acting-glass`).
3. **The switching power supply** - mains in on a **2-pin connector**, "**24V DC** at the output" on
   what the text calls an **8-pin connector** (the wiring diagram draws a 13-way plug, two red Vdc and
   two black GND pins used, and labels it *36v DC*). Held to the frame by **four plastic standoffs**.
4. **The control board (brake controller)** - "the input voltage at the control board at the **4 pin
   connector** for 24V DC"; replace the board if the 24 V is there and nothing lights.
5. **The 6-pin console cable** - "pin 1/pin 6 and pin 3/pin 6 ... for **12V DC**" at the console, and
   "pin 3 and pin 6 of the 6 pin connector at the control board"; 12 V at the board but not at the
   cable means a new cable.

**The three names the parts lists give the same three parts** differ between the two books and
between the text layer and the printed page of the 7.0R list: the 7.0R text reads *Power Adaptor*
(236) and *AC Electronic Module* (238) where the rendered page reads *Switching Power Supply* and *AC
Input Module*; the 7.0U list says *AC Power Input Module* (27), *Switching Power Supply* (124) and a
*Power Cord, Hospital Grade* (161). The 7.0R lists its cord as *Power Cord (Optional)* (43).

**The 24 V against 36 V contradiction is inside each book** and is not resolved anywhere in it; see
`spirit-med-70-bike-specs-wiring-diagram-6-pin-console-9-pin-angle-sensor-and-13-pin-power-cables`.
The 4.0R and 4.0U medical bikes are the opposite design - a generator, no cord, no fuse
(`spirit-med-40-bike-specs-electrical-configuration-generator-brake`); the 8.0U and 8.5R carry a 24 V
Mean Well module instead (`spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v`).


---
id: xterra-trx-specs-electrical-configuration-printed-for-230-vac-with-a-220-volt-incline-motor
title: 'What each electrical part does, printed for a 230 VAC machine: a 0 to 180
  volt DC drive motor and a 220 volt AC incline motor, in a book sold with a 120 volt
  treadmill'
kind: fact
question: What does the electrical configuration chapter of the Xterra TRX treadmill
  service manual say about the motor and incline motor voltages, and why does it read
  230 volts?
asked_as:
- trx3500 incline motor voltage
- trx2500 motor voltage 0-180
- why does the service manual say 230 volts
- trx4500 incline motor wires
keywords:
- electrical configuration
- incline motor
- 220 volt
- 230 vac
- dc motor
- 0 to 180 volt
- wire colour
- position sensor
- main controller
- export version
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx1400-2023-specs-electrical-configuration-incline-motor-110-or-230-volt-ac
- xterra-treadmill-specs-electrical-configuration-0-to-90-volt-at-120-vac-or-0-to-180-volt-at-230-vac
see_also:
- spirit-xt-2015-specs-electrical-part-descriptions-0-to-180-volt
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM (GT90B-NT022) ''3. Electrical Configurations'', PDF p. 11 (printed
    10), lines 122-153, and PDF p. 12 (printed 11), lines 153-191. TRX3500/TRX4500
    SM prints the same text word for word at PDF p. 12 (printed 11), lines 106-137,
    and PDF p. 13 (printed 12), lines 137-175. The 120 V outlet: TRX2500 OM PDF p.
    5, TRX3500 OM PDF p. 5; the TRX4500 OM PDF p. 5 says ''nominal 110-volt circuit'''
  extracted_at: '2026-09-11'
---

**These three books print the export figures.** Their chapter 3 reads, in the TRX2500 book and word for word in the
TRX3500/TRX4500 book:

- **Safety key** - "To fits on the Console that activate all functions. If no safety key, console can not be
  controlled."
- **Console** - "Interface that controls all functions of the treadmill"; contains key control and LCD display.
- **Main controller** - "the DC power supply for console, incline driver and DC motor driver"; includes power supply,
  motor driver control circuit and incline control circuit.
- **Treadmill motor** - "a variable speed for DC motor. To control the **0 – 180 (230VAC)** voltages on the main
  controller"; then "DC motor with variable speed range 0-90 or (0-180) volt. Have three wires red, black and green.
  If there is DC voltage on the Red (white) wire (M+) the treadmill motor will turn clockwise. If there is DC voltage
  on the Black wire (M-) the treadmill motor will turn counter-clockwise. The higher the voltage the faster the motor
  turns. The green wire is ground."
- **Incline motor** - "This is a **220 volt AC motor**. Requires four wire connection: red, black, white and green.
  Has one 3 pins cable for position sensor." AC on the **red** wire (UP) raises the incline, AC on the **black** wire
  (DOWN) lowers it, the **white** wire (COM) is neutral, green/yellow is ground.

**The machines these books ship with are 120 volt.** Their owner's manuals call for a 120-volt, 15-amp outlet
(the TRX4500 book says a "nominal 110-volt circuit"), the circuit diagrams in the same service manuals are titled
"120V" with a separate "220V" or "CEGS 220V" sheet, and the driver-board photographs carry a "110V" sticker. The
service-manual text was written for the 230 VAC export build, on which the drive motor runs 0-180 V and the incline
motor is the 220 V type; on the 120 V machine the drive motor is the 0-90 V range the same sentence names in brackets.
The book never says which incline-motor voltage the 120 V machine uses. The TR260 and TRX5500 books, which print
both voltages side by side, are on a separate card.

The 8.11 troubleshooting matrix in the TRX2500 book keeps the same export figure - "Check the voltage of power is
220V" - which the errors section notes.

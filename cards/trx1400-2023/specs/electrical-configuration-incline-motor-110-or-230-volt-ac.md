---
id: trx1400-2023-specs-electrical-configuration-incline-motor-110-or-230-volt-ac
title: 'What each electrical part does: a 0 to 90 volt DC drive motor, and an incline
  motor that is a 110 or 230 volt AC motor with red up, black down, white common and
  a 3-pin sensor'
kind: fact
question: What does the electrical configuration chapter of the Xterra trx1400-2023
  treadmill service manual say about the drive motor, incline motor, controller and
  console?
asked_as:
- trx1400 incline motor voltage
- trx1400 motor wire colours
- what does the trx1400 main controller do
- incline motor wires red black white
keywords:
- electrical configuration
- incline motor
- 110 volt
- 230 volt
- dc motor
- 0 to 90 volt
- wire colour
- position sensor
- main controller
- cegs
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-electrical-configuration-dc-motor-0-to-90-volt-and-no-incline-motor
- xterra-trx-specs-electrical-configuration-printed-for-230-vac-with-a-220-volt-incline-motor
see_also:
- spirit-xt-2015-specs-electrical-part-descriptions-0-to-180-volt
- trx1400-2023-specs-driver-board-b307d-wire-connections
- trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
- trx1400-2023-specs-incline-position-sensor-pin-1-is-5-volts
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM (T3-NT053-01) '3. Electrical Configurations', PDF p. 13, lines
    141-167, and GENERAL INFORMATION PDF p. 14, lines 167-196; 'Special Note on T3CEGS
    version' PDF p. 5, lines 58-72
  extracted_at: '2026-09-11'
---

**This is the T3 text, which prints the incline motor as "110 or 230 volt".** The GT90 books print it as a 220 volt
motor and the GT65 book has no incline motor.

- **Safety key** - "fits into the Console to activate all functions and treadmill. Without safety key, console cannot
  be controlled and treadmill will not be activated."
- **Console** - "Interface that controls all functions"; contains keys, LCD display, speaker, fan, hand pulse grip
  and safety key.
- **Main controller** - "the DC power supply for console, Incline driver and DC motor driver"; includes power supply,
  motor driver, control circuit, incline control circuit and speed sensor. "The 220V (or CEGS) of Lower Controller
  Area has Filter and Chock."
- **Treadmill motor** - "a DC motor with variable speed. Control the 0 – 90 (or 0-180) voltages from the main
  controller". Three wires, red, black and green: red into M+, "White" into M- (the wiring pages put the **black**
  wire on M-; the text's "white" contradicts its own three-colour list), green is ground.
- **Incline motor** - "an AC motor, used to control variable elevation through the console within main controller";
  "a 110 or 230 volt AC motor. All of five wire connection: red, black, white, green, and has one of 3 pins cable for
  position sensor." AC on the **red** wire = UP, AC on the **black** wire = DOWN, **white** = COM (neutral),
  green/yellow = ground.

The 110 V / 230 V pairing is the two versions of the machine (p. 5): the CE/GS version takes 230 VAC and adds a
filter choke; the US machine is the 110 V version, so its incline motor is the 110 V one. No horsepower or current is
printed.

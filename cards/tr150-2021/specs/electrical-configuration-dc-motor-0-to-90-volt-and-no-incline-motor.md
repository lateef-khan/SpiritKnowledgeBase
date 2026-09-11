---
id: tr150-2021-specs-electrical-configuration-dc-motor-0-to-90-volt-and-no-incline-motor
title: 'What each electrical part does: a 0 to 90 volt DC drive motor with three wires,
  a main controller with no incline driver, and a 230 VAC CE/GS version with a filter
  choke'
kind: fact
question: What does the electrical configuration chapter of the Xterra tr150-2021
  treadmill service manual say about the motor, controller, console and safety key?
asked_as:
- tr150 motor voltage
- what does the tr150 main controller do
- tr150 motor wire colours m plus m minus
- is there a 230 volt tr150
keywords:
- electrical configuration
- dc motor
- motor voltage
- 0 to 90 volt
- main controller
- safety key
- wire colour
- cegs
- filter choke
- no incline
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: specs
  code: '*'
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with:
- trx1400-2023-specs-electrical-configuration-incline-motor-110-or-230-volt-ac
see_also:
- spirit-xt-2015-specs-electrical-part-descriptions-0-to-180-volt
- tr150-2021-specs-driver-board-b426d-wire-connections
- tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM (GT65-NT014) '3. Electrical Configurations', PDF p. 10 (printed
    11), lines 95-116, and GENERAL INFORMATION PDF p. 11 (printed 12), lines 116-135;
    'Special Note on GT65 CEGS version' PDF p. 3 (printed 3), lines 41-50
  extracted_at: '2026-09-11'
---

**This is the GT65 text: a treadmill with no incline motor.** The TRX1400, TR260 and TRX books add an incline
driver and an AC incline motor on their own cards.

- **Safety key** - "fits into the Console to activate all functions and treadmill. Without safety key, console will be
  appeared E0."
- **Console** - "Interface that controls all functions of the treadmill"; contains keys, LCD display, hand pulse grip
  and safety key.
- **Main controller** - "the DC power supply for console, and DC motor driver, links the console to output appropriate
  voltages for motor"; includes power supply, motor driver and control circuit. "The 220V (or CEGS) of Lower
  Controller Area has Filter and Chock."
- **Treadmill motor** - "a DC motor with variable speed. Control the 0 – 90 (or 0-180) voltages from the main
  controller to increase or decrease speed of the running belt." Three wires: red, black and green. "The Red wire is
  inserted into M+. The White wire is inserted into M-. When voltage is higher and higher, the motor will be faster.
  The green wire is grounding wire."

**Two things the book gets at odds with itself.** It lists the motor's three wires as red, black and green and then
says the *white* wire goes to M-; the driver-board page and the circuit diagram both put the **black** wire on M-. And
the 0-90 / 0-180 V pair is the 110 V / 230 V split, which the book states on p. 3: "Besides normal version, GT65
treadmill is with a CE/GS version. Both versions are with exactly the same in functions and outlines except that the
power input is 110AC for normal version versus 230VAC for CEGS version and an additional Filter Choke circuit is added
for CEGS version". The US machine is the 110 V, 0-90 V version.

No motor horsepower, current or work voltage for the console is printed.

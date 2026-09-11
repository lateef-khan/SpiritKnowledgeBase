---
id: spirit-cr800-cu800-2021-specs-electrical-configuration-generator-flywheel
title: Console, main controller and generator flywheel, with the generator power supply
  feeding the console and the controller putting out the braking voltage
kind: fact
question: What electrical parts does the service manual name on a Spirit CR800 or
  CU800 2020-version bike, and what does each do?
asked_as:
- what is the main controller on the cu800 2020
- what changes resistance on the cr800
- what electronic parts are in the cu800
- thumb switch cr800
keywords:
- electrical configuration
- generator flywheel
- generator brake
- main controller
- led display
- cooling fan
- thumb switch
- speed rpm sensor
- controller
- electronic parts
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cu800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800ent-cu800ent-specs-electrical-configuration-induction-brake
see_also:
- spirit-cr800-cu800-2021-specs-unit-block-diagram
- spirit-cr800-cu800-2021-specs-generator-controller-connections
- spirit-bike-specs-generator-brake-or-induction-brake
source:
  ref: spirit-bike-cu800-2021-service-manual
  locator: 'CU800(2020): section 3 Electrical Configurations, PDF p. 9 (printed 9),
    text.md lines 146-165; section 2 Electronic Parts, PDF pp. 7-8, lines 101-139.
    CR800(2020): PDF p. 9, lines 126-145; PDF pp. 7-8, lines 90-119. Identical wording'
  extracted_at: '2026-09-11'
---

Section 3 is a three-row table:

| Part name | Part description as printed |
|---|---|
| **CONSOLE** | Interface that controls all functions of the Bike. |
| **MAIN CONTROLLER** | The circuit board is consist of the generator power supply for console, link the console to output appropriate voltages for braking resistance that control Bike functions. |
| **GENERATOR FLYWHEEL** | It can change to increase or decrease resistance level of brake. |

General information adds that the console holds the keys and **LED display windows**, and the
main controller "include power supply (generator power), driver control circuit".

So on these two bikes the **flywheel is the generator**: it powers the console through the
controller, and the controller feeds a braking voltage back into the flywheel's coil. **No
voltage or current figure is printed** for either direction.

The chapter-2 photographs (named on `spirit-cr800-cu800-2020-specs-parts-electronic-parts-named`)
caption the same unit **GENERATOR BRAKE** - and print it on the *upper controllers* page, beside
the fan and display, although it sits in the flywheel.

**Not the ENT-800 bikes**, which have an induction brake on a mains-fed controller - see
`spirit-cr800ent-cu800ent-specs-electrical-configuration-induction-brake`.


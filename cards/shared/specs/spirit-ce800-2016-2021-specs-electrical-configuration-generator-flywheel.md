---
id: spirit-ce800-2016-2021-specs-electrical-configuration-generator-flywheel
title: Console, main controller and generator flywheel are the three electrical parts
  named, and the main-controller entry says tension motor on a machine that has none
kind: fact
question: What electrical parts does the service manual name on a Spirit CE800 generator
  elliptical, and what does each do?
asked_as:
- what is the generator flywheel on the ce800
- what does the main controller do on the ce800 elliptical
- ce800 electrical configuration
- does the ce800 have a tension motor
keywords:
- electrical configuration
- generator flywheel
- main controller
- generator power
- tension motor
- led display
- ems brake
- generator brake
- cooling fan
- thumb switch
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce800-2016
  - ce800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800ent-electrical-part-descriptions
see_also:
- ce800-2021-specs-unit-block-diagram
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- ce800-2021-specs-generator-controller-connections
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
- spirit-cr800-cu800-2021-specs-electrical-configuration-generator-flywheel
- spirit-elliptical-specs-console-display-type-by-service-manual
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: 'CE800-2021: section 3 Electrical Configurations, PDF p. 11 (printed 10),
    text.md lines 170-190; section 2, PDF pp. 8-9, lines 133-164. CE800-2016: section
    3, PDF p. 10, lines 173-195; section 2, PDF pp. 7-8, lines 130-167. The three
    paragraphs are word for word the same in both books'
  extracted_at: '2026-09-11'
---

Both books print the same three entries:

- **Console** - "interface that controls all functions of the Elliptical"; contains the key controls
  and **LED display windows**.
- **MAIN CONTROLLER** - "the circuit board consist of the generator power supply for console, link
  the console to output appropriate voltages for **tension motor** that control the elliptical
  functions"; the general-information line adds that it includes the power supply (generator power)
  and the driver control circuit.
- **GENERATOR FLYWHEEL** - "it can change to increase or decrease resistance level of brake".

**There is no tension motor on either machine.** The phrase is Dyaco boilerplate from the gear-motor
books: the block diagram, driver board and circuit diagram of both books show a generator feeding a
controller that drives a brake coil, and no motor of any kind. Resistance is set by the voltage
the controller puts on the coil - the *generator brake resistance voltage* lead.

**No voltage, current or resistance figure is printed in the section.** Neither machine has an
adapter or a mains cord: the console is powered by pedalling.

**What the chapter-2 photographs call the parts differs between the two books:**

| Book | Upper controllers | Lower controller and driver |
|---|---|---|
| CE800-2016 | Cooling FAN, Thumb Switch, DISPLAY, **EMS BRAKE** | SPEED RPM SENSOR, CONTROLLER |
| CE800-2021 | Cooling Fan, Thumb Switch, Display, **GENERATOR BRAKE** | Controller, Speed Sensor |

The CE800ENT is not this configuration - it runs from an outlet and its book names an incline
motor it does not have (`ce800ent-electrical-part-descriptions`). The 2020-version CR800 and CU800
bikes print the same three paragraphs, "Elliptical" included
(`spirit-cr800-cu800-2021-specs-electrical-configuration-generator-flywheel`).


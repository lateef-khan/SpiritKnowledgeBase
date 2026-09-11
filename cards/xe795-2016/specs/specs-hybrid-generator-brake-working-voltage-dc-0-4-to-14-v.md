---
id: xe795-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v
title: Hybrid generator brake working voltage is DC 0.4 to 14 V, and the electrical
  configuration names a console, main controller and generator brake with an LCD
kind: spec
question: What voltage does the hybrid generator brake work on in a Spirit xe795-2016
  elliptical, and what electrical parts does the service manual name?
asked_as:
- xe795 generator brake voltage
- xe795 2016 electrical configuration
- what is the working voltage of the xe795 brake
- does the xe795 have an adapter
keywords:
- hybrid generator brake
- working voltage
- dc 0.4-14v
- electrical configuration
- main controller
- generator brake
- console
- lcd
- induction brake
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2016
  applies_to:
  - xe795-2016
  section: specs
  code: '*'
  model_number:
  - '795015'
authority: 3
not_to_be_confused_with:
- xe795-2023-specs-electrical-configuration-generator-brake
- xbr95-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v
see_also:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
- xe795-2016-specs-unit-block-diagram
- xe795-2016-specs-parts-electronic-parts-named
- spirit-elliptical-specs-console-display-type-by-service-manual
source:
  ref: spirit-elliptical-xe795-2016-service-manual
  locator: Section 3 Electrical Configurations, PDF pp. 11-12 (printed 11-12), text.md
    lines 173-200; section 2 Electronic Parts, PDF p. 9, lines 155-167
  extracted_at: '2026-09-11'
---

Section 3 names three parts:

- **CONSOLE** - interface that controls all functions; key controls and an **LCD** display.
- **MAIN CONTROLLER** - "the DC power supply for console" and the driver control circuit.
- **GENERATOR BRAKE** - "it can change to increase or decrease resistance level of brake".

and prints one figure, on the next page:

> **HYBRID GENERATOR BRAKE** - Work voltage: **DC 0.4 ~ 14 V**

That is the voltage the 031101B controller puts on the two-wire brake-coil lead to set
resistance - low for an easy level, up to 14 V for the hardest. It is the only voltage in the
section; **no coil resistance, no generator output and no adapter** are printed, because the
machine has none - the generator powers the console.

The 2016 XBR95 bike prints the same 0.4-14 V for its brake
(`xbr95-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v`); the 2023 XE795 book
drops the figure and names the parts differently
(`xe795-2023-specs-electrical-configuration-generator-brake`). The two flywheel leads are on
`spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads`.


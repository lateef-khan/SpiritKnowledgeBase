---
id: spirit-climber-2024-specs-resistance-system
title: A motor-set magnetic brake on the steppers and vertical climber, and a generator
  brake with a 24 volt power-failure brake on the stair climbers
kind: spec
question: What kind of resistance or brake does a Spirit stepper, vertical climber
  or stair climber use, and does it generate its own power?
asked_as:
- how does the resistance work on the spirit stepper
- is the stair climber magnetic resistance
- does the stepper plug in or make its own power
- what is the brake part on the stair climber
keywords:
- resistance
- brake
- magnetic
- gear motor
- flywheel
- generator brake
- power adapter
- eddy current
- magneto
- brake coil
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - crs800s-2024
  - cs800-2021
  - cs800-2024
  - csc880-2025
  - csc900-2019
  - csc900-2021
  - csc900-2024
  - cvc800
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-residential-bike-specs-gear-motor-or-generator-brake
- spirit-cycle-specs-resistance-systems
- crw800-2024-specs-resistance-system
- spirit-climber-specs-rehabilitation-stepper-brake-magnets-on-a-disc
see_also:
- spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system
- csc900-2019-specs-power-flow-diagrams-alternator-brake-and-power-resistor
- spirit-climber-specs-no-specification-table
- crs800s-2024-specs-parts-list
- cs800-2024-specs-parts-list
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
- spirit-climber-specs-which-manuals-print-a-parts-list
source:
  ref: spirit-climber-crs800s-2024-owners-manual
  locator: "Parts List printed pp. 38-41 (PDF pp. 40-43), items 32, 38, 115, 121, 125 and 247; the
    same item numbers on the CRS800S-2021 Parts List printed pp. 41-44 (PDF pp. 41-44);
    CS800-2024 Parts List printed pp. 39-40 and CS800-2021 Parts List printed pp. 41-42 (PDF
    pp. 43-44), items 26, 27, 32, 33, 36, 37, 124 and 126; CVC800-2021 Parts List printed
    pp. 31-32 (PDF pp. 33-34), items 34, 35, 42, 45 and 46; CSC900-2024 Troubleshooting
    printed p. 34 (PDF p. 36, read from the OCR supplement of a flat-image page); the
    warranty component tables of CSC900-2019 printed p. 30, CSC900-2021 printed p. 34,
    CSC900-2024 printed p. 36 and CSC880-2025 printed p. 38, and the CSC880-2025
    Troubleshooting table printed p. 33. Service manuals: CSC880 (spirit-climber-
    csc880-2025-service-manual) cover PDF p. 1 '(Magnetic)' and Working Principle PDF p. 5;
    CSC900 2022 (spirit-climber-csc900-2024-service-manual) cover '(Magnetic system)' and
    Component Theory PDF p. 4; CSC900 V1.0 (spirit-climber-csc900-2019-service-manual) Power
    Flow-1 and -2, PDF pp. 3-4; CRS800S and CS800(2020) Electrical Configurations, PDF pp. 9
    and 11"
  extracted_at: '2026-09-10'
---

**None of these manuals ever uses the word *magnetic*, and none states a
resistance rating in watts, newtons or kilograms.** What identifies the
resistance unit is the parts list where there is one, and the warranty and
troubleshooting tables where there is not.

| Machine | Resistance unit | Its drive | Power |
|---|---|---|---|
| CRS800S-2021 and CRS800S-2024 | **Fly Wheel** (item 38) and **Magnet** (32) | **Gear Motor** (115) | **Power Adapter (110V,220V)** (125), a 100 mm DC power cord (121) and an optional 220 V transformer power cord (247) |
| CS800-2021 and CS800-2024 | **Flywheel** (26) and **Magnet** (27) | **Gear Motor** (33) | **Power Adaptor** (36), a 100 mm power cord (32) and an optional transformer power cord (37) |
| CVC800-2021 | **Flywheel** (34) and **Magnet** (35) | **Gear Motor** (42) | **Power Adaptor** (45) and a **Transformer Power Cord** (46) |
| CSC900-2019, -2021 and -2024 | **a generator brake**, named in the warranty table of all three, plus a **magneto wheel** and a **24 V power-failure brake** named in the 2024 troubleshooting page | not named - no year of this book prints a parts list | not stated; the electrical safety page gives no voltage or amperage |
| CSC880-2025 | **a brake**, warranted in its own column, described in troubleshooting as a **power-off brake** tested by applying **24 V** | not named - the book prints no parts list | not stated |

**A gear motor moving a magnet against a flywheel is a motor-set magnetic brake.
None of the steppers or the vertical climber generates its own power** - each has
a mains adaptor, and none of their lists contains a `Generator/Brake` row of the
kind the CR800-2024 and CU800-2024 bikes carry.

## The 2021 and 2024 stepper lists use the same item numbers

The CRS800S names its magnet 32, its flywheel 38 and its gear motor 115 in both
the 2021 and the 2024 book; the CS800 names its flywheel 26, its magnet 27 and
its gear motor 33 in both. **The drawing was not renumbered between the two
generations**, so a customer quoting an item number from an older book is quoting
a number that is still current on that machine. That is not true across models -
see the warning at the foot of this card.

**The CS800-2021 list carries a `TV Adapter` (item 125) that the 2024 list does
not.** It is not part of the brake; note it only so that item 125 is not mistaken
for the CRS800S's power adapter, which is also 125.

## The stair climbers are different machines and answer differently

Neither the CSC900 nor the CSC880 prints a parts list, in any year, so the usual
evidence is absent. Two other pages name the brake:

- **The warranty table warrants the brake as a component in its own right.** The
  CSC900 calls it a **`GENERATOR BRAKE`** in 2019, 2021 and 2024 alike, warranted
  for 5 years. The CSC880-2025 heads the same column simply **`Brake`**, also 5
  years. **Only the CSC900 uses the word *generator*** - do not put it in a
  CSC880 answer.
- **The troubleshooting pages name a 24 V brake.** The CSC900-2024 tells a
  technician to "separately supply 24 V voltage to test whether the brake is open
  (there will be a 'click' sound when it is open)", to replace "the power failure
  brake", and - for its `ER02` code - to "check the magneto wheel and the lower
  control connection". The CSC880-2025 prints the same instruction in its own
  words: "Apply a separate 24V voltage to check whether the brake is open (a
  'click' sound will be heard when it is open)", then "Replace the power-off
  brake."

**The CSC900-2024 troubleshooting page is a flat image.** `pdftotext` returns
nothing under its heading; the text above comes from a 300 dpi render read with
`tesseract --psm 4`, so the OCR spells the same page's words inconsistently
("24¥V", "controfier", "@ multimeter"). **Treat the CSC900's 24 V figure as read
from a picture**, confirm it on the machine, and do not quote the OCR's spelling
of any part name. The CSC880-2025's troubleshooting table has a real text layer
and needs no such caution.

## Why the stair climber's brake behaves backwards

On the steppers a higher level means more braking and a harder workout. **On the
CSC900 a higher level means *less* braking**, so the staircase rotates faster and
the user must step faster to keep up. That has been true since the 2019 printing.
The console scale is the same 1 to 20 on the steppers and the CSC900 and means
opposite things - see
`spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top` before answering
any level question for a stair climber. **The CSC880-2025 states no level count
at all**, so nothing can be said about the direction of its scale.

## The rehabilitation steppers are not on this card

The MS300, 7.0S, 7.5S, 8.5S and 8.5S-FIT are a different platform. Three of them
brake with **four permanent magnets on an aluminium disc** and the 8.5S with an
**energised electromagnet coil making eddy currents** - see
`spirit-climber-specs-rehabilitation-stepper-brake-magnets-on-a-disc` and
`spirit-climber-specs-electromagnet-eddy-current-brake`. Their manuals state a
workload in watts, which none of the machines on this card does.

## Where the power supply itself is answered

Whether the machine needs an outlet, and at what voltage and amperage, is a
safety question and lives in the `safety` section, not here. In outline: the
**CRS800S, CS800 and CVC800 books ask for a 110-volt, 15-amp grounded outlet with
a dedicated 5-amp circuit breaker**, and the **CSC900 and CSC880 books state no
circuit requirement at all** while still telling the reader to unplug the machine
and not to run it with a damaged power cord.

**Do not answer a climber from a bike card.** The generator-braked commercial
bikes and the induction-braked ENT bikes are different units in different
machines - see `spirit-bike-specs-generator-brake-or-induction-brake` - and the
gear-motor bikes on `spirit-residential-bike-specs-gear-motor-or-generator-brake`
are residential.

## What the service manuals add

The owner's manuals never say *magnetic*; **the service manuals do, and they split the stair
climbers into two generations**:

- **CSC900-2019 is an alternator drive.** Its V1.0 service manual draws the stepping motion
  turning an **alternator** through a transmission belt, a **speed reducer with a power-off brake**
  on the same shaft, and a **power resistor** (about 0.5 ohm) that the controller switches across the
  alternator to load it - the braking is the generator's load, which is why the warranty table
  says *generator brake* (`csc900-2019-specs-power-flow-diagrams-alternator-brake-and-power-resistor`).
- **CSC900-2024 and CSC880-2025 are a magnetic system.** Both service manuals say so on their
  covers ("Magnetic" / "Magnetic system") and draw a **magnetic flywheel** with a **brake**, a
  **36-hole light-sensor grating** for speed, a **24 V adapter** and a controller that feeds the
  console 12 V (`spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system`). The
  "generator brake" of the 2024 owner's-manual warranty table is a carried-over term; the 2022
  machine's own book names no alternator.
- **The CRS800S and CS800 (2020) service manuals call the gear-motor brake an "ECB BRAKE"** and
  print no working voltage for it; the 2016 CS800 book prints DC 4-6 V for the same kind of motor
  (`spirit-crs800s-cs800-2021-specs-electrical-configuration-ecb-brake-with-no-voltage-printed`,
  `cs800-2016-specs-electrical-configuration-tension-motor-dc-4-to-6-v`).

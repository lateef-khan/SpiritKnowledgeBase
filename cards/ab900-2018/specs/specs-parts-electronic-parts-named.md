---
id: ab900-2018-specs-parts-electronic-parts-named
title: 'The named electronic parts: a console and an RPM sensor, and nothing else'
kind: fact
question: Which electronic parts does the Spirit ab900-2018 service manual name?
asked_as:
- what electronic parts are in the ab900 air bike
- where is the rpm sensor on the air bike
- does the ab900 have a controller board
- air bike console parts
keywords:
- electronic parts
- upper controller
- lower controller
- part names
- service manual
- rpm sensor
- console
- air bike
- batteries
facets:
  brand:
  - spirit
  product_line: bike
  model: ab900-2018
  applies_to:
  - ab900-2018
  section: specs
  code: '*'
  model_number:
  - '900748'
authority: 3
not_to_be_confused_with:
- jb950-2022-specs-parts-electronic-parts-named
- cic850-2022-specs-parts-electronic-parts-named
see_also:
- ab900-2018-specs-parts-air650-discrepancy
- ab900-2018-assembly-tools-needed
- spirit-cycle-specs-resistance-systems
- spirit-treadmill-specs-parts-service-manual-tool-list-is-one-multimeter
source:
  ref: spirit-bike-ab900-2018-service-manual
  locator: 2. Electronic Parts, PDF p. 7 (printed 7), text.md lines 74-83, under the
    chapter title page PDF p. 6; the unit block diagram it agrees with is PDF p. 23,
    lines 412-434
  extracted_at: '2026-09-11'
---

**Two callouts on one page (PDF p. 7): CONSOLE and RPM SENSOR.** The chapter has no Upper Controllers / Lower
Controller split because there is nothing to put under the second heading - the air bike has no motor, no
brake board and no controller. The block diagram on p. 23 agrees: console power is `AA * 4 PCS Batteries`,
and the console's only inputs are the RPM sensor, a wireless (Polar) heart-rate receiver and, on the
Bluetooth build only, a Bluetooth module.

**Bluetooth is a build option, not a part of every AB900.** Every page that mentions it carries the line
"Bluetooth function: Only the model of Bluetooth device configuration"; the Xterra AIR650 built from the
same book has no Bluetooth (`ab900-2018-specs-parts-air650-discrepancy`).

**This book prints no tool list and no part number.** The tools that come in the carton are on
`ab900-2018-assembly-tools-needed`; the wrench sizes the replacement steps call for stay with those steps.

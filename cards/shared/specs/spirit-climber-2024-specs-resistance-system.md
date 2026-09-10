---
id: spirit-climber-2024-specs-resistance-system
title: A motor-set magnetic brake on the two steppers, and a generator brake with a
  24 volt power-failure brake on the stair climber
kind: spec
question: What kind of resistance or brake does a Spirit commercial stepper or stair
  climber use, and does it generate its own power?
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
  - crs800s-2024
  - cs800-2024
  - csc900-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-residential-bike-specs-gear-motor-or-generator-brake
- spirit-cycle-specs-resistance-systems
- crw800-2024-specs-resistance-system
see_also:
- spirit-climber-specs-no-specification-table
- crs800s-2024-specs-parts-list
- cs800-2024-specs-parts-list
- spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top
source:
  ref: spirit-climber-crs800s-2024-owners-manual
  locator: Parts List printed pp. 38-41 (PDF pp. 40-43), items 32, 38, 115, 121, 125
    and 247; also CS800-2024 Parts List printed pp. 39-40, items 26, 27, 32, 33, 36,
    37, 124 and 126; CSC900-2024 Troubleshooting printed p. 34 (PDF p. 36, read from
    the OCR supplement of a flat-image page) and Warranty printed p. 36
  extracted_at: '2026-09-10'
---

**None of the three manuals ever uses the word *magnetic*, and none states a
resistance rating in watts, newtons or kilograms.** What identifies the
resistance unit is the parts list on two of the three, and the troubleshooting
and warranty pages on the third.

| Machine | Resistance unit | Its drive | Power |
|---|---|---|---|
| CRS800S-2024 | **Fly Wheel** (item 38) and **Magnet** (32) | **Gear Motor** (115), with a 350 mm encoder cable (118) | **Power Adapter (110V,220V)** (125), a 100 mm DC power cord (121) and an optional 220 V transformer power cord (247) |
| CS800-2024 | **Flywheel** (26) and **Magnet** (27) | **Gear Motor** (33), with a 200 mm reed switch (34) | **Power Adaptor** (36), a 100 mm power cord (32) and an optional transformer power cord (37) |
| CSC900-2024 | **a generator brake**, named in the warranty table, plus a **magneto wheel** and a **24 V power-failure brake** named in troubleshooting | not named - the book prints no parts list | not stated; the electrical safety page gives no voltage or amperage |

**A gear motor moving a magnet against a flywheel is a motor-set magnetic brake.
Neither stepper generates its own power** - each has a mains adaptor, and neither
list contains a `Generator/Brake` row of the kind the CR800-2024 and CU800-2024
bikes carry.

## The stair climber is a different machine and answers differently

The CSC900 has no parts list, so the usual evidence is absent. Two other pages
name its brake:

- **The warranty table warrants `Frame*`, `Generator Brake`, `Parts, Labor` and
  `Wear Items**` separately** - so the machine has a generator brake, warranted
  for 5 years against the frame's 10.
- **The troubleshooting page names a 24 V brake and a magneto wheel.** It tells a
  technician to "separately supply 24 V voltage to test whether the brake is open
  (there will be a 'click' sound when it is open)", to replace "the power failure
  brake" when the machine will not run, to measure "whether the brake socket of
  the controller has 24 V output voltage after starting", and - for its `ER02`
  code - to "check the magneto wheel and the lower control connection".

**That troubleshooting page is a flat image.** `pdftotext` returns nothing under
its heading; the text above comes from a 300 dpi render read with
`tesseract --psm 4`, so the OCR spells the same page's words inconsistently
("24¥V", "controfier", "@ multimeter"). **Treat the 24 V figure as read from a
picture**, confirm it on the machine, and do not quote the OCR's spelling of any
part name.

## Why the stair climber's brake behaves backwards

On the two steppers a higher level means more braking and a harder workout. **On
the CSC900 a higher level means *less* braking**, so the staircase rotates faster
and the user must step faster to keep up. The console scale is the same 1 to 20
on all three machines and means opposite things - see
`spirit-csc900-specs-twenty-levels-with-less-braking-at-the-top` before answering
any level question for a stair climber.

## Where the power supply itself is answered

Whether the machine needs an outlet, and at what voltage and amperage, is a
safety question and lives in the `safety` section, not here. In outline: the
**CRS800S and CS800 books both ask for a 110-volt, 15-amp grounded outlet with a
dedicated 5-amp circuit breaker**, and the **CSC900 book states no circuit
requirement at all** while still telling the reader to unplug the machine and not
to run it with a damaged power cord.

**Do not answer a climber from a bike card.** The generator-braked commercial
bikes and the induction-braked ENT bikes are different units in different
machines - see `spirit-bike-specs-generator-brake-or-induction-brake` - and the
gear-motor bikes on `spirit-residential-bike-specs-gear-motor-or-generator-brake`
are residential.

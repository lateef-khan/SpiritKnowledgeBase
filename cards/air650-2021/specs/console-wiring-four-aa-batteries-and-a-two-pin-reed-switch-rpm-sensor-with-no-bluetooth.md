---
id: air650-2021-specs-console-wiring-four-aa-batteries-and-a-two-pin-reed-switch-rpm-sensor-with-no-bluetooth
title: The whole electrical system is a console on four AA cells with a two-pin reed-switch
  RPM sensor and a Polar receiver, and no Bluetooth
kind: spec
question: How is the console of an Xterra air650-2021 air bike wired, and what do
  the block diagram and circuit diagram in the service manual show?
asked_as:
- air650 wiring diagram
- where does the rpm sensor plug in on the air650 console
- air650 block diagram
- does the air650 have a controller board
keywords:
- block diagram
- circuit diagram
- console power
- aa batteries
- rpm sensor
- reed switch
- 2 pin sensor wire
- polar receiver
- no bluetooth
- pcb
facets:
  brand:
  - xterra
  product_line: bike
  model: air650-2021
  applies_to:
  - air650-2021
  section: specs
  code: '*'
  model_number:
  - '165718'
authority: 2
not_to_be_confused_with:
- ab900-2018-specs-console-wiring-four-aa-batteries-and-2-pin-reed-switch-rpm-sensor
see_also:
- air650-2021-specs-console-runs-on-four-aa-batteries
- air650-2021-specs-outline-and-skeleton-part-names-per-the-ab900-service-manual
- ab900-2018-specs-parts-air650-discrepancy
- ab900-2018-specs-parts-electronic-parts-named
- xterra-air-specs-fan-resistance-with-no-brake
source:
  ref: spirit-bike-ab900-2018-service-manual
  locator: 'Section 2 Electronic Parts PDF p. 7 lines 73-82; section 3 Electrical
    Configurations PDF p. 9 lines 89-91; section 5 Unit Block Diagrams PDF p. 23 lines
    406-434; Display Board PCB Component Locations, PCB Board Top p. 25 and PCB Board
    Bottom p. 26 lines 446-470; Circuit Diagram ''AU800-GA001 AIR BIKE CIRCUIT DIAGRAM''
    PDF p. 28 lines 478-483, read from the render (OCR supplement lines 1118-1132,
    upside down); Q&A ''console without display'' p. 47 lines 775-787. Applied to
    the AIR650 by xterra-bike-air650-2021-service-note p. 2 (''Blue Tooth: No'').
    AIR650 OM: computer cable (23) through the console base, PDF p. 9 lines 246-257,
    and battery installation p. 15 lines 430-432'
  extracted_at: '2026-09-11'
---

**This is the AIR650 reading of the AB900 service manual: the same two-wire schematic with the Bluetooth items
left out, because the manufacturer's note says the AIR650 has none.** The Spirit card
`ab900-2018-specs-console-wiring-four-aa-batteries-and-2-pin-reed-switch-rpm-sensor` keeps the Bluetooth build.

**Electronic parts (p. 7):** two callouts, CONSOLE and RPM SENSOR. **Electrical configuration (p. 9):** one sentence,
"Console: Interface that controls all functions of the Air Bike. Contains Key controls and LCD Display." No
controller, no motor, no brake circuit.

**Block diagram (p. 23):** CONSOLE POWER "AA * 4 PCS Batteries" into the console; WIRELESS Heart Rate (POLAR) beside
it; RPM SENSOR below. The drawing also shows a BLUETOOTH (For App) box footnoted "Bluetooth function: Only the model
of Bluetooth device configuration" - the AIR650 is not that model.

**PCB Board Bottom (p. 26):** Battery connect, RPM Sensor connector and Wireless Heart rate receiver, with no
connector numbers; the Bluetooth position on the drawing is empty on this build. The PCB Board Top (p. 25) is an
unlabelled photograph.

**Circuit diagram (p. 28), "AU800-GA001 AIR BIKE CIRCUIT DIAGRAM":** a CONSOLE box, a **2pin SENSOR WIRE** and an
**RPM SENSOR (REED SWITCH)**. That is the entire schematic. On the AIR650 the sensor wire is the computer cable (23)
that rises above the fan through the console base to the console set (34).

So the only things the wiring can do wrong are a loose cable (23), flat cells, or the reed switch and its magnet gap;
the service manual's Q&A for a dead console is "check the four batteries are fully charged or installed", and its
no-speed check is the magnet gap under 3 mm (the errors section holds both). The AU800-GA001 code is the factory
drawing number, not an Xterra part number.


---
id: ab900-2018-specs-console-wiring-four-aa-batteries-and-2-pin-reed-switch-rpm-sensor
title: The whole electrical system is a console on four AA batteries with a two-pin
  reed-switch RPM sensor, a Polar receiver and, on one build, Bluetooth
kind: spec
question: How is the console of a Spirit ab900-2018 air bike wired, and what does
  the block diagram and circuit diagram show?
asked_as:
- ab900 wiring diagram
- what powers the ab900 console
- ab900 block diagram
- where does the rpm sensor plug in on the ab900 console
keywords:
- block diagram
- circuit diagram
- console power
- aa batteries
- 4 pcs
- bluetooth for app
- wireless heart rate polar
- rpm sensor
- reed switch
- 2 pin sensor wire
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
- cic850-2022-specs-wireless-speed-transmitter-block-and-circuit-diagram
- jb950-2022-specs-circuit-diagram-9-pin-console-cable-and-6-pin-key-cable
see_also:
- ab900-2018-specs-parts-electronic-parts-named
- ab900-2018-specs-outline-and-skeleton-part-names
- ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm
- ab900-2018-specs-parts-air650-discrepancy
source:
  ref: spirit-bike-ab900-2018-service-manual
  locator: Section 3 Electrical Configurations, PDF p. 9 (printed 9), text.md lines
    89-91; section 5 Unit Block Diagrams, PDF p. 23 (printed 23), lines 408-433; Display
    Board PCB Component Locations, PCB Board Bottom, PDF p. 26 (printed 26), lines
    446-470, photograph read from a 300 dpi render; Circuit Diagram 'AU800-GA001 AIR
    BIKE CIRCUIT DIAGRAM', PDF p. 28 (printed 28), lines 471-483, read from the render
    (OCR supplement lines 1118-1132, upside down)
  extracted_at: '2026-09-11'
---

**Electrical configuration (one sentence):** "Console: Interface that controls all functions of the
Air Bike. Contains Key controls and **LCD Display**." Nothing else - no controller, no motor, no
brake circuit, because the resistance is the fan.

**Block diagram (p. 23):** **CONSOLE POWER - AA x 4 PCS Batteries** into the console (spelt
COSNOLE on the drawing); **BLUETOOTH (For App)** and **WIRELESS Heart Rate (POLAR)** beside it;
**RPM SENSOR** below it. Footnote: "Bluetooth function: Only the model of Bluetooth device
configuration".

**PCB Board Bottom (p. 26)** names four things on the back of the display board: **Bluetooth**
(top right, with the same build-only footnote), **Battery connect**, **RPM Sensor connector** and
**Wireless Heart rate receiver**. No connector numbers are printed.

**Circuit diagram (p. 28), "AU800-GA001 AIR BIKE CIRCUIT DIAGRAM":** a CONSOLE box, a **2pin
SENSOR WIRE** and an **RPM SENSOR (REED SWITCH)**. That is the entire schematic - two wires.

So there is no adapter, no mains lead and no board below the console; four AA cells run
everything, and the only fault the wiring can have is the reed switch and its magnet gap
(`ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm`). The AU800-GA001 code on the
drawing is the factory drawing number for this book's machine, not a Spirit part number.


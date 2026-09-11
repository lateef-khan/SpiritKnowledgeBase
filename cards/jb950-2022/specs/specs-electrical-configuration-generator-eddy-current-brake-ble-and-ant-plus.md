---
id: jb950-2022-specs-electrical-configuration-generator-eddy-current-brake-ble-and-ant-plus
title: A generator-fed lower controller, an eddy-current brake set by a gear motor
  with a closed-loop encoder, and a console with LED display, BLE on two channels
  and ANT+
kind: fact
question: What does the electrical configuration page of the Spirit jb950-2022 service
  manual say the console, lower controller and brake consist of?
asked_as:
- how does the jb950 brake work
- does the jb950 have ant+
- what is the lower controller on the jb950
- jb950 eddy current brake
keywords:
- electrical configuration
- lower controller
- generator interface
- switching power supply
- brake motor control
- neodymium magnets
- eddy current
- gear motor
- closed-loop encoder
- led display
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: specs
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-cr900-cu900-2018-specs-electrical-configuration-generator-brake
see_also:
- jb950-2022-specs-parts-electronic-parts-named
- spirit-cycle-specs-resistance-systems
- jb950-2022-specs-lower-control-board-cs52003-connectors-and-pin-definitions
- jb950-2022-specs-brake-assembly-limit-sensor-board-cs63027-and-encoder-board-cs63029
- jb950-2022-errors-leds-not-bright-enough-30-v-at-30-rpm
- spirit-jb950-specs-twenty-motor-driven-resistance-levels
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: Section 3 Electrical Configurations, General Information, PDF p. 25 (printed
    25), text.md lines 344-362
  extracted_at: '2026-09-11'
---

Four paragraphs, the console described twice:

- **CONSOLE** - the interface that controls all functions of the indoor cycle; it "contains the
  **LED display**, computer IC (**MCU**), memory, control circuitry and communications module for
  **BLE (2 channels)** and **ANT+**".
- **LOWER CONTROLLER** - "consists of the **generator interface** and **switching power supply**
  for the console and **brake motor control circuitry**".
- **BRAKE** - "**Neodymium magnets** for creating **Eddy current** resistance, a **gear motor** to
  control resistance levels and **closed-loop feedback encoder** for precise brake position
  information to the console".

**So the bike is self-powered and the brake is positioned, not energised.** The generator on the
flywheel feeds the lower board, which makes the console's supply; resistance comes from how close
the motor has driven the magnet carrier to the flywheel, and the encoder reports where it is. No
coil voltage exists to measure - the only electrical figure the book gives for the drive is the
troubleshooting check that the generator should put out **30 V at 30 rpm** or be replaced
(`jb950-2022-errors-leds-not-bright-enough-30-v-at-30-rpm`).

The parts these paragraphs describe are photographed on the chapter-2 pages
(`jb950-2022-specs-parts-electronic-parts-named`); how the wiring runs between them is on the
board cards. The commercial CR900/CU900 use a generator too, but theirs *is* the brake
(`spirit-cr900-cu900-2018-specs-electrical-configuration-generator-brake`).


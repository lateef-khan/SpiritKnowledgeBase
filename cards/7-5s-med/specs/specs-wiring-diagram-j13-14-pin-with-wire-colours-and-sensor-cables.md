---
id: 7-5s-med-specs-wiring-diagram-j13-14-pin-with-wire-colours-and-sensor-cables
title: Wiring diagram with the console's 14-pin J13 defined by colour, from brown
  M- to red-with-black GND, and the power, hall sensor, IR sensor and brake motor
  plugs
kind: spec
question: What are the pins and wire colours of the console connector and the sensor
  and motor cables on a Spirit 7-5s-med recumbent stepper?
asked_as:
- 7.5s wiring diagram
- j13 pinout on the 7.5s console
- which wire is 12v on the spirit rehab stepper
- hall sensor and ir sensor plug pins 7.5s
keywords:
- wiring diagram
- j13
- 14 pin
- wire colours
- hall sensor
- ir sensor
- brake motor
- mpos
- sen1 sen2
- reflective encoder disc
facets:
  brand:
  - spirit
  product_line: climber
  model: 7-5s-med
  applies_to:
  - 7-5s-med
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
see_also:
- 7-5s-med-specs-service-manual-switching-power-supply-12-vdc-1-6-a
- 7-5s-med-specs-component-description-ten-numbered-parts
- spirit-climber-specs-parts-electronic-parts-named
source:
  ref: spirit-stepper-7-5s-med-service-manual
  locator: 8. Wiring Diagram, '7.5S Wiring Diagram', PDF p. 55 (printed 55), text.md
    line 873; the page is one 1350 x 873 pixel embedded image (pdfimages) whose pin
    tables the OCR supplement (1212-1247) cannot read, so every table was read from
    crops of the embedded image; cross-checked against the pin numbers quoted in 5.2.3
    Troubleshooting, PDF pp. 13-19, lines 125-201
  extracted_at: '2026-09-11'
---

The drawing shows the **Console** with two **Hand pulse** leads, its **J13** socket, and a bus down
to five plugs, each with a table for the cable end and the device end. The tables are printed
very small; the colours below were read from the embedded image and agree with the pin numbers
the troubleshooting chapter quotes.

**J13 - console, 14 pins**

| Pin | Colour | Signal | Level | Pin | Colour | Signal | Level |
|---|---|---|---|---|---|---|---|
| P1 | Brown | **M-** | waveform symbol | P8 | Gray | **SEN2** | square-wave symbol |
| P2 | Red | **M+** | waveform symbol | P9 | White | +5V | +5V |
| P3 | Orange | +5V | +5V | P10 | Light Blue | **VIN** | **12V** |
| P4 | Yellow | **MPOS(VR)** | ramp symbol | P11 | Pink | GND | 0 |
| P5 | Green | GND | 0 | P12 | Light Green | +5V | +5V |
| P6 | Blue | **SEN1** | square-wave symbol | P13 | Brown with Black | **SEN** | square-wave symbol |
| P7 | Purple | GND | 0 | P14 | Red with Black | GND | 0 |

(The Level column prints small waveform glyphs for the signal lines; they are described, not
transcribed.)

The troubleshooting chapter uses exactly these: "pin 10 and pin 11 of the 14 pin cable" for
12 V DC, "pin 1 and pin 2" for the motor armature (**about 2~3 ohm**), "pin 3 and pin 5" for the
motor position sensor (**about 5k ohm**).

**The four branch cables** (cable side / device side)

| Cable | Pins on the cable | Pins at the device |
|---|---|---|
| **Power** | P1 Light Blue VIN 12V, P2 Pink GND 0 | P1 Red VIN 12V, P2 Black GND 0 |
| **Hall sensor** (IR Sensor Board, one-sensor version, **Brake RPM**) | P1 Light Green +5V, P2 Brown with Black SEN, P3 Red with Black GND | P1 White +5V, P2 Red SEN, P3 Black GND |
| **IR sensors** (IR Reflective Sensor Board, reads the **Reflective Encoder Disc**) | P1 Blue SEN1, P2 Purple GND, P3 Gray SEN2, P4 White +5V | the same four |
| **Brake Motor** | P1 Brown M-, P2 Red M+, P3 Orange +5V, P4 Yellow MPOS(VR), P5 Green GND | **cut off by the page edge** - only P1-P5 survive |

So the console's 14 lines are the four cables laid end to end: motor 1-5, IR reflective 6-9, power
10-11, hall/RPM 12-14. The brake motor's plug is M- on pin 1, the stepper convention.

The power block is drawn as a **Switching Power Supply, 90 ~ 260 VAC input, 12 VDC output, 1.6A**
- a figure that disagrees with the owner's manual
(`7-5s-med-specs-service-manual-switching-power-supply-12-vdc-1-6-a`). The two red sensor boards
are photographed in chapter 2 (`spirit-climber-specs-parts-electronic-parts-named`).


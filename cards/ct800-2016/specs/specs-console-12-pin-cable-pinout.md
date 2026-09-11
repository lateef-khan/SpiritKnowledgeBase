---
id: ct800-2016-specs-console-12-pin-cable-pinout
title: 'The 12-pin console cable: wire colours from the circuit diagram and the two
  pin tables that do not agree'
kind: spec
question: What is the 12-pin console cable pinout on a Spirit ct800-2016 treadmill,
  and what colour is each wire?
asked_as:
- what are the 12 pins on the ct800 console cable
- wire colours of the treadmill computer cable
- which pin is the safety switch on the 2016 ct800
- system cable pinout
keywords:
- 12 pin
- console cable
- system cable
- computer cable
- pinout
- wire colour
- pin definition
- vr in
- speed sensor input
- controller
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: specs
  code: '*'
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- ct850-2016-console-12-pin-connector-pinout
see_also:
- ct800-2016-specs-circuit-diagram
- ct800-2016-specs-display-board-connectors-and-pinouts
- ct800-2016-specs-driver-board-connectors-and-leds
- ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12
- spirit-ct800-2016-xt-2007-assembly-replacing-wire-harness
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: 'Wire colours: PDF p. 4 (printed 3) circuit diagram, read from the render.
    Pin tables: PDF p. 44 (printed 43) ''Pin definition'', JK13, text.md lines 758-764,
    and PDF p. 46 (printed 45) ''Pin definition'', JK1 (CONNECTION TO CONSOLE), lines
    828-839. Pins 10-12 wire colours: PDF p. 54 (printed 53), lines 1063-1066'
  extracted_at: '2026-09-11'
---

The console cable is a **12-pin** cable. It lands on **JK13** ("SYSTEM CABLE (12 PINS)") on the bottom of
the display board and on **JK1** ("CONNECTION TO CONSOLE") on the driver board. The book prints the same
signal list for both ends.

**Pin table as printed on pp. 44 and 46 (JK13 and JK1 are identical):**

| Pin | Signal | Pin | Signal | Pin | Signal |
|---|---|---|---|---|---|
| P1 | Controller S/W | P5 | Speed up output | P9 | Speed sensor input |
| P2 | UP | P6 | Speed down output | P10 | +VCC |
| P3 | DOWN | P7 | GND | P11 | VR IN |
| P4 | Vin | P8 | GND | P12 | GND |

**Wire colours as printed on the circuit diagram (p. 4):**

| Pin | Colour | Label | Pin | Colour | Label | Pin | Colour | Label |
|---|---|---|---|---|---|---|---|---|
| 1 | Black | S/W | 5 | Yellow | FAST | 9 | Gray | SPD |
| 2 | Brown | DOWN | 6 | Green | SLOW | 10 | White | VR1 |
| 3 | Red | UP | 7 | Blue | GND | 11 | Light blue | VR2 |
| 4 | Orange | VCC | 8 | Purple | SPD | 12 | Pink | VR3 |

**The two lists disagree, inside one book.** The pin tables put UP on P2 and DOWN on P3; the circuit
diagram puts DOWN on pin 2 (brown) and UP on pin 3 (red). The tables give P8 as GND and P9 as the speed
sensor input; the diagram labels both 8 and 9 "SPD". Nothing in the manual reconciles them. Meter the
wire before you trust either.

The incline-calibration text on p. 54 does agree with the diagram's colours for the last three pins: **Pin
10 = white wire, 5vdc; Pin 11 = light blue wire, position signal 0~5vdc; Pin 12 = pink wire, ground**,
and says these connections "are the same on the incline board and at the console". Its p. 46 counterpart
gives the same three pins without colours.

The CT850-2016 has a 12-pin console cable too, with different signals and colours on every pin - see
`ct850-2016-console-12-pin-connector-pinout`. The CT800-2020 replaces this cable with a 6-pin one.

---
id: jb950-2022-specs-lower-control-board-cs52003-connectors-and-pin-definitions
title: 'The CS52003 lower control board: generator power in, nine-pin system cable,
  RPM sensor, eight-pin level-control brake cable and a 9 V external power input'
kind: spec
question: What plugs into the lower control board of a Spirit jb950-2022 indoor cycle,
  and what is on each pin?
asked_as:
- jb950 lower board connectors
- cs52003 pinout
- which pin is home on the jb950 brake cable
- where does the 9v adapter plug in on the jb950
keywords:
- lower control board
- cs52003
- controller
- pin definition
- j1 generator power in
- j2 system cable
- j3 speed rpm sensor
- j4 level control brake cable
- j5 power 9 vin
- external power 9 v dc
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
- spirit-cr900-cu900-2018-specs-driver-board-blcb002a-connections
- xbr95-2023-specs-generator-controller-cs52005-33-connections
see_also:
- jb950-2022-specs-mcu-board-connectors-j1-to-j5-pin-definitions
- jb950-2022-specs-brake-assembly-limit-sensor-board-cs63027-and-encoder-board-cs63029
- jb950-2022-specs-circuit-diagram-9-pin-console-cable-and-6-pin-key-cable
- jb950-2022-console-power-and-wake-sequence
- jb950-2022-errors-no-resistance-control-board-wiring-then-brake-test
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 4.3 Lower Control Board Wire Connections / Function, PDF p. 31 (printed
    31), text.md lines 434-459, photograph read from a 300 dpi render (board silkscreen
    CS52003 Rev 1.0); Lower Control Board PIN Definition, PDF p. 32, lines 461-487
  extracted_at: '2026-09-11'
---

The board under the chain cover, silkscreened **CS52003 Rev 1.0** and labelled CONTROLLER CS52003
on the circuit diagram:

| Connector | Lead | Pins |
|---|---|---|
| **J1** | GENERATOR POWER IN | 1 **VIN**, 2 GND |
| **J2** | SYSTEM CABLE (9 PIN) to console | 1 GND, 2 **VDD**, 3 **MTR UP**, 4 **MTR DN**, 5 **CHR**, 6 **OPT1**, 7 **OPT2**, 8 **RPM**, 9 **CNT** |
| **J3** | SPEED RPM SENSOR | 1 **RPM**, 2 GND |
| **J4** | Level control brake CABLE (motor, encoder, position sensors) | 1 **MTR UP**, 2 **MTR DN**, 3 **HOME**, 4 **OPT1**, 5 GND, 6 **VCC_5V**, 7 **VCC_6V**, 8 **MCT_IN** |
| **J5** | POWER 9 VIN - "External Power 9 V DC" | 1 **VCC_9V**, 2 GND |

**Two power inputs.** J1 is the two-wire generator lead - the generator is drawn with a single
lead to J1 on the circuit diagram, so its rectifier is on the generator, not on this board. J5 is
where the **optional 9 V DC adapter** plugs in to light the console without pedalling (the
console card `jb950-2022-console-power-and-wake-sequence` covers when to use it); no rating
beyond "9 V DC" is printed and the adapter is not pictured.

**The brake cable carries eight wires**, and the names say what the limit-sensor board on the
brake does with them: MTR UP / MTR DN drive the DC motor, HOME is the home-position sensor, OPT1
and MCT_IN are the encoder signals, and the board gets both a 5 V and a 6 V rail. The system
cable's OPT1 / OPT2 / CNT pins pass the same encoder information on to the console.

The J2 list is printed identically on the console's MCU board page, where pin 2 reads
*VDD +6v* (`jb950-2022-specs-mcu-board-connectors-j1-to-j5-pin-definitions`).


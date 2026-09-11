---
id: spirit-crs800s-cs800-2021-specs-unit-block-diagram
title: Unit block diagram with a cooling fan, USB charge and Bluetooth on the display
  board; the recumbent adds an F/R sensor, the upright draws an AC adapter
kind: spec
question: What does the unit block diagram of the Spirit CRS800S or CS800 (2020 version)
  stepper service manual show?
asked_as:
- block diagram of the crs800s
- cs800 2020 stepper configuration diagram
- what is the f/r sensor on the crs800s
- what connects to the display board on the spirit stepper
keywords:
- block diagram
- stepper configuration
- display board
- cooling fan
- usb charge
- bluetooth
- rpm sensor
- f/r sensor
- tension motor
- ac adapter
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - cs800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2016-specs-unit-block-diagram-climber-configuration
- spirit-xs895-specs-unit-block-diagram-display-board-driver-board-amplifier-and-fuse
see_also:
- spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections
- crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board
- cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 'CRS800S: 5. Unit Block Diagrams, ''Stepper Configuration'', PDF p. 16
    (printed 16), text.md lines 231-236, a flattened image read from a 110 dpi render
    (OCR supplement 742-762). CS800(2020): PDF p. 18 (printed 17), line 306 (supplement
    1099-1115), read the same way'
  extracted_at: '2026-09-11'
---

**Nearly the same drawing in the two books; two blocks differ.** No driver board is drawn - the
display board does everything.

| Block | Direction | CRS800S | CS800 (2020) |
|---|---|---|---|
| HR HANDLEBAR | into the display board | yes | yes |
| KEY | into | yes | yes |
| WIRELESS HR | into | yes | yes |
| COOLING FAN | out | yes | yes |
| USB CHARGE | out | yes | yes |
| RPM SENOR [sic] | into | yes | yes |
| **F/R SENOR** [sic] | into | **yes** | **no** |
| BLUETOOTH | into | yes | yes |
| TENSION MOTOR | out | yes | yes |
| POWER -> POWER SWITCH -> | into | POWER SWITCH feeds the display board directly | POWER SWITCH -> **AC Adapter** -> display board |

**The F/R sensor** is the recumbent's forward/reverse step sensor - the photo-coupler board the
CRS800S circuit diagram and its speed troubleshooting call the *Optical Sensor Board* on the cable
drive pulley. The upright CS800 has only the RPM sensor.

**The AC adapter block** is the CS800's own drawing of what its circuit diagram shows: an
appliance inlet with a switch and fuse feeding an internal adapter. The CRS800S draws its adapter
on the circuit diagram too but leaves it off the block diagram - both machines run from an
adapter; the CRS800S's is external
(`crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board`,
`cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse`).

The 2016 CS800 book prints the older, plainer diagram with no fan, USB or Bluetooth
(`cs800-2016-specs-unit-block-diagram-climber-configuration`).


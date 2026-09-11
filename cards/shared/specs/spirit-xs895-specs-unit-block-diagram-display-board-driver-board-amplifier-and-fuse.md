---
id: spirit-xs895-specs-unit-block-diagram-display-board-driver-board-amplifier-and-fuse
title: Unit block diagram with a display board over a driver board, mains through
  a fuse, an amplifier with line-in and speakers, and an incline motor with a VR set
kind: spec
question: What does the unit block diagram of the Spirit XS895 incline stepper service
  manual show?
asked_as:
- block diagram of the xs895
- does the xs895 have a driver board
- where is the fuse on the xs895 block diagram
- what is vr set on the xs895
keywords:
- block diagram
- display board
- driver board
- fuse
- amplifier
- line in
- speaker
- incline motor
- vr set
- thumb switch
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-crs800s-cs800-2021-specs-unit-block-diagram
- cs800-2016-specs-unit-block-diagram-climber-configuration
see_also:
- spirit-xs895-specs-display-board-aa0175-interface-board-and-amplifier-yj-8509-connections
- spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor
- spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 5. Unit Block Diagrams, PDF p. 17 (printed 16), text.md line 287, a flattened
    image read from a 110 dpi render (OCR supplement 1204-1227)
  extracted_at: '2026-09-11'
---

**The only stepper in this family drawn with a separate driver board.** Two large blocks joined by a
double-headed arrow.

**Around the DISPLAY BOARD:** KEY (in), COOLING FAN (out), HR HANDLEBAR (in), WIRELESS HR RECEIVER
(in), THUMB SWITCH (in), and an **AMPLIFIER** fed by the display board and by a **LINE IN**, driving
**SPEAKER L/R**.

**Around the DRIVER BOARD:** POWER -> POWER SWITCH -> **FUSE** -> DRIVER BOARD; RPM SENSOR (in);
TENSION MOTOR (out); INCLINE MOTOR (out); **VR SET** (in) - the incline position potentiometer.

**What it tells a technician.** The console is not the controller here: the fuse, the motor
drivers and the incline drive all live on the lower board, which the circuit diagram calls the
CONTROLLER and feeds from an appliance inlet with ACN/ACL leads
(`spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor`). The E2 test
tells you to check "power socket the holder FUSE" and the drive board's POWER LED before
condemning anything. The console's own sockets, the interface board and the YJ-8509 amplifier are
on `spirit-xs895-specs-display-board-aa0175-interface-board-and-amplifier-yj-8509-connections`.

The CS800 and CRS800S have no driver board, no fuse and no amplifier on their diagrams
(`spirit-crs800s-cs800-2021-specs-unit-block-diagram`).


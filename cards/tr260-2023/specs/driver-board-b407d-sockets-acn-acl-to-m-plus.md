---
id: tr260-2023-specs-driver-board-b407d-sockets-acn-acl-to-m-plus
title: 'The nine numbered driver-board sockets: ACN and ACL for 120 or 230 VAC in,
  incline power white, red and black, the console connection, speed sensor, M- to
  the black motor wire and M+ to the red'
kind: spec
question: Which wire goes to which socket on the driver board (motor controller) of
  an Xterra tr260-2023 treadmill, and what board is it?
asked_as:
- tr260 controller board connections
- tr260 incline motor wires on the controller
- tr260 driver board model number
- which terminal is acn on the tr260
keywords:
- driver board
- motor controller
- sockets
- wire connections
- acn
- acl
- incline power
- m plus
- m minus
- b407d
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-driver-board-b426d-wire-connections
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
see_also:
- tr260-2023-specs-driver-board-led-location-a-single-speed-led
- tr260-2023-specs-display-board-a3404-connections
- tr260-2023-specs-circuit-diagram-with-a-filter-and-a-relay-pwm-vdd-rpm-gnd-pin-define
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM (GT75A-NT050) 'Driver Board Function', PDF p. 25 (printed 25),
    lines 349-371 - the numbered socket table; 'Driver Board Wire Connections' PDF
    p. 21 (printed 21), lines 313-319, OCR supplement lines 1321-1392 - the captioned
    drawing; 'Driver Board PCB Component Locations' PDF p. 22, lines 319-325, uncaptioned.
    Board markings read from the 110 dpi renders
  extracted_at: '2026-09-11'
---

The book gives this board twice: a captioned silkscreen drawing headed "Driver Board Wire Connections", and a
photograph with nine red numbers headed "Driver Board Function" beside this table:

| No. | Socket Description |
|---|---|
| 1 | ACN 120 or 230 VAC IN |
| 2 | ACL 120 or 230 VAC IN |
| 3 | Incline Power WHITE |
| 4 | Incline Power RED |
| 5 | Incline Power BLACK |
| 6 | Connection to Console |
| 7 | Speed Sensor |
| 8 | M- TO DC MOTOR (BLACK WIRE) |
| 9 | M+ TO DC MOTOR (RED WIRE) |

The drawing's captions say the same in words: AC POWER INPUT (110V or 220v) on **ACN** and **ACL**; "This area is
Incline power output socket, respectively: **Com** ... connected with white incline power wires; **UP** ... red;
**DOWN** ... black"; **M-** connected with the black wire of the motor and **M+** with the red; an **Incline VR
socket** (silkscreen INC) for the 3-pin VR wires; a **Speed sensor socket** (silkscreen SP) for the 2-pin sensor
wires; and the **MAIN control wires socket** for the 5-pin control wires. The incline VR socket is the one
connection the numbered table leaves out.

**Board identity.** The drawing is titled **MODEL: B407DV20**, ShangHai EWay Electronics Co., LTD., with a fuse drawn
as **1.6A 250V** and tick boxes 110V / 220V. The photographs on the function and LED pages show a board silkscreened
**MODEL: B407DV12** with a 110V sticker, a SONGLE SLA-12VDC-SL-A relay, a SONGLE SRD-12VDC-SL-C relay and a
PEE25-030 transformer - a different revision from the drawing. The book does not remark on the difference.

---
id: xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
title: 'The circuit diagram of the folding TRX family: a 120 V sheet and a 220 V sheet
  with a choke, handrail keys on 3+2-pin black cables, 5-pin upper, middle and lower
  main control wires, and an incline motor on down, up and com'
kind: spec
question: What does the circuit diagram in the Xterra TRX treadmill service manual
  show, and what differs between the 120 V and 220 V sheets?
asked_as:
- trx3500 wiring diagram
- trx5500 circuit diagram
- trx2500 handrail key cable pins
- trx4500 220 volt wiring
keywords:
- circuit diagram
- wiring diagram
- main control wires
- handrail keys
- hand pulse
- incline motor
- breaker
- choke
- controller
- 120 v
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
- tr260-2023-specs-circuit-diagram-with-a-filter-and-a-relay-pwm-vdd-rpm-gnd-pin-define
see_also:
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
- trx5500-2024-specs-driver-board-wire-connections-120-vac-in
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: 'TRX3500/TRX4500 SM ''8.9 Circuit diagram'': PDF p. 63 (printed 62) ''GT90C-NT023
    120V'', lines 1077-1083, OCR supplement lines 2280-2289; p. 64 ''GT90C-NT023 CEGS
    220V'', OCR supplement lines 2290-2309; p. 65 ''GT90D-NT024 120V'', OCR supplement
    lines 2310-2339; p. 66 ''GT90D-NT024 CEGS 220V'', OCR supplement lines 2340-2347.
    TRX2500 SM PDF p. 57 (printed 56) ''GT90B-NT022 120V'', lines 1036-1042, OCR supplement
    lines 2329-2380, and p. 58 ''GT90B-NT022 220V'', OCR supplement lines 2381-2453.
    TRX5500 SM ''8. Circuit Diagram'' PDF p. 70 (printed 69) ''GT90D-NT041 120V'',
    lines 1040-1046, and p. 71 ''GT90D-NT041 230V'', lines 1046-1052. The 120 V sheets
    of the TRX2500, TRX3500 and TRX5500 books read from 150-160 dpi renders'
  extracted_at: '2026-09-11'
---

Four books, one drawing. Each prints a **120V** sheet and a **220V** (TRX5500: **230V**) sheet titled with its Dyaco
code - GT90B-NT022 (TRX2500), GT90C-NT023 (TRX3500), GT90D-NT024 (TRX4500), GT90D-NT041 (TRX5500) - and the
TRX5500 sheet draws its touch-screen console in place of the LCD one. Everything else is the same.

**Mains path.** AC POWER INPUT PLUG → Power cable → Connector → AC SOCKET; the green wire (green with yellow) to a
ground lug captioned "CARD". **WHITE WIRE** and **BLACK WIRE** to the AC SWITCH; the black wire through the
**BREAKER**; both into the CONTROLLER's **AC1** and **AC2**.

**Controller outputs.** **M+** ← motor RED WIRE, **M-** ← motor BLACK WIRE, motor GROUND WIRE. One **JK** takes the
**2-PIN SENSOR WIRE**; the other takes the **5-PIN LOWER MAIN CONTROL WIRES**, which join the **5-PIN MIDDLE** and
**5-PIN UPPER MAIN CONTROL WIRES** up to the console. The three incline terminals **DOWN**, **UP** and **COM** take the
INCLINE MOTOR's **BLACK**, **RED** and **WHITE** wires; a **3-PIN INCLINE COMPUTER CABLE** returns from the position
sensor; the incline motor has its own GROUND WIRE.

**Console side.** Each handlebar grip is captioned "Incline Handrail keys & Hand pulse" and carries a **3+2 PIN
CABLE BLACK** - three pins for the rocker (UP/DOWN on the left grip, FAST/SLOW on the right) and two for the pulse
plates. The right grip is captioned "Incline" like the left although it is drawn with FAST and SLOW; the driver
board and display board cards name it the speed handrail.

**5-PIN MAIN CONTROL WIRES DEFINITION**: 1 S/W, 2 VDD, 3 TXD, 4 RXD, 5 GND (see the 5-pin card).

**220 V / 230 V sheet.** The same drawing with a **CHOCK** (choke) and filter in the mains path before the
controller. The US machines are the 120 V build.

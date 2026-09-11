---
id: xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
title: 'The incline position sensor wires: red is ground, white the position signal,
  black is 5 V DC, reading 0 to 5 V with the incline; power wires red up, black down,
  white common'
kind: spec
question: What are the wire colours and voltages of the incline motor position sensor
  (VR) cable and the incline power wires on an Xterra treadmill with a Dyaco service
  manual?
asked_as:
- incline sensor wire colours xterra
- which incline wire is 5 volts
- trx3500 incline vr cable
- incline motor red black white wires
keywords:
- incline position sensor
- vr
- potentiometer
- wire colours
- 5 volts
- position signal
- incline power
- up
- down
- com
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr260-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx1400-2023-specs-incline-position-sensor-pin-1-is-5-volts
- spirit-xt-specs-incline-sensor-pinout-pin-1-ground
- spirit-xt-2015-specs-incline-sensor-pinout-pin-1-5v
see_also:
- xterra-trx-specs-electrical-configuration-printed-for-230-vac-with-a-220-volt-incline-motor
- xterra-treadmill-specs-electrical-configuration-0-to-90-volt-at-120-vac-or-0-to-180-volt-at-230-vac
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: TRX3500/TRX4500 SM 'Test Configuration. Incline motor control functions
    relate parts location', PDF p. 54 (printed 53), lines 860-887; TRX2500 SM PDF
    p. 49 (printed 48), lines 815-846; TRX5500 SM PDF p. 48 (printed 47), lines 711-743;
    TR260 SM PDF p. 41, lines 604-639. All four print the same photograph with the
    same six labels
  extracted_at: '2026-09-11'
---

**This is the colour-coded table of the TR260, TRX2500, TRX3500, TRX4500 and TRX5500 books.** The TRX1400 book
prints pin numbers instead, and the Spirit XT books print the opposite colours; both have their own cards.

The four books print one photograph of the incline motor and controller with these labels:

| Label | Meaning |
|---|---|
| The position sensor wires: **Red = Ground** | ground |
| **White = Position signal** | the wiper, 0~5 V depending on incline position |
| **Black = 5vdc** | the sensor supply |
| **INCLINE POWER COM (WHITE)** | neutral / common |
| **INCLINE POWER DOWN (BLACK)** | AC on this wire lowers the incline |
| **INCLINE POWER UP (RED)** | AC on this wire raises the incline |

The same photograph carries the 5-pin main-control socket labelled 1. SW 2. +12V 3. TXD 4. RXD 5. GND (see the
5-pin card). The ER / E3 troubleshooting that follows this picture - reconnecting the VR wires, testing whether the VR
voltage varies at the incline wire terminal - is on the errors section's cards.

**The colours are the reverse of most Spirit XT books**, which print Black = Ground and Red = 5vdc
(`spirit-xt-specs-incline-sensor-pinout-pin-1-ground`). A replacement sensor cable may be either; identify ground,
wiper and 5 V with a meter, not by colour.

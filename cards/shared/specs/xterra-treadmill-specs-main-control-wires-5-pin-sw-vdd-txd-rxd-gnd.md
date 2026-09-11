---
id: xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
title: 'The 5-pin main control wires between console and controller: SW, VDD or +12V,
  TXD, RXD, GND, and one book that prints a different list'
kind: spec
question: What is the pin definition of the 5-pin main control wires (computer cable)
  between the console and the controller on an Xterra treadmill with a Dyaco service
  manual?
asked_as:
- 5 pin computer cable pinout xterra
- which pin is txd on the treadmill console cable
- main control wires pin define
- what is the sw pin on the 5 pin cable
keywords:
- 5-pin
- main control wires
- computer cable
- pin definition
- pinout
- sw
- vdd
- txd
- rxd
- gnd
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr260-2023
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2019-main-control-cable-pinout
- spirit-xt-specs-console-cable-6-pin-pinout
see_also:
- spirit-xt-ent-specs-console-cable-5-pin-pinout
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
- tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
- trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
- tr260-2023-specs-circuit-diagram-with-a-filter-and-a-relay-pwm-vdd-rpm-gnd-pin-define
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM circuit diagram PDF p. 57, OCR supplement lines 2329-2380, and
    ER test page PDF p. 49, lines 815-846. TRX3500/TRX4500 SM PDF p. 63-65 (OCR supplement
    lines 2310-2339) and p. 54, lines 860-887. TRX5500 SM PDF p. 70 and p. 48, lines
    711-743. TRX1400 SM PDF p. 58 (OCR supplement lines 2417-2461) and the pin-define
    page PDF p. 48, lines 782-797. TR150 SM PDF p. 46-47 (OCR supplement lines 1301-1328).
    TR260 SM PDF p. 46 (OCR supplement lines 2020-2056, read from the render) against
    PDF p. 41, lines 604-639. The TRX1400 driver-board drawing, PDF p. 29, silkscreens
    the socket SW VDD TXD RXD GND
  extracted_at: '2026-09-11'
---

**This is the 5-pin console-to-controller cable.** The Spirit XT and Sole F-series non-ENT machines use a 6-pin
cable with a different order; do not carry it across.

Every Dyaco-built Xterra service manual in this wave draws the cable's pin list on its circuit diagram:

| Pin | Circuit diagrams (TR150, TRX1400, TRX2500, TRX3500, TRX4500, TRX5500) | ER/E3 test pages (TR260, TRX2500, TRX3500/4500, TRX5500) | TRX1400 pin-define page |
|---|---|---|---|
| 1 | S/W | SW | SW |
| 2 | VDD | **+12V** | VDD |
| 3 | TXD | TXD | TXD |
| 4 | RXD | RXD | RXD |
| 5 | GND | GND | GND |

VDD and +12V are the same line - the console supply. SW is the safety-switch loop: the E0 page of the TR150 and
TRX1400 books says the lower controller "sent (+12V) signal via S/W of main control wires to upper control board to
form a safety switch loop". TXD and RXD carry the speed signal and the console-to-controller traffic. The TRX1400
driver-board drawing prints the socket silkscreen in this order: SW VDD TXD RXD GND. The cable runs in three lengths
on the TRX books - UPPER, MIDDLE and LOWER MAIN CONTROL WIRES - and in two on the TR150 and TRX1400 (MIDDLE and LOWER).

**The TR260 book contradicts itself.** Its circuit diagram prints the pin define as **1 RELAY, 2 PWM, 3 VDD, 4 RPM, 5
GND**, while its E3 test page (p. 41) prints "1. SW 2.+12V 3.TXD 4.RXD 5.GND" like every other book. Nothing in the
book reconciles the two; on a TR260 identify the lines with a meter before relying on either list.

No wire colours are printed for this cable in any book. The Spirit XT485ENT/XT685ENT sheets print the same five
signals in the same order (`spirit-xt-ent-specs-console-cable-5-pin-pinout`).

---
id: ct800-2016-specs-driver-board-connectors-and-leds
title: Driver board connectors, pin definitions and the eight indicator LED positions
  on the 2016 lower controller
kind: spec
question: Where are the connectors and the indicator LEDs on the driver board of a
  Spirit ct800-2016 treadmill, and what are the pin definitions?
asked_as:
- ct800 2016 lower controller connectors
- which plug is the incline vr on the ct800 driver board
- where is the pwm led on the treadmill controller
- dc motor m plus m minus wires
keywords:
- driver board
- lower controller
- controller
- connector
- pin definition
- led
- incline vr
- incline power
- reed switch
- transformer
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
- ct850-2016-inverter-board-connector-locations
- ct850-2016-inverter-board-connector-pinouts
see_also:
- ct800-2016-specs-console-12-pin-cable-pinout
- ct800-2016-specs-circuit-diagram
- spirit-ct800-specs-driver-board-connector-locations
- ct800-2016-errors-controller-led-debugging-90-to-110-v
- ct800-2016-assembly-replacing-drive-motor
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: PDF p. 25 (printed 24) '6.3 DRIVER BOARD PCB Component Locations', text.md
    lines 415-444; PDF p. 26 (printed 25) '6.4 DRIVER BOARD LED Indicator Locations',
    lines 445-473; PDF p. 45 (printed 44) with pin numbering, lines 798-825; pin definitions
    PDF p. 46 (printed 45), lines 828-859. Board marking and fuse rating read from
    the render
  extracted_at: '2026-09-11'
---

The lower controller is the **YJ-2350L** control board (sticker A512-090908001); the same board is drawn
on the circuit diagram. A **3.15A/250V** fuse sits beside the AC IN terminals and the electrolytic
capacitor is marked 110VAC. Section 6.3 calls out:

| Call-out | What it is | Pin numbering as drawn on p. 45 |
|---|---|---|
| AC IN | mains in, two terminals | - |
| DC MOTOR M+ / DC MOTOR M- | drive motor | - |
| INCLINE DOWN / INCLINE COM / INCLINE UP | incline motor power, three terminals | JK2, P3-P1 |
| TO AC FAN | heat-sink fans | - |
| TRANSFORMER | JK5 / JK6 / JK7 | - |
| INCLINE VR | JK4, 3-pin position sensor | - |
| REED SWITCH SENSOR | speed sensor | - |
| CONNECTION TO CONSOLE | JK1, 12-pin | P12-P1 |

**Pin definitions (p. 46).** JK1 carries the same twelve signals as JK13 on the display board (see the
console-cable card). **JK4 (INCLINE VR)**: P1 +VCC, P2 VR IN, P3 GND. **JK2 (INCLINE POWER)**: BLACK WIRE
= DOWN, WHITE WIRE = COM, RED WIRE = UP. **DC MOTOR (MOTOR POWER)**: WHITE WIRE = M-, RED WIRE = M+.

**LED positions (p. 26).** Eight LEDs are ringed on the photograph: **MOT_DRV** and **SHUT_DOWN** near the
top right edge, **LIMI** and **RPM SENSOR** below them, **PWM** and **POWER** in the middle, and **INC_UP**
and **INC_DW** at the bottom left beside the incline connectors. What each LED means when it lights is on
the LED-debugging cards, not here.

The 2020 CT800 uses a different board, the AE00301L-002, with a 6-pin console socket; the CT850-2016 uses
an RM6T3 inverter with no transformer at all.

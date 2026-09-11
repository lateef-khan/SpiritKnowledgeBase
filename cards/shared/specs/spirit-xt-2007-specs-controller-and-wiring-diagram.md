---
id: spirit-xt-2007-specs-controller-and-wiring-diagram
title: 'The dealer manual''s controller diagram: ten numbered connections, a torque
  boost dial and six LEDs, plus a pictorial wiring sheet'
kind: spec
question: What does the controller diagram in the Spirit XT175 / XT275 / XT375 / XT475
  / XT675 dealer service manual show, and what is on each connection?
asked_as:
- controller connections on the old xt treadmill
- which wire goes to ac1 on the xt controller
- where is the torque boost on the xt475 controller
- transformer wires jk5 jk6 jk7
keywords:
- controller diagram
- wiring diagram
- controller
- transformer
- torque boost
- led
- incline motor
- speed sensor
- wire harness
- xt series
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt175-2007
  - xt275-2007
  - xt375-2007
  - xt475-2007
  - xt675-2007
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
- ct800-2016-specs-driver-board-connectors-and-leds
see_also:
- spirit-xt-2007-maintenance-adjusting-torque-boost
- spirit-ct800-2016-xt-2007-assembly-replacing-controller
- spirit-ct800-2016-xt-2007-assembly-replacing-wire-harness
- spirit-xt175-errors-checking-wire-harness-continuity
- spirit-xt175-errors-ls-error-no-belt-movement-pwm-led
source:
  ref: spirit-treadmill-xt175-xt275-xt375-xt475-xt675-2007-service-manual
  locator: PDF p. 8 (printed 8), PROCEDURE 11 Controller diagram, text.md lines 274-344;
    PDF p. 9, PROCEDURE 12 Wiring diagram, lines 345-350, a faint pictorial read from
    the render
  extracted_at: '2026-09-11'
---

**Controller diagram (Procedure 11).** One controller board drawn with ten numbered call-outs and a key:

| # | Connection | As printed |
|---|---|---|
| 1 | AC1 | White wire from power switch |
| 2 | AC2 | Black wire from power switch |
| 3 | Incline motor connection | Down - black wire to inc mtr; Com - white wire to inc mtr; Up - red wire to inc mtr |
| 4 | Transformer connections | JK5 - Black, Black; JK6 - Blue, Blue; JK7 - Red, Red |
| 5 | Incline potentiometer (VR) | - |
| 6 | Lower wiring harness connection | drawn as JK1 |
| 7 | Speed sensor connection | drawn as JK2 |
| 8 | Torque boost adjustment | "Adjust at lower speeds to eliminate motor surging" |
| 9 | Motor connection M- | Black motor wire |
| 10 | Motor connection M+ | Red motor wire |

The drawing also shows a **FUSE** beside AC1 / AC2 and six indicator LEDs labelled **SHUT DOWN**, **MOT
DRV**, **POWER**, **LIMIT**, **PWM** and **TORQUE**. The book prints no pin table for the harness and no
LED-debugging table; the LEDs' meanings are on the errors cards for this family.

**Wiring diagram (Procedure 12).** A pictorial sheet signed "XT Series": the console with its display
board, two speakers, a pulse-grip board, the stop-key switch and the two handrail switch pods ("To Spd
Switch", "To Inc Switch"), an upright harness down to the controller, the motor, the incline motor, the
speed sensor, and the power switch, circuit breaker and A.C. plug wired black / white. It carries no part
numbers, pin numbers or wire lengths.

The 2015 and later XT service manuals draw a different board (JK80 / JK60 / JK90 / JK50) and print a
proper schematic; do not carry the JK numbers here across to them.

---
id: ct850-2020-driver-board-connector-locations
title: Driver board connectors on the lower controller
kind: spec
question: Where are the connectors on the driver board (inverter) of a Spirit CT850-2020
  or CT850ENT treadmill?
asked_as:
- ct850 2020 lower controller connectors
- where does the console plug into the driver board
- which terminal is ac in on the ct850 driver
- incline vr plug on the lower board
keywords:
- driver board
- lower controller
- inverter
- connector
- incline ac
- incline vr
- esp
- console
- ac motor
- rhymebus
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct850-2020
  - ct850ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-specs-driver-board-connector-locations
- 40t-2026-specs-rear-incline-interface-board-and-inverter-connectors
see_also:
- ct850-2020-treadmill-circuit-diagram
- ct850ent-2022-specs-circuit-diagram
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: p. 29 (printed 28), section 6-1-5 'DRIVER BOARD PCB Component Locations(YT058)'.
    The CT850ENT-2022 service manual prints the same photograph as 'Inverter Component
    Locations' at PDF p. 18 (printed 18), text.md lines 307-333
  extracted_at: '2026-09-08'
---

Read from the 300 dpi render; the page is a flattened image. The driver is a boxed unit with a
**RHYMEBUS** logo on its cover.

**Left-hand edge**, top to bottom: **INCLINE AC**, **INCLINE VR**, **ESP**, **CONSOLE**. The board
silkscreen beside them reads INCLINE, VR, SB, ESP, CONSOLE.

**Right-hand edge**: **AC IN** with terminals **N** and **L**, and **AC MOTOR** with terminals
**W**, **V**, **U**.

The section heading tags this board **(YT058)**. The circuit diagram on p. 53 gives the same
board as inverter **RM6T6-1003, AC100-120V 50/60Hz** and numbers its plugs CN2, CN3, CN4 and CN5.

The CT850ENT book shows the same boxed inverter with the call-outs worded **Incline Motor AC**,
**Incline Motor VR**, **ESP**, **Console RM6T3**, **AC Input N / L** and **AC Motor W / V / U**; its
circuit diagram prints no inverter model. The 40T's Rhymebus inverter carries the same left-edge
call-outs but sits behind a rear incline interface board, on its own card.

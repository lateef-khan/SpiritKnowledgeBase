---
id: spirit-xe400-xe500-2007-specs-incline-controller-alt-670100a-wiring
title: 'Seven leads on the ALT-670100A incline controller: mains from the switch,
  black and red transformer plugs, up, common and down to the motor, the main harness
  and the motor harness'
kind: spec
question: What wires go where on the incline controller of a Spirit XE400-2007 or
  XE500-2007 elliptical?
asked_as:
- xe500 incline controller wiring
- alt-670100a board connections
- where do the transformer wires go on the xe400 controller
- jk7 up com down xe500
keywords:
- incline controller
- alt-670100a
- ac1 ac2
- transformer
- jk7
- up com down
- main harness
- incline motor harness
- procedure 6
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe400-2007
  - xe500-2007
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xe400-xe500-2007-specs-wiring-schematic
- spirit-xe-2007-errors-incline-does-not-work-check-the-incline-wires-and-controller
- spirit-xe-2007-specs-electrical-configuration-adapter-or-mains-incline-transformer
- xe400-2007-specs-parts-list
source:
  ref: spirit-elliptical-xe100-xe200-xe300-xe400-xe500-2007-service-manual
  locator: Repair Procedures, PROCEDURE 6, Incline controller connections, PDF p.
    7, text.md lines 202-243; a labelled photograph read from a 300 dpi render, matched
    against the schematic on PDF p. 9
  extracted_at: '2026-09-11'
---

Procedure 6 is a photograph of the controller with seven call-outs. The board is the **Incline
Controller ALT#670100A** of the parts lists.

| Call-out | On the schematic |
|---|---|
| **Red wire from the on/off switch** (two spades) | AC1 / AC2, the fused mains |
| **Black wires from the transformer** | the 4-pin plug on JK2 |
| **Red wires from the transformer** | the 3-pin plug on JK6 |
| **JK7 - UP / COM / DOWN**, red / white / black | the incline motor's three drive wires |
| **Main wire harness** | JK5, the 10-pin loom to the console |
| **Harness from the incline motor** | JK1, the 3-pin VR (position) cable |

So the controller does three jobs: switches mains to the incline motor's up and down windings,
steps the transformer's output down for the console, and passes the motor's position sensor to
the console through the main harness. The whole console loom carries power on **pins 1 and 3**
(Procedure 2).

**No voltages are printed on the page** - the meter checks the manual gives are for the gear
motor and its potentiometer, not for this board. The full loom is on
`spirit-xe400-xe500-2007-specs-wiring-schematic`; the fault-finding order is
`spirit-xe-2007-errors-incline-does-not-work-check-the-incline-wires-and-controller`.


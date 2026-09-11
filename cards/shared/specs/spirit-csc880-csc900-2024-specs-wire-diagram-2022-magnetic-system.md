---
id: spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system
title: 'The 2022 wire diagram of the magnetic stair climbers: a 24 V adapter into
  the controller, a magnetic flywheel with a brake and a 36-hole light-sensor grating,
  and a communication wire to the console'
kind: spec
question: What does the wire diagram of the Spirit CSC880 or CSC900 (2022 magnetic
  system) stair climber service manual show, and how does the magnetic system work?
asked_as:
- csc880 wiring diagram
- csc900 2022 wire diagram
- how does the magnetic stair climber brake work
- what voltage is the csc880 adapter
keywords:
- wire diagram
- wiring diagram
- magnetic system
- magnetic flywheel
- brake
- light sensor
- 36 holes grating
- controller
- adaptor
- communication wire
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - csc880-2025
  - csc900-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- csc900-2019-specs-power-flow-diagrams-alternator-brake-and-power-resistor
see_also:
- csc880-2025-specs-controller-seven-cables-named
- spirit-climber-2024-specs-resistance-system
- csc880-2025-specs-exploded-view-with-no-parts-list
source:
  ref: spirit-climber-csc880-2025-service-manual
  locator: 'CSC880: 4. Working Principle, PDF p. 5 (printed 5), text.md lines 102-120
    (OCR supplement 361-401); the wire diagram, PDF p. 7 (printed 7), line 122 (supplement
    417-424, the title only), read from a 200 dpi render; adapter/controller voltages
    in 5. Troubleshooting, PDF p. 8, supplement 427-504 (a flat-image table). CSC900
    2022: 4. Part Identification & Component Theory, PDF p. 4 (printed 4), lines 65-96;
    the wire diagram, PDF p. 5, lines 97-101 (supplement 418-437); 6. Troubleshooting,
    PDF p. 10, supplement 463-536'
  extracted_at: '2026-09-11'
---

**Both books print the same sheet**, titled **CSC880 2022 WIRE DIAGRAM** in one and **CSC900 2022
WIRE DIAGRAM** in the other, and both covers say *Magnetic* / *Magnetic system*. This is the
magnetic-brake generation; the 2019 CSC900 book draws an alternator instead
(`csc900-2019-specs-power-flow-diagrams-alternator-brake-and-power-resistor`).

**What the drawing names**

| Part | Lead |
|---|---|
| Console Assembly | **Communication wire** down the right-hand column to the controller |
| Emergency stop button | on the console mast, below the console |
| **Brake** | on the flywheel housing; **Brake connection wire** to the controller |
| **36 Holes grating** | the slotted disc on the flywheel's fan, read by the **Light sensor** on its **Light sensor stand**; **Light sensor wire** to the controller |
| Magnetic control wheel | **Magnetic control wheel connection wire** to the controller |
| **Adaptor** | fed by a **Power cord with plug**; its **Power cord** goes to the controller |
| Controller | a circuit board on a metal tray in the base |

**How it works** (the working-principle / component-theory page): the console talks to the
controller over the communication wire; the controller drives **resistance control** to the
**Magnetic Flywheel and Brake**, and reads **speed control** back from the **light sensor**. The
mechanical page draws the **Drive Belt** from the magnetic flywheel to the step **Chain**.

**Voltages, from the troubleshooting tables of both books:** the **adapter** puts out **DC 24V**,
the **controller** puts out **DC 12V** for the console, and the brake is tested by applying
**24V** separately ("a click sound will be heard when it is open"). The brake is a *power-off
brake* - it holds the stairs when unpowered. **No wattage, current or part number is printed for
the adapter**, and the 2024 owner's-manual card for this family knew none of this
(`spirit-climber-2024-specs-resistance-system`). The seven leads on the CSC880's controller are
named on `csc880-2025-specs-controller-seven-cables-named`.

The CSC900 2022 book is a 14-page reprint that omits the CSC880's controller-cable list and its
LED page; the wire diagram and the component theory are otherwise the same.


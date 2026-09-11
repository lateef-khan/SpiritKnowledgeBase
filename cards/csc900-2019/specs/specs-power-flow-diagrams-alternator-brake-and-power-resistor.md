---
id: csc900-2019-specs-power-flow-diagrams-alternator-brake-and-power-resistor
title: 'Two power-flow diagrams of the alternator-drive stair climber: console to
  control board, a speed reducer with a brake, an alternator, a power resistor, magnetic
  and proximity switches and an adapter'
kind: spec
question: What do the power flow diagrams of the Spirit csc900-2019 stair climber
  service manual show, and how is the alternator drive wired?
asked_as:
- csc900 2019 wiring diagram
- how does the alternator work on the csc900
- what is the power resistor on the csc900
- csc900 power flow diagram
keywords:
- power flow
- wiring diagram
- alternator
- generator brake
- speed reducer
- power resistor
- resistance wire
- magnetic switch
- proximity switch
- adopter
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: specs
  code: '*'
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system
see_also:
- csc900-2019-specs-controller-ev60-k2412-dc-dc-converter-and-ai3-console-board
- spirit-climber-2024-specs-resistance-system
- csc900-2019-specs-parts-proximity-switch-tl-n20me1
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: '4. How the machine works: Power Flow-1, PDF p. 3 (printed 3), text.md
    lines 65-88 (bilingual labels, native; OCR supplement 663-685); Power Flow-2,
    PDF p. 4 (printed 4), lines 89-129 (supplement 688-715), both read from 150 dpi
    renders; brake and resistor measurements, PDF p. 11, lines 405-448'
  extracted_at: '2026-09-11'
---

**This is the V1.0 book of the alternator-drive CSC900, not the magnetic 2022 system**
(`spirit-csc880-csc900-2024-specs-wire-diagram-2022-magnetic-system`). Its diagrams are bilingual,
Chinese under English.

**Power Flow-1 (block form)**

- **Console** (電子表) <-> **Control Board** (控制器) over the **Wire** (通讯线, communication wire).
- **Speed reducer** (减速机) with a **Brake** (刹车) on its shaft, driven by the **Transmission belt**
  (传动皮带) from the **Alternator** (发电机).
- A **Supply Power wire** from the control board to the brake, and a **Power supply wire** from the
  alternator to the control board.

**Power Flow-2 (the machine drawn)**

| Part | Lead |
|---|---|
| Console | **Upper wire** down the right-hand column |
| Emergency switch | on the mast below the console |
| **Brake** and **Speed reducer** | on one shaft above the alternator |
| **Alternator** | belt-driven; its leads to the controller |
| **Magnetic switch** | a reed switch on a lead to the controller |
| **Controller** | the small board in the base |
| **Power resistor** | a finned block under the controller, on the **Resistance wire** |
| **Proximity switch** | a lead from the controller |
| **Adopter** [sic] | a mains plug and adapter block, on the **Power wire** to the **Power socket** |

**How it reads.** The user's stepping turns the alternator through the belt; the alternator's
output is dumped into the **power resistor** to make the braking load, which is why the ER22
"speed out of control" page checks the alternator wire, the resistor wire and the resistor, and
why the resistor is metered at "close to **0.5 ohms**". The **brake** is a power-off brake fed by
the controller, tested by applying the adapter's **DC 24V** to its two wires for a "snap". The
magnetic switch is the reed switch that reports step movement; the proximity switch is
`csc900-2019-specs-parts-proximity-switch-tl-n20me1`. The adapter's own rating is printed nowhere;
24 V is the figure the brake test names.

**No pin, connector or wire colour is defined** - except the "motor signal feedback line (blue)"
in the troubleshooting table. The controller's internals are on
`csc900-2019-specs-controller-ev60-k2412-dc-dc-converter-and-ai3-console-board`.


---
id: spirit-ct-ent-specs-unit-block-diagram
title: The ENT unit block diagram, with a converter and a power bridge board between
  mains and console
kind: spec
question: What does the unit block diagram of a Spirit CT800ENT or CT850ENT treadmill
  show?
asked_as:
- block diagram of the ct800 ent
- how are the boards connected on the ct850 ent
- what does the power bridge board feed
- treadmill configuration diagram ent console
keywords:
- block diagram
- treadmill configuration
- console back cover transfer board
- converter
- power bridge board
- filter
- ac fan
- headphone port
- signal flow
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-unit-block-diagram
see_also:
- ct800ent-2022-specs-circuit-diagram
- ct850ent-2022-specs-circuit-diagram
- ct800ent-2022-specs-console-transfer-and-power-bridge-boards
- ct850ent-2022-specs-console-transfer-and-power-bridge-boards
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: 'CT800ENT-2022: PDF p. 16 (printed 16) ''Treadmill Configuration'', text.md
    lines 268-297. CT850ENT-2022: PDF p. 16 (printed 16), lines 268-299, OCR supplement
    lines 1260-1282'
  extracted_at: '2026-09-11'
---

Both books draw the same diagram; only the drive-side boxes differ.

**Upper half.** HR handle bar, HDMI / coaxial cable / C-SAFE, and KEY feed the **Console back cover
transfer Board**, which also drives the **Cooling Fan** and the **Headphone port**.

**Power.** POWER goes through the **Power Switch** to a **Filter**, then to the **Converter** and the
**Power Bridge Board**; an **AC Fan** hangs off the same feed.

**Drive side.** The CT800ENT shows a **Drive Board** feeding a **DC Drive Motor**, with an **RPM Sensor**,
an **Incline Motor** and a **VR Set** around it. The CT850ENT shows an **Inverter** feeding an **AC Drive
Motor**, with the same Incline Motor and VR Set beside it and no RPM-sensor box.

This is a different drawing from the CT800-2020 / CT850-2020 "Treadmill Configuration", which has no
converter, no power bridge board and no transfer board.

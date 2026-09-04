---
id: sr550-2023-gear-motor-voltage-test
title: Gear motor voltage test procedure
kind: procedure
question: How do I test the gear motor voltage on a Sole sr550-2023 rower?
asked_as:
- how do i test the resistance motor on a sole rower
- what voltage should i read at the gear motor
- multimeter test for e2 on an sr550
keywords:
- voltage test
- multi-meter
- 20vdc
- brown wire
- black wire
- drive board
- level up
- level down
- probes
facets:
  brand:
  - sole
  product_line: rower
  model: sr550-2023
  applies_to:
  - sr550-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- sr550-2023-e2-gear-motor-failure
- sr550-2023-gear-motor-spec
source:
  ref: sole-rower-sr550-2023-service-manual
  locator: Section 8.1, Gear Motor Voltage Test Procedure, page 17
  extracted_at: '2026-09-04'
---

1. Put the multi-meter on the **20VDC** setting and place the probes on the motor control wire (**red probe in brown wire, black probe in black wire**) on the drive board.
2. Turn on the unit power. The display will light up.
3. Press **LEVEL UP**. The normal reading should be **+5~6.0 VDC**, and the motor should operate with resistance increasing.
4. Press **LEVEL DOWN**. The normal reading should be **-5~6.0 VDC**, and the motor should operate with resistance decreasing.

The probe placement is repeated in the same words in the caption beside the photograph, so the wire colours are stated twice and agree.

**The procedure has no step for a zero reading.** It stops at step 4; it does not tell you what to check when there is no voltage at all. The E2 troubleshooting table covers that case: if there is no power output, inspect whether the transformer has power.

Note also that section 3 gives the gear motor's working voltage as **DC 4.5~5.5V**, which is lower than the 6.0V top of the normal band here.

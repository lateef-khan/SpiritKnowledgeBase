---
id: sr500-2016-tension-motor-voltage-test
title: Cable tensioner voltage measurement procedure
kind: procedure
question: How do I measure the cable tensioner voltage on a Sole sr500-2016 rower?
asked_as:
- how do i test the resistance motor on a sole rower
- what voltage should i read at the cable tensioner
- multimeter test for e2 on an sr500
keywords:
- voltage test
- multimeter
- 12vdc
- blue wire
- green wire
- drive board
- power adapter
- level up
- level down
facets:
  brand:
  - sole
  product_line: rower
  model: sr500-2016
  applies_to:
  - sr500-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- sr500-2016-e2-motor-error
- sr500-2016-tension-motor-spec
source:
  ref: sole-rower-sr500-2016-service-manual
  locator: Section 7.2, Cable tensioner fault / Voltage measurement procedure
  extracted_at: '2026-09-04'
---

1. Place the multifunction meter at **12VDC**. Place the probes on the motor control line on the drive board: **red probe on the blue wire, black probe on the green wire**.
2. Turn on the power of the device. The console display lights.
3. Press **LEVEL UP**. Normal reading: **+5.5 ~ 6.5VDC**. The motor acts and resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-5.5 ~ 6.0VDC**. The motor works and resistance decreases.
5. If there is no voltage, check whether there is voltage at the power adapter socket terminals; if not, change the power adapter for another one.
6. If the adapter power supply is working fine, **replace the cable tensioner**.

Two things about the printed list. The steps are numbered 1, 3, 4, 5, 6, 7 - **there is no step 2 in the manual**, and the numbering above closes that gap without changing any step. And the two normal readings are not symmetric as printed: up is 5.5~6.5V, down is 5.5~6.0V.

The probe placement is repeated in the same words under the photograph, so the wire colours are stated twice and agree. **Note that these are blue and green wires**, not the brown and black wires used on Sole ellipticals.

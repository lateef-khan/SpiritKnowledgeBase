---
id: sole-bike-tension-motor-voltage-test
title: "Tension motor voltage test"
kind: procedure
question: "How do I voltage test the tension motor on a Sole B94-2016, B94-2019 or R92-2016?"
asked_as:
- "how do i test the resistance motor on my bike"
- "multimeter test for the bike tension motor"
- "check drive board output to the motor"
keywords:
- "voltage test"
- "multi-meter"
- "tension motor"
- "drive board"
- "20vdc"
- "fuse"
- "power led"
- "bike"
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - b94-2016
  - b94-2019
  - r92-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bike-tension-motor-error
- sole-bike-tension-motor-connector-pinout
source:
  ref: sole-bike-b94-2016-service-manual
  locator: "Section 8, Tension Motor Voltage Test Procedure (same procedure in the B94 2016, B94 2019 and R92 2016 manuals)"
  extracted_at: '2026-09-03'
---

1. Set the multi-meter to **20VDC**. Put the probes on the motor control wire at the drive board: **red probe on the brown wire, black probe on the black wire**.
2. Switch the unit on. The display lights up.
3. Press **LEVEL UP**. Normal reading is **+5 to 6.0 VDC**. The motor runs and resistance increases.
4. Press **LEVEL DOWN**. Normal reading is **-5 to 6.0 VDC**. The motor runs and resistance decreases.
5. If there is no voltage, check the fuse in the power socket holder. Replace it if it is blown.
6. Check whether the POWER LED on the drive board is lit. If it is not lit the drive board is bad. Replace it.

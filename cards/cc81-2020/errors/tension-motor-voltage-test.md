---
id: cc81-2020-tension-motor-voltage-test
title: "Tension motor voltage test at the drive board"
kind: procedure
question: "How do I voltage test the tension motor on a Sole CC81-2020 climber?"
asked_as:
- "how do i test the resistance motor on my sole climber"
- "multimeter test for the climber tension motor"
- "check drive board output on the cc81"
keywords:
- "voltage test"
- "multi-meter"
- "20vdc"
- "tension motor"
- "drive board"
- "probes"
- "transformer"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81-2020
  applies_to:
  - cc81-2020
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- cc81-2020-tension-motor-console-output-check
- cc81-2020-tension-motor-connector-pinout
- cc81-2020-e2-tension-motor-failure
- sole-bike-tension-motor-voltage-test
source:
  ref: sole-climber-cc81-2020-service-manual
  locator: "Sections 7-2 Prepare tools and 7-4-3 Tension motor voltage test procedure"
  extracted_at: '2026-09-03'
---

Tool needed: a **multi-meter**. It is the only tool the manual lists for the error section.

1. Set the multi-meter to the **20 VDC** setting. Place the probes on the motor control wire at the **drive board**: **red probe in palm wire, black probe in black wire**.
2. Turn the unit power on. The display lights up.
3. Press **LEVEL UP**. Normal reading: **+5 to 6 VDC**. The motor operates and resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-5 to 6 VDC**. The motor operates and resistance decreases.
5. If there is no voltage, check the transformer. If there is no output, replace it.

**Two things to know before you trust a reading.**

- The manual prints **5 to 6 VDC** here and **4 to 5 VDC** in section 7-4-1/7-4-2 for the same measurement. See the card `cc81-2020-tension-motor-console-output-check`. It never says how they relate.
- **"Palm wire" is printed exactly as shown.** The wire colour is not otherwise named in this manual. The matching Sole bike procedure calls the same wire the **brown** wire. Confirm the wire at the connector before probing.

---
id: sc200-2019-tension-motor-voltage-test
title: Tension motor voltage test procedure
kind: procedure
question: How do I voltage test the tension motor on a Sole sc200-2019?
asked_as:
- how to test the tension motor on my sole climber
- what voltage should the resistance motor read on an sc200
- multimeter test resistance motor climber
keywords:
- tension motor
- voltage test
- multimeter
- 20vdc
- 2.5vdc
- blue wire
- transformer
- resistance
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2019
  applies_to:
  - sc200-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2019-e2-tension-motor-failure
- sc200-2019-tension-motor-spec
- sc200-2019-no-display
source:
  ref: sole-elliptical-sc200-2019-service-manual
  locator: Section 8-2, pages 35-36
  extracted_at: '2026-09-04'
---

1. Put the multi-meter to the **20VDC** setting. Place probes on the motor control wire (**red probe in blue wire, black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press LEVEL UP. Normal reading: **+2.2~2.7VDC**. Motor operates. Resistance increases.
4. Press LEVEL DOWN. Normal reading: **-2.2~2.7VDC**. Motor operates. Resistance decreases.
5. If there is no voltage, **check the transformer; if there is no output, replace it.**

**A contradiction in this manual, left as printed.** Step 1 says the black probe goes in the **green** wire. The caption under the photo on the next page says "Place probes on the motor control wire (Red probe in blue wire, **Black probe in Brown wire**) on the drive board." The red probe is blue in both. Identify the wire on the machine before probing.

The expected readings here, **+/-2.2~2.7VDC**, are half those of the 2019 Sole ellipticals, whose manuals give +/-5~6.0VDC. Step 5 also differs: the elliptical manuals send you to a fuse, this one to the transformer. This manual has no fuse replacement section.

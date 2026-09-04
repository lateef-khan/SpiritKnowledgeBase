---
id: sc200-2016-tension-motor-connector-pinout
title: Tension motor connector pin definition
kind: spec
question: What is the tension motor connector pinout on a Sole sc200-2016 climber?
asked_as:
- tension motor connector pins on my sole sc200
- what are the 8 pins on the resistance motor
- wiring for the gear motor plug
keywords:
- tension motor
- connector
- pinout
- 8 pin
- count
- zero
- vin
- speed sensor
- steel rope
facets:
  brand:
  - sole
  product_line: elliptical
  model: sc200-2016
  applies_to:
  - sc200-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sc200-2016-tension-motor-spec
- sc200-2016-e2-tension-motor-failure
- sc200-2016-console-connector-pinout
source:
  ref: sole-elliptical-sc200-2016-service-manual
  locator: Tension Motor connector definition function, page 31, and the test configuration,
    page 41
  extracted_at: '2026-09-04'
---

The **console to tension motor connector**, from the test configuration drawing:

| Pin | Signal |
|---|---|
| 1 | VIN |
| 2 | M+ |
| 3 | M- |
| 4 | COUNT |
| 5 | ZERO |
| 6 | 3V |
| 7 | GND |
| 8 | SPEED |

**The earlier drawing in section 6 is incomplete.** The page headed "Tension Motor connector definition function" numbers the main control plug 1 to 8 but prints **no signal names beside them**. Only the drawing on page 41 names the pins.

The speed sensor plug on that same page is printed damaged. It is drawn with pins **1 and 2**, but the labels beside it read:

```
SPEED
SENSOR
2. GND
3. SPEED
```

The label numbers 2 and 3 do not match the two pins drawn. The E95 and E95S manuals of the same year print the same plug as **1. GND, 2. SPEED**. This manual's numbering is not reproduced here as fact.

The E2 troubleshooting tables call the cable to the tension motor the **8-pin cable**.

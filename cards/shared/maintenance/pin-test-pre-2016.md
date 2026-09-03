---
id: sole-pin-test-pre-2016
title: Pin test on a pre-2016 treadmill
kind: procedure
question: How do I run a pin test on an older Sole treadmill?
asked_as:
- how do i do a pin test on a treadmill
- test speed and incline without the console
keywords:
- pin test
- twist ties
- console mast
- connector pins
- older than 2016
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - '*'
  section: maintenance
  code: '*'
authority: 2
not_to_be_confused_with: []
see_also:
- sole-ls-error
- sole-e3-error
source:
  ref: sole-tm-pin-test-treadmill-older-than-2016
  locator: whole document
  extracted_at: '2026-09-03'
---

This test only applies to treadmills built **before 2016**. It drives speed and incline directly, so it tells you whether the fault is above or below the connector.

**Getting to the connector**

1. Use a screwdriver to remove the console mast cover on the user's right hand side.
2. Disconnect the bigger of the 2 connectors.
3. Hold the half coming out of the upright with the thumb latch on top. The bottom left corner is pin 1, counting right to pin 6. The top right corner is pin 7, counting right to pin 12.
4. Use twist ties to join pins together.

**Pin layout, thumb clip on top**

```
 7  8  9 10 11 12
 1  2  3  4  5  6
```

| Pin | Wire colour | Function |
|---|---|---|
| 1 | Black | S/W |
| 2 | Brown | Down |
| 3 | Red | Up |
| 4 | Orange | VCC |
| 5 | Yellow | Fast |
| 6 | Green | Slow |
| 7 | Blue | Ground |
| 8 | Violet | Spd |
| 9 | Gray | Spd |
| 10 | White | VR-1 |
| 11 | Light green | VR-2 |
| 12 | Pink | VR-3 |

**Testing incline**: join pin 4 and 3 for UP. Join pin 4 and 2 for DOWN.

**Testing speed**: join pin 1 and 4, then:
- pin 7 and 5, putting the end for 5 in and out 15 times to speed the belt up.
- pin 7 and 6, putting the end for 6 in and out 15 times to slow the belt down.

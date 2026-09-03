---
id: cc81-2020-no-pulse-displayed
title: "No heart rate shown on the monitor"
kind: troubleshooting
question: "My Sole CC81-2020 climber shows no pulse at all. What do I check?"
asked_as:
- "no heart rate on my sole climber"
- "chest strap not reading on the climber"
- "cc81 wireless heart rate stopped working"
keywords:
- "no pulse"
- "wireless"
- "chest belt"
- "receiver range"
- "battery"
- "cr2032"
- "heart rate"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81-2020
  applies_to:
  - cc81-2020
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cc81-2020-erratic-pulse-display
- cc81-2020-console-data-ranges
source:
  ref: sole-climber-cc81-2020-service-manual
  locator: "Section 7-7 Troubleshooting procedure matrix, wireless lost its function row and the final row"
  extracted_at: '2026-09-03'
---

| Reason | What to do |
|---|---|
| The chest belt is not worn properly. | Check the belt makes proper contact with the skin and is the right way round. |
| The distance is too far and beyond the receiver's range. | Use the chest belt in front of the console, **within 30 cm**. |
| The chest belt battery is weak or dead. | Replace with a new lithium battery, **type CR2032**. |

**One row in the source is damaged.** The last row of the matrix is headed "Chest belt too close to the climber", but its reason is "Weak battery" and its fix is the same CR2032 battery replacement. The heading does not match the reason. The battery fix is real; the "too close" heading contradicts the row above it, which says the belt must be within 30 cm. Treat the heading as an error in the manual.

If the reading is present but jumping, see the card `cc81-2020-erratic-pulse-display`.

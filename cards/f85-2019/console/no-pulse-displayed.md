---
id: f85-2019-no-pulse-displayed
title: No heart rate shown at all
kind: troubleshooting
question: Why is no heart rate shown on my Sole F85-2019 treadmill?
asked_as:
- no pulse showing on my treadmill
- hand grips do not read my heart rate
- chest strap will not show heart rate
keywords:
- no pulse
- hand pulse
- chest belt
- wireless receiver
- heart rate
- cr2032
- hand pulse board
- grip sensors
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2019-erratic-pulse-display
see_also:
- f85-2019-erratic-pulse-display
- f85-2019-console-data-ranges
- f85-2019-display-board-connections
source:
  ref: sole-tm-f85-2019-service-manual
  locator: section 8.10 troubleshooting matrix, printed page 80
  extracted_at: '2026-09-04'
---

**This is no reading at all. A reading that appears but jumps around is a different card.**

**Hand pulse lost its function**

| Reason | Solve |
|---|---|
| Hands are not on the sensors, or only one hand is | Hold both hand pulse grips. |
| The HANDPULSE wire connector and the console are not connected properly | Connect the cable again. |
| The wires were damaged when the HANDPULSE wire was connected to the console | Replace with a new cable. |
| The hand pulse board is broken | Replace the console or the hand pulse board. |

**Wireless lost its function**

| Reason | Solve |
|---|---|
| The chest belt is not worn properly | Check the belt has proper contact with the skin and is oriented correctly. |
| The distance is too far and exceeds the range of the receiver | Use the chest belt in front of the console, within **3 feet**. |
| The chest belt battery is weak or dead | Replace with a new **CR2032** lithium battery. |

The wireless heart receiver and the heart module both plug into the display board, so a console fault can take out the chest belt path while the hand grips still work, and the other way round.

The console drops the pulse window to 0 after **8 seconds** with no signal, so a reading that disappears mid workout is the same fault as one that never arrives.

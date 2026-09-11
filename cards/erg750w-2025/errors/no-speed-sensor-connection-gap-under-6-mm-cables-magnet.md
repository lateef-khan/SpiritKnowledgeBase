---
id: erg750w-2025-errors-no-speed-sensor-connection-gap-under-6-mm-cables-magnet
title: 'No speed: the speed sensor connection, then a sensor-to-magnet gap under 6
  mm, then a shorted or damaged sensor or cable, then a fallen magnet'
kind: troubleshooting
question: Why does the console show no speed or stroke rate while rowing on an Xterra
  erg750w-2025 water rower, and what is the sensor gap?
asked_as:
- xterra water rower no speed
- erg750w not counting strokes
- rower speed sensor gap
- water rower magnet fell off strap wheel
keywords:
- no speed
- speed sensor
- sensor gap
- 6 mm
- induction magnets
- strap wheel
- sensor cable
- sensor mounting screws
- water rower
facets:
  brand:
  - xterra
  product_line: rower
  model: erg750w-2025
  applies_to:
  - erg750w-2025
  section: errors
  code: '*'
  model_number:
  - '175926'
authority: 3
not_to_be_confused_with:
- erg600w-2021-errors-console-shows-no-data-batteries-wires-magnets-sensor-gap-5-mm
- erg750w-2025-errors-console-vr-resistance-level-three-terminal-checks
see_also:
- xterra-rower-errors-no-count-or-distance-sensor-wire-then-monitor
- erg750w-2025-errors-no-action-or-dim-lcd-power-failure-batteries-and-battery-case-wires
- erg750w-2025-errors-console-vr-resistance-level-three-terminal-checks
- erg600w-2021-errors-console-shows-no-data-batteries-wires-magnets-sensor-gap-5-mm
- crw900-2021-errors-speed-sensor-gap-2-to-3-mm-and-six-magnets
source:
  ref: xterra-rower-erg750w-2025-service-manual
  locator: ERG-750W SM "TZ-8145-2AA Trouble Shooting" table (Problem / Possible cause
    / Things to Check / Solution), PDF p. 26, text.md lines 360-391; the page was
    also read from a 110 dpi render because the text layer interleaves the columns;
    "Common Problems of Sensors" page (Model row reads R48), PDF p. 25, lines 345-360,
    read from a render as well (three photos)
  extracted_at: '2026-09-11'
---

**The gap figure here is under 6 mm, and it is this book's.** The ERG600W's service manual says 5 mm for its own sensor bar (`erg600w-2021-errors-console-shows-no-data-batteries-wires-magnets-sensor-gap-5-mm`); no owner's manual in the range prints a gap at all.

The *No speed* row of the console troubleshooting table (the console is named by its part number, TZ-8145-2AA):

| Possible cause | Things to check | Solution |
|---|---|---|
| 1. Computer didn't receive speed signals | Check the speed sensor is in good connection | Make sure the good connection for cables |
| 2. The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | Keep the gap distance **less than 6 mm** |
| 3. Defective sensor or bad cable connection | Check the sensor and cables are circuit short or damaged | Change the sensor or cables |
| 4. The magnet has fallen off | Check whether the magnet has fallen off | Reset the magnet firmly |

A second page of the same manual, headed *Common Problems of Sensors*, gives the mechanical side of the same fault as three checks with photos: whether the **sensor mounting screws** are misaligned, whether the **two induction magnets on the strap wheel** are loose or have fallen off, and whether the upper terminals of the console are loose or detached. So this rower carries two magnets on its strap wheel, and a magnet that has dropped out is reseated rather than replaced.

The owner's manual's version of the fault is the three-row *No count or distance* table with no gap and no magnets (`xterra-rower-errors-no-count-or-distance-sensor-wire-then-monitor`). A wrong resistance level on the display is the VR page, not this one (`erg750w-2025-errors-console-vr-resistance-level-three-terminal-checks`).

The Spirit CRW900 water rower prints 2-3 mm and six magnets for its own sensor (`crw900-2021-errors-speed-sensor-gap-2-to-3-mm-and-six-magnets`); neither figure is this machine's.

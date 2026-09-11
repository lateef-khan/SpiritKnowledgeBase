---
id: xterra-rower-errors-no-count-or-distance-sensor-wire-then-monitor
title: 'No count or distance on the monitor while rowing: connect or replace the sensor
  wire, then replace the monitor'
kind: troubleshooting
question: Why does the monitor show no stroke count or distance while I row on an
  Xterra ERG rower?
asked_as:
- xterra rower not counting strokes
- erg rower distance stays at zero
- rowing machine console lit but nothing counts
- xterra rower no speed reading
keywords:
- no count
- no distance
- no speed
- sensor wire
- speed sensor
- replace monitor
- magnetic wheel
- magnet
- reed switch
- rower
facets:
  brand:
  - xterra
  product_line: rower
  model: '*'
  applies_to:
  - erg220-2023
  - erg500-2018
  - erg550w-2023
  - erg600w-2021
  - erg650w-2021
  - erg750w-2025
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-errors-no-speed-or-distance-sensor-wire-monitor-or-magnetic-wheel
- xterra-rower-errors-monitor-does-not-display-install-batteries-then-computer-wires
see_also:
- xterra-rower-errors-monitor-does-not-display-install-batteries-then-computer-wires
- erg550w-2023-errors-console-shows-no-data-full-stroke-of-1-m-then-batteries-wires-two-magnets
- erg600w-2021-errors-console-shows-no-data-batteries-wires-magnets-sensor-gap-5-mm
- erg750w-2025-errors-no-speed-sensor-connection-gap-under-6-mm-cables-magnet
- xterra-errors-no-speed-or-distance-sensor-wire-monitor-or-magnetic-wheel
- crw800h2o-console-shows-no-data
source:
  ref: xterra-rower-erg500-2018-owners-manual
  locator: ERG500 OM Trouble Shooting, PDF p. 19 (printed 17), text.md lines 506-542;
    ERG550W OM Trouble Shooting, PDF p. 24 (printed 22), lines 815-846; ERG600W OM
    Trouble Shooting, PDF p. 23 (printed 21), lines 651-683; ERG650W OM Troubleshooting,
    PDF p. 20 (printed 17), lines 547-575; ERG750W OM TROUBLESHOOTING, PDF p. 22 (printed
    21), lines 672-699; ERG220 OM Troubleshooting, PDF p. 21 (printed 18), lines 598-652;
    ERG160 OM Troubleshooting, PDF p. 22 (printed 20), lines 787-803
  extracted_at: '2026-09-11'
---

**The console is on but does not register the stroke.** A console that shows nothing at all is a different row (`xterra-rower-errors-monitor-does-not-display-install-batteries-then-computer-wires`).

Five books print the row with three causes, in this order:

| Problem | Cause | Solution |
|---|---|---|
| No count or distance displays on the monitor | Sensor wire not connected | Ensure the computer wires are connected properly at the upright and the computer |
| | Sensor wire not working properly | Replace sensor wire |
| | Monitor not working properly | Replace monitor |

That is the ERG500, ERG550W, ERG600W, ERG650W and ERG750W. **The ERG220 prints the problem as *Console does not display speed or distance* and adds a fourth cause**, which the other five do not have:

| | Magnetic wheel not working properly | Replace magnetic wheel |
|---|---|---|

The magnetic wheel is the flywheel-side magnet assembly the sensor counts on that magnetic rower; the bike twin of the row lists it too (`xterra-errors-no-speed-or-distance-sensor-wire-monitor-or-magnetic-wheel`), and the ERG160 book, whose console is a two-AA unit of the same kind, prints no such row at all.

**The order is the book's - connections, then the wire, then the monitor.** No owner's manual in this family prints a sensor gap. The service manuals do: the ERG600W's Q&A says to move the sensor bar if it sits more than **5 mm** from the magnet (`erg600w-2021-errors-console-shows-no-data-batteries-wires-magnets-sensor-gap-5-mm`), the ERG750W's table says to keep the gap under **6 mm** (`erg750w-2025-errors-no-speed-sensor-connection-gap-under-6-mm-cables-magnet`), and the ERG550W's Q&A starts somewhere else entirely - with whether the stroke was a full metre (`erg550w-2023-errors-console-shows-no-data-full-stroke-of-1-m-then-batteries-wires-two-magnets`). Each figure is printed for its own machine only.

---
id: spirit-xt-errors-does-not-start-motor-m-plus-m-minus-wire
title: The treadmill does not start when START is pressed, on the row that names the
  motor M+ and M- wires
kind: troubleshooting
question: Why does a Spirit XT 2015, XT 2023 or CT1000ENT treadmill not start when
  I press START?
asked_as:
- treadmill does nothing when i press start
- belt will not move on my spirit treadmill
- start button does not work
keywords:
- will not start
- start button
- motor wire
- m+
- m-
- controller
- shut down led
- belt not moving
- replace motor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct1000ent-2023
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt685-2023
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ct850-2016-does-not-start-when-start-pressed
- ct850-2020-does-not-start-when-start-pressed
see_also:
- ct850-2016-stops-immediately-after-start
- xt-2023-errors-e1-motor-not-responsive
- spirit-xt-errors-e4-motor-power-wire-not-plugged
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT185 2015 service manual Troubleshooting procedure matrix, PDF p. 60-62
    (printed 55-57), text.md lines 1119-1221; XT285 2015 service manual Troubleshooting
    procedure matrix, PDF p. 61-63 (printed 55-57), text.md lines 1189-1291; XT385
    2015 service manual Troubleshooting procedure matrix, PDF p. 60-62, text.md lines
    933-1039; XT485 2015 service manual Troubleshooting procedure matrix, PDF p. 61-63,
    text.md lines 941-1047; XT185 2023 service manual Troubleshooting procedure matrix,
    PDF p. 35-37, text.md lines 705-825; XT285 2023 service manual Troubleshooting
    procedure matrix, PDF p. 36-38, text.md lines 707-827; XT385 2023 service manual
    Troubleshooting procedure matrix, PDF p. 36-38, text.md lines 631-743; XT485 2023
    service manual Troubleshooting procedure matrix, PDF p. 36-38, text.md lines 636-748;
    XT685 2023 service manual Troubleshooting procedure matrix, PDF p. 34-36, text.md
    lines 670-794; CT1000ENT 2023 service manual 6.4 Troubleshooting procedure Matrix,
    PDF p. 19-21, text.md lines 428-549
  extracted_at: '2026-09-11'
---

Three causes, in the order the manual lists them.

| Reason | Solve |
|---|---|
| Motor M+ or M- wire isn't connected into right position | Please check and plug again |
| Motor is broken | Replace motor or check the wire and connector if it was broken |
| Treadmill controller shut down and LED would be ON | Turn off the ON/OFF switch and turn on power again |

The 2023 XT185 to XT685, the 2015 XT385 and XT485 and the CT1000ENT 2023 service manuals print this word for word. **The 2015 XT185 and XT285 shorten the third cause to `Treadmill controller shut down` and say `Turn off the AC switch`**; same fault, same fix.

These are DC-motor machines with two motor wires, red to M+ and black to M-. **The CT1000ENT is an AC-motor machine and prints this row anyway** - its own motor has U, V and W wires and no M+ or M-, so on that machine read the row as *check the motor wiring*. The CT800 2016 and CT900ENT print the row as `AC Motor U or V or W wire` (`ct850-2016-does-not-start-when-start-pressed`); the CT800 2020 family says only `Motor wire` (`ct850-2020-does-not-start-when-start-pressed`).

If the belt starts and then stops, that is `ct850-2016-stops-immediately-after-start`; if the display shows E1 first, `xt-2023-errors-e1-motor-not-responsive`.

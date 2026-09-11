---
id: ct850-2016-does-not-start-when-start-pressed
title: The treadmill does not start when START is pressed
kind: troubleshooting
question: Why does a Spirit CT800 2016, CT850 2016 or CT900ENT treadmill not start
  when I press START?
asked_as:
- treadmill does nothing when i press start
- belt will not move on my spirit treadmill
- start button does not work
keywords:
- will not start
- start button
- ac motor
- u v w
- motor wire
- controller
- shut down led
- belt not moving
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - ct850-2016
  - ct900ent
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ct850-2020-does-not-start-when-start-pressed
see_also:
- ct850-2020-does-not-start-when-start-pressed
- ct850-2016-stops-immediately-after-start
- ct850-2016-low-speed-after-eight-seconds
- spirit-xt-errors-does-not-start-motor-m-plus-m-minus-wire
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Section 8.3 Troubleshooting procedure matrix, pages 49-52 (printed 48-51);
    CT800 2016 service manual 8.4 Troubleshooting procedure matrix, PDF p. 56-59 (printed
    55-58), text.md lines 1076-1215; CT900ENT service manual Troubleshooting procedure
    matrix, PDF p. 45-48, text.md lines 691-842
  extracted_at: '2026-09-08'
---

Three causes, in the order the manual lists them.

| Reason | Solve |
|---|---|
| AC Motor U or V or W wire isn't connected into right position | Please check and plug again |
| Motor is broken | Replace motor or check the wire and connector if it was broken |
| Treadmill controller shut down and LED would be ON | Turn off the AC switch and turn on power again |

This machine has a **three-phase AC motor with U, V and W wires**. The CT850 2020 manual prints the
same row but says only `Motor wire isn't connected into right position`:
`ct850-2020-does-not-start-when-start-pressed`.

If the belt starts and then stops, that is a different row: `ct850-2016-stops-immediately-after-start`.
If the belt never moves and the window shows a low speed message, see
`ct850-2016-low-speed-after-eight-seconds`.

**The CT800 2016 and CT900ENT service manuals print this row word for word, U, V and W wires included.** The CT900ENT is an AC-motor machine and the row fits it; the CT800 2016 book describes a DC motor with a `90V~` work voltage on its electrical page and an M+/M- driver board on its component page, then prints `AC Motor U or V or W wire` here - the row was carried over from the CT850 and does not match that machine's own wiring. The XT and CT1000ENT books print the DC version, `Motor M+ or M- wire` (`spirit-xt-errors-does-not-start-motor-m-plus-m-minus-wire`).

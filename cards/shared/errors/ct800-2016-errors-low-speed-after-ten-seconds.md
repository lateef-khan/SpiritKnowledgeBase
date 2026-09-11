---
id: ct800-2016-errors-low-speed-after-ten-seconds
title: The belt does not run and the window shows a low speed message after ten seconds
kind: troubleshooting
question: Why does the belt not run and the window show LOW SPEED after ten seconds
  on a Spirit ct800-2016 or ct900ent treadmill?
asked_as:
- belt not moving and low speed showing
- treadmill shows ls1 after 10 seconds
- spirit treadmill belt will not run
keywords:
- low speed
- ls1
- shut down light
- ac motor
- computer cable
- motor belt
- controller
- ten seconds
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - ct900ent
  section: errors
  code: low-speed
authority: 3
not_to_be_confused_with:
- ct850-2016-low-speed-after-eight-seconds
see_also:
- ct850-2016-low-speed-error-message
- ct850-2016-low-speed-solution-flow-chart
- ct850-2016-low-speed-troubleshooting-form
- ct850-2016-does-not-start-when-start-pressed
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: CT800 2016 service manual 8.4 Troubleshooting procedure matrix, PDF p.
    57 (printed 56), text.md lines 1117-1159; CT900ENT service manual Troubleshooting
    procedure matrix, PDF p. 46, text.md lines 732-776
  extracted_at: '2026-09-11'
---

The matrix row, printed condition first:

> When press "START" button to start treadmill, running belt isn't running and window displays "LS1/LOW SPEED" error message after 10 seconds.

Eight causes, in the order the manual lists them.

| Reason | Solve |
|---|---|
| Controller experienced unusual shut down; the Shut_DOWN light will be always bright | Turn off power and reset the treadmill |
| AC Motor wires (U or V or W) aren't plugged into controller | Plug wires again |
| Computer cables not connected properly | Plug the wire again on controller, connector and console |
| Computer cables are broken or damaged | Replace with new wires |
| Motor belt is broken | Replace with new motor belt |
| Controller is broken | Replace with new controller |
| AC Motor is broken | Replace with new AC motor |
| Console is broken | Replace with new console |

**The CT850 2016 service manual prints this row with `after 8 seconds`** (`ct850-2016-low-speed-after-eight-seconds`); the eight causes are the same. The CT800 2016 and the CT900ENT say ten. The CT800 2016's own troubleshooting form two chapters earlier says the monitor raises the message after **8 seconds** without a speed signal (`ct850-2016-low-speed-troubleshooting-form`), so that book carries both figures.

**The CT800 2016 is described as a DC-motor machine everywhere else in its book** - `DC MOTOR, work voltage DC 90V~` on its electrical page, M+ and M- terminals on its driver board - and this row still names AC motor wires U, V and W. The row fits the CT900ENT, whose motor is an AC one; on the CT800 2016 read it as *check the motor wires*. The CT900ENT's own error table has no LS1 code (`ct900ent-errors-error-code-messages-list`).

---
id: xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change
title: 'E6 on the JKEXER console: the incline motor''s VR value did not change, fixed
  by re-seating the telescopic tube at 268.5 mm or by the motor''s cable'
kind: troubleshooting
question: What does E6 mean on an Xterra tr75h-2025 or tr95h-2024 treadmill, and what
  should I do?
asked_as:
- e6 on my tr95h incline
- tr75h e6 incline motor
- incline stuck e6 xterra
keywords:
- e6
- incline motor
- vr value
- telescopic tube
- 268.5 mm
- 6 seconds
- incline stuck
- connection cable
- driver board
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e6-lower-controller-component-fault
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- xterra-ws-errors-e06-system-self-check-failed
see_also:
- xterra-tr-errors-jkexer-error-messages-e1-e3-e6-and-dashes
- xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit
- xterra-tr-errors-e3-jkexer-poor-communication-upper-lower-controller
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: TR95H SM 11. Explanation and troubleshooting of error messages, PDF pp.
    16-17; text.md lines 209-258; TR75H SM 12. Explanation and troubleshooting of
    error messages, PDF pp. 16-17; text.md lines 346-421; TR95H OM Troubleshooting,
    PDF p. 53 (printed 52); text.md lines 1920-1939; TR75H OM Troubleshooting, PDF
    p. 49 (printed 48); text.md lines 1845-1864
  extracted_at: '2026-09-11'
---

**On the TR75H and TR95H, E6 is an incline fault.** On the Dyaco-built Xterra treadmills E6 is a lower-controller component fault (`xterra-treadmill-errors-e6-lower-controller-component-fault`).

*Owner's manual:* E6 (Error 6): when the machine starts but the computer could not read the VR signal from the incline motor for **6 seconds**, E6 is shown. Consult the distributor.

*Service manual:* cause - the console did not receive the change in the VR value of the incline motor.

- *Scenario 1 - the VR value of the incline motor is out of range, causing the telescopic tube to get stuck.* (a) Remove the incline motor and connect it to the driver board. (b) Turn on the treadmill's power; the incline motor will automatically rotate to the position of the correct VR value. (c) Rotate the telescopic tube and adjust it to the correct assembly size: **268.5 mm between the upper and lower holes.** (d) Install the incline motor back in its original position. (The TR95H book numbers these a, b, c, e; the TR75H book a to d.)
- *Scenario 2 - the incline motor does not operate.* (a) Check whether the incline motor's connection cable is connected properly or damaged. (b) Incline motor failure - replace.

The driver board's *incline motor start indicator light* (item 15 on the parts callout) is the only incline LED these books name, without a meaning. The incline motor replacement steps (section 6 of each service manual) are assembly cards.

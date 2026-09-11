---
id: spirit-xs895-errors-incline-buttons-do-not-work-cable-connectors-and-the-switch
title: 'The incline switch does nothing, or works only up or only down: the incline
  cable connectors at the console and at the switch, then the cable, then the buttons'
kind: troubleshooting
question: Why do the incline up and down buttons not work, or work in only one direction,
  on a Spirit XS895 stepper?
asked_as:
- xs895 incline button does nothing
- stepper incline only goes up not down
- incline switch on my spirit stepper stopped working
keywords:
- incline adjustment switch
- incline cable
- connector
- up only
- down only
- replace buttons
- replace cable
- incline stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr
- spirit-xs895-errors-incline-motor-no-function-and-no-resistance-gear-motor
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 7-8 Troubleshooting procedure matrix, the three INCLINE ADJUSTMENT SWITCH
    rows, PDF p. 36 (printed 35); text.md lines 564-580
  extracted_at: '2026-09-11'
---

The matrix prints three conditions against one shared list of causes and fixes:

- UP/DOWN button of INCLINE ADJUSTMENT SWITCH can't be used.
- Incline button just can press UP, can't press DOWN.
- Incline button just can press DOWN, can't press UP.

| Reason | Solve |
|---|---|
| 1. The connector of INCLINE CABLE and CONSOLE not connected properly. | 1. Connect the wires again. |
| 2. The connector of INCLINE CABLE and INCLINE ADJUSTMENT SWITCH W/CABLE not connected properly. | 2. Connect the wires again. |
| 3. The connector of INCLINE CABLE or INCLINE ADJUSTMENT SWITCH CABLE got damage. | 3. Replace the cable. |
| 4. Button of INCLINE ADJUSTMENT SWITCH is broken. | 4. Replace buttons. |
| 5. The connector of INCLINE CABLE or INCLINE ADJUSTMENT SWITCH CABLE got damage. | 5. Replace the cable. |
| 6. The connector of INCLINE CABLE or INCLINE ADJUSTMENT SWITCH CABLE damaged. | 6. Replace the cable. |

**Causes 3, 5 and 6 are the same sentence three times**, printed that way on the page; the list is really two connectors to reseat, a cable to replace and a button to replace. **A switch that works one way and not the other points at the button** - a cable fault would usually take both directions - but the book does not say so; it gives the same list for all three conditions.

**This is the switch, not the motor.** The incline adjustment switch sits on the handlebar; a motor that does not move when the console commands it is a different page (`spirit-xs895-errors-incline-motor-no-function-and-no-resistance-gear-motor`), and a motor whose position reading is lost is `E3` (`spirit-xs895-errors-e3-incline-motor-error-step-error-and-the-incline-vr`).

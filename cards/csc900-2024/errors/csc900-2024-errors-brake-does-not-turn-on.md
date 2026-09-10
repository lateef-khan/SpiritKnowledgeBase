---
id: csc900-2024-errors-brake-does-not-turn-on
title: The brake does not turn on and the machine will not run, and the test is 24 volts and a click
kind: troubleshooting
question: Why will a Spirit stair climber not run after pressing START, with the brake still on?
asked_as:
- my stairclimber wont move when i press start
- csc900 brake wont engage
- stair climber steps wont run
- csc880 brake not releasing
keywords:
- brake
- 24v
- click
- multimeter
- brake socket
- controller
- power failure brake
- stairclimber
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - csc880-2025
  - csc900-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-er12-console-not-receiving-controller-data
see_also:
- csc900-2024-errors-error-code-table
- csc880-2025-errors-error-code-table
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er12-console-not-receiving-controller-data
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: 'CSC900 2024: TROUBLESHOOTING, Problem / Reason / Method table on printed
    page 34; that page is a flat picture with no text layer and was read from the rendered
    page at 500 dpi. Extended 2026-09-10 with the CSC880 2025 owner''s manual,
    spirit-climber-csc880-2025-owners-manual, TROUBLESHOOTING - CONTINUED row 7 on printed
    page 34 (PDF page 36), read from the native text layer and confirmed against a 400
    dpi render.'
  extracted_at: '2026-09-10'
---

**Condition:** After pressing "START" to start, the brake does not turn on, the machine cannot run.

| Reason | Method |
|---|---|
| The brake is no power or failure | 1. Check whether the connecting wire is off and damaged. 2. Separately supply **24V** voltage to test whether the brake is open (there will be a "click" sound when it is open). Replace the power failure brake. |
| Control board failure | Use a multimeter to measure whether the brake socket of the controller has **24V** output voltage after starting. Replace the controller. |

**Two tests, and both turn on the same 24 volts.** Feed the brake 24 V from a bench supply and
listen for the click - that separates a dead brake from a controller that is not sending it power.
Then measure the controller's brake socket after pressing start; 24 V present with no click condemns
the brake, no 24 V condemns the controller.

**The click is the pass condition.** The manual gives no resistance, no current and no dwell time -
only the sound.

If the console reports `ER02` at the same time, the magnet wheel wiring is the first thing to reseat
(`csc900-2024-errors-er02-magnetic-wheel-or-control-board`). A machine that runs but will not brake
is `ER12` instead (`csc900-2024-errors-er12-console-not-receiving-controller-data`).

## The CSC880 2025 stair climber prints the same row, with the same 24 volts

Its wording names the part a **power-off brake** - a brake held open by power, so that losing power
applies it - and gives the same two tests:

> 1. Check whether the connection cable is loose or damaged.
> 2. Apply a separate 24V voltage to check whether the brake is open (a "click" sound will be heard
>    when it is open).
> 3. Replace the power-off brake.
>
> Controller failure: After startup, use a multimeter to measure whether there is a 24V output
> voltage at the controller brake connector. Replace the controller.

Same figure, same pass condition, same order. The only difference is the name: the CSC900 book calls
it "the brake is no power or failure", the CSC880 book calls it a power-off brake.

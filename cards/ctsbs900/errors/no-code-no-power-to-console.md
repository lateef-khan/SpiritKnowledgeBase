---
id: ctsbs900-no-code-no-power-to-console
title: No Code — no power to console
kind: troubleshooting
question: Why is there no power to the console on a CTSBS900 and no error code shown?
asked_as:
- console screen is completely blank
- treadmill wont turn on at all
- no display no lights
keywords:
- no power
- console dead
- blank screen
- wont turn on
- power switch off
- inverter no dc 12v
facets:
  product_line: treadmill
  model: ctsbs900
  applies_to:
  - ctsbs900
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ctsbs900-esp-emergency-stop-activated
- ctsbs900-le1-inverter-low-voltage
see_also:
- ctsbs900-powering-on
- ctsbs900-troubleshooting-common-problems
source:
  ref: ctsbs900-om
  locator: p. 46
  extracted_at: '2026-08-24'
---

This is a blank/dead-console condition rather than a coded error message (no error code is displayed at all). Not to be confused with **ESP** (emergency stop activated, which does show a code) or **LE1** (inverter low voltage, which also shows a code).

| Possible Cause | Corrective Action |
|---|---|
| Power switch is OFF | Turn on the power switch |
| Power switch indicator not lit | Check outlet with multimeter |
| Inverter no DC 12V output | Replace inverter |
| Control cable failure | Replace control cable |
| Console failure | Replace console |
| ERP small board failure | Replace ERP small board |

See also [assembly/powering-on.md](../assembly/powering-on.md) for the normal power-on sequence, and [maintenance/troubleshooting-common-problems.md](../maintenance/troubleshooting-common-problems.md) ("Display does not light") for additional causes such as the tether cord not being in position or a tripped circuit breaker.

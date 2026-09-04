---
id: f60-2016-e5-error-code
title: 'E5 error: bad communication'
kind: troubleshooting
question: What does an E5 error mean on a Sole F60-2016?
asked_as:
- e5 error on my treadmill
- console not talking to the controller
- sole treadmill error e5
keywords:
- e5
- e5 error
- communication
- 5-pin signal wires
- tx rx
- pins slide
- console board
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: errors
  code: e5
authority: 3
not_to_be_confused_with:
- f60-2016-e0-error-code
- f60-2016-e1-error-code
- f60-2016-incline-er-message
- f60-2016-e2-error-code
- f60-2016-e4-error-code
- f60-2016-e6-error-code
see_also:
- f60-2016-error-code-list
- f60-2016-console-to-controller-pinout
source:
  ref: sole-tm-f60-2016-service-manual
  locator: page 56, 8.6 Error Message E5
  extracted_at: '2026-09-04'
---

**This is E5, not E6 (lower controller broken) and not E4 (motor wires).**

**Definition**: the communication is bad.

**Cause**: normally the **5-pin main signal wires** are pressured, fractured, or the pins have slid, which breaks the transmission and reception pins (TX, RX). Less often the upper console or the lower controller is bad in its signal communication or main IC components.

| Possible cause | Things to check | Solution |
|---|---|---|
| Main signal wire is bad | Check whether the signal wires are pressured or fractured, or the pins have slid | Re-wire the signal wires, or change the signal wires |
| Lower controller or upper console possibly broken | If E5 is still there after re-wiring or changing the signal wires, the controller or the console may be broken | Change the lower controller or the upper console |

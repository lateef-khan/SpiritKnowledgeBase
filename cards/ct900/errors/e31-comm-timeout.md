---
id: ct900-e31-comm-timeout
title: Error E31 - COMM TIMEOUT (communication timeout)
kind: troubleshooting
question: What does error E31 COMM TIMEOUT mean on a CT900 and how do I fix it?
asked_as:
- what does e31 mean on the treadmill
- error 31 communication timeout
keywords:
- e31
- comm timeout
- communication timeout
- console inverter connection
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e31
authority: 3
not_to_be_confused_with:
- ct900-e27-comm-code-err
- ct900-e30-comm-cmd-err
- ct900-ce10-modbus-transmission-timeout
see_also:
- ct900-e27-comm-code-err
- ct900-e30-comm-cmd-err
- ct900-ce10-modbus-transmission-timeout
source:
  ref: ct900-om
  locator: p. 45
  extracted_at: '2026-08-24'
---

**This is E31, not E27 (COMM CODE ERR) or E30 (COMM CMD ERR).**

**Description**: The communication transmission timeout error between the console and the inverter.

**Solution**: Check each connector/wire for good [connection].

Compare with the inverter's own [cE10 - ModBus transmission time-out](ce10-modbus-transmission-timeout.md) warning code, a related but separate fault in the inverter's own code namespace.

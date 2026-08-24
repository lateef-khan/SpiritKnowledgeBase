---
id: ct900-ce10-modbus-transmission-timeout
title: Inverter warning cE10 - ModBus transmission time-out
kind: troubleshooting
question: What does inverter warning cE10 mean on a CT900 and how do I clear it?
asked_as:
- what does ce10 mean on the inverter display
- modbus transmission time-out error
keywords:
- ce10
- modbus transmission timeout
- kpc-cc01
- inverter warning
facets:
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: ce10
authority: 3
not_to_be_confused_with:
- ct900-ce1-communication-command-defected
- ct900-ce2-address-of-data-defected
- ct900-ce3-length-of-communication-data-defected
- ct900-ce4-communications-written-read-only-address
- ct900-e31-comm-timeout
see_also:
- ct900-ce4-communications-written-read-only-address
- ct900-e31-comm-timeout
source:
  ref: ct900-om
  locator: p. 46
  extracted_at: '2026-08-24'
---

**This is cE10 (warning code #5), not cE1-cE4, and not the console's own [E31 COMM TIMEOUT](e31-comm-timeout.md) code (a related but separate fault in the console's own error code namespace).** Press RESET to clear any Warning Code.

**Corrective actions**:
1. Verify the communication cable and the communication quality.
2. Clear the fault and then press RESET button.

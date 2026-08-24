---
id: ct900-ce2-address-of-data-defected
title: Inverter warning cE2 - Address of data defected
kind: troubleshooting
question: What does inverter warning cE2 mean on a CT900 and how do I clear it?
asked_as:
- what does ce2 mean on the inverter display
- address of data defected error
keywords:
- ce2
- address of data defected
- modbus
- kpc-cc01
- inverter warning
facets:
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: ce2
authority: 3
not_to_be_confused_with:
- ct900-ce1-communication-command-defected
- ct900-ce3-length-of-communication-data-defected
- ct900-ce4-communications-written-read-only-address
- ct900-ce10-modbus-transmission-timeout
- ct900-e28-data-addrs-flt
see_also:
- ct900-ce1-communication-command-defected
- ct900-e28-data-addrs-flt
source:
  ref: ct900-om
  locator: p. 46
  extracted_at: '2026-08-24'
---

**This is cE2 (warning code #2), not cE1, cE3, cE4, or cE10.** Press RESET to clear any Warning Code. Compare with the console's own [E28 DATA ADDRS FLT](e28-data-addrs-flt.md), a similar but separate concept in the console's error code namespace.

**Corrective actions**:
1. Verify if the data address of the ModBus fits the specifications of the motor drive.
2. Verify the communication cable and the communication quality.
3. Clear the fault and then press RESET button.

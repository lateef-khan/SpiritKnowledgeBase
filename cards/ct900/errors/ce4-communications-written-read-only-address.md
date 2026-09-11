---
id: ct900-ce4-communications-written-read-only-address
title: Inverter warning cE4 - Communications being written to a read-only address
kind: troubleshooting
question: What does inverter warning cE4 mean on a CT900 and how do I clear it?
asked_as:
- what does ce4 mean on the inverter display
- communications written in a read only address error
keywords:
- ce4
- communications written read only address
- modbus
- kpc-cc01
- inverter warning
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: ce4
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-ce1-communication-command-defected
- ct900-ce2-address-of-data-defected
- ct900-ce3-length-of-communication-data-defected
- ct900-ce10-modbus-transmission-timeout
see_also:
- ct900-ce3-length-of-communication-data-defected
- ct900-ce10-modbus-transmission-timeout
source:
  ref: ct900-om
  locator: p. 46; CT900 service manual List of Warning Codes, PDF p. 44-45, text.md
    lines 841-947
  extracted_at: '2026-08-24'
---

**This is cE4 (warning code #4), not cE1, cE2, cE3, or cE10.** Press RESET to clear any Warning Code.

**Corrective actions**:
1. Verify if the ModBus command fits the specifications of the motor drive.
2. Verify if the ModBus command was sent too rapidly.
3. Verify the communication cable and the communication quality.
4. Clear the fault and then press RESET button.

**The CT900 service manual prints this warning row word for word** in its *List of Warning Codes*, corrective actions included.

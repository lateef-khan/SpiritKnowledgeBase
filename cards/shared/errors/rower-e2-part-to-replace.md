---
id: sole-rower-e2-part-to-replace
title: Which part to replace for an E2 error on a rower
kind: troubleshooting
question: What part do I replace when a Sole rower shows an E2 error?
asked_as:
- my sole rower shows e2
- e2 error on a rowing machine what do i replace
- resistance stopped and the rower says e2
- e2 code on my sole rower
keywords:
- e2
- gear motor
- computer cable
- display board
- error code
- rower
- resistance
- cable tensioner
facets:
  brand:
  - sole
  product_line: rower
  model: '*'
  applies_to:
  - sr500-2016
  - sr550-2023
  section: errors
  code: e2
authority: 2
not_to_be_confused_with:
- sole-rower-e1-part-to-replace
see_also:
- sr550-2023-e2-gear-motor-failure
- sr500-2016-e2-motor-error
source:
  ref: sole-rw-e2-error-rower
  locator: whole document
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (EEPROM / display board).**

E2 means the machine sees something wrong with the gear motor, or cannot talk to it.

1. Ask whether the machine has recently been assembled, disassembled or moved.
2. **Yes** - replace the **Computer Cable**.
3. **No** - replace the **Gear Motor**.
4. If the fault is still there after replacing both the Computer Cable and the Gear Motor, replace the **Display Board**.

**The two rowers name the part differently.** The sr550-2023 manual prints E2 as "Gear motor is failure". The sr500-2016 manual prints E2 as "Cable tension communication error" and calls the same actuator the cable tensioner or tension motor. The manual cards `sr550-2023-e2-gear-motor-failure` and `sr500-2016-e2-motor-error` hold the voltage checks for each machine.

---
id: 80t-2026-errors-conf-rs-485-communication-error-cn8-j18-j19-then-tx-rx-leds
title: conF on the inverter is an RS-485 communication error, worked from the inverter
  mains to the TX and RX LEDs
kind: troubleshooting
question: What does inverter error conF mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- conf error on treadmill
- inverter shows conf
- rs-485 communication error 8.0t
- treadmill drive not talking to the controller
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- conf
- rs-485
- communication
- tx rx leds
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: conf
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-pgo-abnormal-motor-speed-encoder-cable-brake-then-transmission
- 70t-2026-errors-e22-rs-485-flt
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
- 80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 23 conF, PDF p. 21; text.md lines
    289-331
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `conF`, row 23 of the 48-row table** - not `Pgo` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 23. conF | RS-485 communication transmission error | Check the RS-485 wiring between the controller and the inverter. |

**The table row is one line; the troubleshooting chapter prints the procedure, headed *RS-485 Communication Error*:**

1. Measure the AC input voltage at terminal **CN8** on the inverter. If no AC voltage is measured or the voltage is incorrect, proceed to Step 2. If the AC voltage is correct, proceed to Step 3.
2. Check the wiring at terminals **#258 and #274** between the LCB and the inverter (see the Electrical Wiring Diagram section), then measure the AC output voltage at connectors **J18 and J19** on the LCB. If no correct AC voltage is measured, **replace the LCB**. If the AC voltage is correct, **replace the wiring**.
3. Check whether both ends of the **#272 cable** between the inverter and the LCB are properly connected. If the cable is properly connected, proceed to the next step.
4. Check whether the **TX and RX indicator LEDs** on the inverter are flashing. If there is no flash, **replace the inverter**. If the LEDs are flashing, **replace the #272 cable**.

**The order matters: an inverter with no mains cannot answer, so its supply is proved before its serial link.** The LCB feeds the inverter its AC (the circuit-board page says the LCB switches the inverter input for sleep mode), which is why a dead CN8 sends you to J18/J19 on the LCB rather than to the wall. Cable #272 is the *RS-485 & Safety Switch Cable* on the wiring diagram, so it carries the `EF` safety circuit as well.

This is the drive-to-controller link. The console-to-controller link failing is a different message, `UART Communication Error` (`80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version`).

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.


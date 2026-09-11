---
id: 80t-2026-errors-pgo-abnormal-motor-speed-encoder-cable-brake-then-transmission
title: Pgo on the inverter is abnormal motor speed from the encoder, worked through
  the encoder cable, the brake and the transmission
kind: troubleshooting
question: What does inverter error Pgo mean on a Spirit 80t-2026 treadmill, and what
  does the service manual say to check?
asked_as:
- pgo error on treadmill
- inverter shows pgo
- 8.0t encoder error
- belt speed wrong pgo code
keywords:
- inverter error
- error code
- medical treadmill
- drive fault
- mt2000
- pgo
- encoder
- motor speed
- electromagnetic brake
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: pgo
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-os-speed-exceeds-maximum-limit
- 80t-2026-errors-oes-excessive-load-speed-deviation-brake-released
- 80t-2026-errors-conf-rs-485-communication-error-cn8-j18-j19-then-tx-rx-leds
- ct900-pger-pg-feedback-loss-warning
- mt200-2022-errors-e27-encoder-email-encoder-then-inverter-then-motor
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
- 80t-2026-errors-no-power-console-does-not-light-j16-j17-d17-then-12-vdc
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Category Inverter, row 27 Pgo, PDF p. 21; text.md lines
    289-331
  extracted_at: '2026-09-11'
---

**This is the 8.0T inverter code `Pgo`, row 27 of the 48-row table** - not `oS`, `oES`, `conF` on the same table, and not the same letters on any other Spirit treadmill (see the links below). It is an inverter (drive) fault, and it is printed only in the service manual - the owner's manual has no code list (`80t-2026-errors-console-shows-message-with-solution`).

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Inverter | 27. Pgo | Abnormal motor speed detected via encoder feedback | Refer to the troubleshooting section for details. |

**The table row says only *refer to the troubleshooting section*; that section is headed *PGO Error*:**

1. Check if **encoder cable #279** is properly connected at both the LCB and the encoder. If not connected, reconnect it or replace the cable if faulty. If properly connected, proceed to the next step.
2. **Release the brake in maintenance mode** (see the Maintenance Mode section). Use your foot to drag the running belt to confirm brake release. If the belt cannot be dragged, the brake is not released - proceed to Step 3. If the brake is released, proceed to Step 5.
3. Measure the voltage between **pin 1 and pin 3 of J10** on the LCB. If **12 VDC** is not measured, replace the LCB. If 12 VDC is present, proceed to Step 4.
4. Check if the brake cable is properly connected to J10 on the LCB. If not, reconnect it. If properly connected, the issue is a **mechanical fault in the motor's internal electromagnetic brake, and the entire motor must be replaced**.
5. Release the brake in engineering mode and then inspect transmission components related to the running belt. Check for friction or mechanical issues that may cause increased load. If such issues are found, investigate the transmission system further. If no issues are found, **replace the inverter and encoder**.

**Table 1 - normal values, motor tested in maintenance mode with no belt load:**

| Belt speed | Rotational speed | Current |
|---|---|---|
| 0.1 kph | 22 to 25 rpm | 2.97 to 3.63 Amp |
| 0.1 mph | 35 to 39 rpm | 2.88 to 3.52 Amp |

**The brake is the fork in the road.** A belt you cannot drag with the brake commanded off means the brake never released - a 12 V LCB output or a brake cable if either is missing, and otherwise the motor itself, because the electromagnetic brake is inside it and is not sold separately. A belt that drags freely means the drive turned and the encoder disagreed, so the transmission is inspected for load before the inverter and encoder are replaced together. The flow chart names the parts as LCB #269, motor #280, inverter #282 and encoder #284.

The whole table, with the fourteen codes the book marks *Not applicable to this model*, is `80t-2026-errors-inverter-error-code-table-48-rows`.


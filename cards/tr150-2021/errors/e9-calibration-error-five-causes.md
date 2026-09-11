---
id: tr150-2021-errors-e9-calibration-error-five-causes
title: 'E9 calibration error: five causes from a sensor gap over 3 mm to a wrong parameter,
  and a six-part troubleshooting table'
kind: troubleshooting
question: What does E9 mean on an Xterra tr150-2021 treadmill, and what should I check?
asked_as:
- tr150 e9 calibration error
- e9 during calibration xterra
- calibration fails with e9
keywords:
- e9
- calibration error
- speed sensor
- 3 mm
- main wires
- power off
- unstable power
- parameter
- lower driver board
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: errors
  code: e9
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with:
- trx5500-2024-errors-e9-speed-calibration-error
- xt485ent-2023-errors-e9-speed-calibration-error
see_also:
- xterra-treadmill-errors-e1-check-rpm-sensor-procedure
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: 'TR150 SM 8.8 Error Message: E9, PDF p. 45; text.md lines 766-804; TR150
    SM 8. Error code items, PDF p. 32 (printed 33); text.md lines 432-461'
  extracted_at: '2026-09-11'
---

**This is the TR150's E9, a general calibration error.** The TRX5500's E9 is a speed calibration error with a different procedure (`trx5500-2024-errors-e9-speed-calibration-error`). No other Xterra book prints an E9.

*Definition.* Calibration error. The configuration is the E1 drawing: speed signal over TX/RX of the 5-pin main wires.

*Possible causes*

1. In the calibration, the speed sensor may have come off, or its gap is more than 3 mm.
2. In the calibration, the main wires may have come off or make defective contact.
3. In the calibration, power was switched off and then on immediately.
4. In the calibration, the power is unstable or low.
5. In the calibration, the parameter may not be correct, or the parameter was not stored entirely.

*Troubleshooting*

| Part | What to do |
|---|---|
| Wall outlet | Use a multi-meter on the AC 1000 V range to check whether the wall outlet is 110 V AC or 220 V AC, and whether it is stable |
| Speed sensor | Check the speed sensor gap is less than 3 mm |
| Main wires | Check whether the main wires are broken |
| Calibration again | Before the calibration, check the parameters are set correctly. During the calibration, no person or thing may stand or be put on the belt |
| Lower driver board | Replace lower driver board |
| Upper control board | Replace upper control board |

The calibration procedure itself (Eng mode, wheel 42, 1-16 km/h) is a console card. The sensor check is `xterra-treadmill-errors-e1-check-rpm-sensor-procedure`.

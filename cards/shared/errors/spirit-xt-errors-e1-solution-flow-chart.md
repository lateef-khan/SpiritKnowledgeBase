---
id: spirit-xt-errors-e1-solution-flow-chart
title: Working through an E1 step by step, from a power reset to replacing the motor
kind: procedure
question: How do I diagnose an E1 on a Spirit XT 2015, XT 2023 or XT ENT treadmill?
asked_as:
- step by step for e1 on my spirit treadmill
- e1 troubleshooting flow
- belt does not move and shows e1 what next
keywords:
- e1
- flow chart
- rpm sensor
- main control line
- driver board
- dc12v
- pin2 pin5
- replace motor
- reset power
- countdown
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- ct850-2016-low-speed-solution-flow-chart
see_also:
- xt-2023-errors-e1-motor-not-responsive
- spirit-xt-errors-e1-check-rpm-sensor-procedure
- ct850-2016-low-speed-solution-flow-chart
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT185 2023 service manual E1 solution follow chart, a flat picture read
    from the render, PDF p. 21, text.md lines 422-428; XT285 2023 service manual E1
    solution follow chart, a flat picture read from the render, PDF p. 22, text.md
    lines 424-430; XT385 2023 service manual E1 solution follow chart, a flat picture
    read from the render, PDF p. 23, text.md lines 388-391; XT485 2023 service manual
    E1 solution follow chart, a flat picture read from the render, PDF p. 23, text.md
    lines 388-391; XT685 2023 service manual E1 solution follow chart, a flat picture
    read from the render, PDF p. 22, text.md lines 429-435; XT185 2015 service manual
    E1 solution follow chart, read from the render, PDF p. 40, text.md lines 656-662;
    XT285 2015 service manual E1 solution follow chart, read from the render, PDF
    p. 41 (printed 40), text.md lines 725-731; XT385 2015 service manual E1 solution
    follow chart, read from the render, PDF p. 41, text.md lines 614-620; XT485 2015
    service manual E1 solution follow chart, read from the render, PDF p. 41, text.md
    lines 614-620; XT485ENT 2023 service manual E1 solution follow chart, read from
    the render, PDF p. 37, text.md lines 529-535; XT685ENT 2023 service manual E1
    solution follow chart, read from the render, PDF p. 23, text.md lines 394-397
  extracted_at: '2026-09-11'
---

Every XT service manual draws the same flow chart under *E1 solution follow chart*. It is a picture with no text layer, read from the rendered page. In order:

1. **E1 showing up** -> reset power -> press start again.
2. **Does the display count down after pressing start?** No -> replace the upper console board, or update its program. Yes -> continue.
3. **Did the belt move after start?**
   - **Yes** -> check the RPM sensor (step 5).
   - **No** -> **is the main control line split?** Yes -> replace the main control line, then re-test from step 3. No -> step 4.
4. **Does the lower control driver board have enough power? (AC 220V)** No -> check the power source from the wall is a stable AC 220 V. Yes -> **use a multi-meter to check main control line socket pin 2 and pin 5 for DC 12 V.** No -> replace the lower control driver board. Yes -> press start and use the multi-meter to check whether the driver board motor socket has voltage. No -> replace the lower control driver board. Yes -> **replace the motor**.
5. **Is the RPM sensor good?** No -> replace the RPM sensor. Yes -> **adjust the sensor gap to 2 mm** -> did the belt move after start? Yes -> problem solved. No -> back to the driver-board power check in step 4.

Two things the chart says that the text around it does not.

- **The chart sets the sensor gap at 2 mm; the troubleshooting form on the facing page and the sensor flow chart say less than 3 mm.** Both figures are printed in every one of these books. Set the sensor as close to the magnet as it will go without touching and either figure is satisfied.
- **The chart tests for AC 220 V.** The safety pages of the same books say the machine is built for 220 V or, on the 120 VAC electronic power system, 110 V. Test against the supply the machine is actually on.

The detailed sensor check the chart branches to is on `spirit-xt-errors-e1-check-rpm-sensor-procedure`. What E1 means is on `xt-2023-errors-e1-motor-not-responsive`.

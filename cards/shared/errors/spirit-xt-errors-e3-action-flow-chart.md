---
id: spirit-xt-errors-e3-action-flow-chart
title: How the E3 action flow chart walks the incline VR voltage from the sensor to
  the display board
kind: procedure
question: What does the E3 action flow chart in a Spirit XT service manual check,
  in order?
asked_as:
- e3 flow chart on my spirit treadmill
- where is the incline voltage lost when e3 shows
- incline vr voltage check order
keywords:
- e3
- flow chart
- incline vr
- vr voltage
- driver board
- cable
- display board
- err appears
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
  code: e3
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
- spirit-xt-2023-errors-e3-incline-vr-out-of-range
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- xt485ent-2023-errors-e3-incline-vr-out-of-range
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT185 2023 service manual Action Flow Chart under 8.4, read from the render,
    PDF p. 24, text.md lines 475-495; XT285 2023 service manual Action Flow Chart
    under 8.4, read from the render, PDF p. 25, text.md lines 477-497; XT385 2023
    service manual Action Flow Chart under 8.4, read from the render, PDF p. 26, text.md
    lines 434-450; XT485 2023 service manual Action Flow Chart under 8.4, read from
    the render, PDF p. 26, text.md lines 434-450; XT685 2023 service manual Action
    Flow Chart under 8.4, read from the render, PDF p. 25, text.md lines 480-500;
    XT185 2015 service manual Action Flow Chart under Case of E3, read from the render,
    PDF p. 45, text.md lines 754-765; XT285 2015 service manual Action Flow Chart
    under Case of E3, read from the render, PDF p. 46 (printed 45), text.md lines
    823-834; XT385 2015 service manual Action Flow Chart under Case of E3, read from
    the render, PDF p. 46, text.md lines 681-691; XT485 2015 service manual Action
    Flow Chart under Case of E3, read from the render, PDF p. 46, text.md lines 682-692;
    XT485ENT 2023 service manual Action Flow Chart, read from the render, PDF p. 42,
    text.md lines 600-601; XT685ENT 2023 service manual Action Flow Chart, read from
    the render, PDF p. 29, text.md lines 464-484
  extracted_at: '2026-09-11'
---

Every XT service manual prints the same chart under *Action Flow Chart* in the E3 section. It is a picture with no text layer, and reads the same in all eleven books:

1. **INCLINE VR** - is the VR reading between 0 and 5 V? No -> ERR appears on the display.
2. **DRIVER BOARD** - is the VR voltage present there? No -> ERR appears on the display.
3. **CABLE** - is the VR voltage present on the cable? No -> ERR appears on the display.
4. **DISPLAY BOARD** - is the VR voltage present there? No -> ERR appears on the display. Yes -> the display operates normally.

So the chart follows the 0 to 5 V position signal along its path - potentiometer, driver board, console cable, display board - and the first point where it is missing is the fault. The chart ends at `ERR APPEARS ON THE DISPLAY`, not `E3`; the message a customer sees is `E3`.

The voltages to expect at each point, and how to measure them, are the nine-step test on `spirit-xt-errors-e3-incline-test-procedure-nine-steps`. The part tables that go with the chart are on `spirit-xt-2023-errors-e3-incline-vr-out-of-range`, `spirit-xt-2015-errors-e3-incline-vr-out-of-range` and `xt485ent-2023-errors-e3-incline-vr-out-of-range`.

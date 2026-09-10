---
id: ct800ent-2024-console-calibration-defaults-0-5-to-12-0-mph
title: The touchscreen calibration defaults - 0.5 to 12.0 mi/hr and fifteen incline levels
kind: spec
question: What speed and incline does calibration default to on a Spirit ct800ent-2024 or ct850ent-2024
  treadmill?
asked_as:
- what is the top speed of the spirit ent treadmill
- what should the calibration be set to on the touchscreen treadmill
- how many incline levels does the treadmill have
- where is calibration on the ent treadmill screen
keywords:
- calibration
- default speed
- minimum speed
- maximum speed
- 12.0 mph
- 0.5 mph
- incline level
- 15 level
- maintenance mode
- touchscreen
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2024
  - ct850ent-2024
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850ent-2022-console-calibration-touchscreen
- ct900-calibration-procedure
- ct850-2020-console-calibration-minimum-speed-0-3
- ct850-2016-console-calibration-minimum-speed-0-5
- spirit-ct800-console-calibration-with-grade-return
see_also:
- cu800ent-2024-console-maintenance-mode-and-engineering-menu
- ct850-2020-factory-setting-ranges
source:
  ref: spirit-treadmill-ct800ent-2024-owners-manual
  locator: p. 52, ENGINEERING MODE MENU, Calibration block; the CT850ENT-2024 owner's manual prints
    the same block on its p. 52
  extracted_at: '2026-09-10'
---

**This is not a numbered routine. It is three lines under Calibration in maintenance mode**, and the
manual prints the figures as *defaults*, not as values to set:

1. The default Speed is **Minimum 0.5 (mi/hr) - Maximum 12.0 (mi/hr)**.
2. The default Incline is **15 level**.
3. **Click on the Calibration to start setting.**

Reach it by pressing **Hello Guest ten times**, then **Service > Calibration**:
`cu800ent-2024-console-maintenance-mode-and-engineering-menu`.

**There is no wheel size step and no Metric or Imperial step here.** Every earlier Spirit treadmill
calibration routine has both. Units are set from the Gear icon in the status bar or from Machine
Setup, not from this block, and no wheel diameter is printed anywhere in either book.

**The manual does not say what the machine does during calibration**, whether the belt moves, or what
to do when calibration fails.

**Calibration is where the ENT bike and elliptical have a PWM Test.** The CE800ENT-2024,
CR800ENT-2024 and CU800ENT-2024 Service lists read Key Test, Information, **PWM Test**, Ethernet
Setup, Error Code Log; the two ENT treadmills read **Calibration** in that third position. Do not
offer either machine the other's entry.

**These are not the LED CT800 and CT850 figures.** The 2024 LED consoles run an eight-step Start +
Speed Up routine with wheel size 2.98, minimum 0.5, maximum 12.0 and maximum elevation 15
(`ct900-calibration-procedure`) - the same speeds, but reached a completely different way and with
two steps this console does not have. **The 2022 ENT treadmill is different again**: it is entered by
tapping the Home icon ten times and sets a minimum of **0.3** and a maximum of **15.0**
(`ct850ent-2022-console-calibration-touchscreen`). **Three Spirit ENT treadmill generations therefore
print three different maxima and three different entry gestures**; read the book for the machine in
front of you.

**Incline "15 level" here is a count, not a percent.** The console displays incline as percent of
grade during a workout (`ct850-2020-incline-adjustment`), and neither 2024 ENT manual says whether
the fifteen levels correspond to fifteen percent.

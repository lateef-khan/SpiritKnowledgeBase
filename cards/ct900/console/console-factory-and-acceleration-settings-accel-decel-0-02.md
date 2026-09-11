---
id: ct900-console-factory-and-acceleration-settings-accel-decel-0-02
title: Factory settings with an acceleration and deceleration time of 0:02, a minimum
  speed of 0.3 to 0.7, and no wheel size step
kind: procedure
question: What are the factory and acceleration settings on a Spirit ct900 treadmill
  and how do I reach them?
asked_as:
- how do i get into factory settings on the treadmill
- how do i change how fast the belt accelerates
- what minimum speed can the ct900 be set to
- how do i calibrate the incline
keywords:
- factory settings
- acceleration time
- deceleration time
- min speed
- max speed
- units
- enter to calibrate
- finished
- start and speed fast
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: console
  code: '*'
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-calibration-procedure
- ct850-2020-factory-setting-ranges
- ct850-2020-incline-calibration
- 40t-2026-console-factory-settings-min-0-3-to-0-7-max-down-to-10-0
- 70t-2026-console-factory-settings
see_also:
- ct900-engineering-mode-menu
- spirit-2026t-console-belt-acceleration-time
source:
  ref: spirit-treadmill-ct900-service-manual
  locator: Section 8, Factory and Acceleration Settings, PDF p. 37 (printed 37); text.md
    lines 519-537
  extracted_at: '2026-09-11'
---

**This routine has an ACCEL and a DECEL step and no wheel size or maximum elevation step.** The
owner's-manual calibration for the same machine is an eight-step routine with wheel size 2.98,
minimum 0.5, maximum 12.0 and elevation 15 (`ct900-calibration-procedure`); the CT850-2020 and
CT800-2020 service manuals print wheel size and elevation ranges but no acceleration step
(`ct850-2020-factory-setting-ranges`). The 4.0T prints the same first three prompts and then goes
straight to calibration (`40t-2026-console-factory-settings-min-0-3-to-0-7-max-down-to-10-0`).

**To enter: press Start and Speed Fast while the console is in power-up reset.** Press Enter to
begin; Enter accepts each prompt.

| Prompt | Default | Range |
|---|---|---|
| UNITS: ENGLISH | English | Any up/down arrow changes it to Metric |
| ADJUST MIN SPEED 0.5 | **0.5 mph** | **0.3 to 0.7 mph**; the value is shown in the speed window |
| ADJUST MAX SPEED 12.0 | **12.0 mph** | **down to 10.0 mph**; the value is shown in the speed window |
| ADJUST ACCEL 0:02 | **0:02 seconds**, shown in the Time window | 0:01 to 0:04 seconds |
| ADJUST DECEL 0:02 | **0:02 seconds**, shown in the Time window | 0:01 to 0:04 seconds |
| CALIBRATION | The display shows **"FINISHED"** then **"ENTER TO CALIBRATE"**. **Press ENTER if the machine needs an incline calibration; press STOP to skip it, and the console resets.** | |

**The minimum-speed range is wider here than on the CT800-2020 and CT850-2020**, which allow 0.3 to
0.5. The 7.0T medical treadmill prints its acceleration time per 1 mph with a range of 0:01 to 1:00
(`spirit-2026t-console-belt-acceleration-time`); the CT900's 0:01 to 0:04 is a different setting on a
different console, so do not carry either figure across.

The Maintenance Mode menu of the same book - Key Test, Display Test, Sleep, Odometer, Units, Speaker,
Incline Return and a Service Mode with RPM and AMPS readouts - is already on
`ct900-engineering-mode-menu`, which the service manual prints word for word on its p. 38.


---
id: 40t-2026-console-factory-settings-min-0-3-to-0-7-max-down-to-10-0
title: 'Factory settings: Start and Speed Fast at power-up, a minimum speed of 0.3
  to 0.7, a maximum down to 10.0, then a two-reading incline calibration'
kind: procedure
question: How do I open the factory settings and calibrate a Spirit 40t-2026 treadmill?
asked_as:
- how do i get into factory settings on the treadmill
- how do i calibrate the 4.0t
- what minimum speed can the treadmill be set to
- what does a1 a2 mean on the display
keywords:
- factory settings
- calibration
- min speed
- max speed
- units
- confirm key
- a1 a2
- calibrated
- console reset
- start and speed fast
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 40t-2026
  applies_to:
  - 40t-2026
  section: console
  code: '*'
  model_number:
  - '740885'
authority: 3
not_to_be_confused_with:
- ct900-console-factory-and-acceleration-settings-accel-decel-0-02
- 70t-2026-console-factory-settings
- ct850-2020-factory-setting-ranges
see_also:
- 40t-2026-console-maintenance-mode-as-the-service-manual-prints-it
- 40t-2026-console-maintenance-mode-menu
source:
  ref: spirit-treadmill-40t-2026-service-manual
  locator: Section 8, Factory and Acceleration Settings, PDF p. 31 (printed 31); text.md
    lines 455-472. 4.0T ST8700A-ST026-01 service manual (spirit-treadmill-40t-2026-service-manual-st8700a,
    the later revision of the ST8700-ST017 book) Factory and Acceleration Settings,
    PDF p. 32 (printed 32), text.md lines 463-502
  extracted_at: '2026-09-11'
---

**The 4.0T owner's manual prints no factory settings or calibration at all; this is the only place
they are written down.** The console's confirm key is called **Confirm**, not Enter, throughout.

**To enter: press Start and Speed Fast while the console is in power-up reset.** Press Confirm to
begin; Confirm accepts each prompt.

| Prompt | Default | Range |
|---|---|---|
| UNITS: ENGLISH | English | Any up/down arrow changes it to Metric |
| ADJUST MIN SPEED 0.5 | **0.5 mph** | **0.3 to 0.7 mph**; the value is shown in the speed window |
| ADJUST MAX SPEED 12.0 | **12.0 mph** | **down to 10.0 mph**; the value is shown in the speed window |
| FINISHED | The message window shows **"PRESS CONFIRM TO CALIBATE OR STOP TO EXIT"** (sic). Press Confirm. | |
| Calibration | The message window shows **"A1 xxxxx A2 xxxxx"**, then **"CALIBRATED"**, and the console resets. | |

**There is no wheel size, no maximum elevation and no acceleration step.** The CT900 routine adds
ACCEL and DECEL prompts between max speed and calibration
(`ct900-console-factory-and-acceleration-settings-accel-decel-0-02`); the 7.0T routine adds reverse
speed, acceleration per 1 mph and separate max incline and max decline prompts
(`70t-2026-console-factory-settings`). Neither belongs on a 4.0T.

**A1 and A2 are the two incline position readings** the Service Mode's INCLINE test shows on the same
console - "USE INCLINE KEYS then MW displays: A1 xxxxx A2 xxxxx" - see
`40t-2026-console-maintenance-mode-as-the-service-manual-prints-it`. The manual does not say what
values they should reach.

**The ST8700A-ST026-01 revision prints these settings unchanged on its p. 32** - the same gesture, the same minimum and maximum ranges and the same acceleration items; only the step numbering is spaced differently.


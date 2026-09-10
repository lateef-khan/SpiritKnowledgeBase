---
id: ct850-2020-factory-setting-ranges
title: Default and allowed values for each factory setting
kind: spec
question: What are the factory setting ranges on a Spirit CT850-2020 treadmill?
asked_as:
- what should the wheel size be set to
- what is the maximum speed setting on the treadmill
- what is the default max elevation
keywords:
- factory settings
- default value
- wheel size 2.98
- min speed
- max speed
- max elevation
- units
- english
- metric
- range
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2020
  applies_to:
  - ct850-2020
  section: console
  code: '*'
  model_number: '850840'
authority: 3
not_to_be_confused_with:
- ctsbs900-factory-mode-min-max-speed
- ct850-2020-console-calibration-minimum-speed-0-3
see_also:
- ct850-2020-incline-calibration
- ct850-2016-calibration-procedure-metric-or-english
- ct850-2016-calibration-procedure-english-only
- ctsbs900-factory-mode-min-max-speed
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-5 Factory and Acceleration Settings, p. 45 (printed 44)
  extracted_at: '2026-09-08'
---

| Setting | Default | Adjustable range |
|---|---|---|
| UNITS | ENGLISH | English or Metric |
| ADJUST WHEEL SIZE | 2.98 | 1.50 to 3.50 |
| ADJUST MIN SPEED | 0.5 mph | 0.3 to 0.5 mph |
| ADJUST MAX SPEED | 12.0 mph | 10.0 to 12 mph |
| ADJUST MAX ELEVATION | 15 | 10 to 15 |

The min and max speed values are described as "the speed number to be shown in the speed window".
The elevation prompt is printed as `ADJUST MAX MAX ELEVATION` with MAX twice; it is one setting.

**These are the 2020 manual's values, and they are not shared with the rest of the range.**

- The **2016** CT850 service manual prints different limits in two different places, and one of those
  is in kilometres per hour.
- The **CTSBS900** enters factory settings with the same Start + Speed Up gesture at power-on reset,
  but its ranges are min 0.5-0.6 mph / 0.8-1.0 kph and max 10.0-15.6 mph / 16.0-25.0 kph. Do not
  carry a value across from one machine to the other.

**The CT850-2020 owner's manual tells the reader to set values this table does not allow.** Its
calibration procedure on p. 38 says minimum speed **0.3** and maximum speed **15.0**
(`ct850-2020-console-calibration-minimum-speed-0-3`); 15.0 is above the 10.0 to 12 range printed
above, and 0.3 is the bottom of the min-speed range rather than the 0.5 default. The two documents
describe the same machine. Both figures are reproduced as printed.

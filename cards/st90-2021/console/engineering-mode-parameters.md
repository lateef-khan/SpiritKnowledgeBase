---
id: st90-2021-engineering-mode-parameters
title: Base parameters in engineering mode
kind: spec
question: What speed and incline limits can I set on a Sole ST90-2021 treadmill?
asked_as:
- what is the top speed of my st90
- how do i change the max incline on the treadmill
- engineering mode settings on my sole treadmill
keywords:
- max speed
- min speed
- max incline
- engineering mode
- calibration
- adc
- default
- range
facets:
  brand:
  - sole
  product_line: treadmill
  model: st90-2021
  applies_to:
  - st90-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- st90-2021-calibration-procedure
- st90-2021-units-setting
- st90-2021-engineering-mode-entry
source:
  ref: sole-tm-st90-2021-service-manual
  locator: Section 8-2-3 Engineering Mode, page 47
  extracted_at: '2026-09-04'
---

The calibration uses these values as its limits, so a change here changes what the machine calibrates to.

| Item | Range | Default |
|---|---|---|
| Max. Incline | 10 to 15% | 15% |
| Units | KM or MILE | MILE |
| Max. Speed | 12.0 to 13.0 MPH / 20.0 to 22.0 KPH | 12 MPH / 22 KPH |
| Min. Speed | 0.3 to 0.5 MPH / 0.5 to 1.0 KPH | 0.5 MPH / 0.8 KPH |

Three read-only values sit below them and fill in during a calibration: **Max. Incline** (the maximum incline AD value), **ADC** (the value now) and **Min. Incline** (the minimum incline AD value).

**Two things in this table do not line up.** The name `Max. Incline` is used twice, once for the incline percentage and once for the AD value. And the printed default pairs 12 MPH with 22 KPH, which are not the same speed; 12 mph is about 19.3 kph.

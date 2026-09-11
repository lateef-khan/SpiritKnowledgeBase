---
id: spirit-xt-errors-e7-input-power-unstable
title: 'E7: the input power is too low, too high or unstable, so test the wall outlet
  before the controller'
kind: troubleshooting
question: What does E7 mean on a Spirit XT 2015 or XT 2023 treadmill, and what does
  the service manual say to check?
asked_as:
- what does e7 mean on my spirit treadmill
- treadmill shows e7 input power
- e7 error unstable voltage
keywords:
- e7
- input power
- wall outlet
- unstable voltage
- ac 1000v
- multi-meter
- lower controller
- error code
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
  - xt685-2023
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- xt485ent-2023-errors-e7-incline-calibration-error
- 70t-2026-errors-e7-thrm-ovrload
- ct900-e7-eeprom-wr-err
- f65-2023-e7-input-power-error
- spirit-2024-errors-e7-abnormal-ac-input-voltage
see_also:
- spirit-xt-errors-error-code-list-eight-codes
- f65-2023-e7-input-power-error
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: 'XT185 2023 service manual 8.8 Error Message: E7, PDF p. 31, text.md lines
    636-659; XT285 2023 service manual 8.8 Error Message: E7, PDF p. 32, text.md lines
    638-661; XT385 2023 service manual 8.8 Error Message: E7, PDF p. 33, text.md lines
    576-596; XT485 2023 service manual 8.8 Error Message: E7, PDF p. 33, text.md lines
    576-596; XT685 2023 service manual 8.8 Error Message: E7, PDF p. 32, text.md lines
    641-664; XT185 2015 service manual Error Message: E7, PDF p. 56-57, text.md lines
    1039-1087; XT285 2015 service manual Error Message: E7, PDF p. 57-58 (printed
    56-57), text.md lines 1109-1157; XT385 2015 service manual Error Message: E7,
    PDF p. 57-58, text.md lines 875-900; XT485 2015 service manual Error Message:
    E7, PDF p. 57-58, text.md lines 878-905'
  extracted_at: '2026-09-11'
---

**This is the E7 of the 2015 and 2023 XT185 to XT685 - not the XT485ENT's E7, which is an incline calibration error (`xt485ent-2023-errors-e7-incline-calibration-error`), not E7 on a Spirit 7.0T or MT200 (thermal overload), not the CT900's E7 EEPROM write error, and not Sole's E7 (`f65-2023-e7-input-power-error`), which is the same Dyaco text filed for Sole machines.** The XT685ENT prints no E7 at all.

Definition: *Input power anomaly, possibly too low or too high or unstable.* Cause: *The wall outlet possibly unstable, cause to treadmill working power does not stable. Another problem possibly power part of lower controller board is broken.*

The configuration drawing shows the wall outlet - `AC 110V or AC 220V` - through the power switch into the lower controller, whose overload protection reports over the main control wire; the CE build adds a filter and choke to match 220 V.

| Part | Troubleshooting |
|---|---|
| Wall outlet | Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110 ACV or 220 AC or not. And the voltage whether stable or not. |
| Controller | Replace Lower controller board. |

So: set the meter to its AC 1000 V range, confirm the outlet is a steady 110 V or 220 V, and only then replace the lower controller board. All nine books print this word for word.

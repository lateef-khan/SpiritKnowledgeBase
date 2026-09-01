---
id: ct900-e33-incline-err
title: Error E33 - INCLINE ERR
kind: troubleshooting
question: What does error E33 INCLINE ERR mean on a CT900 and how do I fix it?
asked_as:
- what does e33 mean on the treadmill
- incline error
- why does my incline not match the console
keywords:
- e33
- incline err
- incline error
- abnormal elevation
- incline calibration
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: e33
authority: 3
not_to_be_confused_with:
- ct900-e3-igbt-over-temp
see_also:
- ct900-incline-position-mismatch-e33
- ct900-calibration-procedure
- ct900-incline-adjustment
source:
  ref: ct900-om
  locator: p. 45
  extracted_at: '2026-08-24'
---

**This is E33 (INCLINE ERR), not E3 (IGBT OVER TEMP) - the numbers look similar but these are unrelated faults.**

**Description**: Abnormal elevation, which means that the incline motor AD value cannot be returned to the initial positive [value]. On the first calibration, or if the error occurs after calibration, the difference in the AD value between the highest and lowest points of the incline motor is too small.

**Solution**: On the first calibration, if the calibration or error occurs after calibration, you need to replace the incline motor or inverter.

See also the corresponding troubleshooting-table entry at [incline position mismatch (E33)](../maintenance/incline-position-mismatch-e33.md), and the [calibration procedure](../maintenance/calibration-procedure.md) that this error relates to.

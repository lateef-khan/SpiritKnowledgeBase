---
id: ct900-incline-position-mismatch-e33
title: Incline position doesn't match console / INCLINE E33
kind: troubleshooting
question: Why doesn't the incline on my CT900 match the console, or show INCLINE E33?
asked_as:
- the incline is different than what the console shows
- what does incline e33 mean
keywords:
- incline mismatch
- incline err
- incline e33
- incline not calibrated
- incline motor
facets:
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900-e33-incline-err
see_also:
- ct900-e33-incline-err
- ct900-calibration-procedure
- ct900-incline-adjustment
source:
  ref: ct900-om
  locator: p. 42
  extracted_at: '2026-08-24'
---

## Incline position doesn't match console
**Reason**: Console is not calibrated. **Solve**: Calibrate the console - see [calibration procedure](calibration-procedure.md).

## INCLINE ERR, INCLINE window displays "INCLINE E33"
**Reason**: Position sensor value of incline motor is wrong. **Solve**: Turn off the AC switch and turn on power again; calibrate the monitor.

This is the troubleshooting-table entry for the console's formal [error E33 INCLINE ERR](../errors/e33-incline-err.md), which gives a fuller description of the fault (the AD value of the incline motor cannot return to its initial positive value, or the difference between the highest and lowest points measured during calibration is too small).

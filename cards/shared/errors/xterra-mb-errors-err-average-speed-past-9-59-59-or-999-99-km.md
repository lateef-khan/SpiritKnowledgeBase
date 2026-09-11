---
id: xterra-mb-errors-err-average-speed-past-9-59-59-or-999-99-km
title: 'Err in the average-speed mode means time has passed 9:59:59 or distance 999.99
  km: reset time and distance'
kind: troubleshooting
question: Why does the console show Err on an Xterra MB indoor cycle?
asked_as:
- xterra spin bike shows err
- mb550 console err on average speed
- indoor cycle display says err
- err message on my xterra indoor cycle
keywords:
- err
- error
- average speed
- avs mode
- maximum limit
- '9:59:59'
- '999.99'
- reset
- indoor cycle
- not a fault
facets:
  brand:
  - xterra
  product_line: bike
  model: '*'
  applies_to:
  - mb500-2014
  - mb550-2018
  section: errors
  code: err
authority: 3
not_to_be_confused_with:
- spirit-cic850-errors-err-transmitter-pairing-failed
- xterra-trx-errors-err-incline-vr-out-of-range
- xterra-treadmill-errors-incline-err-window-position-sensor-power-cycle-then-calibrate
see_also:
- xterra-mb-errors-cadence-jumps-high-or-low-console-code-or-rf-interference
source:
  ref: xterra-bike-mb550-2018-owners-manual
  locator: MB550 OM Console Operation, AVS MODE note, PDF p. 13 (printed 11); text.md
    lines 410-457 (OCR supplement lines 842-886); MB500 OM (scan) Console Operation,
    PDF p. 7 (printed 10-11 spread), OCR supplement; text.md lines 280-346
  extracted_at: '2026-09-11'
---

**This is `Err` on the MB500 / MB550 indoor-cycle console, and it is a range overflow, not a fault.** It is
not the incline `Err` of the Xterra treadmills and not the Spirit CIC850's pairing `Err`.

The note under *AVS MODE (Average Speed Mode)*:

> If your time or distance is over the maximum limit (time 9 hr:59 min:59 sec and distance: 999.99 km),
> then the console will not allow you to measure the correct average speed and show "Err" on the display.
> Once the time and distance value has been reset, the average speed will show normally.

So `Err` appears only in the average-speed readout, only after the elapsed time passes **9:59:59** or the
distance passes **999.99 km**, and clears as soon as time and distance are reset. Nothing needs replacing.
The MBX2500 book prints no average-speed mode and no `Err`.


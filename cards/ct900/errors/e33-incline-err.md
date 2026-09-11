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
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ct900-e3-igbt-over-temp
see_also:
- ct900-incline-position-mismatch-e33
- ct900-calibration-procedure
- ct900-incline-adjustment
- ct900-errors-incline-e33-no-vr-change-during-incline-action
- ct850-2020-e3-incline-motor-cannot-work
source:
  ref: ct900-om
  locator: 'p. 45; CT900 service manual Error code items, PDF p. 30, text.md lines
    401-426; CT900 service manual Error Message: E33, PDF p. 32-34, text.md lines
    440-475'
  extracted_at: '2026-08-24'
---

**This is E33 (INCLINE ERR), not E3 (IGBT OVER TEMP) - the numbers look similar but these are unrelated faults.**

**Description**: Abnormal elevation, which means that the incline motor AD value cannot be returned to the initial positive [value]. On the first calibration, or if the error occurs after calibration, the difference in the AD value between the highest and lowest points of the incline motor is too small.

**Solution**: On the first calibration, if the calibration or error occurs after calibration, you need to replace the incline motor or inverter.

See also the corresponding troubleshooting-table entry at [incline position mismatch (E33)](../maintenance/incline-position-mismatch-e33.md), and the [calibration procedure](../maintenance/calibration-procedure.md) that this error relates to.

**Service manual remedy.** The CT900 service manual gives E33 two sections. The first, *Error Message: E33*, defines it as the reading being out of range: *The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. "E33" appears on the display.* Case of INCLINE E33: *Incline VR value exceeds the range. INCLINE E33 appears on the display. Incline motor isn't operation up or down, making the VR value exceed the range. After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so INCLINE E33 appears.* The drawing shows the driver board's `INCLINE DOWN RELAY` and `INCLINE UP RELAY`, and the action flow chart runs INCLINE VR -> DRIVER BOARD -> DISPLAY BOARD to *display operates normally* or *ERR appears on the display*.

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and console cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| Console cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Incline | Inspect the display board console cable connections. |

This is the CT850 2020's E3 table under the CT900's number (`ct850-2020-e3-incline-motor-cannot-work`). The second section, raised while the incline is being driven, is on `ct900-errors-incline-e33-no-vr-change-during-incline-action`; the two together are what the owner's-manual row above calls the AD value not returning and the high-low difference being too small.

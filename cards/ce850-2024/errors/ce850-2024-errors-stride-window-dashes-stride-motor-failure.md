---
id: ce850-2024-errors-stride-window-dashes-stride-motor-failure
title: Three dashes in place of a stride number mean the stride motor has failed
kind: troubleshooting
question: What do the dashes in the stride window mean on a Spirit CE850-2020 or CE850-2024
  elliptical?
asked_as:
- my elliptical shows dashes instead of stride length
- stride window shows lines not numbers
- elliptical stride display is blank dashes
keywords:
- dashes
- stride motor
- stride window
- error message
- stride length
- elliptical
- failure
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2020
  - ce850-2024
  section: errors
  code: dashes
authority: 3
not_to_be_confused_with:
- ce850-2024-errors-err-tension-motor-failure
- ce850-2024-errors-stride-err-position-sensor-wrong
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
see_also:
- ce850-2024-errors-stride-err-position-sensor-wrong
- ce850-2024-errors-err-tension-motor-failure
- ce900-2025-errors-eeprom-error-replace-upper-controller
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
source:
  ref: spirit-elliptical-ce850-2024-owners-manual
  locator: 'TROUBLE SHOOTING - CONTINUED & ERROR CODES, printed page 39. That page
    is a flat picture with no text layer and was read from the rendered page; CE850
    (2020) service manual 8-3 Error Message: - - -, Case of STRIDE ERROR, Troubleshooting,
    Error Message: ---, Cause of "- - -" on STRIDE window and Troubleshooting, PDF
    p. 37-45, text.md lines 624-797'
  extracted_at: '2026-09-10'
---

| Error Message | Explain |
|---|---|
| `---` | Stride motor is failure |

**The message is three dashes, not a word and not a code.** A reader looking for letters or a number
will not find one; the `STRIDE` window simply shows `---` where a stride length should be.

**That is the whole of what this manual says about it.** No definition, no window named beyond the
table, and no troubleshooting step.

**The troubleshooting matrix of the same manual describes the same display and gives it a name and a
remedy.** Its row reads `STRIDE ERR, STRIDE window displays "---"`, blames a wrong position sensor
value on the stride motor and asks for a power cycle and then a calibration. That is the half of
this fact with something to do in it:
`ce850-2024-errors-stride-err-position-sensor-wrong`. **Neither half is complete on its own** - the
error table names the failed part, the matrix names the remedy - and nothing in the manual joins
them up.

The other two rows of the error table are `EEPROM ERROR`
(`ce900-2025-errors-eeprom-error-replace-upper-controller`) and `ERR`, which is the **tension**
motor rather than the stride motor (`ce850-2024-errors-err-tension-motor-failure`).

**The CE850 (2020) service manual prints the same three-row table and then the chapter the owner's manual leaves out, twice, for two cases.** Its `8-3 Error Message: - - -` reads: *The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. "- - -" appears on the STRIDE WINDOW.*

**Case 1 - stride VR value out of range (the `Case of STRIDE ERROR` page).** *Stride VR value exceeds the range. --- appears on the display. Stride motor isn't operation up or down, making the VR value exceed the range. After turning on the unit, the display board detects that the stride VR voltage exceeds the range, so --- appears.*

| Part | Troubleshooting |
|---|---|
| Stride VR | 1. Reconnect VR wires. 2. Inspect whether the stride wires are broken or disconnected. |
| Display board | 1. Inspect the stride wire and 14-pin cable connections. 2. Test whether the VR voltage varies at the stride wire terminal. |
| 14-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Driver board | Inspect the display board 14-pin connections. |

**Case 2 - no VR change during stride action (the `Cause of "- - -" on STRIDE window` page).** *During stride action, the display board CPU cannot read the VR value, so --- appears. Press the stride UP/DOWN key. The stride doesn't operate. --- appears on the display.* Explanation: pressing the stride UP or DOWN key the stride operates and moves the VR, and the VR value changes; if the display board CPU sees no VR value change, the stride is not operating when it should be, and --- appears.

| Part | Troubleshooting |
|---|---|
| Display board | If not as above, inspect the cable and connections. |
| 14-pin cable | 1. Inspect whether the 14-PIN cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | 1. Press stride UP or DOWN key again, making the stride motor return to its position. 2. If --- still appears, re-calibrate the stride set. |
| Stride motor | 1. Inspect whether the stride motor is stuck. 2. Inspect whether the stride gears are cracked. 3. Test whether the stride motor has a broken circuit. 4. Re-calibrate the stride set. |

Between the two cases the book prints the console-to-driver-board 14-pin definition (`1 MTR-, 2 MTR+, 3 +5V, 4 MPOS, 5 GND, 6 RPM, 7 GND, 8 NC, 9 5V, 10 +12V, 11 GND, 12 INC+, 13 INC-, 14 IPOS` - pins 6, 8 and 9 differ from the CE850 2016's) and the nine-step motor and position-sensor test: `spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac`. The CE850 2016 prints the same two cases with the message `E3` (`spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read`).

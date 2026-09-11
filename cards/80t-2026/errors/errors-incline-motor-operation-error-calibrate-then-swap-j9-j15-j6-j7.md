---
id: 80t-2026-errors-incline-motor-operation-error-calibrate-then-swap-j9-j15-j6-j7
title: 'Incline Motor operation error: calibrate both incline motors, watch the two
  red indicator lights while driving them, then swap the front and rear connectors
  to blame a motor or the LCB'
kind: troubleshooting
question: What do I do when a Spirit 80t-2026 treadmill shows an Incline Motor operation
  error or the incline will not calibrate?
asked_as:
- 8.0t incline motor operation error
- treadmill incline calibration fails
- front or rear incline not working on the medical treadmill
- how to tell a bad incline motor from a bad board
keywords:
- incline motor
- operation error
- calibration
- front incline
- rear incline
- d13
- d6
- j9 j15
- j6 j7
- lower control board
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: no-code
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-err-incline-err
- spirit-mt200-errors-e41-incline-err
- ct850-2020-incline-err
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
- 80t-2026-errors-console-shows-message-with-solution
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Incline Motor / Message row, PDF p. 22, text.md line
    358; 5. Troubleshooting, Incline Motor Control Function Fault, steps 1-3 and the
    Check Procedure flow chart, PDF p. 33-34, text.md lines 466-491 and the OCR supplement
    for page 34
  extracted_at: '2026-09-11'
---

**The message is the words `Incline Motor operation error`** - the error table lists it as an *Incline Motor - Message* row and sends you to the troubleshooting chapter, which heads the procedure *Incline Motor Control Function Fault*. This treadmill has **two** incline motors, front and rear, and the procedure tests both.

**Step 1.** In maintenance mode, **calibrate the front and rear incline motor positions** (see the Maintenance Mode section). If calibration fails, proceed to the next step.

**Step 2.** Check whether the cable connectors at **J9, J15, J6 and J7** on the LCB are properly connected. If any are loose, reconnect them. If all are properly connected, enter a value higher than the current D/A value in Maintenance Mode to raise the treadmill platform; entering a lower value will lower the platform. During **front** platform movement, check if indicator light **D13** turns red; for **rear** platform movement, check **D6**. If the light does not turn on, **replace the LCB**. If the light turns on, proceed to the next step.

**Step 3.** **Swap the front and rear incline motor connectors on the LCB: exchange J9 with J15, and J6 with J7.** Then perform Step 2 again. Check whether the issue shifts along with the connector swap. If the previously faulty incline control function becomes normal and the previously normal incline control function becomes faulty, **replace the original faulty incline motor**. If the original faulty incline control function remains faulty and the original normal incline control function remains normal, **replace the LCB**.

**The swap is the diagnosis.** Two motors on one board give a free substitution test: move the fault with the connector and it is the motor (#276 front or #277 rear on the flow chart); leave it behind and it is the board (#269). The D/A value the maintenance screen takes is 10-1020 on the screen shot, higher meaning steeper.

The calibration screen itself - *Incline Motor > Calibration* under Service in Maintenance Mode - is carded under `section: console`. The MT8000-based 7.0T answers a stuck incline with numbered codes instead, `ERR` and `ER2` (`70t-2026-errors-err-incline-err`, `70t-2026-errors-er2-decline-err`); those do not appear on this machine.


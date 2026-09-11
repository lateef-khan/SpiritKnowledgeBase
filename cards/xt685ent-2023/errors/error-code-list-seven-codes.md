---
id: xt685ent-2023-errors-error-code-list-seven-codes
title: Seven error codes and no input-power code at all
kind: spec
question: What error codes can a Spirit xt685ent-2023 treadmill display and what does
  each one mean?
asked_as:
- list of error codes for my spirit xt685ent
- what do the e codes mean on the ent treadmill
- touchscreen treadmill error code table
keywords:
- error code
- error code table
- list
- index
- safety key
- touch screen
- ent
- rpm signal
facets:
  brand:
  - spirit
  product_line: treadmill
  model: xt685ent-2023
  applies_to:
  - xt685ent-2023
  section: errors
  code: '*'
  model_number:
  - '685523'
authority: 3
not_to_be_confused_with:
- spirit-xt-errors-error-code-list-eight-codes
- xt485ent-2023-errors-error-code-list-nine-codes
see_also:
- spirit-xt-errors-e0-safety-key-loop
- xt-2023-errors-e1-motor-not-responsive
- spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
- spirit-xt-2023-errors-e3-incline-vr-out-of-range
- spirit-xt-errors-e4-motor-power-wire-not-plugged
- spirit-xt-errors-e5-console-controller-communication-poor
- spirit-xt-errors-e6-lower-controller-component-fault
source:
  ref: spirit-treadmill-xt685ent-2023-service-manual
  locator: XT685ENT 2023 service manual ERROR CODE LIST, PDF p. 19, text.md lines
    315-336
  extracted_at: '2026-09-11'
---

The XT685ENT service manual prints seven rows. There is no E7 in this book - not in the table and not as a section.

| Code | Description |
|---|---|
| E0 | The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed. |
| E1 | Display board CPU did not receive the RPM signal. (only calibration) |
| E2 | Treadmill motor is over current. |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |
| E4 | Treadmill motor wires or volt possible abnormal. |
| E5 | Communication single is abnormal. |
| E6 | Lower Control board possible broken. |

The only tool the chapter names is a **multi-meter**.

The eight-code table of the 2015 and 2023 XT185 to XT685 books adds `E7 Input power error` (`spirit-xt-errors-error-code-list-eight-codes`); the XT485ENT adds `E7` and `E9` as calibration errors (`xt485ent-2023-errors-error-code-list-nine-codes`). The per-code sections that follow this table in the XT685ENT book are word for word the 2023 XT485 ones, with one extra troubleshooting row under E3 for the 5-pin cable.

This book also has **no troubleshooting procedure matrix** and no service checklist; the Condition / Reason / Solve rows every other XT service manual prints are absent from it, and the checklist rows are held by the XT685ENT owner's manual cards instead.

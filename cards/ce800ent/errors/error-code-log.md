---
id: ce800ent-error-code-log
title: Reading the error code log in the diagnostics menu
kind: procedure
question: Where do I find the logged error codes on a Spirit CE800ENT elliptical?
asked_as:
- where is the error log on my spirit elliptical
- how to see past errors on the console
- diagnostics screen on a ce800
keywords:
- error code log
- diagnostics
- engineering mode
- fault history
- logged errors
- console
- hex code
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800ent
  applies_to:
  - ce800ent
  section: errors
  code: '*'
  model_number: '800054'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-e5-console-controller-communication
- cu900ent-error-code-log
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: Engineering Mode Instructions, Engineering Mode Settings page 29 and Diagnostics
    page 32. Page 32 is a flattened image and was read from raw/page-32.png
  extracted_at: '2026-09-08'
---

The console records faults while the machine runs and shows them under **Diagnostics** in
engineering mode. The settings table describes the entry as `The Error Diagnostics`, and the
Diagnostics page itself says:

> Recorder the error code on machine during running.

Each logged line is a hexadecimal code and a short description. The screenshot in the manual shows
three identical lines:

| Code | Description |
|---|---|
| 0x0021 | Treadmill-> Motor Error |
| 0x0021 | Treadmill-> Motor Error |
| 0x0021 | Treadmill-> Motor Error |

Two warnings.

- **The screenshot is from a treadmill**, not from an elliptical. It is the only worked example the
  manual gives, and `0x0021` is the only code number printed anywhere in this manual. Do not read it
  as a list of the codes a CE800ENT can log.
- **This manual gives no way to clear the log.** The CU900ENT manual, which has the same console
  family, says to press the `Error Code Log` button ten times in a row to clear it - see
  `cu900ent-error-code-log`. The CE800ENT manual does not repeat that instruction.

To reach engineering mode, click the Home icon at the top centre of the main page ten times.

The one error message this manual documents in full is `ce800ent-e5-console-controller-communication`.

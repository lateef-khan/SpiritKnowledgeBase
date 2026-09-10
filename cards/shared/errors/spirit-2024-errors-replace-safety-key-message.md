---
id: spirit-2024-errors-replace-safety-key-message
title: Replace Safety Key on the display means the safety key is not fitted
kind: troubleshooting
question: What does the message Replace Safety Key mean on a Spirit CT800ENT-2024 or
  CT850ENT-2024 treadmill?
asked_as:
- my treadmill says replace safety key
- console keeps asking for the safety key
- what does replace safety key mean
keywords:
- replace safety key
- safety key
- tether cord
- magnet
- console message
- not inserted
- stop key
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2024
  - ct850ent-2024
  section: errors
  code: safety-key
authority: 3
not_to_be_confused_with:
- spirit-2024-errors-safety-lock-child-mode
- ct850-2020-e-25h-emergency-stop-warning
see_also:
- spirit-2024-errors-safety-lock-child-mode
- ct850-2016-operates-without-safety-key
- ct850-2016-does-not-stop-after-safety-key-removed
source:
  ref: spirit-treadmill-ct800ent-2024-owners-manual
  locator: ERROR CODES, printed page 60 of the CT800ENT 2024 manual and printed page 61
    of the CT850ENT 2024 manual. Both pages are flat pictures with no text layer and
    were read from the rendered page.
  extracted_at: '2026-09-10'
---

**This is a message, not a code.** It is printed in the ERROR CODES table of both books, below the
numbered codes, and it has no `E` and no number.

| Error Message | Cause | Troubleshooting |
|---|---|---|
| Replace Safety Key | Safety key is not inserted. | Insert Safety key back. |

That is the whole of it. The manual offers no check for a key that *is* fitted and still produces
the message; for that fault see the safety-device rows in the troubleshooting matrix -
`ct850-2016-operates-without-safety-key` and
`ct850-2016-does-not-stop-after-safety-key-removed`.

The other message printed in the same table is `SAFETY LOCK`, which is a child-lock mode and not a
missing key: `spirit-2024-errors-safety-lock-child-mode`.

**On the CT850ENT 2024 this message sits under the twenty-three-code inverter table**, which
carries a separate emergency-stop code `E-25H` for the safety key wiring
(`ct850-2020-e-25h-emergency-stop-warning`). They are not the same thing: `E-25H` is raised by the
inverter, this message by the console.

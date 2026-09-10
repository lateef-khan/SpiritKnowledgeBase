---
id: spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
title: E2 is a drive motor over-current, and both books answer it with belt lubricant
kind: troubleshooting
question: What does E2 mean on a Spirit CT800-2024 or CT800ENT-2024 treadmill?
asked_as:
- what does e2 mean on my spirit treadmill
- treadmill showing e2
- how do i fix e2 on a spirit treadmill
keywords:
- e2
- over current
- overcurrent
- drive motor
- driver board
- running belt
- lubricate
- worn belt
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2024
  - ct800ent-2024
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- ct900-e2-over-voltage
- f85-2019-e2-over-current
- crw800-2024-errors-e2-cable-tension-communication-error
- ct850-2020-e-0ah-motor-overcurrent
see_also:
- spirit-2024-errors-seven-code-table-with-no-hyphen
source:
  ref: spirit-treadmill-ct800-2024-owners-manual
  locator: ERROR CODES, printed page 42 of the CT800 2024 owner's manual and printed
    page 60 of the CT800ENT 2024 owner's manual. Both pages are flat pictures with no
    text layer and were read from the rendered page.
  extracted_at: '2026-09-10'
---

| Field | CT800 2024 | CT800ENT 2024 |
|---|---|---|
| Cause | The overcurrent of the controller to the motor. | Drive motor current is overload to trigger the protection of Driver Board. |
| Solution | The running belt is worn need lubricate or replacement. | Check the situation of Running Belt and Deck; try to apply Lube between Running Belt and Running Deck. |

**Both books send the reader to the same place - friction between belt and deck** - and neither
asks for an electrical measurement first. The CT800 2024 goes further and offers belt
**replacement** as an alternative to lubricating; the ENT book stops at lubricating.

The CT850 2024 and CT850ENT 2024 of the same family use a different controller and answer motor
over-current with `E-0AH`, with the same belt-and-lubricant remedy
(`ct850-2020-e-0ah-motor-overcurrent`).

Look-alikes: `E2` on a Spirit CT900 is an inverter over-voltage (`ct900-e2-over-voltage`), `E2` on
the Spirit CRW800 2024 rower is a cable tension communication error
(`crw800-2024-errors-e2-cable-tension-communication-error`), and Sole's F85 uses `E2` for its own
over-current (`f85-2019-e2-over-current`).

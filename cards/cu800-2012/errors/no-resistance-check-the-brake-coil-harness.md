---
id: cu800-2012-errors-no-resistance-check-the-brake-coil-harness
title: 'No resistance: the induction brake rarely fails, so open both chain covers
  and check the brake coil harness for a break or a disconnection'
kind: troubleshooting
question: What does the service manual say to check when there is no resistance on
  a Spirit cu800-2012 upright bike?
asked_as:
- no resistance on my 2012 spirit cu800
- xu878 pedals spin free
- cu800 2012 induction brake not working
- brake coil wire on the spirit upright bike
keywords:
- no resistance
- induction brake
- brake coil harness
- chain cover
- wire
- disconnection
- upright bike
- q&a
facets:
  brand:
  - spirit
  product_line: bike
  model: cu800-2012
  applies_to:
  - cu800-2012
  section: errors
  code: no-code
  model_number:
  - '800343'
authority: 3
not_to_be_confused_with:
- ce800ent-no-resistance
see_also:
- ce800ent-no-resistance
- spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller
- cu800-2012-errors-no-display-check-the-power-adaptor-dc-connector-and-harnesses
source:
  ref: spirit-bike-cu800-2012-service-manual
  locator: CU800 2012 (XU878) service manual 8-12 Induction Brake, PDF p. 49, text.md
    lines 779-802
  extracted_at: '2026-09-11'
---

Section 8-12, `Induction Brake`, in full:

> There is usually no problem with the Induction Brake. **If there is no resistance, disassemble left and right chain covers and make sure that Wire Brake Coil Harness is connected properly and no breakage or disconnection with other wire harness.**

That is the Q&A's whole answer - a harness check, and a statement that the brake itself is rarely the fault. The matrix on an earlier page of the same book gives the same symptom two parts: the control board and the resistance-voltage wire (`ce800ent-no-resistance`, where this book's two-cause version is described). Between them: the coil harness and the resistance-voltage wire first, the control board second, and the brake last.

The XU878 is an induction-brake bike with an AC adaptor, the one CU800 generation whose console is not generator-fed; its later 2020-book sisters answer this row from the generator side. The XBR25/XBR55 2007 dealer manual, on the same kind of brake, prints a DC-voltage test that separates console, controller and coil: `spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller`.

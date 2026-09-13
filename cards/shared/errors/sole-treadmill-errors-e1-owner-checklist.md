---
id: sole-treadmill-errors-e1-owner-checklist
title: 'E1 no motor output signal: owner''s checklist'
kind: troubleshooting
question: What should I check when a Sole treadmill shows E1?
asked_as:
- treadmill shows e1 and stops
- e1 no motor output
- what does e1 mean on my sole
keywords:
- e1
- no motor output
- speed sensor
- console cable
- controller
- start button
- owner checklist
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  section: errors
  applies_to:
  - f80-2023
  - f85-2020
  - f85-2021
  - f85-2023
  - f89-2023
  - tt8-2021
  - tt8-2023
  code: e1
authority: 3
not_to_be_confused_with:
- sole-treadmill-errors-e2-owner-checklist
- sole-treadmill-errors-e3-owner-checklist
- sole-treadmill-errors-e4-owner-checklist
- sole-treadmill-errors-e5-owner-checklist
- sole-treadmill-errors-e6-owner-checklist
- sole-treadmill-errors-e7-owner-checklist
- f63-2026-e01-error-code
see_also:
- f65-2023-e1-no-rpm-signal
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-f80-2023-owners-manual
  locator: 'ERROR MESSAGES FOR DIGITAL-CONTROL SYSTEM TREADMILLS: sole-tm-f80-2023-owners-manual
    PDF p. 31 (printed 29); sole-tm-f85-2021-owners-manual PDF p. 33 (printed 31);
    sole-tm-f85-2023-owners-manual PDF p. 31; sole-tm-f89-2023-owners-manual PDF p.
    32; sole-tm-tt8-2021-owners-manual PDF p. 33 (printed 31); sole-tm-tt8-2023-owners-manual
    PDF p. 29 (printed 27)'
  extracted_at: '2026-09-12'
---

**This is the stencil-era owner's-manual E1 (no motor output signal), not the 2026 E01 (over-current) and not Spirit's E1.**

The six owner's manuals print the same ERROR MESSAGES table with OK/NG checkboxes. The F80-2023, F85-2023 and F89-2023 prints read 'E1_'..'E7_' on the OCR layer — the render shows a plain code beside the checkbox column.

| ERROR | MEANING | POSSIBLE CAUSE |
|---|---|---|
| Console showing E1 | No motor output signal | 1. Does motor run after 'Start' button is pressed? 2. Connector could be loose for the cable connecting between controller and speed sensor. 3. Check if speed sensor is defective. 4. Check if the cable connecting the console and controller is connected properly. |

The service manuals' deeper E1 procedure (RPM signal, sensor gap, TX/RX wiring) is a separate card: see `f65-2023-e1-no-rpm-signal`.

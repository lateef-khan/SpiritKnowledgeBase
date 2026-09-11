---
id: spirit-xt-errors-e4-motor-power-wire-not-plugged
title: 'E4: the motor power wire is not plugged into the lower controller'
kind: troubleshooting
question: What does E4 mean on a Spirit XT 2015, XT 2023 or XT ENT treadmill, and
  what does the service manual say to check?
asked_as:
- what does e4 mean on my spirit treadmill
- treadmill shows e4 and the belt will not run
- motor wire error e4
keywords:
- e4
- motor power wire
- m+
- m-
- lower controller
- drive motor
- display board
- not plugged in
- error code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e4
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e4-ground-fault
- ct900-e4-motor-overload
- f65-2023-e4-motor-power-wire
- spirit-2024-errors-e4-drive-motor-input-voltage-abnormal
see_also:
- spirit-xt-errors-error-code-list-eight-codes
- f65-2023-e4-motor-power-wire
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: 'XT185 2023 service manual 8.5 Error Message: E4, PDF p. 28, text.md lines
    572-594; XT285 2023 service manual 8.5 Error Message: E4, PDF p. 29, text.md lines
    574-596; XT385 2023 service manual 8.5 Error Message: E4, PDF p. 30, text.md lines
    521-540; XT485 2023 service manual 8.5 Error Message: E4, PDF p. 30, text.md lines
    521-540; XT685 2023 service manual 8.5 Error Message: E4, PDF p. 29, text.md lines
    576-598; XT185 2015 service manual Error Message: E4, PDF p. 53, text.md lines
    929-965; XT285 2015 service manual Error Message: E4, PDF p. 54 (printed 53),
    text.md lines 999-1035; XT385 2015 service manual Error Message: E4, PDF p. 54,
    text.md lines 820-837; XT485 2015 service manual Error Message: E4, PDF p. 54,
    text.md lines 823-840; XT485ENT 2023 service manual 8.5 Error Message: E4, PDF
    p. 50, text.md lines 738-755; XT685ENT 2023 service manual 8.5 Error Message:
    E4, PDF p. 34, text.md lines 557-578'
  extracted_at: '2026-09-11'
---

**This is the XT E4 - not E4 on a Spirit 7.0T or MT200, which is an inverter ground fault (`70t-2026-errors-e4-ground-fault`), not the CT900's E4 motor overload, and not Sole's E4 (`f65-2023-e4-motor-power-wire`), which is the same Dyaco text filed for Sole machines.**

Definition: *Motor power wire error.* Cause: *Power wire of Motor does not insert lower controller.*

The configuration drawing shows the driver board sending the motor its power on the M+ and M- wires while the start and speed commands and the RPM return travel over the TX/RX lines of the main control wire.

| Part | Troubleshooting |
|---|---|
| Controller | Insert power wire of motor. |
| Drive Motor | Replace Motor. |
| Display board | Replace upper control board. |

All eleven XT service manuals print this word for word; the 2015 books and the XT485ENT say *Lower controller* and *Motor* for the first two parts. The XT485ENT and XT685ENT code lists word the row *Treadmill motor wires or volt possible abnormal.*, so on those two the code also covers an abnormal motor voltage.

The motor wires themselves are red to M+ and black to M- (the parts replacing chapter, not this card).

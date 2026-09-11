---
id: spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
title: 'E2 over current: lubricate the belt, then replace a worn belt, then the controller
  before the motor'
kind: troubleshooting
question: What does E2 mean on a Spirit XT 2023 or XT685ENT treadmill, and what does
  the service manual say to do?
asked_as:
- what does e2 mean on my spirit treadmill
- treadmill shows e2 over current
- e2 after lubricating the belt
keywords:
- e2
- over current
- overcurrent
- running belt
- lubricate
- worn belt
- friction
- controller
- drive motor
- protection
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2023
  - xt285-2023
  - xt385-2023
  - xt485-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- spirit-xt-2015-errors-e2-over-current-silicone-oil-then-board-or-motor
- f65-2023-e2-over-current
- f65-2026-e01-over-current
- spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
- 70t-2026-errors-e2-over-volt
see_also:
- spirit-xt-errors-error-code-list-eight-codes
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: 'XT185 2023 service manual 8.3 Error Message: E2/OVER CURRENT, PDF p. 23,
    text.md lines 434-475; XT285 2023 service manual 8.3 Error Message: E2/OVER CURRENT,
    PDF p. 24, text.md lines 436-477; XT385 2023 service manual 8.3 Error Message:
    E2/OVER CURRENT, PDF p. 25, text.md lines 394-434; XT485 2023 service manual 8.3
    Error Message: E2/OVER CURRENT, PDF p. 25, text.md lines 394-434; XT685 2023 service
    manual 8.3 Error Message: E2/OVER CURRENT, PDF p. 24, text.md lines 441-480; XT685ENT
    2023 service manual 8.3 Error Message: E2/OVER CURRENT, PDF p. 28, text.md lines
    428-464'
  extracted_at: '2026-09-11'
---

**This is the 2023 XT and XT685ENT E2 - not the 2015 XT and XT485ENT E2, whose books print a shorter remedy (`spirit-xt-2015-errors-e2-over-current-silicone-oil-then-board-or-motor`), and not E01 on a Sole 2026 treadmill, which is that family's over-current code.**

Section 8.3 is headed `Error Message: E2/OVER CURRENT`.

Definition, as printed: *When the controller detects that the operating current for the drive motor is above standard, the display will light up and show the message "E2." This indicates that the controller needs to protect itself and the drive motor in order to prevent damage. Typically, this is due to the running belt needing lubricate or its bottom fiber being worn seriously and requiring replacement. A dried or worn running belt generates more friction between itself and the running deck. The resulting high friction causes the controller requires to provide more current for the drive motor to maintain speed.*

The remedy, in the order the book gives it:

1. **Lubricate the bottom of the running belt** as the owner's manual describes.
2. If that does not clear it, the belt is worn: **replace the running belt**, which brings the motor current back to normal.
3. If E2 still occurs after a new belt, **either the controller or the drive motor is defective**. The book says the motor is a passive part and less likely to be the cause, so **replace the controller first**.

No current figure is printed anywhere in the section. The LED that lights when the lower board trips this protection is the `Limit current` LED (`spirit-xt-2023-errors-controller-led-debugging-five-leds`).

---
id: spirit-xb-2023-errors-lcd-not-bright-replace-generator-controller
title: The display backlight is dim or incomplete, on the row that ends at a new generator
  controller
kind: troubleshooting
question: Why is the display dim or incomplete on a Spirit XBR55-2023 or XBR95-2023
  recumbent bike?
asked_as:
- spirit recumbent screen is dim
- xbr95 display half lit
- console backlight faint on my 2023 spirit bike
- lcd not bright on xbr55
keywords:
- lcd
- dim display
- incomplete
- backlight
- power to console
- generator controller
- faint
- recumbent
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55-2023
  - xbr95-2023
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-lcd-dim-or-incomplete
- xbu55-2023-errors-lcd-not-bright-check-power-to-console
- spirit-residential-bike-errors-display-does-not-light-115-vac
see_also:
- spirit-lcd-dim-or-incomplete
- xbu55-2023-errors-lcd-not-bright-check-power-to-console
- spirit-erratic-pulse-display
- spirit-hand-pulse-not-working
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: XBR55 2023 service manual 8.4 Troubleshooting procedure Matrix, PDF p.
    16, text.md lines 323-343; XBR95 2023 service manual 8.4 Troubleshooting procedure
    Matrix, PDF p. 15, text.md lines 252-293
  extracted_at: '2026-09-11'
---

The condition is printed as `LCDs not bright, incomplete, or imperfect`.

| Reason | Solve |
|---|---|
| LCD light is broken | Replace with new LCD or console |
| Power to console too low | Check power to console. Replace generator controller. |

**No voltage figure is printed**, unlike the 2016 residential books that answer the same row with `Check AC power is 110-120V` (`spirit-lcd-dim-or-incomplete`), and the part at the end is a **generator controller** rather than the lower controller every other Spirit book names.

**That part name is right for one of the two books and wrong for the other.** The XBR95 2023 brakes with a generator and has a generator controller. The XBR55 2023 has a gear motor, an AC adapter and a drive board - its own electrical chapter names no generator anywhere - yet its matrix prints the same row, generator controller included. The row is inherited from the XBR95 book. On an XBR55 2023, read the third step as the drive board.

The XBU55 2023, printed in the same August 2023 family, stops one step short and names no controller at all: `xbu55-2023-errors-lcd-not-bright-check-power-to-console`.

**Neither book prints a second row for dead segments**; the 2016 books do (`spirit-lcd-displays-dim-or-incomplete`). The 2023 matrices are three rows - this one, erratic pulse (`spirit-erratic-pulse-display`) and hand pulse (`spirit-hand-pulse-not-working`) - and end there.

A display that shows nothing at all is a different question, answered in the Q&A chapter of the same books (`spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter`) and, for a customer, by the owner's manual row that ends at a 115 VAC outlet (`spirit-residential-bike-errors-display-does-not-light-115-vac`).

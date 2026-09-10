---
id: cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
title: The display light is dim or incomplete, on the row that names two supply voltages at once
kind: troubleshooting
question: Why is the display dim or partly lit on a Spirit CS800-2024 stepper?
asked_as:
- spirit stepper screen is dim
- console backlight faint on my stepper
- display half lit on my spirit stepper
keywords:
- led
- dim display
- incomplete
- backlight
- 220-240v
- 110-120v
- lower controller
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2024
  applies_to:
  - cs800-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-lcd-dim-or-incomplete
- ct850-2020-led-dim-or-incomplete
- spirit-2024-errors-leds-not-bright-generator-power-connection
see_also:
- spirit-lcd-dim-or-incomplete
- ct850-2020-led-displays-dim-or-incomplete
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: TROUBLESHOOTING, Condition / Reason / Solve matrix on printed page 36. That
    page is a flat picture with no text layer and was read from the rendered page.
  extracted_at: '2026-09-10'
---

The condition is printed as `LEDs not bright, incomplete or imperfect`.

| Reason | Solve |
|---|---|
| LED light is broken | Replace with new LED or console |
| Power to console too low | Check AC power is **220-240V or 110-120V**. Check power to console. Replace lower controller. |

**No other Spirit manual in the repository prints two supply bands in this row.** Every other
version names one figure or none: `110-120V` on the CT850 2016, CVC800, CE850 2024 and CRS800S 2024
(`spirit-lcd-dim-or-incomplete`), `120V` on the CT850 2020
(`ct850-2020-led-dim-or-incomplete`), none on the CE900 2025 family
(`ce900-2025-errors-leds-not-bright-incomplete-or-imperfect`).

**The two bands are alternatives for two markets, not a range to measure across.** Read the
machine's own rating plate and check against the band that matches it; a 110-120V machine reading
around 230V is a fault, not a pass.

**The CRS800S 2024 semi-recumbent stepper, sold beside this machine, prints `110~120V` only** and
otherwise the same four steps (`spirit-lcd-dim-or-incomplete`). Do not carry the 220-240V band onto
it.

Dead segments rather than a dim light are the next row down:
`ct850-2020-led-displays-dim-or-incomplete`.
